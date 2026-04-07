# Référence composants Cunningham

Composants de base importés depuis `@gouvfr-lasuite/cunningham-react`.

> **Note** : `@gouvfr-lasuite/cunningham-react` est le fork gouvernemental de `@openfun/cunningham-react`. L'API est identique. Les nouveaux projets doivent utiliser `@gouvfr-lasuite/*`.

---

## Button

```tsx
import { Button } from "@gouvfr-lasuite/cunningham-react";

<Button>Valider</Button>
<Button variant="secondary">Annuler</Button>
<Button variant="tertiary" color="error" icon={<Icon name="delete" />}>Supprimer</Button>
<Button variant="bordered" disabled>Indisponible</Button>
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `variant` | `"primary" \| "secondary" \| "tertiary" \| "bordered"` | `"primary"` | Style du bouton |
| `color` | `"brand" \| "neutral" \| "info" \| "warning" \| "error" \| "success"` | `"brand"` | Couleur sémantique |
| `size` | `"small" \| "medium"` | `"medium"` | Taille |
| `icon` | `ReactNode` | — | Icône à gauche du label |
| `disabled` | `boolean` | `false` | Désactive le bouton |
| `fullWidth` | `boolean` | `false` | Prend toute la largeur |
| `type` | `"button" \| "submit" \| "reset"` | `"button"` | Type HTML |

---

## Input

```tsx
import { Input } from "@gouvfr-lasuite/cunningham-react";

<Input label="Email" fullWidth />
<Input label="Nom" defaultValue="Jean" icon={<Icon name="person" />} />
<Input label="Mot de passe" state="error" text="Champ obligatoire" />
```

| Prop | Type | Description |
|------|------|-------------|
| `label` | `string` | Label du champ |
| `defaultValue` | `string` | Valeur initiale |
| `value` | `string` | Valeur contrôlée |
| `onChange` | `(e) => void` | Callback de changement |
| `icon` | `ReactNode` | Icône à gauche |
| `rightIcon` | `ReactNode` | Icône à droite |
| `state` | `"error" \| "success" \| "default"` | État visuel |
| `text` | `string` | Message sous le champ |
| `textItems` | `string[]` | Liste de messages (erreurs multiples) |
| `rightText` | `string` | Texte à droite sous le champ (compteur) |
| `disabled` | `boolean` | Désactive le champ |
| `fullWidth` | `boolean` | Prend toute la largeur |

---

## Select

```tsx
import { Select } from "@gouvfr-lasuite/cunningham-react";

<Select
  label="Ville"
  fullWidth
  options={[
    { label: "Paris", value: "paris" },
    { label: "Lyon", value: "lyon" },
    { label: "Marseille", value: "marseille" },
  ]}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `label` | `string` | Label du champ |
| `options` | `{ label: string; value: string }[]` | Options disponibles |
| `value` | `string` | Valeur contrôlée |
| `onChange` | `(e) => void` | Callback de changement |
| `state` | `"error" \| "success" \| "default"` | État visuel |
| `text` | `string` | Message sous le champ |
| `disabled` | `boolean` | Désactive le champ |
| `fullWidth` | `boolean` | Prend toute la largeur |

---

## TextArea

```tsx
import { TextArea } from "@gouvfr-lasuite/cunningham-react";

<TextArea label="Description" fullWidth />
```

Mêmes props que `Input` (sans `icon`/`rightIcon`).

---

## Checkbox

```tsx
import { Checkbox } from "@gouvfr-lasuite/cunningham-react";

<Checkbox label="Accepter les conditions" fullWidth />
```

| Prop | Type | Description |
|------|------|-------------|
| `label` | `string` | Label affiché |
| `checked` | `boolean` | État contrôlé |
| `onChange` | `(e) => void` | Callback |
| `disabled` | `boolean` | Désactive |
| `fullWidth` | `boolean` | Prend toute la largeur |

---

## Radio / RadioGroup

```tsx
import { Radio, RadioGroup } from "@gouvfr-lasuite/cunningham-react";

<RadioGroup fullWidth>
  <Radio name="role" label="Lecteur" />
  <Radio name="role" label="Éditeur" />
  <Radio name="role" label="Admin" />
</RadioGroup>
```

| Prop (Radio) | Type | Description |
|------|------|-------------|
| `name` | `string` | Nom du groupe (doit être identique) |
| `label` | `string` | Label affiché |
| `value` | `string` | Valeur |
| `fullWidth` | `boolean` | Prend toute la largeur |

---

## Switch

```tsx
import { Switch } from "@gouvfr-lasuite/cunningham-react";

<Switch label="Notifications par SMS" fullWidth />
<Switch label="Newsletter" fullWidth />
```

Mêmes props que `Checkbox`.

---

## Modal

