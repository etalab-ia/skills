---
name: react-dsfr
description: Créer des interfaces React conformes au Design System de l'État français (DSFR) avec @codegouvfr/react-dsfr. Utiliser cette skill quand l'utilisateur demande de créer des pages, composants ou interfaces en React utilisant le DSFR, quand il mentionne react-dsfr, le design system de l'État, ou quand le projet utilise @codegouvfr/react-dsfr. Couvre les composants natifs react-dsfr (pas MUI), le routing, les icônes, les couleurs et les patterns de mise en page.
---

# react-dsfr

Bibliothèque React pour le Design System de l'État français. Package : `@codegouvfr/react-dsfr`.

## Import pattern

Chaque composant a son propre chemin d'import :
```tsx
import { Button } from "@codegouvfr/react-dsfr/Button";
import { Alert } from "@codegouvfr/react-dsfr/Alert";
import { Card } from "@codegouvfr/react-dsfr/Card";
// etc.
```

## Routing et liens

Enregistrer le composant `Link` du framework une seule fois au démarrage. Tous les composants react-dsfr utilisant `linkProps` s'en serviront automatiquement.

- Liens internes : utilisent le routeur (client-side navigation)
- URLs externes (`https://...`) : rendus comme `<a>` classiques
- `href="#"` + `onClick` : convertis automatiquement en `<button>` accessible

Voir [references/setup.md](references/setup.md) pour le setup par framework (Next.js, Vite, CRA).

## Utilitaire CSS : `fr.cx()`

```tsx
import { fr } from "@codegouvfr/react-dsfr";

// Appliquer des classes utilitaires DSFR
<div className={fr.cx("fr-grid-row", "fr-grid-row--gutters")}>
    <div className={fr.cx("fr-col-12", "fr-col-md-6")}>...</div>
</div>

// Spacing
<div className={fr.cx("fr-mt-4w", "fr-mb-2w", "fr-p-3w")}>...</div>
```

## Grille

Le DSFR utilise une grille 12 colonnes :
```tsx
<div className={fr.cx("fr-grid-row", "fr-grid-row--gutters")}>
    <div className={fr.cx("fr-col-12", "fr-col-md-6", "fr-col-lg-4")}>Col 1</div>
    <div className={fr.cx("fr-col-12", "fr-col-md-6", "fr-col-lg-4")}>Col 2</div>
    <div className={fr.cx("fr-col-12", "fr-col-lg-4")}>Col 3</div>
</div>
```

Breakpoints : `sm` (576px), `md` (768px), `lg` (992px), `xl` (1248px).

## Icônes

Deux familles d'icônes disponibles :
- **DSFR** : `fr-icon-*` (ex: `"fr-icon-add-line"`, `"fr-icon-delete-fill"`, `"fr-icon-arrow-right-line"`)
- **Remix Icon** : `ri-*` (ex: `"ri-account-box-line"`, `"ri-information-line"`)

Les icônes sont typées : TypeScript offre l'autocomplétion.

## Couleurs et thème

```tsx
import { useColors } from "@codegouvfr/react-dsfr/useColors";

function MyComponent() {
    const theme = useColors();
    // theme.decisions.background.default.grey.default
    // theme.decisions.text.title.grey.default
    // theme.decisions.border.default.grey.default
}
```

Le thème respecte automatiquement le mode clair/sombre.

