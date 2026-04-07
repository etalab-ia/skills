---
name: lasuite-ui-kit
description: Créer des interfaces React pour les applications LaSuite (Docs, Drive, People, Webinaire, Messagerie, etc.) avec @gouvfr-lasuite/ui-kit et @gouvfr-lasuite/cunningham-react. Utiliser cette skill quand l'utilisateur travaille sur une application LaSuite, mentionne @gouvfr-lasuite/ui-kit, @gouvfr-lasuite/cunningham-react, @openfun/cunningham-react, ou développe des composants pour la suite numérique de l'État. Couvre le layout applicatif, la navigation, la recherche rapide, les utilisateurs, les badges, les icônes Material, les menus contextuels et les patterns de partage.
---

# lasuite-ui-kit

Bibliothèque React de composants partagés entre les applications LaSuite. Deux packages principaux :
- `@gouvfr-lasuite/ui-kit` — composants applicatifs LaSuite (layout, recherche, menus, partage)
- `@gouvfr-lasuite/cunningham-react` — composants de base (Button, Input, Select, Modal, DataGrid)

## Import pattern

Composants LaSuite depuis le ui-kit :
```tsx
import { UserRow, QuickSearch, Badge, Icon, MainLayout } from "@gouvfr-lasuite/ui-kit";
```

Composants de base depuis Cunningham :
```tsx
import { Button, Input, Select, Modal, DataGrid } from "@gouvfr-lasuite/cunningham-react";
```

## Provider obligatoire

Toujours utiliser `CunninghamProvider` depuis `@gouvfr-lasuite/ui-kit` (il enrichit celui de cunningham-react avec les traductions LaSuite FR/EN) :

```tsx
import { CunninghamProvider } from "@gouvfr-lasuite/ui-kit";

function App() {
  return <CunninghamProvider>{children}</CunninghamProvider>;
}
```

## Design tokens CSS

Les composants utilisent des CSS custom properties Cunningham :
```css
/* Couleurs */
var(--c--theme--colors--primary-600)
var(--c--theme--colors--greyscale-100)

/* Espacements */
var(--c--theme--spacings--xs)    /* 0.5rem */
var(--c--theme--spacings--base)  /* 1rem */
var(--c--theme--spacings--lg)    /* 2rem */

/* Typographie */
var(--c--theme--font--sizes--sm)   /* 0.875rem */
var(--c--theme--font--sizes--h1)   /* 2rem */
```

## Icônes Material

```tsx
import { Icon, IconType, IconSize } from "@gouvfr-lasuite/ui-kit";

<Icon name="add" />
<Icon name="delete" type={IconType.OUTLINED} />
<Icon name="settings" size={IconSize.LARGE} color="var(--c--theme--colors--primary-600)" />
```

- `type` : `IconType.FILLED` (défaut) ou `IconType.OUTLINED`
- `size` : `IconSize.X_SMALL` | `SMALL` | `MEDIUM` | `LARGE` | `X_LARGE` ou un nombre (pixels)
- Noms d'icônes : noms Material Icons en snake_case (ex: `"arrow_drop_down"`, `"open_in_new"`, `"delete"`)

## Responsive

```tsx
import { useResponsive } from "@gouvfr-lasuite/ui-kit";

const { isMobile, isTablet, isDesktop } = useResponsive();
```

Breakpoints : mobile (768px), tablet (1024px).

## Pattern : MainLayout

Structure de page complète avec header, panneau gauche et panneau droit :

```tsx
import { MainLayout } from "@gouvfr-lasuite/ui-kit";
import { Button } from "@gouvfr-lasuite/cunningham-react";

<MainLayout
  icon={<img src="/logo.svg" alt="Mon App" />}
  leftPanelContent={<nav>Menu</nav>}
  rightPanelContent={<aside>Détails</aside>}
  rightHeaderContent={<LaGaufreV2 apiUrl="..." />}
  enableResize
  rightPanelIsOpen={isRightOpen}
  onToggleRightPanel={() => setIsRightOpen(!isRightOpen)}
>
  <main>Contenu principal</main>
</MainLayout>
```

Props clés : `icon`, `leftPanelContent`, `rightPanelContent`, `rightHeaderContent`, `languages`, `enableResize`, `rightPanelIsOpen`, `onToggleRightPanel`, `hideLeftPanelOnDesktop`, `isLeftPanelOpen`, `setIsLeftPanelOpen`.

## Pattern : QuickSearch

Recherche rapide avec groupes et templates :

```tsx
import {
  QuickSearch,
  QuickSearchGroup,
  QuickSearchItemTemplate,
  UserRow,
} from "@gouvfr-lasuite/ui-kit";
import { QuickSearchData } from "@gouvfr-lasuite/ui-kit";

type User = { id: string; name: string; email: string };

const [group, setGroup] = useState<QuickSearchData<User>>({
  groupName: "Utilisateurs",
  elements: users,
  showWhenEmpty: true,
  emptyString: "Aucun résultat",
});

<QuickSearch placeholder="Rechercher..." loading={isLoading} onFilter={handleFilter}>
  <QuickSearchGroup
    group={group}
    onSelect={(user) => handleSelect(user)}
    renderElement={(user) => (
      <QuickSearchItemTemplate
        left={<UserRow fullName={user.name} email={user.email} showEmail />}
        right={<Icon name="add" />}
      />
    )}
  />
</QuickSearch>
```

