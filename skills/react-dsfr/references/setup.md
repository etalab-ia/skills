# Setup react-dsfr par framework

> **Choisir la bonne section selon le framework — ne pas mélanger les patterns.** Chaque framework a sa propre intégration ; les balises `<link rel="stylesheet" href="/dsfr/...">` ci-dessous **n'existent que pour Vite** (assets servis depuis `public/`). En **Next.js (App Router ou Pages Router)**, le CSS se charge par `import` et le `<link>` manuel est à proscrire. Aller directement à la section du framework utilisé : [Vite](#vite) · [Next.js App Router](#nextjs-app-router) · [Next.js Pages Router](#nextjs-pages-router) · [Create React App](#create-react-app).

## Installation

```bash
npm install --save @codegouvfr/react-dsfr
# ou yarn add @codegouvfr/react-dsfr
# ou pnpm add @codegouvfr/react-dsfr (requiert .npmrc avec enable-pre-post-scripts=true)
```

## Vite

1. Copier les assets DSFR dans le dossier `public/` et ajouter les scripts dans `package.json` :
```bash
cp -r node_modules/@codegouvfr/react-dsfr/dsfr public/dsfr
```

Pour automatiser cette copie après chaque `npm install`, ajouter un script `postinstall` :
```json
{
  "scripts": {
    "postinstall": "cp -r node_modules/@codegouvfr/react-dsfr/dsfr public/dsfr",
    "predev": "react-dsfr update-icons",
    "prebuild": "react-dsfr update-icons"
  }
}
```

2. Dans `index.html`, ajouter les assets DSFR (CSS, favicon) :
```html
<link rel="stylesheet" href="/dsfr/dsfr.min.css" />
<link rel="stylesheet" href="/dsfr/utility/icons/icons.min.css" />
<link rel="apple-touch-icon" href="/dsfr/favicon/apple-touch-icon.png" />
<link rel="icon" href="/dsfr/favicon/favicon.svg" type="image/svg+xml" />
```

3. Dans `src/main.tsx` :
```tsx
import { startReactDsfr } from "@codegouvfr/react-dsfr/spa";
import { Link } from "react-router-dom";

startReactDsfr({ defaultColorScheme: "system", Link });

declare module "@codegouvfr/react-dsfr/spa" {
    interface RegisterLink {
        Link: typeof Link;
    }
}
```

## Next.js App Router

> **Attention — chemins d'import v1.30+** : depuis react-dsfr v1.30, le module Next.js App Router s'appelle `next-app-router` (et non `next-appdir`). Les exports sont `DsfrHeadBase`, `DsfrProviderBase`, `StartDsfrOnHydration` et `createGetHtmlAttributes`. Les anciens noms (`DsfrHead`, `DsfrProvider`, `StartDsfr`, `getHtmlAttributes`) n'existent plus dans le package.

### Comprendre le flash dark mode

Le flash blanc au chargement en mode sombre est la régression la plus courante avec react-dsfr en App Router. Deux éléments sont **indispensables** pour l'éviter (le pattern recommandé ci-dessous les inclut) :

1. **`createGetHtmlAttributes()`** : crée une fonction qui retourne les attributs `data-fr-scheme`, `data-fr-theme` et `suppressHydrationWarning` pour la balise `<html>` côté SSR.
2. **`getScriptToRunAsap()`** : génère un script inline à placer dans `<head>` qui détecte le thème (localStorage ou `prefers-color-scheme`) **avant** le premier paint CSS.

**Piège courant** : utiliser `DsfrProviderBase` seul (sans `getHtmlAttributes` ni le script) provoque un flash car le thème n'est résolu que côté client après hydratation.

### Pattern 1 — Recommandé : sans `transpilePackages` (imports directs)

Cette approche utilise les imports directs depuis `.../getHtmlAttributes` et `.../scriptToRunAsap` pour éviter le tree-shake de `DsfrHead.js` qui tirerait les fonts `.woff2`. Pas besoin de configurer webpack ni de `transpilePackages`.

`src/app/layout.tsx` :

