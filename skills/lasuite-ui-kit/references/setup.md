# Setup @gouvfr-lasuite/ui-kit

## Installation

```bash
npm install @gouvfr-lasuite/ui-kit @gouvfr-lasuite/cunningham-react @gouvfr-lasuite/cunningham-tokens @fontsource/material-icons
# ou yarn add / pnpm add
```

Dépendances peer requises : `react >= 19`, `react-dom >= 19`.

## Configuration Cunningham

Créer un fichier `cunningham.ts` à la racine du projet :

```typescript
import { cunninghamConfig } from "@gouvfr-lasuite/ui-kit";

export default {
  ...cunninghamConfig,
};
```

Ce fichier est lu par le toolchain Cunningham pour générer les design tokens CSS. Il peut être étendu pour surcharger des tokens :

```typescript
import { cunninghamConfig } from "@gouvfr-lasuite/ui-kit";

export default {
  ...cunninghamConfig,
  // Surcharges locales
  themes: {
    ...cunninghamConfig.themes,
    default: {
      ...cunninghamConfig.themes.default,
      theme: {
        ...cunninghamConfig.themes.default.theme,
        font: {
          ...cunninghamConfig.themes.default.theme.font,
          sizes: {
            ...cunninghamConfig.themes.default.theme.font.sizes,
            h1: "2.5rem",
          },
        },
      },
    },
  },
};
```

## Génération des tokens CSS

Après avoir créé `cunningham.ts`, générer les tokens :

```bash
npx cunningham -g css,scss,ts -o src
```

Cela génère les fichiers de variables CSS (`cunningham-tokens.css`) utilisées par les composants.

## Styles

Importer les styles dans le point d'entrée de l'application :

```typescript
// Styles de base des composants ui-kit
import "@gouvfr-lasuite/ui-kit/style";

// Police Marianne (optionnel, utilisée par défaut dans le thème LaSuite)
import "@gouvfr-lasuite/ui-kit/fonts/Marianne";

// Tokens CSS générés
import "./cunningham-tokens.css";
```

En SCSS, les fonts peuvent être importées via :
```scss
@import "@gouvfr-lasuite/ui-kit/sass/fonts";
```

## Provider

Envelopper l'application avec `CunninghamProvider` importé depuis **`@gouvfr-lasuite/ui-kit`** (et non depuis `@gouvfr-lasuite/cunningham-react`) :

```tsx
import { CunninghamProvider } from "@gouvfr-lasuite/ui-kit";

function App() {
  return (
    <CunninghamProvider>
      {children}
    </CunninghamProvider>
  );
}
```

**Important** : le provider du ui-kit enrichit celui de cunningham-react avec les traductions LaSuite (FR/EN). Utiliser directement celui de cunningham-react ferait perdre ces traductions.

## Vite

Aucune configuration spéciale requise. Exemple minimal `vite.config.ts` :

```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
});
```

## Next.js App Router

`CunninghamProvider` est un composant client. Créer un wrapper :

```tsx
// src/components/ClientProviders.tsx
"use client";

import { CunninghamProvider } from "@gouvfr-lasuite/ui-kit";

export function ClientProviders({ children }: { children: React.ReactNode }) {
  return <CunninghamProvider>{children}</CunninghamProvider>;
}
```

```tsx
// src/app/layout.tsx
import { ClientProviders } from "@/components/ClientProviders";
import "@gouvfr-lasuite/ui-kit/style";
import "@gouvfr-lasuite/ui-kit/fonts/Marianne";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body>
        <ClientProviders>{children}</ClientProviders>
      </body>
    </html>
  );
}
```

## Next.js Pages Router

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import { CunninghamProvider } from "@gouvfr-lasuite/ui-kit";
import "@gouvfr-lasuite/ui-kit/style";
import "@gouvfr-lasuite/ui-kit/fonts/Marianne";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <CunninghamProvider>
      <Component {...pageProps} />
    </CunninghamProvider>
  );
}
```

## Thèmes

Le ui-kit fournit trois palettes de couleurs globales :

| Thème | Import | Usage |
|-------|--------|-------|
| White Label (défaut) | `whiteLabelGlobals` | Applications LaSuite standard (violet/bleu) |
| DSFR | `dsfrGlobals` | Applications respectant le Design System de l'État |
| ANCT | `anctGlobals` | Applications de l'Agence Nationale de la Cohésion des Territoires |

Les thèmes sont déjà configurés dans `cunninghamConfig`. Le thème par défaut est White Label avec support du mode sombre.

## i18n

Le `CunninghamProvider` du ui-kit injecte automatiquement des traductions FR et EN pour les labels internes des composants (boutons, pagination, messages vides, etc.).

Pour accéder aux traductions dans vos composants :

```tsx
import { useCustomTranslations } from "@gouvfr-lasuite/ui-kit";

function MyComponent() {
  const { t } = useCustomTranslations();
  return <span>{t("some.key")}</span>;
}
```

## Design tokens CSS

Les composants utilisent des CSS custom properties Cunningham. Les plus courantes :

```css
/* Couleurs */
var(--c--theme--colors--primary-600)
var(--c--theme--colors--primary-text)
var(--c--theme--colors--secondary-600)
var(--c--theme--colors--greyscale-100)

/* Espacements */
var(--c--theme--spacings--xs)    /* 0.5rem */
var(--c--theme--spacings--sm)    /* 0.75rem */
var(--c--theme--spacings--base)  /* 1rem */
var(--c--theme--spacings--md)    /* 1.5rem */
var(--c--theme--spacings--lg)    /* 2rem */

/* Typographie */
var(--c--theme--font--sizes--sm)   /* 0.875rem */
var(--c--theme--font--sizes--md)   /* 1rem */
var(--c--theme--font--sizes--lg)   /* 1.125rem */
var(--c--theme--font--sizes--h1)   /* 2rem */

/* Breakpoints */
var(--c--theme--breakpoints--mobile)   /* 768px */
var(--c--theme--breakpoints--tablet)   /* 1024px */
```

## Différence @openfun vs @gouvfr-lasuite

`@gouvfr-lasuite/cunningham-react` est le fork gouvernemental de `@openfun/cunningham-react`. Les deux sont fonctionnellement identiques. Les anciens projets utilisent encore `@openfun/*`, les nouveaux doivent utiliser `@gouvfr-lasuite/*`. Les imports et l'API sont les mêmes.