```tsx
import { Modal, ModalSize, useModal, Button } from "@gouvfr-lasuite/cunningham-react";

function MyComponent() {
  const modal = useModal();

  return (
    <>
      <Button onClick={() => modal.open()}>Ouvrir</Button>
      <Modal
        {...modal}
        size={ModalSize.MEDIUM}
        title="Confirmer"
        rightActions={
          <>
            <Button variant="bordered" onClick={() => modal.close()}>Annuler</Button>
            <Button onClick={handleConfirm}>Confirmer</Button>
          </>
        }
      >
        Êtes-vous sûr de vouloir continuer ?
      </Modal>
    </>
  );
}
```

| Prop | Type | Défaut | Description |
|------|------|--------|-------------|
| `isOpen` | `boolean` | — | Contrôle l'ouverture |
| `onClose` | `() => void` | — | Callback de fermeture |
| `size` | `ModalSize` | `MEDIUM` | Taille de la modale |
| `title` | `string` | — | Titre affiché |
| `titleIcon` | `ReactNode` | — | Icône à côté du titre |
| `rightActions` | `ReactNode` | — | Boutons d'action en bas à droite |
| `hideCloseButton` | `boolean` | `false` | Cache le bouton X |
| `closeOnClickOutside` | `boolean` | `false` | Ferme au clic extérieur |
| `closeOnEsc` | `boolean` | `true` | Ferme avec Échap |
| `preventClose` | `boolean` | `false` | Empêche toute fermeture |

**ModalSize** : `SMALL`, `MEDIUM`, `LARGE`, `EXTRA_LARGE`, `FULL`.

**useModal()** : retourne `{ isOpen, open(), close(), onClose }`. Passer `{...modal}` au composant Modal.

---

## DataGrid / SimpleDataGrid

```tsx
import { DataGrid, SimpleDataGrid, Button } from "@gouvfr-lasuite/cunningham-react";
import { Icon } from "@gouvfr-lasuite/ui-kit";

// DataGrid : rendu côté serveur (pagination/tri manuels)
<DataGrid
  columns={[
    { field: "name", headerName: "Nom", highlight: true },
    { field: "email", headerName: "Email" },
  ]}
  rows={data}
  emptyPlaceholderLabel="Aucun élément"
  emptyCta={<Button icon={<Icon name="add" />}>Créer</Button>}
/>

// SimpleDataGrid : rendu côté client (pagination/tri automatiques)
<SimpleDataGrid
  columns={[
    { field: "name", headerName: "Nom", enableSorting: false },
    { field: "price", headerName: "Prix", highlight: true },
  ]}
  rows={allData}
  defaultPaginationParams={{ pageSize: 10 }}
  defaultSortModel={[{ field: "price", sort: "desc" }]}
/>
```

| Prop | Type | Description |
|------|------|-------------|
| `columns` | `Column[]` | Définition des colonnes |
| `rows` | `object[]` | Données à afficher |
| `emptyPlaceholderLabel` | `string` | Message quand la table est vide |
| `emptyCta` | `ReactNode` | Bouton d'action quand vide |

**Column** :
| Champ | Type | Description |
|-------|------|-------------|
| `field` | `string` | Clé de la donnée dans row |
| `headerName` | `string` | Label de l'en-tête |
| `highlight` | `boolean` | Met en gras la colonne |
| `enableSorting` | `boolean` | Active le tri (défaut: true) |
| `renderCell` | `(params) => ReactNode` | Rendu personnalisé |

**SimpleDataGrid** ajoute :
| Prop | Type | Description |
|------|------|-------------|
| `defaultPaginationParams` | `{ pageSize: number }` | Pagination automatique |
| `defaultSortModel` | `{ field: string; sort: "asc" \| "desc" }[]` | Tri par défaut |

---

## Tooltip

```tsx
import { Tooltip, Button } from "@gouvfr-lasuite/cunningham-react";

<Tooltip content="Aide contextuelle">
  <Button variant="tertiary" icon={<Icon name="help" />} />
</Tooltip>
```

| Prop | Type | Description |
|------|------|-------------|
| `content` | `ReactNode` | Contenu du tooltip |
| `children` | `ReactNode` | Élément déclencheur |

---

## Loader

```tsx
import { Loader } from "@gouvfr-lasuite/cunningham-react";

<Loader />
```

Indicateur de chargement simple, sans props requises.

---

## Formulaire complet (exemple)

```tsx
import { Button, Input, Select, TextArea, Checkbox, Radio, RadioGroup, Switch } from "@gouvfr-lasuite/cunningham-react";
import { Label } from "@gouvfr-lasuite/ui-kit";

<form style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
  <Input label="Email" fullWidth />
  <Select label="Ville" fullWidth options={cityOptions} />
  <TextArea label="Description" fullWidth />
  <Label text="Genre">
    <RadioGroup fullWidth>
      <Radio name="gender" label="Masculin" />
      <Radio name="gender" label="Féminin" />
    </RadioGroup>
  </Label>
  <Switch label="Notifications SMS" fullWidth />
  <Checkbox label="J'accepte les CGU" fullWidth />
  <Button fullWidth>Envoyer</Button>
  <Button fullWidth variant="secondary">Annuler</Button>
</form>
```