**Attention au flash dark mode** : en Next.js App Router, utiliser `getHtmlAttributes()` + `<StartDsfr />` + `<DsfrHead />` pour éviter le flash blanc au chargement. Voir [references/setup.md](references/setup.md#prévention-du-flash-dark-mode-nextjs-app-router) pour le détail.

## Pattern : page complète

```tsx
import { Header } from "@codegouvfr/react-dsfr/Header";
import { Footer } from "@codegouvfr/react-dsfr/Footer";
import { Breadcrumb } from "@codegouvfr/react-dsfr/Breadcrumb";
import { fr } from "@codegouvfr/react-dsfr";

export function Page() {
    return (
        <>
            <Header
                brandTop={<>RÉPUBLIQUE<br />FRANÇAISE</>}
                homeLinkProps={{ href: "/", title: "Accueil" }}
                serviceTitle="Mon service"
            />
            <div className={fr.cx("fr-container", "fr-my-4w")}>
                <Breadcrumb
                    homeLinkProps={{ href: "/" }}
                    segments={[{ label: "Section", linkProps: { href: "/section" } }]}
                    currentPageLabel="Page courante"
                />
                <h1>Titre de la page</h1>
                {/* Contenu */}
            </div>
            <Footer
                accessibility="partially compliant"
                brandTop={<>RÉPUBLIQUE<br />FRANÇAISE</>}
                homeLinkProps={{ href: "/", title: "Accueil" }}
            />
        </>
    );
}
```

## Pattern : page avec menu latéral

```tsx
<div className={fr.cx("fr-container", "fr-my-4w")}>
    <div className={fr.cx("fr-grid-row", "fr-grid-row--gutters")}>
        <div className={fr.cx("fr-col-12", "fr-col-md-4")}>
            <SideMenu
                title="Rubrique"
                burgerMenuButtonText="Menu"
                items={[
                    { text: "Page 1", linkProps: { href: "/p1" }, isActive: true },
                    { text: "Page 2", linkProps: { href: "/p2" } },
                ]}
            />
        </div>
        <div className={fr.cx("fr-col-12", "fr-col-md-8")}>
            {/* Contenu principal */}
        </div>
    </div>
</div>
```

## Pattern : formulaire

```tsx
import { Input } from "@codegouvfr/react-dsfr/Input";
import { Select } from "@codegouvfr/react-dsfr/Select";
import { Checkbox } from "@codegouvfr/react-dsfr/Checkbox";
import { ButtonsGroup } from "@codegouvfr/react-dsfr/ButtonsGroup";
import { Alert } from "@codegouvfr/react-dsfr/Alert";

export function MyForm() {
    return (
        <form>
            <Input label="Nom" nativeInputProps={{ required: true }} />
            <Input label="Email" nativeInputProps={{ type: "email" }} />
            <Select label="Département" nativeSelectProps={{ name: "dept" }}>
                <option value="" disabled hidden>Sélectionnez</option>
                <option value="75">Paris</option>
            </Select>
            <Checkbox
                legend="Préférences"
                options={[{ label: "Newsletter", nativeInputProps: { name: "newsletter" } }]}
            />
            <ButtonsGroup
                inlineLayoutWhen="always"
                buttons={[
                    { children: "Envoyer", type: "submit" },
                    { children: "Annuler", priority: "secondary", type: "reset" },
                ]}
            />
        </form>
    );
}
```

## Pattern : liste de cartes

```tsx
<div className={fr.cx("fr-grid-row", "fr-grid-row--gutters")}>
    {items.map(item => (
        <div key={item.id} className={fr.cx("fr-col-12", "fr-col-md-6", "fr-col-lg-4")}>
            <Card
                enlargeLink
                title={item.title}
                desc={item.description}
                linkProps={{ href: `/items/${item.id}` }}
                imageUrl={item.imageUrl}
                imageAlt={item.imageAlt}
                badge={<Badge severity="info">{item.category}</Badge>}
            />
        </div>
    ))}
</div>
```

## Référence des composants

Consulter [references/components.md](references/components.md) pour l'API complète de chaque composant :
- **Layout** : Header, Footer, SideMenu, Breadcrumb, Pagination, Stepper
- **Contenu** : Card, Tile, Table, Accordion, Tabs, Badge, Tag, Quote, Highlight, CallOut
- **Formulaires** : Input, Select, Checkbox, RadioButtons, ToggleSwitch, Upload, Button, ButtonsGroup
- **Feedback** : Alert, Notice, Modal

## Setup par framework

Consulter [references/setup.md](references/setup.md) pour l'installation et la configuration avec Next.js (App Router / Pages Router), Vite ou Create React App.
