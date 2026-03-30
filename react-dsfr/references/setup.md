# Setup react-dsfr par framework

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

1. Ajouter `transpilePackages` et la règle webpack pour les fonts dans `next.config.mjs` :

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

> **Note** : Next.js 14 ne supporte pas `next.config.ts`. Utiliser `.mjs` ou `.js`.

2. Dans `src/app/layout.tsx` :
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
                <StartDsfrOnHydration />
                <DsfrHeadBase Link={Link} />
            </head>
            <body>
                <DsfrProviderBase lang={lang} Link={Link} defaultColorScheme={defaultColorScheme}>
                    {children}
                </DsfrProviderBase>
            </body>
        </html>
    );
}
```

### Chargement des icônes DSFR

Le composant `DsfrHeadBase` importe un fichier SCSS (`dsfr_plus_icons.scss`) qui n'inclut **que les icônes détectées** par le script `react-dsfr update-icons`. Ce script scanne les fichiers source du projet à la recherche de noms d'icônes. Cependant, les icônes passées dynamiquement en props (par exemple `iconId: "fr-icon-add-circle-line"` dans un `Header`) ne sont **pas détectées** par le scanner.

**Symptôme** : un carré coloré vide s'affiche à la place de l'icône.

**Solution recommandée** : importer le CSS complet des icônes dans le layout :

```tsx
import "@codegouvfr/react-dsfr/dsfr/utility/icons/icons.main.min.css";
```

Ce fichier contient toutes les icônes DSFR et Remix Icon. Il est plus lourd que le bundle optimisé par `update-icons`, mais garantit que toutes les icônes fonctionnent sans configuration supplémentaire.

**Alternative** (optimisée mais fragile) : ne pas importer ce CSS et s'appuyer uniquement sur le SCSS généré par `react-dsfr update-icons`. Dans ce cas, vérifier que le script postinstall est configuré et que toutes les icônes utilisées sont détectées. Les icônes utilisées via `iconId` en prop string ne seront probablement pas détectées.

### Prévention du flash dark mode (Next.js App Router)

Le flash blanc au chargement en mode sombre est un problème courant. Deux éléments sont **indispensables** pour l'éviter :

1. **`createGetHtmlAttributes()`** : crée une fonction qui retourne les attributs `data-fr-scheme`, `data-fr-theme` et `suppressHydrationWarning` pour la balise `<html>` côté SSR.

2. **`getScriptToRunAsap()`** : génère un script inline à placer dans `<head>` qui détecte le thème (localStorage ou `prefers-color-scheme`) **avant** le premier paint CSS.

**Piège courant** : utiliser `DsfrProviderBase` seul (sans `getHtmlAttributes` ni le script) provoque un flash car le thème n'est résolu que côté client après hydratation.

#### Setup sans `transpilePackages`

Sans `transpilePackages`, `DsfrHeadBase` échoue au build car webpack ne sait pas traiter les `.woff2` importés par le SCSS. Dans ce cas, utiliser les imports directs :

```tsx
import { DsfrProviderBase } from '@codegouvfr/react-dsfr/next-app-router';
import { createGetHtmlAttributes } from '@codegouvfr/react-dsfr/next-app-router/getHtmlAttributes';
import { getScriptToRunAsap } from '@codegouvfr/react-dsfr/useIsDark/scriptToRunAsap';
import '@codegouvfr/react-dsfr/dsfr/dsfr.min.css';
import '@codegouvfr/react-dsfr/dsfr/utility/icons/icons.main.min.css';

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
                </DsfrProviderBase>
            </body>
        </html>
    );
}
```

**Points clés** :
- `createGetHtmlAttributes` est importé depuis `.../getHtmlAttributes` (pas `server-only-index` qui tire `DsfrHead` et ses fonts)
- Le CSS DSFR est importé via `import '@codegouvfr/react-dsfr/dsfr/dsfr.min.css'` (géré par Next.js)
- Le script anti-flash est injecté manuellement via `dangerouslySetInnerHTML`

### Re-initialisation DSFR après hydratation React

Le JS DSFR scanne le DOM au chargement initial pour bind les événements (modales, disclosures, accordéons). Mais React hydrate **après** ce scan : les éléments rendus par React (comme `<Display />` ou des modales `createModal`) ne sont pas découverts.

**Symptôme** : les boutons avec `aria-controls` sont présents dans le DOM mais ne déclenchent rien au clic.

**Solution** : appeler `window.dsfr.start()` après l'hydratation React pour forcer un re-scan du DOM.

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

Placer `<DsfrStartup />` dans le layout racine, après tous les composants DSFR :

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
    "react/no-unescaped-entities": "off",
    "@next/next/no-css-tags": "off"
  }
}
```

### Pourquoi ces règles sont désactivées

- **`react/no-unescaped-entities`** : le texte français contient des apostrophes partout (`l'État`, `d'utilisation`, `n'est`). Forcer `&apos;` sur chaque occurrence rend le JSX illisible. Cette règle est conçue pour l'anglais où les apostrophes dans le JSX sont rares.

- **`@next/next/no-css-tags`** : react-dsfr nécessite un `<link>` manuel vers `/dsfr/utility/icons/icons.min.css` dans le layout. Ce fichier statique n'est pas un module CSS et ne peut pas être importé via `import`. Le warning est un faux positif.

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