## Pattern : Badge

```tsx
import { Badge } from "@gouvfr-lasuite/ui-kit";

<Badge type="success">Actif</Badge>
<Badge type="danger" uppercased>Supprimé</Badge>
<Badge type="info">En cours</Badge>
<Badge type="neutral">Brouillon</Badge>
```

Types : `"accent"` (défaut), `"neutral"`, `"danger"`, `"success"`, `"warning"`, `"info"`.

## Pattern : DropdownMenu

```tsx
import { DropdownMenu, useDropdownMenu, Icon } from "@gouvfr-lasuite/ui-kit";
import { Button } from "@gouvfr-lasuite/cunningham-react";

const { isOpen, setIsOpen } = useDropdownMenu();

<DropdownMenu
  isOpen={isOpen}
  onOpenChange={setIsOpen}
  options={[
    { label: "Modifier", icon: <Icon name="edit" />, callback: () => edit() },
    { label: "Télécharger", icon: <Icon name="download" />, callback: () => download() },
    { type: "separator" },
    { label: "Supprimer", icon: <Icon name="delete" />, callback: () => remove(), variant: "danger" },
  ]}
>
  <Button onClick={() => setIsOpen(!isOpen)}>Actions</Button>
</DropdownMenu>
```

Props options : `label`, `subText?`, `icon?`, `callback?`, `isDisabled?`, `isHidden?`, `variant?: "default" | "danger"`, `value?`, `isChecked?`. Séparateur : `{ type: "separator" }`.

Mode sélection : ajouter `selectedValues` et `onSelectValue`.

## Pattern : ContextMenu

Requiert `ContextMenuProvider` à la racine de l'application :

```tsx
import { ContextMenuProvider, ContextMenu, Icon } from "@gouvfr-lasuite/ui-kit";

// À la racine :
<ContextMenuProvider>
  <App />
</ContextMenuProvider>

// Sur un élément :
<ContextMenu
  options={[
    { label: "Ouvrir", icon: <Icon name="open_in_new" />, callback: () => open() },
    { type: "separator" },
    { label: "Supprimer", icon: <Icon name="delete" />, callback: () => remove(), variant: "danger" },
  ]}
>
  <div>Clic droit ici</div>
</ContextMenu>
```

Menu dynamique avec contexte :
```tsx
<ContextMenu options={(file) => getMenuItems(file)} context={file}>
  <FileCard file={file} />
</ContextMenu>
```

Props supplémentaires : `disabled?`, `asChild?` (évite le wrapper div), `onFocus?` / `onBlur?` (suivi d'état du menu).

Le type `MenuItem` est partagé avec `DropdownMenu` : définir une fois, utiliser dans les deux.

## Pattern : Hero + page d'accueil

```tsx
import { Hero, HomeGutter, ProConnectButton } from "@gouvfr-lasuite/ui-kit";

<Hero
  logo={<img src="/logo.svg" alt="App" />}
  title="Nom de l'application"
  subtitle="Description courte"
  banner="/banner.jpg"
  mainButton={<ProConnectButton onClick={handleLogin} />}
/>
<HomeGutter>
  {/* contenu de la page */}
</HomeGutter>
```

## Pattern : partage et invitations

```tsx
import { InvitationUserSelectorList, AccessRoleDropdown } from "@gouvfr-lasuite/ui-kit";

<InvitationUserSelectorList
  users={selectedUsers}
  onRemoveUser={(user) => removeUser(user)}
  roles={[
    { label: "Lecteur", value: "reader" },
    { label: "Éditeur", value: "editor" },
  ]}
  selectedRole={selectedRole}
  onSelectRole={setSelectedRole}
  onShare={handleShare}
/>

<AccessRoleDropdown
  selectedRole={currentRole}
  roles={availableRoles}
  onSelect={(role) => updateRole(role)}
  canUpdate={hasPermission}
  onDelete={() => removeAccess()}
  canDelete={isAdmin}
/>
```

## Référence des composants

Consulter les fichiers de référence pour l'API complète de chaque composant :
- [references/components.md](references/components.md) — composants ui-kit (Layout, Navigation, Recherche, Utilisateurs, Affichage, Modales, Auth, Partage)
- [references/cunningham.md](references/cunningham.md) — composants Cunningham de base (Button, Input, Select, Modal, DataGrid, etc.)

## Setup par framework

Consulter [references/setup.md](references/setup.md) pour l'installation, la configuration du provider, les thèmes, les design tokens CSS, et le setup Vite / Next.js (App Router / Pages Router).
