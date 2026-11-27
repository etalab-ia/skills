# Nom et prénom

> Bloc de saisie du nom et des prénoms

Voir aussi : [Exemples](exemples.md)

Le bloc fonctionnel de “demande de nom et prénoms permet d’aider un utilisateur à saisir son nom et son/ses prénom(s).

## Structure

Le bloc fonctionnel de demande de nom et prénom défaut est composé de :

- Un champ input “Nom” - obligatoire
- Un champ input “Prénom” - obligatoire

<div class="dsfr-doc-preview">
  <fieldset class="fr-fieldset" aria-label="Demande de nom et prénom" aria-describedby="name-1-fieldset-messages">
      <div class="fr-fieldset__element">
          <div class="fr-input-group">
              <label class="fr-label" for="input-family-name-1">
                  Nom
              </label>
              <input class="fr-input" spellcheck="false" autocomplete="family-name" name="family-name" id="input-family-name-1" type="text">
          </div>
      </div>
      <div class="fr-fieldset__element">
          <div class="fr-input-group">
              <label class="fr-label" for="input-firstname-1">
                  Prénom
              </label>
              <input class="fr-input" spellcheck="false" autocomplete="given-name" name="given-name" id="input-firstname-1" type="text">
          </div>
      </div>
      <div class="fr-messages-group" aria-live="polite" id="name-1-fieldset-messages">
      </div>
  </fieldset>
</div>

**Extrait de code**

```html
<fieldset class="fr-fieldset" aria-label="Demande de nom et prénom" aria-describedby="name-1-fieldset-messages">
    <div class="fr-fieldset__element">
        <div class="fr-input-group">
            <label class="fr-label" for="input-family-name-1">
                Nom
            </label>
            <input class="fr-input" spellcheck="false" autocomplete="family-name" name="family-name" id="input-family-name-1" type="text">
        </div>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-input-group">
            <label class="fr-label" for="input-firstname-1">
                Prénom
            </label>
            <input class="fr-input" spellcheck="false" autocomplete="given-name" name="given-name" id="input-firstname-1" type="text">
        </div>
    </div>
    <div class="fr-messages-group" aria-live="polite" id="name-1-fieldset-messages">
    </div>
</fieldset>
```

**Le bloc fonctionnel de demande de nom et prénom peut être composé de plusieurs fonctionnalités :**

- Un champ input “Nom” - obligatoire
- Un champ input “Nom d’usage” - optionnel
- Un champ input “Prénom” - obligatoire
- Une case à cocher “Je n’ai pas de prénom” - optionnel
- Un bouton “Ajouter un prénom” - optionnel

<div class="dsfr-doc-preview">
  <fieldset class="fr-fieldset" aria-label="Demande de nom et prénom" id="name-1510-fieldset" aria-labelledby="name-1510-fieldset-messages">
    <div class="fr-fieldset__element">
        <div class="fr-input-group">
            <label class="fr-label" for="input-family-name-1512">
                Nom
            </label>
            <input class="fr-input" spellcheck="false" autocomplete="family-name" aria-describedby="input-family-name-1512-messages" name="family-name" id="input-family-name-1512" type="text">
            <div class="fr-messages-group" id="input-family-name-1512-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-fieldset" id="firstname-fieldset-1517" aria-labelledby="firstname-fieldset-1517-messages">
            <div class="fr-fieldset__element">
                <div class="fr-input-group">
                    <label class="fr-label" for="input-firstname-1516">
                        Prénom
                    </label>
                    <input class="fr-input" spellcheck="false" autocomplete="given-name" aria-describedby="input-firstname-1516-messages" name="given-name" id="input-firstname-1516" type="text">
                    <div class="fr-messages-group" id="input-firstname-1516-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-fieldset__element">
                <button class="fr-btn fr-btn--sm fr-btn--secondary" onclick="addFirstname(this, 'input-firstname-1516')" type="button">
                    Ajouter un prénom
                </button>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-1517-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="toggleDisabled(this, 'firstname-fieldset-1517')" name="firstname-disabled" id="checkbox-name-1518" type="checkbox" aria-describedby="checkbox-name-1518-messages">
            <label class="fr-label" for="checkbox-name-1518">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="checkbox-name-1518-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="name-1510-fieldset-messages" aria-live="polite">
    </div>
  </fieldset>
</div>

**Extrait de code**

