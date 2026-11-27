# Bandeau d'information importante : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

## Contenu des Bandeaux d'information importante

### Bandeau d'information minimum

```html
<div class="fr-notice fr-notice--info">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau d'information</h2>
            </div>
        </div>
    </div>
</div>
```

### Bandeau d'information avec bouton fermer

```html
<div class="fr-notice fr-notice--info">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau</h2>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Bandeau d'information sans icône

```html
<div class="fr-notice fr-notice--info fr-notice--no-icon">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau</h2>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Bandeau d'information avec icone personnalisée

```html
<div class="fr-notice fr-notice--info">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title fr-icon-virus-fill">Titre du bandeau</h2>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Bandeau d'information cas max

```html
<div class="fr-notice fr-notice--info">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau assez long</h2>
                <p class="fr-notice__desc">Texte de description plutot long lorem ipsum sit consectetur adipiscing elit. Sed</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

## Bandeaux génériques

### Bandeau d'information

Il existe 3 bandeaux génériques utilisables en fonction du niveau de gravité de l'information. L'icône peut être modifiée et seul le titre est obligatoire

```html
<div class="fr-notice fr-notice--info">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau d'information</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Bandeau d'avertissement

```html
<div class="fr-notice fr-notice--warning">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau d'avertissement</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Bandeau d'alerte

```html
<div class="fr-notice fr-notice--alert">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Titre du bandeau d'alerte</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

## Bandeaux vigilance météo

### Vigilance météo orange

Il existe 3 bandeaux météo utilisables en fonction du niveau d'alerte météo. L'icône peut être modifiée et seul le titre est obligatoire

```html
<div class="fr-notice fr-notice--weather-orange">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Vigilance météo orange</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Vigilance météo rouge

```html
<div class="fr-notice fr-notice--weather-red">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Vigilance météo rouge</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Vigilance météo violette

```html
<div class="fr-notice fr-notice--weather-purple">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Vigilance météo violette</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

## Bandeaux d'alertes

### Alerte attentat

Il existe 3 bandeaux d'alertes utilisables en fonction du type d'alerte. L'icône ne peut pas être modifiée et les intitulés officiels doivent être utilisés

```html
<div class="fr-notice fr-notice--attack">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Attentat en cours</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Appel à témoins

```html
<div class="fr-notice fr-notice--witness">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Appel à témoins</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```

### Alerte technologique

```html
<div class="fr-notice fr-notice--cyberattack">
    <div class="fr-container">
        <div class="fr-notice__body">
            <div>
                <h2 class="fr-notice__title">Cyber-attaque</h2>
                <p class="fr-notice__desc">Texte de description lorem ipsum sit consectetur adipiscing.</p>
                <a title="Lien de consultation - nouvelle fenêtre" href="#" target="_blank" rel="noopener external" class="fr-notice__link">Lien de consultation</a>
            </div>
            <button title="Masquer le message" onclick="const notice = this.parentNode.parentNode.parentNode; notice.parentNode.removeChild(notice)" type="button" class="fr-btn--close fr-btn">Masquer le message</button>
        </div>
    </div>
</div>
```
