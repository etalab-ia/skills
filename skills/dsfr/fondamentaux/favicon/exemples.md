# Icône de favori : exemples officiels

Extraits de code des pages d'exemple du DSFR 1.15.4. Les `id` sont à rendre uniques dans la page qui les reprend. Les extraits de plus de 4 ko sont dans des fichiers à part.

### Snippet à inclure dans <head></head>

```html
<meta name="theme-color" content="#000091"><!-- Défini la couleur de thème du navigateur (Safari/Android) -->
<link rel="apple-touch-icon" href="../../../dist/favicon/apple-touch-icon.png"><!-- 180×180 -->
<link rel="icon" href="../../../dist/favicon/favicon.svg" type="image/svg+xml">
<!-- si favicon.ico peut etre placé à la racine du serveur, retirer la ligne ci-dessous -->
<link rel="shortcut icon" href="../../../dist/favicon/favicon.ico" type="image/x-icon"><!-- 32×32 -->
<link rel="manifest" href="../../../dist/favicon/manifest.webmanifest" crossorigin="use-credentials">
<!-- Modifier les chemins relatifs des favicons en fonction de la structure du projet -->
<!-- Dans le fichier manifest.webmanifest aussi, modifier les chemins vers les images -->
```