```tsx
import { DsfrProviderBase, StartDsfrOnHydration } from "@codegouvfr/react-dsfr/next-app-router";
import { createGetHtmlAttributes } from "@codegouvfr/react-dsfr/next-app-router/getHtmlAttributes";
import { getScriptToRunAsap } from "@codegouvfr/react-dsfr/useIsDark/scriptToRunAsap";
import "@codegouvfr/react-dsfr/dsfr/dsfr.min.css";
import "@codegouvfr/react-dsfr/dsfr/utility/icons/icons.main.min.css";
import Link from "next/link";

declare module "@codegouvfr/react-dsfr/next-app-router" {
    interface RegisterLink {
        Link: typeof Link;
    }
}

const defaultColorScheme = "system" as const;
const { getHtmlAttributes } = createGetHtmlAttributes({ defaultColorScheme });

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html {...getHtmlAttributes({ lang: "fr" })}>
            <head>
                <script
                    dangerouslySetInnerHTML={{
                        __html: getScriptToRunAsap({
                            defaultColorScheme,
                            nonce: undefined,
                            trustedTypesPolicyName: "react-dsfr",
                        }),
                    }}
                />
            </head>
            <body>
                <DsfrProviderBase lang="fr" Link={Link} defaultColorScheme={defaultColorScheme}>
                    {children}
                    <StartDsfrOnHydration />
                </DsfrProviderBase>
            </body>
        </html>
    );
}
```

**Points clés** :

- `createGetHtmlAttributes` est importé depuis `.../getHtmlAttributes` (pas depuis `next-app-router` directement, qui tire `DsfrHead` et ses fonts `.woff2`)
- Le CSS DSFR est importé via `import "@codegouvfr/react-dsfr/dsfr/dsfr.min.css"` (géré par Next.js — pas besoin de `<link>` manuel ni de copier `public/dsfr/`)
- Le script anti-flash est injecté manuellement via `dangerouslySetInnerHTML`
- `StartDsfrOnHydration` re-scan le DOM après hydratation React pour bind les `Display`, modales et accordéons (cf. section "Re-initialisation" plus bas)

> **Sous Content-Security-Policy (CSP)** — fréquent sur les projets administration : `nonce: undefined` ne convient qu'en dev sans CSP. Avec une CSP active, le `<script>` inline serait bloqué. Génère un `nonce` par requête (middleware Next.js ou en-tête serveur), lis-le côté layout via `headers()` de `next/headers`, puis passe-le **à la fois** au prop `nonce` de `getScriptToRunAsap(...)` **et** à l'attribut `nonce` de la balise `<script>`. Renseigne aussi `trustedTypesPolicyName` dans ta directive CSP `trusted-types` (ici `react-dsfr react-dsfr-asap`). Voir la doc react-dsfr (CSP / Trusted Types) pour le détail.

**Pas de `next.config.mjs` requis** pour react-dsfr avec ce pattern. (Tu peux quand même en avoir un pour d'autres besoins Next.js — Next.js 14 ne supporte pas `next.config.ts` côté config, utilise `.mjs` ou `.js`.)

### Pattern 2 — Variante avec `DsfrHeadBase` (nécessite `transpilePackages`)

Si tu préfères que `DsfrHeadBase` gère lui-même les imports DSFR (CSS, fonts, script anti-flash) plutôt que de les injecter à la main, il faut configurer webpack pour transpiler le package et accepter les `.woff2` importés par le SCSS interne :

`next.config.mjs` :

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
    transpilePackages: ["@codegouvfr/react-dsfr"],
    webpack: (config) => {
        config.module.rules.push({
            test: /\.woff2$/,
            type: "asset/resource",
        });
        return config;
    },
};

export default nextConfig;
```

`src/app/layout.tsx` :

```tsx
import { DsfrHeadBase } from "@codegouvfr/react-dsfr/next-app-router/DsfrHead";
import { DsfrProviderBase, StartDsfrOnHydration } from "@codegouvfr/react-dsfr/next-app-router";
import { createGetHtmlAttributes } from "@codegouvfr/react-dsfr/next-app-router/getHtmlAttributes";
import "@codegouvfr/react-dsfr/dsfr/utility/icons/icons.main.min.css";
import Link from "next/link";

declare module "@codegouvfr/react-dsfr/next-app-router" {
    interface RegisterLink {
        Link: typeof Link;
    }
}

