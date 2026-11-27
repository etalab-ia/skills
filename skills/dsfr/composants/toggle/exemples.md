# Interrupteur : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Toggle simple avec bouton

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3872" aria-describedby="toggle-3872-messages">
    <label class="fr-toggle__label" for="toggle-3872">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3872-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple avec bouton + texte d’aide

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3876" aria-describedby="toggle-hint-3877 toggle-3876-messages">
    <label class="fr-toggle__label" for="toggle-3876">Libellé de l'interrupteur</label>
    <p class="fr-hint-text" id="toggle-hint-3877">Texte de description additionnel</p>
    <div class="fr-messages-group" id="toggle-3876-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple avec bouton + état

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3880" aria-describedby="toggle-3880-messages">
    <label class="fr-toggle__label" for="toggle-3880" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3880-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple avec bouton + état + texte d’aide

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3884" aria-describedby="toggle-hint-3885 toggle-3884-messages">
    <label class="fr-toggle__label" for="toggle-3884" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <p class="fr-hint-text" id="toggle-hint-3885">Texte de description additionnel</p>
    <div class="fr-messages-group" id="toggle-3884-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple avec bouton + état + séparateur

```html
<div class="fr-toggle fr-toggle--border-bottom">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3888" aria-describedby="toggle-3888-messages">
    <label class="fr-toggle__label" for="toggle-3888" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3888-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple avec bouton + état + séparateur + texte d’aide

```html
<div class="fr-toggle fr-toggle--border-bottom">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3892" aria-describedby="toggle-hint-3893 toggle-3892-messages">
    <label class="fr-toggle__label" for="toggle-3892" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <p class="fr-hint-text" id="toggle-hint-3893">Texte de description additionnel</p>
    <div class="fr-messages-group" id="toggle-3892-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple disabled avec bouton

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3896" disabled aria-describedby="toggle-3896-messages">
    <label class="fr-toggle__label" for="toggle-3896">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3896-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple disabled avec bouton + état

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3899" disabled aria-describedby="toggle-3899-messages">
    <label class="fr-toggle__label" for="toggle-3899" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3899-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple disabled et pré-coché avec bouton + état

```html
<div class="fr-toggle">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3902" disabled checked aria-describedby="toggle-3902-messages">
    <label class="fr-toggle__label" for="toggle-3902" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3902-messages" aria-live="polite">
    </div>
</div>
```

### Toggle simple en erreur

```html
<div class="fr-toggle fr-toggle--error">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3905" aria-describedby="toggle-3905-messages">
    <label class="fr-toggle__label" for="toggle-3905">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3905-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="toggle-3905-message-error">Texte d’erreur obligatoire</p>
    </div>
</div>
```

### Toggle avec état - en erreur

```html
<div class="fr-toggle fr-toggle--error">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3908" aria-describedby="toggle-3908-messages">
    <label class="fr-toggle__label" for="toggle-3908" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3908-messages" aria-live="polite">
        <p class="fr-message fr-message--error" id="toggle-3908-message-error">Texte d’erreur obligatoire</p>
    </div>
</div>
```

### Toggle simple valide

```html
<div class="fr-toggle fr-toggle--valid">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3911" aria-describedby="toggle-3911-messages">
    <label class="fr-toggle__label" for="toggle-3911">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3911-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="toggle-3911-message-valid">Texte de validation</p>
    </div>
</div>
```

### Toggle avec état - valide

```html
<div class="fr-toggle fr-toggle--valid">
    <input type="checkbox" class="fr-toggle__input" id="toggle-3914" aria-describedby="toggle-3914-messages">
    <label class="fr-toggle__label" for="toggle-3914" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
    <div class="fr-messages-group" id="toggle-3914-messages" aria-live="polite">
        <p class="fr-message fr-message--valid" id="toggle-3914-message-valid">Texte de validation</p>
    </div>
</div>
```

### Groupe de toggles simple avec bouton

```html
<fieldset class="fr-fieldset" id="toggle-group-3927" aria-labelledby="toggle-group-3927-legend toggle-group-3927-messages">
    <legend class="fr-fieldset__legend" id="toggle-group-3927-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <ul class="fr-toggle__list">
            <li>
                <div class="fr-toggle" id="group-1-toggle-3922">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3922" aria-describedby="toggle-3922-messages">
                    <label class="fr-toggle__label" for="toggle-3922">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3922-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle" id="group-1-toggle-3923">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3923" aria-describedby="toggle-3923-messages">
                    <label class="fr-toggle__label" for="toggle-3923">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3923-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle" id="group-1-toggle-3924">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3924" aria-describedby="toggle-3924-messages">
                    <label class="fr-toggle__label" for="toggle-3924">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3924-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle" id="group-1-toggle-3925">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3925" aria-describedby="toggle-3925-messages">
                    <label class="fr-toggle__label" for="toggle-3925">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3925-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle" id="group-1-toggle-3926">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3926" aria-describedby="toggle-3926-messages">
                    <label class="fr-toggle__label" for="toggle-3926">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3926-messages" aria-live="polite">
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="fr-messages-group" id="toggle-group-3927-messages" aria-live="polite">
    </div>
</fieldset>
```

### Groupe de toggles simple avec bouton + séparateur