```html
<fieldset class="fr-fieldset" aria-label="Demande de nom et prénom" id="name-1510-fieldset" aria-labelledby="name-1510-fieldset-messages">
    <div class="fr-fieldset__element">
        <div class="fr-input-group">
            <label class="fr-label" for="input-family-name-1512">
                Nom
            </label>
            <input class="fr-input" spellcheck="false" autocomplete="family-name" aria-describedby="input-family-name-1512-messages" name="family-name" id="input-family-name-1512" type="text">
            <div class="fr-messages-group" id="input-family-name-1512-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-fieldset__element">
        <fieldset class="fr-fieldset" id="firstname-fieldset-1517" aria-labelledby="firstname-fieldset-1517-messages">
            <div class="fr-fieldset__element">
                <div class="fr-input-group">
                    <label class="fr-label" for="input-firstname-1516">
                        Prénom
                    </label>
                    <input class="fr-input" spellcheck="false" autocomplete="given-name" aria-describedby="input-firstname-1516-messages" name="given-name" id="input-firstname-1516" type="text">
                    <div class="fr-messages-group" id="input-firstname-1516-messages" aria-live="polite">
                    </div>
                </div>
            </div>
            <div class="fr-fieldset__element">
                <button class="fr-btn fr-btn--sm fr-btn--secondary" onclick="if (this.firstnamesCount === undefined) this.firstnamesCount = 1;
                else this.firstnamesCount++;
                const getFieldsetElement = (node) => {
                  const parent = node.parentNode;
                  if (parent.className.indexOf('fr-fieldset__element') > -1) return parent;
                  return getFieldsetElement(parent);
                };
                const firstname = getFieldsetElement(document.getElementById('input-firstname-1516'));
                const reference = getFieldsetElement(this);
                const copy = firstname.cloneNode(true);
                copy.innerHTML = copy.innerHTML.replace(/input-firstname-1516/g, `input-firstname-1516-added-${this.firstnamesCount}`).replace('name=\"firstname\"', `name=\"firstname-${this.firstnamesCount}\"`);
                const container = reference.parentNode;
                container.insertBefore(copy, reference);
                " type="button">
                    Ajouter un prénom
                </button>
            </div>
            <div class="fr-messages-group" id="firstname-fieldset-1517-messages" aria-live="polite">
            </div>
        </fieldset>
    </div>
    <div class="fr-fieldset__element">
        <div class="fr-checkbox-group fr-checkbox-group--sm">
            <input onclick="const fieldset = document.getElementById('firstname-fieldset-1517');
if (this.checked) fieldset.setAttribute('disabled', '');
else fieldset.removeAttribute('disabled');
" name="firstname-disabled" id="checkbox-name-1518" type="checkbox" aria-describedby="checkbox-name-1518-messages">
            <label class="fr-label" for="checkbox-name-1518">
                Je n'ai pas de prénom
            </label>
            <div class="fr-messages-group" id="checkbox-name-1518-messages" aria-live="polite">
            </div>
        </div>
    </div>
    <div class="fr-messages-group" id="name-1510-fieldset-messages" aria-live="polite">
    </div>
</fieldset>
```

Une déclinaison à l’international existe correspondant à un plus grand nombre de cas d’usage (absence de nom de famille par exemple, présence de caractères particuliers). Cette déclinaison permet d’agir sur des contraintes spécifiques de chacun des champs.

Le bloc fonctionnel de nom et prénom aide à la saisie :

- en permettant le copier coller
- en autorisant les numéros, les caractères spéciaux, les caractères de ponctuation, les espaces
- en ne limitant pas la taille du champ
- en ne normalisant pas la casse
- en utilisant l’attribut autocomplete, et en désactivant le spellcheck

## Bonnes pratiques

- Il vaut mieux de demander l'« ancien nom » plutôt que le « Nom de jeune fille » ou « née ».
- Ne considérez pas que tous les membres d'une même famille auront le même nom de famille
- Si vous ne souhaitez que des caractères latins ou ASCII, vous devez l'indiquer à l'utilisateur
- Ne demander le prénom et le nom que quand c’est nécessaire.
- Choisissez le modèle qui fonctionne le mieux pour un maximum de vos utilisateurs.

## Accessibilité

- Reprendre les recommandations [du composant champ de saisie](../../../composants/input/index.md)
- Utiliser l’attribut spellcheck="false" sur les champs relatifs au nom et aux prénoms afin de désactiver la correction orthographique.
- Utiliser l’attribut autocomplete="family-name" sur les champs “nom de famille”, et autocomplete="given-name" sur les champs “prénom”.