const defaultColorScheme = "system" as const;
const { getHtmlAttributes } = createGetHtmlAttributes({ defaultColorScheme });

export default function RootLayout({ children }: { children: React.ReactNode }) {
    const lang = "fr";
    return (
        <html {...getHtmlAttributes({ lang })}>
            <head>
                <DsfrHeadBase Link={Link} />
            </head>
            <body>
                <DsfrProviderBase lang={lang} Link={Link} defaultColorScheme={defaultColorScheme}>
                    {children}
                    <StartDsfrOnHydration />
                </DsfrProviderBase>
            </body>
        </html>
    );
}
```

> **Placement de `StartDsfrOnHydration`** : c'est un composant client qui ne fait que lancer un `useEffect` au montage (il rend `null`). Sa position dans le DOM est donc sans effet fonctionnel : on le place dans le `<body>`, à l'intérieur de `DsfrProviderBase`, **identique au Pattern 1**. Éviter de le mettre dans `<head>` — un composant client dans `<head>` peut déclencher un warning d'hydratation sur Next.js 15 / React 19 pour aucun bénéfice.

### Choisir entre Pattern 1 et Pattern 2

| Critère | Pattern 1 (imports directs) | Pattern 2 (`DsfrHeadBase`) |
|---|---|---|
| `transpilePackages` requis | Non | Oui |
| Règle webpack `.woff2` requise | Non | Oui |
| Anti-flash | À la main (script inline) | Géré par `DsfrHeadBase` |
| Surface webpack | Minimale | Étendue |
| Recommandation | ✅ Par défaut | Si tu utilises déjà `transpilePackages` pour d'autres raisons |

### Chargement des icônes DSFR

Le composant `DsfrHeadBase` (et le SCSS embarqué) importe un fichier qui n'inclut **que les icônes détectées** par le script `react-dsfr update-icons`. Ce script scanne les fichiers source du projet à la recherche de noms d'icônes. Cependant, les icônes passées dynamiquement en props (par exemple `iconId: "fr-icon-add-circle-line"` dans un `Header`) ne sont **pas détectées** par le scanner.

**Symptôme** : un carré coloré vide s'affiche à la place de l'icône.

**Solution recommandée** : importer le CSS complet des icônes dans le layout (déjà inclus dans les deux patterns ci-dessus) :

```tsx
import "@codegouvfr/react-dsfr/dsfr/utility/icons/icons.main.min.css";
```

Ce fichier contient toutes les icônes DSFR et Remix Icon. Il est plus lourd que le bundle optimisé par `update-icons`, mais garantit que toutes les icônes fonctionnent sans configuration supplémentaire.

> **`icons.main.min.css` vs `icons.min.css`** : ces deux fichiers ont un contenu **identique** (jeu d'icônes complet). La différence est le mode de chargement, pas le contenu : en Next.js on importe le module `.../icons/icons.main.min.css` (résolu par le bundler), tandis qu'en Vite on sert le fichier `/dsfr/utility/icons/icons.min.css` copié dans `public/` via une balise `<link>`. C'est pourquoi la section Vite plus haut référence `icons.min.css` et la section Next.js `icons.main.min.css` — c'est volontaire et correct.

**Alternative** (optimisée mais fragile) : ne pas importer ce CSS et s'appuyer uniquement sur le SCSS généré par `react-dsfr update-icons`. Dans ce cas, vérifier que le script postinstall est configuré et que toutes les icônes utilisées sont détectées. Les icônes utilisées via `iconId` en prop string ne seront probablement pas détectées.

### Re-initialisation DSFR après hydratation React (Display, modales)

Le JS DSFR scanne le DOM au chargement initial pour bind les événements (modales, disclosures, accordéons). Mais React hydrate **après** ce scan : les éléments rendus par React (comme `<Display />` ou des modales `createModal`) ne sont pas découverts.

**Symptôme** : les boutons avec `aria-controls` sont présents dans le DOM mais ne déclenchent rien au clic.

**Solution standard** : utiliser `<StartDsfrOnHydration />` du package (déjà inclus dans les deux patterns ci-dessus). Ce composant appelle `window.dsfr.start()` au montage côté client pour forcer un re-scan du DOM.

**Fallback manuel** : si pour une raison spécifique `StartDsfrOnHydration` ne suffit pas (cas exotiques de routing dynamique, par exemple), tu peux écrire un client component équivalent :

```tsx
// components/DsfrStartup.tsx
"use client";

