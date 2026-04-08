# Référence composants @gouvfr-lasuite/ui-kit

Import unique : `import { ComponentName } from "@gouvfr-lasuite/ui-kit"`

## Table des matières

- [Layout](#layout) : MainLayout, Header, Footer, Hero, HomeGutter
- [Navigation](#navigation) : DropdownMenu, ContextMenu, CustomTabs, TreeView
- [Recherche](#recherche) : QuickSearch, QuickSearchGroup, QuickSearchItem, QuickSearchItemTemplate
- [Utilisateurs](#utilisateurs) : UserRow, UserAvatar
- [Affichage](#affichage) : Badge, Icon, Spinner, HorizontalSeparator, VerticalSeparator
- [Modales](#modales) : OnboardingModal, ReleaseNoteModal
- [Auth / Intégration](#auth--intégration) : ProConnectButton, LaGaufre, LaGaufreV2
- [Partage](#partage) : ShareModal, InvitationUserSelectorList, AccessRoleDropdown
- [Formulaires](#formulaires) : Filter, Label

---

## Layout

### MainLayout

Structure de page complète avec header, panneaux latéraux et contenu principal.

```tsx
import { MainLayout } from "@gouvfr-lasuite/ui-kit";

<MainLayout
  icon={<img src="/logo.svg" alt="App" />}
  leftPanelContent={<nav>Sidebar</nav>}
  rightPanelContent={<aside>Détails</aside>}
  rightHeaderContent={<LaGaufreV2 apiUrl="..." />}
  enableResize
  rightPanelIsOpen={isRightOpen}
  onToggleRightPanel={() => setIsRightOpen(!isRightOpen)}
  languages={[{ label: "Français", isChecked: true }, { label: "English" }]}
>
  <main>Contenu principal</main>
</MainLayout>
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `icon` | `ReactNode` | — | Logo de l'application (slot header gauche) |
| `leftPanelContent` | `ReactNode` | — | Contenu du panneau gauche |
| `rightPanelContent` | `ReactNode` | — | Contenu du panneau droit |
| `rightHeaderContent` | `ReactNode` | — | Contenu header droit (ex: LaGaufre) |
| `languages` | `DropdownMenuOption[]` | — | Sélecteur de langue |
| `enableResize` | `boolean` | `false` | Active le redimensionnement des panneaux |
| `rightPanelIsOpen` | `boolean` | — | Contrôle l'ouverture du panneau droit |
| `onToggleRightPanel` | `() => void` | — | Callback toggle panneau droit |
| `hideLeftPanelOnDesktop` | `boolean` | `false` | Cache le panneau gauche sur desktop |
| `isLeftPanelOpen` | `boolean` | — | Contrôle l'ouverture du panneau gauche (mobile) |
| `setIsLeftPanelOpen` | `(open: boolean) => void` | — | Setter panneau gauche |

### Header

Barre de navigation supérieure.

```tsx
import { Header } from "@gouvfr-lasuite/ui-kit";

<Header
  leftIcon={<img src="/logo.svg" alt="App" />}
  rightIcon={<Icon name="help_outline" />}
  languages={[{ label: "Français", isChecked: true }, { label: "English" }]}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `leftIcon` | `ReactNode` | Icône/logo à gauche |
| `rightIcon` | `ReactNode` | Icône à droite |
| `languages` | `DropdownMenuOption[]` | Options de langue |
| `onTogglePanel` | `() => void` | Callback toggle du panneau (hamburger) |
| `isPanelOpen` | `boolean` | État du panneau (mobile) |

### Footer

```tsx
import { Footer } from "@gouvfr-lasuite/ui-kit";

<Footer
  externalLinks={[
    { label: "legifrance.gouv.fr", href: "https://legifrance.gouv.fr/" },
    { label: "service-public.fr", href: "https://service-public.fr/" },
  ]}
  legalLinks={[
    { label: "Mentions légales", href: "/legal-notice" },
    { label: "Accessibilité", href: "/accessibility" },
  ]}
  license={{
    label: "Sauf mention contraire, tout le contenu est sous",
    link: { label: "licence etalab-2.0", href: "https://..." },
  }}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `externalLinks` | `{ label: string; href: string }[]` | Liens institutionnels |
| `legalLinks` | `{ label: string; href: string }[]` | Liens légaux |
| `license` | `{ label: string; link: { label: string; href: string } }` | Mention de licence |
| `logo` | `{ src: string; width?: number; height?: number; alt: string }` | Logo personnalisé |

### Hero + HomeGutter

Page d'accueil avec bandeau héro.

```tsx
import { Hero, HomeGutter, ProConnectButton } from "@gouvfr-lasuite/ui-kit";

<HomeGutter>
  <Hero
    logo={<img src="/logo.svg" alt="App" width={64} />}
    title="Stockage et partage faciles."
    subtitle="Stockez et partagez vos fichiers simplement."
    banner="/hero-image.png"
    mainButton={<ProConnectButton onClick={handleLogin} />}
  />
</HomeGutter>
```

| Prop (Hero) | Type | Description |
|------|------|-------------|
| `logo` | `ReactNode` | Logo de l'application |
| `title` | `string` | Titre principal |
| `subtitle` | `string` | Sous-titre |
| `banner` | `string` | URL de l'image du bandeau |
| `mainButton` | `ReactNode` | Bouton d'action principal |

`HomeGutter` : wrapper centré, accepte uniquement `children`.

---

## Navigation

### DropdownMenu

Menu déroulant au clic.

```tsx
import { DropdownMenu, useDropdownMenu, Icon } from "@gouvfr-lasuite/ui-kit";
import { Button } from "@gouvfr-lasuite/cunningham-react";

const { isOpen, setIsOpen } = useDropdownMenu();

<DropdownMenu
  isOpen={isOpen}
  onOpenChange={setIsOpen}
  options={[
    { label: "Ouvrir", icon: <Icon name="open_in_new" />, callback: () => open() },
    { label: "Télécharger", icon: <Icon name="download" />, callback: () => download() },
    { type: "separator" },
    { label: "Supprimer", icon: <Icon name="delete" />, callback: () => remove(), variant: "danger" },
  ]}
>
  <Button onClick={() => setIsOpen(!isOpen)}>Actions</Button>
</DropdownMenu>
```

| Prop | Type | Description |
|------|------|-------------|
| `options` | `DropdownMenuItem[]` | Items du menu |
| `isOpen` | `boolean` | Contrôle l'ouverture |
| `onOpenChange` | `(isOpen: boolean) => void` | Callback ouverture/fermeture |
| `selectedValues` | `string[]` | Valeurs sélectionnées (mode sélection) |
| `onSelectValue` | `(value: string) => void` | Callback de sélection |
| `topMessage` | `string` | Message en haut du menu |
| `children` | `ReactNode` | Élément déclencheur |

**DropdownMenuItem** :

| Champ | Type | Description |
|-------|------|-------------|
| `label` | `string` | Texte de l'item |
| `subText` | `string` | Texte secondaire |
| `icon` | `ReactNode` | Icône à gauche |
| `callback` | `() => void` | Action au clic |
| `isDisabled` | `boolean` | Désactive l'item |
| `isHidden` | `boolean` | Cache l'item |
| `variant` | `"default" \| "danger"` | Style (danger = rouge) |
| `value` | `string` | Valeur pour le mode sélection |
| `isChecked` | `boolean` | Affiche un checkmark |

Séparateur : `{ type: "separator" }`.

### ContextMenu

Menu contextuel au clic droit. Requiert `ContextMenuProvider` à la racine.

```tsx
import { ContextMenuProvider, ContextMenu, Icon } from "@gouvfr-lasuite/ui-kit";

// Racine de l'app :
<ContextMenuProvider><App /></ContextMenuProvider>

// Statique :
<ContextMenu options={menuItems}>
  <div>Clic droit ici</div>
</ContextMenu>

// Dynamique avec contexte :
<ContextMenu options={(file) => getMenuItems(file)} context={file}>
  <FileCard file={file} />
</ContextMenu>

// Sans wrapper div :
<ContextMenu options={items} asChild>
  <li>Élément de liste</li>
</ContextMenu>
```

| Prop | Type | Description |
|------|------|-------------|
| `options` | `MenuItem[] \| (context) => MenuItem[]` | Items du menu (statique ou fonction) |
| `context` | `any` | Données passées à la fonction `options` |
| `disabled` | `boolean` | Désactive le menu contextuel |
| `asChild` | `boolean` | Clone l'enfant au lieu d'ajouter un wrapper div |
| `onFocus` | `() => void` | Appelé quand le menu s'ouvre sur cet élément |
| `onBlur` | `() => void` | Appelé quand le menu se ferme |

Le type `MenuItem` est partagé avec `DropdownMenu` : mêmes champs (label, icon, callback, variant, etc.).

### CustomTabs

Onglets avec icônes Material.

```tsx
import { CustomTabs } from "@gouvfr-lasuite/ui-kit";

<CustomTabs
  defaultSelectedTab="info"
  tabs={[
    { id: "info", label: "Infos", icon: "info", content: <InfoPanel /> },
    { id: "activity", label: "Activités", icon: "list", content: <ActivityPanel /> },
    { id: "notifs", label: "Notifications", icon: "notifications", content: <NotifPanel /> },
  ]}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `tabs` | `TabData[]` | Définition des onglets |
| `defaultSelectedTab` | `string` | ID de l'onglet sélectionné par défaut |
| `fullWidth` | `boolean` | Les onglets prennent toute la largeur |

**TabData** : `{ id: string; label: string; icon?: string; content: ReactNode }`. Le champ `icon` est un nom Material Icons.

### TreeView

Arborescence hiérarchique avec drag-and-drop, chargement asynchrone et types de nœuds.

```tsx
import { TreeView, useTree } from "@gouvfr-lasuite/ui-kit";

const tree = useTree({
  data: treeData,
  rootNodeId: "root",
  selectedNodeId: selectedId,
  renderNode: (node) => <TreeNodeComponent node={node} />,
  canDrag: (node) => node.data.type !== "root",
  canDrop: (node, target) => target.data.type === "folder",
  afterMove: (movedNodes, parentId) => handleMove(movedNodes, parentId),
});

<TreeView tree={tree} />
```

Composant complexe — voir le source pour les types détaillés (`TreeViewDataType`, `TreeViewNodeTypeEnum`). Principalement utilisé pour les navigations fichiers/dossiers (Drive).

---

## Recherche

### QuickSearch

Interface de recherche rapide composable (basée sur `cmdk`).

```tsx
import {
  QuickSearch,
  QuickSearchGroup,
  QuickSearchItem,
  QuickSearchItemTemplate,
} from "@gouvfr-lasuite/ui-kit";
```

**QuickSearch** (conteneur) :

| Prop | Type | Description |
|------|------|-------------|
| `onFilter` | `(filter: string) => void` | Callback de filtrage |
| `placeholder` | `string` | Placeholder du champ de recherche |
| `loading` | `boolean` | Affiche un indicateur de chargement |
| `inputValue` | `string` | Valeur contrôlée du champ |
| `showInput` | `boolean` | Affiche/cache le champ de recherche |
| `label` | `string` | Label du champ |
| `children` | `ReactNode` | Groupes de résultats |

**QuickSearchGroup\<T\>** (groupe de résultats) :

| Prop | Type | Description |
|------|------|-------------|
| `group` | `QuickSearchData<T>` | Données du groupe |
| `renderElement` | `(element: T) => ReactNode` | Rendu de chaque élément |
| `onSelect` | `(element: T) => void` | Callback de sélection |

**QuickSearchData\<T\>** :

| Champ | Type | Description |
|-------|------|-------------|
| `groupName` | `string` | Nom du groupe affiché |
| `elements` | `T[]` | Éléments du groupe |
| `emptyString` | `string` | Message quand vide |
| `showWhenEmpty` | `boolean` | Affiche le groupe même vide |
| `startActions` | `QuickSearchAction[]` | Actions avant les résultats |
| `endActions` | `QuickSearchAction[]` | Actions après les résultats |

**QuickSearchItem** : `{ onSelect?: () => void; id?: string; children: ReactNode }`.

**QuickSearchItemTemplate** :

| Prop | Type | Description |
|------|------|-------------|
| `left` | `ReactNode` | Contenu gauche (requis) |
| `right` | `ReactNode` | Contenu droit (visible desktop) |
| `alwaysShowRight` | `boolean` | Affiche `right` aussi sur mobile |
| `testId` | `string` | Attribut data-testid |

---

## Utilisateurs

### UserRow

Affiche un utilisateur avec avatar et email.

```tsx
import { UserRow } from "@gouvfr-lasuite/ui-kit";

<UserRow fullName="Jean Dupont" email="jean@gouv.fr" showEmail />
<UserRow email="anonymous@gouv.fr" />  {/* Fallback: email comme nom */}
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `fullName` | `string` | — | Nom complet (si vide, utilise email) |
| `email` | `string` | — | Adresse email |
| `showEmail` | `boolean` | `true` | Affiche l'email sous le nom |

### UserAvatar

Avatar avec initiales et couleur déterministe.

```tsx
import { UserAvatar } from "@gouvfr-lasuite/ui-kit";

<UserAvatar fullName="Jean Dupont" />
<UserAvatar fullName="Marie Martin" size="large" />
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `fullName` | `string` | — | **Requis**. Génère initiales + couleur |
| `size` | `"xsmall" \| "small" \| "medium" \| "large"` | `"medium"` | Taille |
| `forceColor` | `string` | — | Couleur CSS forcée |
| `backgroundColor` | `string` | — | Couleur de fond parmi la palette |

---

## Affichage

### Badge

Étiquette de statut avec variantes sémantiques.

```tsx
import { Badge } from "@gouvfr-lasuite/ui-kit";

<Badge type="accent">Accent</Badge>
<Badge type="success" uppercased>Actif</Badge>
<Badge type="danger">Erreur</Badge>
<Badge type="warning">Attention</Badge>
<Badge type="info">Info</Badge>
<Badge type="neutral">Neutre</Badge>
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `type` | `"accent" \| "neutral" \| "danger" \| "success" \| "warning" \| "info"` | `"accent"` | Variante de couleur |
| `uppercased` | `boolean` | `false` | Texte en majuscules |
| `children` | `ReactNode` | — | Contenu du badge |

### Icon

Wrapper Material Icons avec tailles et types.

```tsx
import { Icon, IconType, IconSize } from "@gouvfr-lasuite/ui-kit";

<Icon name="add" />
<Icon name="delete" type={IconType.OUTLINED} />
<Icon name="settings" size={IconSize.LARGE} />
<Icon name="star" size={24} color="gold" />
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `name` | `string` | — | **Requis**. Nom Material Icon (snake_case) |
| `type` | `IconType` | `FILLED` | `IconType.FILLED` ou `IconType.OUTLINED` |
| `size` | `IconSize \| number` | — | Enum (`X_SMALL`/`SMALL`/`MEDIUM`/`LARGE`/`X_LARGE`) ou pixels |
| `color` | `string` | — | Couleur CSS |
| `className` | `string` | — | Classe CSS additionnelle |

### Spinner

```tsx
import { Spinner } from "@gouvfr-lasuite/ui-kit";

<Spinner />
<Spinner size="lg" />
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `size` | `"sm" \| "md" \| "lg" \| "xl"` | `"sm"` | Taille du spinner |

### HorizontalSeparator / VerticalSeparator

```tsx
import { HorizontalSeparator, VerticalSeparator } from "@gouvfr-lasuite/ui-kit";

<HorizontalSeparator />
<VerticalSeparator />
```

Séparateurs visuels, pas de props.

---

## Modales

### OnboardingModal

Assistant d'accueil en étapes avec zone de prévisualisation.

```tsx
import { OnboardingModal } from "@gouvfr-lasuite/ui-kit";
import type { OnboardingStep } from "@gouvfr-lasuite/ui-kit";

const steps: OnboardingStep[] = [
  {
    icon: <Icon name="grid_view" />,
    title: "Composez facilement",
    description: "Déplacez, dupliquez et transformez votre contenu.",
    content: <img src="/onboarding-1.png" alt="Étape 1" />,
  },
  {
    icon: <Icon name="share" />,
    title: "Partagez et collaborez",
    description: "Décidez qui peut voir, commenter ou modifier.",
    content: <img src="/onboarding-2.png" alt="Étape 2" />,
  },
];

<OnboardingModal
  isOpen={isOpen}
  appName="Découvrir Docs"
  mainTitle="Les principes clés"
  steps={steps}
  onClose={() => setIsOpen(false)}
  onSkip={() => setIsOpen(false)}
  onComplete={() => setIsOpen(false)}
  footerLink={{ label: "En savoir plus", href: "/help" }}
  labels={{ skip: "Ignorer", next: "Continuer", previous: "Retour", complete: "J'ai compris !" }}
/>
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `isOpen` | `boolean` | — | Contrôle l'ouverture |
| `mainTitle` | `string` | — | Titre principal |
| `steps` | `OnboardingStep[]` | — | Étapes (recommandé : 4 max) |
| `onComplete` | `() => void` | — | Callback fin du parcours |
| `onClose` | `() => void` | — | Callback fermeture |
| `appName` | `string` | — | Nom de l'app (au-dessus du titre) |
| `size` | `ModalSize` | `LARGE` | Taille de la modale |
| `initialStep` | `number` | `0` | Étape initiale |
| `hideContent` | `boolean` | `false` | Mode texte uniquement (sans zone de prévisualisation) |
| `onSkip` | `() => void` | — | Callback "Ignorer" (si absent, bouton masqué) |
| `footerLink` | `{ label: string; href?: string; onClick?: () => void }` | — | Lien en bas |
| `labels` | `{ skip?; next?; previous?; complete? }` | — | Labels personnalisés (i18n) |

**OnboardingStep** : `{ icon: ReactNode; activeIcon?: ReactNode; title: string; description?: string; content?: ReactNode }`.

### ReleaseNoteModal

Modale pour afficher les notes de version. Même API que `OnboardingModal` mais en mode texte uniquement et taille `MEDIUM` par défaut.

---

## Auth / Intégration

### ProConnectButton

Bouton d'authentification ProConnect officiel.

```tsx
import { ProConnectButton } from "@gouvfr-lasuite/ui-kit";

<ProConnectButton onClick={handleLogin} />
<ProConnectButton disabled />
```

| Prop | Type | Description |
|------|------|-------------|
| `onClick` | `() => void` | Callback au clic |
| `disabled` | `boolean` | Désactive le bouton |

### LaGaufre / LaGaufreV2

Widget de navigation inter-services de l'État (la "Gaufre").

```tsx
import { LaGaufreV2 } from "@gouvfr-lasuite/ui-kit";

<LaGaufreV2 apiUrl="https://api.lasuite.numerique.gouv.fr/gaufre" />
```

| Prop (V2) | Type | Description |
|------|------|-------------|
| `apiUrl` | `string` | URL de l'API (mutuellement exclusif avec `data`) |
| `data` | `ServicesResponse` | Données statiques (mutuellement exclusif avec `apiUrl`) |

`LaGaufre` (V1) : pas de props, injecte le script legacy.

---

## Partage

### ShareModal

Modale de partage complète avec recherche d'utilisateurs, invitations, gestion des membres et paramètres de lien. Composant générique fortement typé.

```tsx
import { ShareModal } from "@gouvfr-lasuite/ui-kit";
import type { UserData, InvitationData, AccessData } from "@gouvfr-lasuite/ui-kit";

type MyUser = { id: string; full_name: string; email: string };
type MyInvitation = { id: string; role: string };
type MyAccess = { id: string; role: string };

<ShareModal<MyUser, MyInvitation, MyAccess>
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
  modalTitle="Partager le document"
  // Recherche
  onSearchUsers={(query) => searchUsers(query)}
  searchUsersResult={searchResults}
  searchPlaceholder="Rechercher un utilisateur..."
  loading={isSearching}
  // Invitations
  invitations={pendingInvitations}
  invitationRoles={[
    { label: "Lecteur", value: "reader" },
    { label: "Éditeur", value: "editor" },
  ]}
  onInviteUser={(users, role) => inviteUsers(users, role)}
  onUpdateInvitation={(invitation, role) => updateInvitation(invitation, role)}
  onDeleteInvitation={(invitation) => deleteInvitation(invitation)}
  // Membres existants
  accesses={members}
  getAccessRoles={(access) => getRolesFor(access)}
  onUpdateAccess={(access, role) => updateAccess(access, role)}
  onDeleteAccess={(access) => deleteAccess(access)}
  accessRoleTopMessage={(access) => {
    if (access.role === "admin") return "Impossible de modifier le rôle d'un admin";
    return undefined;
  }}
  // Lien de partage
  linkSettings
  linkReachChoices={[
    { value: "restricted", subText: "Lien restreint" },
    { value: "authenticated", subText: "Utilisateurs authentifiés" },
    { value: "public", subText: "Lien public" },
  ]}
  linkReach={currentReach}
  onUpdateLinkReach={(value) => setReach(value)}
  linkRoleChoices={[{ value: "reader" }, { value: "editor" }]}
  linkRole={currentLinkRole}
  onUpdateLinkRole={(value) => setLinkRole(value)}
  // Contenu bas de modale
  outsideSearchContent={
    <ShareModalCopyLinkFooter onCopyLink={() => copyLink()} onOk={() => setIsOpen(false)} />
  }
  // Permissions
  canUpdate={hasEditPermission}
  canView={hasViewPermission}
/>
```

**Props principales :**

| Prop | Type | Description |
|------|------|-------------|
| `isOpen` | `boolean` | Contrôle l'ouverture |
| `onClose` | `() => void` | Callback fermeture |
| `modalTitle` | `string` | Titre de la modale |
| `canUpdate` | `boolean` | Autorise les modifications (défaut: true) |
| `canView` | `boolean` | Affiche la liste des membres (défaut: true) |

**Props recherche :**

| Prop | Type | Description |
|------|------|-------------|
| `onSearchUsers` | `(search: string) => void` | Callback de recherche |
| `searchUsersResult` | `UserData<T>[]` | Résultats de recherche |
| `searchPlaceholder` | `string` | Placeholder du champ |
| `loading` | `boolean` | Indicateur de chargement |

**Props invitations :**

| Prop | Type | Description |
|------|------|-------------|
| `invitations` | `InvitationData<U, T>[]` | Invitations en cours |
| `invitationRoles` | `DropdownMenuOption[]` | Rôles proposés |
| `onInviteUser` | `(users: UserData<U>[], role: string) => void` | Callback d'invitation |
| `onUpdateInvitation` | `(invitation, role) => void` | Modifier le rôle |
| `onDeleteInvitation` | `(invitation) => void` | Supprimer l'invitation |
| `hideInvitations` | `boolean` | Cache la section invitations |

**Props membres (accesses) :**

| Prop | Type | Description |
|------|------|-------------|
| `accesses` | `AccessData<U, T>[]` | Membres existants |
| `getAccessRoles` | `(access) => DropdownMenuOption[]` | Rôles par membre |
| `onUpdateAccess` | `(access, role) => void` | Modifier le rôle |
| `onDeleteAccess` | `(access) => void` | Retirer l'accès |
| `hideMembers` | `boolean` | Cache la section membres |
| `hasNextMembers` / `onLoadNextMembers` | `boolean` / `() => void` | Pagination |

**Autres props membres :**

| Prop | Type | Description |
|------|------|-------------|
| `accessRoleTopMessage` | `(access) => string \| undefined` | Message conditionnel au-dessus du menu de rôle |
| `outsideSearchContent` | `ReactNode` | Contenu sous la recherche (ex: `ShareModalCopyLinkFooter`) |

**Props lien de partage :**

| Prop | Type | Description |
|------|------|-------------|
| `linkSettings` | `boolean` | Active la section lien |
| `linkReachChoices` | `{ value: string; subText?: string }[]` | Options de portée (note : `subText`, pas `label`) |
| `linkReach` | `string` | Portée actuelle |
| `onUpdateLinkReach` | `(value: string) => void` | Modifier la portée |
| `linkRoleChoices` | `DropdownMenuOption[]` | Options de rôle du lien |
| `linkRole` | `"reader" \| "editor"` | Rôle actuel |
| `onUpdateLinkRole` | `(value: string) => void` | Modifier le rôle |

**Types de données :**

- `UserData<T>` : `{ id: string; full_name: string; email: string } & T`
- `InvitationData<U, T>` : `{ id: string; role: string; email: string; user: UserData<U> } & T`
- `AccessData<U, T>` : `{ id: string; role: string; user: UserData<U>; is_explicit?: boolean; can_delete?: boolean } & T`

---

### InvitationUserSelectorList

Liste d'utilisateurs sélectionnés pour invitation avec choix de rôle.

```tsx
import { InvitationUserSelectorList } from "@gouvfr-lasuite/ui-kit";

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
```

| Prop | Type | Description |
|------|------|-------------|
| `users` | `UserData<T>[]` | Utilisateurs sélectionnés |
| `onRemoveUser` | `(user: T) => void` | Retirer un utilisateur |
| `roles` | `DropdownMenuOption[]` | Rôles disponibles |
| `selectedRole` | `string` | Rôle sélectionné |
| `onSelectRole` | `(role: string) => void` | Callback changement de rôle |
| `onShare` | `() => void` | Callback partage |
| `shareButtonLabel` | `string` | Label du bouton de partage |
| `rightActions` | `ReactNode` | Actions additionnelles à droite |

### AccessRoleDropdown

Sélecteur de rôle d'accès pour un utilisateur existant.

```tsx
import { AccessRoleDropdown } from "@gouvfr-lasuite/ui-kit";

<AccessRoleDropdown
  selectedRole={currentRole}
  roles={availableRoles}
  onSelect={(role) => updateRole(role)}
  canUpdate={hasPermission}
  onDelete={() => removeAccess()}
  canDelete={isAdmin}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `selectedRole` | `string` | Rôle actuellement sélectionné |
| `roles` | `DropdownMenuOption[]` | Rôles disponibles |
| `onSelect` | `(value: string) => void` | Callback changement de rôle |
| `canUpdate` | `boolean` | Autorise la modification |
| `onDelete` | `() => void` | Callback suppression de l'accès |
| `canDelete` | `boolean` | Autorise la suppression |
| `isOpen` | `boolean` | Contrôle l'ouverture |
| `onOpenChange` | `(isOpen: boolean) => void` | Callback ouverture/fermeture |
| `roleTopMessage` | `string` | Message en haut du menu de rôles |

---

## Formulaires

### Filter

Filtre sous forme de bouton-pilule qui ouvre un dropdown (basé sur react-aria Select).

```tsx
import { Filter } from "@gouvfr-lasuite/ui-kit";

<Filter
  label="Statut"
  options={[
    { label: "Actif", value: "active" },
    { label: "Inactif", value: "inactive" },
    { label: "Archivé", value: "archived", showSeparator: true },
  ]}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `label` | `string` | Label affiché sur le bouton |
| `options` | `FilterOption[]` | Options du filtre |
| + props `Select` de react-aria-components | | |

**FilterOption** : `{ label: string; value: string; render?(): ReactNode; showSeparator?: boolean; isChecked?: boolean }`.

### Label / WithLabel

Wrapper de label pour les champs de formulaire.

```tsx
import { Label } from "@gouvfr-lasuite/ui-kit";

<Label text="Sélectionner un genre">
  <RadioGroup>...</RadioGroup>
</Label>
```