```html
<fieldset class="fr-fieldset" id="toggle-group-3940" aria-labelledby="toggle-group-3940-legend toggle-group-3940-messages">
    <legend class="fr-fieldset__legend" id="toggle-group-3940-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <ul class="fr-toggle__list">
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-3935">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3935" aria-describedby="toggle-3935-messages">
                    <label class="fr-toggle__label" for="toggle-3935">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3935-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-3936">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3936" aria-describedby="toggle-3936-messages">
                    <label class="fr-toggle__label" for="toggle-3936">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3936-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-3937">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3937" aria-describedby="toggle-3937-messages">
                    <label class="fr-toggle__label" for="toggle-3937">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3937-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-3938">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3938" aria-describedby="toggle-3938-messages">
                    <label class="fr-toggle__label" for="toggle-3938">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3938-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-2-toggle-3939">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3939" aria-describedby="toggle-3939-messages">
                    <label class="fr-toggle__label" for="toggle-3939">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3939-messages" aria-live="polite">
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="fr-messages-group" id="toggle-group-3940-messages" aria-live="polite">
    </div>
</fieldset>
```

### Groupe de toggles simple avec bouton + séparateur + texte d’aide

```html
<fieldset class="fr-fieldset" id="toggle-group-3958" aria-labelledby="toggle-group-3958-legend toggle-group-3958-messages">
    <legend class="fr-fieldset__legend" id="toggle-group-3958-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <ul class="fr-toggle__list">
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-3953">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3953" aria-describedby="toggle-hint-3959 toggle-3953-messages">
                    <label class="fr-toggle__label" for="toggle-3953">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3959">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3953-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-3954">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3954" aria-describedby="toggle-hint-3960 toggle-3954-messages">
                    <label class="fr-toggle__label" for="toggle-3954">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3960">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3954-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-3955">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3955" aria-describedby="toggle-hint-3961 toggle-3955-messages">
                    <label class="fr-toggle__label" for="toggle-3955">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3961">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3955-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-3956">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3956" aria-describedby="toggle-hint-3962 toggle-3956-messages">
                    <label class="fr-toggle__label" for="toggle-3956">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3962">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3956-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-3-toggle-3957">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3957" aria-describedby="toggle-hint-3963 toggle-3957-messages">
                    <label class="fr-toggle__label" for="toggle-3957">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3963">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3957-messages" aria-live="polite">
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="fr-messages-group" id="toggle-group-3958-messages" aria-live="polite">
    </div>
</fieldset>
```

### Groupe de toggles simple avec bouton + état + séparateur

```html
<fieldset class="fr-fieldset" id="toggle-group-3976" aria-labelledby="toggle-group-3976-legend toggle-group-3976-messages">
    <legend class="fr-fieldset__legend" id="toggle-group-3976-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <ul class="fr-toggle__list">
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-3971">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3971" aria-describedby="toggle-3971-messages">
                    <label class="fr-toggle__label" for="toggle-3971" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3971-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-3972">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3972" aria-describedby="toggle-3972-messages">
                    <label class="fr-toggle__label" for="toggle-3972" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3972-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-3973">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3973" aria-describedby="toggle-3973-messages">
                    <label class="fr-toggle__label" for="toggle-3973" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3973-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-3974">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3974" aria-describedby="toggle-3974-messages">
                    <label class="fr-toggle__label" for="toggle-3974" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3974-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-4-toggle-3975">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3975" aria-describedby="toggle-3975-messages">
                    <label class="fr-toggle__label" for="toggle-3975" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <div class="fr-messages-group" id="toggle-3975-messages" aria-live="polite">
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="fr-messages-group" id="toggle-group-3976-messages" aria-live="polite">
    </div>
</fieldset>
```

### Groupe de toggles simple avec bouton + état + séparateur + texte d’aide

```html
<fieldset class="fr-fieldset" id="toggle-group-3994" aria-labelledby="toggle-group-3994-legend toggle-group-3994-messages">
    <legend class="fr-fieldset__legend" id="toggle-group-3994-legend">
        Légende pour l’ensemble des éléments
    </legend>
    <div class="fr-fieldset__element">
        <ul class="fr-toggle__list">
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-3989">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3989" aria-describedby="toggle-hint-3995 toggle-3989-messages">
                    <label class="fr-toggle__label" for="toggle-3989" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3995">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3989-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-3990">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3990" aria-describedby="toggle-hint-3996 toggle-3990-messages">
                    <label class="fr-toggle__label" for="toggle-3990" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3996">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3990-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-3991">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3991" aria-describedby="toggle-hint-3997 toggle-3991-messages">
                    <label class="fr-toggle__label" for="toggle-3991" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3997">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3991-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-3992">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3992" aria-describedby="toggle-hint-3998 toggle-3992-messages">
                    <label class="fr-toggle__label" for="toggle-3992" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3998">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3992-messages" aria-live="polite">
                    </div>
                </div>
            </li>
            <li>
                <div class="fr-toggle fr-toggle--border-bottom" id="group-5-toggle-3993">
                    <input type="checkbox" class="fr-toggle__input" id="toggle-3993" aria-describedby="toggle-hint-3999 toggle-3993-messages">
                    <label class="fr-toggle__label" for="toggle-3993" data-fr-checked-label="Activé" data-fr-unchecked-label="Désactivé">Libellé de l'interrupteur</label>
                    <p class="fr-hint-text" id="toggle-hint-3999">Texte de description additionnel</p>
                    <div class="fr-messages-group" id="toggle-3993-messages" aria-live="polite">
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="fr-messages-group" id="toggle-group-3994-messages" aria-live="polite">
    </div>
</fieldset>
```

### Groupe de toggles simple avec bouton + état + séparateur + texte d’aide + erreur

Extrait complet : [exemples/groupe-de-toggles-simple-avec-bouton-etat-separate-1.html](exemples/groupe-de-toggles-simple-avec-bouton-etat-separate-1.html) (4 ko)

### Groupe de toggles simple avec bouton + état + séparateur + texte d’aide + valide

Extrait complet : [exemples/groupe-de-toggles-simple-avec-bouton-etat-separate-2.html](exemples/groupe-de-toggles-simple-avec-bouton-etat-separate-2.html) (4 ko)