import { useEffect } from "react";

export function DsfrStartup() {
    useEffect(() => {
        if (typeof window !== "undefined" && window.dsfr) {
            window.dsfr.start();
        }
    }, []);
    return null;
}
```

Et le placer dans le layout après tous les composants DSFR :

```tsx
<DsfrProviderBase lang="fr" Link={Link} defaultColorScheme={defaultColorScheme}>
    <Header />
    <main>{children}</main>
    <Footer />
    <Display />
    <DsfrStartup />
</DsfrProviderBase>
```

**Important** : sans ce re-scan, les composants suivants ne fonctionneront pas au clic :
- `<Display />` (paramètres d'affichage)
- Modales créées via `createModal()`
- Tout composant DSFR qui repose sur le mécanisme natif de disclosure (`aria-controls`)

## Next.js Pages Router

1. Ajouter dans `next.config.js` :
```js
module.exports = {
    transpilePackages: ["@codegouvfr/react-dsfr", "tss-react"],
};
```

2. Configurer `pages/_app.tsx` et `pages/_document.tsx` avec `createNextDsfrIntegrationApi` :
```tsx
import Link from "next/link";
import { createNextDsfrIntegrationApi } from "@codegouvfr/react-dsfr/next-pagesdir";

declare module "@codegouvfr/react-dsfr/next-pagesdir" {
    interface RegisterLink {
        Link: typeof Link;
    }
}

const { withDsfr, dsfrDocumentApi } = createNextDsfrIntegrationApi({
    defaultColorScheme: "system",
    Link,
});

// Dans _app.tsx : export default withDsfr(App);
// Dans _document.tsx : utiliser dsfrDocumentApi
```

## ESLint avec react-dsfr

### Configuration requise

Un projet Next.js + DSFR avec du contenu français nécessite un `.eslintrc.json` **avant** de lancer `next lint`, sinon la commande bloque en mode interactif (échec garanti en CI).

```json
{
  "extends": "next/core-web-vitals",
  "rules": {
    "react/no-unescaped-entities": "off"
  }
}
```

### Pourquoi cette règle est désactivée

- **`react/no-unescaped-entities`** : le texte français contient des apostrophes partout (`l'État`, `d'utilisation`, `n'est`). Forcer `&apos;` sur chaque occurrence rend le JSX illisible. Cette règle est conçue pour l'anglais où les apostrophes dans le JSX sont rares.

> **Note** — `@next/next/no-css-tags` : les patterns Next.js recommandés ci-dessus (Pattern 1 **et** Pattern 2) chargent le CSS DSFR via `import`, **sans `<link>` manuel** dans le layout. La règle `@next/next/no-css-tags` ne se déclenche donc pas et n'a pas besoin d'être désactivée. Ne l'ajouter (`"@next/next/no-css-tags": "off"`) **que** si tu charges un CSS via une balise `<link rel="stylesheet">` manuelle (approche non recommandée en App Router).

### Compatibilité ESLint / Next.js

| Next.js | ESLint | eslint-config-next |
|---------|--------|--------------------|
| 14.x    | 8.x    | 14.x               |
| 15.x    | 9.x    | 15.x               |

**Piège** : `npm install eslint` installe ESLint 9 par défaut, qui est incompatible avec Next.js 14 (`Unknown options: useEslintrc, extensions...`). Forcer la version : `npm install --save-dev eslint@^8 eslint-config-next@14`.

---

## Create React App

1. Scripts dans `package.json` :
```json
{
  "scripts": {
    "postinstall": "react-dsfr update-icons",
    "prestart": "react-dsfr update-icons",
    "prebuild": "react-dsfr update-icons"
  }
}
```

2. Configurer Jest : `transformIgnorePatterns: []`

3. Lier les assets DSFR dans `public/index.html` et initialiser dans `src/index.tsx` avec `startReactDsfr`.
