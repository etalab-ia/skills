# rgaa

Skill pour assistants de code IA — auditer la conformité [RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/) de sites web et composants HTML, React/JSX et Rails/ERB.

## Ce que fait cette skill

Quand elle est activée, l'assistant IA peut :

- **Auditer du code** HTML, React/JSX ou Rails/ERB selon les 106 critères RGAA 4.1.2 (basés sur WCAG 2.1 niveau AA), avec des corrections dans la stack du code audité
- **Produire un rapport structuré** avec statut C/NC/NA/NT (non testé) par critère, en mode page ou composant, non-conformités détaillées et corrections priorisées (🔴 Bloquant, 🟠 Majeur, 🟡 Mineur)
- **Exporter le rapport** dans `audits/rgaa-YYYY-MM-DD.md`

C'est un outil d'**audit a posteriori** : on lui fournit du code à analyser, il produit un rapport. Ce n'est pas un outil de génération de code.

## Contenu

| Fichier | Description |
|---------|-------------|
| [`SKILL.md`](SKILL.md) | Audit en trois phases (analyse du code, vérifications en conditions réelles, format de sortie) et format de rapport standardisé |
| [`references/impacts.md`](references/impacts.md) | Impacts des défauts par mécanisme de blocage, pour la ligne « Impact utilisateur » |
| [`references/classement/`](references/classement/) | Mode d’évaluation de chacun des 106 critères (code, mixte, conditions réelles, jugement humain), en cinq fichiers par groupe de thèmes — classement provisoire, en attente de l’avis du pôle accessibilité numérique |
| [`scripts/check-classement.py`](scripts/check-classement.py) | Vérifie la complétude du classement des critères |
| [`references/criteres-images-cadres-couleurs.md`](references/criteres-images-cadres-couleurs.md) | Thèmes 1 à 3 : Images, Cadres, Couleurs |
| [`references/criteres-multimedia-tableaux-liens-scripts.md`](references/criteres-multimedia-tableaux-liens-scripts.md) | Thèmes 4 à 7 : Multimédia, Tableaux, Liens, Scripts |
| [`references/criteres-structure-presentation.md`](references/criteres-structure-presentation.md) | Thèmes 8 à 10 : Éléments obligatoires, Structure, Présentation |
| [`references/criteres-formulaires.md`](references/criteres-formulaires.md) | Thème 11 : Formulaires (13 critères) |
| [`references/criteres-navigation-consultation.md`](references/criteres-navigation-consultation.md) | Thèmes 12 à 13 : Navigation, Consultation |

## Installation

```bash
# Avec Vercel Skills CLI (recommandé)
npx skills add etalab-ia/skills --skill rgaa

# Claude Code
npx skills add etalab-ia/skills --skill rgaa -a claude-code

# OpenCode
npx skills add etalab-ia/skills --skill rgaa -a opencode
```

## Exemples d'utilisation

Une fois la skill installée, l'assistant IA peut répondre à des demandes comme :

- *"Audite l'accessibilité de ce composant formulaire"*
- *"Mon site est-il conforme RGAA ? Voici le code de la page d'accueil"*
- *"Génère un rapport de conformité RGAA pour ces composants React"*
- *"Quelles sont les non-conformités RGAA de ce HTML ?"*

## Vérifier le classement des critères

Le classement dit, pour chaque critère, ce que l’assistant peut trancher à la lecture du code. Après avoir modifié un fichier de `references/classement/` ou le catalogue des questions de phase 2 du `SKILL.md`, lancer depuis le dossier de la skill :

```bash
python3 scripts/check-classement.py
```

Le script vérifie que les 106 critères sont classés une fois chacun (répartition officielle par thème), que chaque ligne autre que « code » dit ce qui reste à vérifier, que chaque question citée existe dans le catalogue de phase 2 et que le rappel des modes est identique dans les cinq fichiers. Il affiche la répartition par mode et signale chaque anomalie avec fichier et ligne (code de sortie 1).

Le script a son propre test, sans réseau :

```bash
sh scripts/test-check-classement.sh
```

## Liens utiles

- [Référentiel RGAA 4.1.2](https://accessibilite.numerique.gouv.fr/)
- [WCAG 2.1](https://www.w3.org/TR/WCAG21/)
- [Critères et tests RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/)

## Licence

MIT

`references/impacts.md` et la méthode d’audit par impact sont adaptés du dépôt [Isalafont/claude-skill-rgaa-dev](https://github.com/Isalafont/claude-skill-rgaa-dev) d’Isabelle Lafont (Licence Ouverte 2.0), en co-maintenance avec la DINUM.
