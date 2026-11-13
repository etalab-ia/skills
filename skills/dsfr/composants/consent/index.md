# Gestionnaire de consentement

> Gérer le consentement des usagers sur les cookies et données personnelles.

Voir aussi : [Design](design.md) · [Code](code.md) · [Accessibilité](accessibilite.md) · [Exemples](exemples.md)

Le gestionnaire de consentement permet à l'usager de définir ses préférences sur l'utilisation de ses données personnelles, notamment le dépôt de cookies non fonctionnels dans son navigateur.

## Quand utiliser ce composant ?

**Intégrer un gestionnaire de consentement est une obligation** pour l’ensemble des sites dès lors qu’ils déposent ou lisent des cookies non essentiels.

Toutefois, le DSFR ne contraint pas l’utilisation de son composant natif. Il est par exemple possible d’intégrer l’extension Tarte au Citron, référencée dans les extensions du DSFR.

## Comment utiliser ce composant ?

- **Afficher le bandeau à l’arrivée sur le site** pour permettre le recueil du consentement des usagers dès le début de leur navigation.
- **Ferrer le bandeau en bas à gauche de la fenêtre du navigateur, en desktop, et en bas, en mobile.** Lorsque la hauteur maximum du bandeau est atteinte, dans le cas d’un texte explicatif long, un scroll vertical apparait sur l’ensemble du bandeau permettant à l’usager de prendre connaissance de la totalité du message avant de faire son choix.
- **Permettre l’obtention du consentement de manière globale (tout accepter ou tout refuser) ou par finalité et sous-finalité (accepter ou refuser)**.
- **Utiliser la modale de gestion du consentement pour lister les cookies par finalité** et ainsi permettre à l’usager de gérer son consentement de façon granulaire (au clic sur le bouton “Personnaliser”).
- **Proposer des sous-finalités pour présenter le détail des partenaires associés à chaque finalité.**
- **Rendre la modale de gestion du consentement accessible à n’importe quel moment de la navigation de l’usager**. Pour ce faire, un lien permettant d’y accéder doit toujours être présent dans le pied de page.

## Règles éditoriales

Pour les éléments de contenus obligatoires à afficher au sein du gestionnaire de consentement, et la présentation des finalités, [consultez les directives CNIL](https://www.cnil.fr/fr/questions-reponses-lignes-directrices-modificatives-et-recommandation-cookies-traceurs).
