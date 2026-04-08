# Référence composants react-dsfr

Tous les imports suivent le pattern : `import { Component } from "@codegouvfr/react-dsfr/Component"`

## Table des matières

- [Layout](#layout) : Header, Footer, SideMenu, Breadcrumb, Pagination, Stepper, SkipLinks
- [Contenu](#contenu) : Card, Tile, Table, Accordion, Tabs, Badge, Tag, Quote, Highlight, CallOut, Display
- [Formulaires](#formulaires) : Input, Select, SelectNext, Checkbox, RadioButtons, ToggleSwitch, Upload, Button, ButtonsGroup, Range
- [Feedback](#feedback) : Alert, Notice, Modal
- [Navigation](#navigation) : MainNavigation (intégré dans Header)

---

## Layout

### Header

```tsx
import { Header } from "@codegouvfr/react-dsfr/Header";
```

| Prop | Type | Requis |
|------|------|--------|
| `brandTop` | `ReactNode` | Oui |
| `homeLinkProps` | `RegisteredLinkProps & { title: string }` | Oui |
| `serviceTitle` | `ReactNode` | Non |
| `serviceTagline` | `ReactNode` | Non |
| `navigation` | `MainNavigationProps.Item[] \| ReactNode` | Non |
| `quickAccessItems` | `(QuickAccessItem \| JSX.Element)[]` | Non |
| `operatorLogo` | `{ orientation: "horizontal"\|"vertical"; imgUrl: string; alt: string }` | Non |
| `renderSearchInput` | `(params) => JSX.Element` | Non |
| `onSearchButtonClick` | `(text: string) => void` | Non |

**Navigation items :**
- `Link` : `{ text, linkProps, isActive? }`
- `Menu` : `{ text, menuLinks: { text, linkProps }[] }`
- `MegaMenu` : `{ text, megaMenu: { leader?, categories } }`

**QuickAccessItem :**
- `{ iconId, text, linkProps }` ou `{ iconId, text, buttonProps }`

```tsx
<Header
    brandTop={<>INTITULE<br />OFFICIEL</>}
    homeLinkProps={{ href: "/", title: "Accueil - Mon service" }}
    serviceTitle="Nom du service"
    serviceTagline="Baseline du service"
    quickAccessItems={[
        { iconId: "fr-icon-add-circle-line", text: "Créer un espace", linkProps: { href: "#" } },
        { iconId: "ri-account-box-line", text: "Se connecter", buttonProps: { onClick: () => {} } },
    ]}
    navigation={[
        { text: "Accueil", linkProps: { href: "/" }, isActive: true },
        { text: "Rubrique", linkProps: { href: "/rubrique" } },
    ]}
/>
```

### Footer

```tsx
import { Footer } from "@codegouvfr/react-dsfr/Footer";
```

| Prop | Type | Requis |
|------|------|--------|
| `accessibility` | `"non compliant" \| "partially compliant" \| "fully compliant"` | Oui |
| `contentDescription` | `ReactNode` | Non |
| `websiteMapLinkProps` | `RegisteredLinkProps` | Non |
| `termsLinkProps` | `RegisteredLinkProps` | Non |
| `bottomItems` | `(BottomItem \| ReactNode)[]` | Non |
| `brandTop` | `ReactNode` | Non |
| `homeLinkProps` | `RegisteredLinkProps & { title: string }` | Non |
| `operatorLogo` | `{ orientation, imgUrl, alt }` | Non |
| `partnersLogos` | `{ main?: Logo; sub?: Logo[] }` | Non |
| `linkList` | `{ categoryName?, links: { text, linkProps }[] }[]` (1-6 colonnes) | Non |
| `domains` | `string[]` | Non (défaut: sites gouv.fr) |

```tsx
<Footer
    accessibility="fully compliant"
    contentDescription="Description du site"
    brandTop={<>RÉPUBLIQUE<br />FRANÇAISE</>}
    homeLinkProps={{ href: "/", title: "Accueil" }}
/>
```

### SideMenu

```tsx
import { SideMenu } from "@codegouvfr/react-dsfr/SideMenu";
```

| Prop | Type | Requis |
|------|------|--------|
| `items` | `SideMenuProps.Item[]` | Oui |
| `burgerMenuButtonText` | `ReactNode` | Oui |
| `title` | `ReactNode` | Non |
| `align` | `"left" \| "right"` | Non |
| `sticky` | `boolean` | Non |
| `fullHeight` | `boolean` | Non |

**Item :** `{ text, linkProps, isActive? }` ou `{ text, items: Item[], expandedByDefault? }`

```tsx
<SideMenu
    title="Rubrique"
    burgerMenuButtonText="Dans cette rubrique"
    items={[
        { isActive: true, text: "Lien actif", linkProps: { href: "#" } },
        { text: "Section", expandedByDefault: true, items: [
            { text: "Sous-item", linkProps: { href: "#" } }
        ]}
    ]}
/>
```

### Breadcrumb

```tsx
import { Breadcrumb } from "@codegouvfr/react-dsfr/Breadcrumb";
```

| Prop | Type | Requis |
|------|------|--------|
| `segments` | `{ label: ReactNode; linkProps: RegisteredLinkProps }[]` | Oui |
| `currentPageLabel` | `ReactNode` | Oui |
| `homeLinkProps` | `RegisteredLinkProps` | Non |

```tsx
<Breadcrumb
    homeLinkProps={{ href: "/" }}
    segments={[{ label: "Section", linkProps: { href: "/section" } }]}
    currentPageLabel="Page courante"
/>
```

### Pagination

```tsx
import { Pagination } from "@codegouvfr/react-dsfr/Pagination";
```

| Prop | Type | Requis |
|------|------|--------|
| `count` | `number` | Oui |
| `defaultPage` | `number` | Non (défaut: 1) |
| `getPageLinkProps` | `(pageNumber: number) => RegisteredLinkProps` | Oui |
| `showFirstLast` | `boolean` | Non (défaut: true) |

```tsx
<Pagination count={100} defaultPage={1} getPageLinkProps={p => ({ href: `/page/${p}` })} />
```

### Stepper

```tsx
import { Stepper } from "@codegouvfr/react-dsfr/Stepper";
```

| Prop | Type | Requis |
|------|------|--------|
| `currentStep` | `number` | Oui |
| `stepCount` | `number` | Oui |
| `title` | `ReactNode` | Oui |
| `nextTitle` | `ReactNode` | Non |

```tsx
<Stepper stepCount={3} currentStep={1} title="Étape en cours" nextTitle="Prochaine étape" />
```

---

## Contenu

### Card

```tsx
import { Card } from "@codegouvfr/react-dsfr/Card";
```

| Prop | Type | Requis |
|------|------|--------|
| `title` | `ReactNode` | Oui |
| `titleAs` | `` `h${2-6}` `` | Non |
| `desc` | `ReactNode` | Non |
| `detail` | `ReactNode` | Non |
| `endDetail` | `ReactNode` | Non |
| `footer` | `ReactNode` | Non |
| `size` | `"small" \| "medium" \| "large"` | Non |
| `enlargeLink` | `boolean` | Non |
| `linkProps` | `RegisteredLinkProps` | Non (requis si enlargeLink) |
| `horizontal` | `boolean` | Non |
| `ratio` | `"33/66" \| "50/50"` | Non (horizontal uniquement) |
| `imageUrl` | `string` | Non |
| `imageAlt` | `string` | Non (requis si imageUrl) |
| `badge` | `ReactNode` | Non |
| `grey` | `boolean` | Non |
| `shadow` | `boolean` | Non |
| `border` | `boolean` | Non |

```tsx
<Card
    enlargeLink
    title="Titre de la carte"
    desc="Description de la carte"
    linkProps={{ href: "#" }}
    imageUrl="/img.jpg"
    imageAlt="Alt"
    badge={<Badge severity="info">Nouveau</Badge>}
/>

// Horizontale
<Card horizontal ratio="33/66" enlargeLink title="Titre" desc="Description" linkProps={{ href: "#" }} imageUrl="/img.jpg" imageAlt="Alt" />
```

### Tile

```tsx
import { Tile } from "@codegouvfr/react-dsfr/Tile";
```

| Prop | Type | Requis |
|------|------|--------|
| `title` | `ReactNode` | Oui |
| `linkProps` | `RegisteredLinkProps` | Non (union avec buttonProps) |
| `desc` | `ReactNode` | Non |
| `detail` | `ReactNode` | Non |
| `start` | `ReactNode` | Non |
| `orientation` | `"horizontal" \| "vertical"` | Non |
| `small` | `boolean` | Non |
| `grey` | `boolean` | Non |
| `imageUrl` | `string` | Non |
| `imageSvg` | `boolean` | Non |
| `pictogram` | `ReactNode` | Non |

```tsx
<Tile title="Tuile" linkProps={{ href: "#" }} desc="Description" imageUrl="/picto.svg" imageSvg />
```

### Table

```tsx
import { Table } from "@codegouvfr/react-dsfr/Table";
```

| Prop | Type | Requis |
|------|------|--------|
| `data` | `ReactNode[][]` | Oui |
| `headers` | `ReactNode[]` | Non |
| `caption` | `ReactNode` | Non |
| `fixed` | `boolean` | Non |
| `bordered` | `boolean` | Non |
| `noScroll` | `boolean` | Non |
| `noCaption` | `boolean` | Non |
| `bottomCaption` | `boolean` | Non |
| `colorVariant` | `string` (ex: `"green-emeraude"`) | Non |

```tsx
<Table
    caption="Résumé"
    headers={["Nom", "Prénom", "Rôle"]}
    data={[
        ["Dupont", "Marie", "Admin"],
        ["Martin", "Jean", "Éditeur"],
    ]}
/>
```

### Accordion

```tsx
import { Accordion } from "@codegouvfr/react-dsfr/Accordion";
```

| Prop | Type | Requis |
|------|------|--------|
| `label` | `ReactNode` | Oui |
| `children` | `ReactNode` | Oui |
| `titleAs` | `` `h${2-6}` `` | Non (défaut: "h3") |
| `defaultExpanded` | `boolean` | Non (uncontrolled) |
| `expanded` | `boolean` | Non (controlled) |
| `onExpandedChange` | `(expanded: boolean, e) => void` | Non |

```tsx
<div className={fr.cx("fr-accordions-group")}>
    <Accordion label="Section 1">Contenu 1</Accordion>
    <Accordion label="Section 2">Contenu 2</Accordion>
</div>
```

### Tabs

```tsx
import { Tabs } from "@codegouvfr/react-dsfr/Tabs";
```

**Uncontrolled :**
```tsx
<Tabs tabs={[
    { label: "Onglet 1", iconId: "fr-icon-add-line", content: <p>Contenu 1</p> },
    { label: "Onglet 2", isDefault: true, content: <p>Contenu 2</p> },
]} />
```

**Controlled :**
```tsx
const [selectedTabId, setSelectedTabId] = useState("tab1");
<Tabs
    selectedTabId={selectedTabId}
    tabs={[
        { tabId: "tab1", label: "Onglet 1" },
        { tabId: "tab2", label: "Onglet 2" },
    ]}
    onTabChange={setSelectedTabId}
>
    <p>Contenu de {selectedTabId}</p>
</Tabs>
```

### Badge

```tsx
import { Badge } from "@codegouvfr/react-dsfr/Badge";
```

| Prop | Type | Requis |
|------|------|--------|
| `severity` | `"success" \| "warning" \| "info" \| "error" \| "new"` | Non |
| `small` | `boolean` | Non |
| `noIcon` | `boolean` | Non |
| `as` | `"p" \| "span"` | Non (défaut: "p") |
| `children` | `ReactNode` | Oui |

```tsx
<Badge severity="success">Actif</Badge>
<Badge severity="new" small>Nouveau</Badge>
<Badge as="span" severity="error" noIcon>Erreur</Badge>
```

### Tag

```tsx
import { Tag } from "@codegouvfr/react-dsfr/Tag";
```

Peut être rendu comme lien (`linkProps`), bouton (`nativeButtonProps`), paragraphe ou span (`as="span"`).

| Prop | Type | Requis |
|------|------|--------|
| `children` | `ReactNode` | Oui |
| `small` | `boolean` | Non |
| `iconId` | `FrIconClassName \| RiIconClassName` | Non |
| `linkProps` | `RegisteredLinkProps` | Non (variante lien) |
| `dismissible` | `boolean` | Non (variante bouton) |
| `pressed` | `boolean` | Non (variante bouton) |

```tsx
<Tag>Label</Tag>
<Tag linkProps={{ href: "#" }}>Lien</Tag>
<Tag dismissible nativeButtonProps={{ onClick: () => {} }}>Supprimable</Tag>
<Tag pressed>Activé</Tag>
```

### Quote

```tsx
import { Quote } from "@codegouvfr/react-dsfr/Quote";
```

| Prop | Type | Requis |
|------|------|--------|
| `text` | `ReactNode` | Oui |
| `author` | `ReactNode` | Non |
| `source` | `ReactNode` | Non |
| `sourceUrl` | `string` | Non |
| `imageUrl` | `string` | Non |
| `size` | `"medium" \| "large" \| "xlarge"` | Non (défaut: "xlarge") |
| `accentColor` | `string` (ex: `"pink-macaron"`) | Non |

```tsx
<Quote text="Citation importante" author="Auteur" source={<cite>Source</cite>} />
```

### Highlight

```tsx
import { Highlight } from "@codegouvfr/react-dsfr/Highlight";
```

| Prop | Type | Requis |
|------|------|--------|
| `children` | `ReactNode` | Oui |
| `size` | `"sm" \| "lg"` | Non |

```tsx
<Highlight>Texte mis en exergue.</Highlight>
<Highlight size="lg">Grand texte en exergue.</Highlight>
```

### CallOut

```tsx
import { CallOut } from "@codegouvfr/react-dsfr/CallOut";
```

| Prop | Type | Requis |
|------|------|--------|
| `children` | `ReactNode` | Oui |
| `title` | `ReactNode` | Non |
| `titleAs` | `` `h${2-6}` \| "p" `` | Non |
| `iconId` | `FrIconClassName \| RiIconClassName` | Non |
| `buttonProps` | `ButtonProps` | Non |
| `colorVariant` | `string` (ex: `"green-emeraude"`) | Non |
| `bodyAs` | `"p" \| "div"` | Non (défaut: "p", utiliser "div" pour du HTML complexe) |

```tsx
<CallOut title="Mise en avant" iconId="ri-information-line" buttonProps={{ children: "En savoir plus" }}>
    Texte de la mise en avant.
</CallOut>
```

### Display (paramètres d'affichage)

```tsx
import { Display, headerFooterDisplayItem } from "@codegouvfr/react-dsfr/Display";
```

Le composant `Display` permet à l'utilisateur de choisir le thème d'affichage (clair, sombre, système). Il s'intègre dans le Header et/ou le Footer via `headerFooterDisplayItem`.

**Intégration dans le Header :**
```tsx
<Header
    quickAccessItems={[
        headerFooterDisplayItem,
        // ... autres items
    ]}
/>
```

**Intégration dans le Footer :**
```tsx
<Footer
    bottomItems={[
        headerFooterDisplayItem,
        // ... autres items (mentions légales, etc.)
    ]}
/>
```

**Placement du composant `<Display />`** dans le layout (obligatoire, une seule fois) :
```tsx
import { Display, headerFooterDisplayItem } from "@codegouvfr/react-dsfr/Display";

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html {...getHtmlAttributes({ defaultColorScheme, lang })}>
            <head>
                <StartDsfr />
                <DsfrHead Link={Link} />
            </head>
            <body>
                <DsfrProvider lang={lang}>
                    <Header quickAccessItems={[headerFooterDisplayItem]} />
                    <main>{children}</main>
                    <Footer bottomItems={[headerFooterDisplayItem]} />
                    <Display />
                </DsfrProvider>
            </body>
        </html>
    );
}
```

Le bouton "Paramètres d'affichage" ouvre automatiquement une modale DSFR avec les options Clair / Sombre / Système.

---

## Formulaires

### Input

```tsx
import { Input } from "@codegouvfr/react-dsfr/Input";
```

| Prop | Type | Requis |
|------|------|--------|
| `label` | `ReactNode` | Oui |
| `hintText` | `ReactNode` | Non |
| `state` | `"success" \| "error" \| "info" \| "default"` | Non |
| `stateRelatedMessage` | `ReactNode` | Non |
| `disabled` | `boolean` | Non |
| `iconId` | `FrIconClassName \| RiIconClassName` | Non |
| `textArea` | `boolean` | Non |
| `addon` | `ReactNode` | Non |
| `nativeInputProps` | `InputHTMLAttributes` | Non |
| `nativeTextAreaProps` | `TextareaHTMLAttributes` | Non (quand textArea=true) |

```tsx
<Input label="Email" nativeInputProps={{ type: "email", placeholder: "nom@example.fr" }} />
<Input label="Message" textArea nativeTextAreaProps={{ rows: 5 }} />
<Input label="Nom" state="error" stateRelatedMessage="Champ obligatoire" />
<Input label="Recherche" addon={<Button>Valider</Button>} />
```

### Select

```tsx
import { Select } from "@codegouvfr/react-dsfr/Select";
```

| Prop | Type | Requis |
|------|------|--------|
| `label` | `ReactNode` | Oui |
| `hint` | `ReactNode` | Non |
| `nativeSelectProps` | `SelectHTMLAttributes` | Oui |
| `children` | `ReactNode` (options) | Oui |
| `disabled` | `boolean` | Non |
| `state` | `"success" \| "error" \| "info" \| "default"` | Non |
| `stateRelatedMessage` | `ReactNode` | Non |

```tsx
<Select label="Département" nativeSelectProps={{ value, onChange: e => setValue(e.target.value) }}>
    <option value="" disabled hidden>Sélectionnez</option>
    <option value="75">Paris</option>
    <option value="69">Rhône</option>
</Select>
```

### Checkbox

```tsx
import { Checkbox } from "@codegouvfr/react-dsfr/Checkbox";
```

| Prop | Type | Requis |
|------|------|--------|
| `legend` | `ReactNode` | Non |
| `options` | `{ label: ReactNode; hintText?: ReactNode; nativeInputProps: InputHTMLAttributes }[]` | Oui |
| `orientation` | `"vertical" \| "horizontal"` | Non |
| `state` | `"success" \| "error" \| "info" \| "default"` | Non |
| `stateRelatedMessage` | `ReactNode` | Non |
| `small` | `boolean` | Non |

```tsx
<Checkbox
    legend="Centres d'intérêt"
    options={[
        { label: "Sport", nativeInputProps: { name: "interest", value: "sport" } },
        { label: "Culture", nativeInputProps: { name: "interest", value: "culture" } },
    ]}
/>
```

### RadioButtons

```tsx
import { RadioButtons } from "@codegouvfr/react-dsfr/RadioButtons";
```

| Prop | Type | Requis |
|------|------|--------|
| `legend` | `ReactNode` | Non |
| `options` | `{ label: ReactNode; hintText?: ReactNode; nativeInputProps: InputHTMLAttributes; illustration?: ReactNode }[]` | Oui |
| `orientation` | `"vertical" \| "horizontal"` | Non |
| `state` | `"success" \| "error" \| "info" \| "default"` | Non |
| `stateRelatedMessage` | `ReactNode` | Non |
| `small` | `boolean` | Non |
| `name` | `string` | Non |

```tsx
<RadioButtons
    legend="Civilité"
    name="civility"
    options={[
        { label: "Madame", nativeInputProps: { value: "mme" } },
        { label: "Monsieur", nativeInputProps: { value: "m" } },
    ]}
/>
```

### ToggleSwitch

```tsx
import { ToggleSwitch } from "@codegouvfr/react-dsfr/ToggleSwitch";
```

| Prop | Type | Requis |
|------|------|--------|
| `label` | `ReactNode` | Oui |
| `helperText` | `ReactNode` | Non |
| `disabled` | `boolean` | Non |
| `labelPosition` | `"left" \| "right"` | Non |
| `showCheckedHint` | `boolean` | Non (défaut: true) |
| `checked` | `boolean` | Non (controlled) |
| `defaultChecked` | `boolean` | Non (uncontrolled) |
| `onChange` | `(checked: boolean, e) => void` | Non |
| `inputTitle` | `string` | Oui (uncontrolled) |

```tsx
<ToggleSwitch label="Activer les notifications" checked={checked} onChange={setChecked} />
```

### Upload

```tsx
import { Upload } from "@codegouvfr/react-dsfr/Upload";
```

| Prop | Type | Requis |
|------|------|--------|
| `label` | `ReactNode` | Non |
| `hint` | `ReactNode` | Non |
| `multiple` | `boolean` | Non |
| `disabled` | `boolean` | Non |
| `state` | `"success" \| "error" \| "default"` | Non |
| `stateRelatedMessage` | `ReactNode` | Non |
| `nativeInputProps` | `InputHTMLAttributes` | Non |

```tsx
<Upload label="Téléverser un fichier" hint="Taille max : 500 Mo. Formats : pdf, jpg" />
<Upload multiple label="Téléverser des fichiers" />
```

### Button

```tsx
import { Button } from "@codegouvfr/react-dsfr/Button";
```

| Prop | Type | Requis |
|------|------|--------|
| `children` | `ReactNode` | Oui (sauf iconOnly) |
| `priority` | `"primary" \| "secondary" \| "tertiary" \| "tertiary no outline"` | Non (défaut: "primary") |
| `size` | `"small" \| "medium" \| "large"` | Non (défaut: "medium") |
| `iconId` | `FrIconClassName \| RiIconClassName` | Non |
| `iconPosition` | `"left" \| "right"` | Non (défaut: "left") |
| `title` | `string` | Oui (si iconOnly, pour l'accessibilité) |
| `disabled` | `boolean` | Non |
| `onClick` | `MouseEventHandler` | Non (variante bouton) |
| `linkProps` | `RegisteredLinkProps` | Non (variante lien) |
| `type` | `"button" \| "submit" \| "reset"` | Non (défaut: "button") |

```tsx
<Button onClick={() => {}}>Valider</Button>
<Button priority="secondary" linkProps={{ href: "#" }}>Annuler</Button>
<Button iconId="fr-icon-add-line" size="small">Ajouter</Button>
<Button iconId="fr-icon-delete-line" title="Supprimer" />
```

### ButtonsGroup

```tsx
import { ButtonsGroup } from "@codegouvfr/react-dsfr/ButtonsGroup";
```

| Prop | Type | Requis |
|------|------|--------|
| `buttons` | `ButtonProps[]` | Oui |
| `alignment` | `"left" \| "center" \| "right" \| "between"` | Non (défaut: "left") |
| `inlineLayoutWhen` | `"always" \| "never" \| "sm and up" \| "md and up" \| "lg and up"` | Non |
| `isReverseOrder` | `boolean` | Non |

```tsx
<ButtonsGroup
    alignment="center"
    inlineLayoutWhen="always"
    buttons={[
        { children: "Valider", onClick: () => {} },
        { children: "Annuler", priority: "secondary", onClick: () => {} },
    ]}
/>
```

---

## Feedback

### Alert

```tsx
import { Alert } from "@codegouvfr/react-dsfr/Alert";
```

| Prop | Type | Requis |
|------|------|--------|
| `severity` | `"success" \| "error" \| "warning" \| "info"` | Oui |
| `title` | `ReactNode` | Oui (taille normale) |
| `description` | `ReactNode` | Oui (si small) |
| `small` | `boolean` | Non |
| `closable` | `boolean` | Non |
| `isClosed` | `boolean` | Non (controlled) |
| `onClose` | `() => void` | Non |

```tsx
<Alert severity="success" title="Opération réussie" description="Les données ont été enregistrées." closable />
<Alert severity="error" small description="Une erreur est survenue." />
```

### Notice

```tsx
import { Notice } from "@codegouvfr/react-dsfr/Notice";
```

| Prop | Type | Requis |
|------|------|--------|
| `title` | `ReactNode` | Oui |
| `description` | `ReactNode` | Non |
| `severity` | `"info" \| "warning" \| "alert" \| "weather-orange" \| "weather-red" \| "weather-purple" \| "witness" \| "kidnapping" \| "attack" \| "cyberattack"` | Non (défaut: "info") |
| `isClosable` | `boolean` | Non |
| `isClosed` | `boolean` | Non (controlled) |
| `onClose` | `(e) => void` | Non |
| `link` | `{ linkProps, text }` | Non |

```tsx
<Notice title="Maintenance prévue le 15 mars de 12h à 14h." isClosable />
```

### Modal

```tsx
import { createModal } from "@codegouvfr/react-dsfr/Modal";
import { useIsModalOpen } from "@codegouvfr/react-dsfr/Modal/useIsModalOpen";
```

**Création :** `createModal({ id: string, isOpenedByDefault: boolean })` retourne `{ buttonProps, Component, close, open, id }`

**Props de Component :**

| Prop | Type | Requis |
|------|------|--------|
| `title` | `ReactNode` | Oui |
| `children` | `ReactNode` | Oui |
| `size` | `"small" \| "medium" \| "large"` | Non |
| `iconId` | `FrIconClassName \| RiIconClassName` | Non |
| `concealingBackdrop` | `boolean` | Non (défaut: true) |
| `buttons` | `(ButtonProps & { doClosesModal?: boolean })[]` | Non |

```tsx
const modal = createModal({ id: "my-modal", isOpenedByDefault: false });

function Page() {
    return (
        <>
            <Button nativeButtonProps={modal.buttonProps}>Ouvrir</Button>
            <modal.Component
                title="Confirmation"
                buttons={[
                    { doClosesModal: true, children: "Annuler" },
                    { doClosesModal: false, children: "Confirmer", onClick: () => { /* action */ modal.close(); } },
                ]}
            >
                Êtes-vous sûr ?
            </modal.Component>
        </>
    );
}
```
