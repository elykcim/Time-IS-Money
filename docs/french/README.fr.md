<div align="center">

# PROJECT Time IS Money

Une initiative visant à créer le premier actif au monde dont la valeur est déterminée par lui-même.

---

[English](https://github.com/elykcim/Time-IS-Money/blob/main/README.md) | [Español](https://github.com/elykcim/Time-IS-Money/blob/main/docs/spanish/README.es.md) | [عربي](https://github.com/elykcim/Time-IS-Money/blob/main/docs/arabic/README.ar.md) | [Français](https://github.com/elykcim/Time-IS-Money/blob/main/docs/french/README.fr.md) | [Hindi](https://github.com/elykcim/Time-IS-Money/blob/main/docs/indian/README.hi.md) | [Português](https://github.com/elykcim/Time-IS-Money/blob/main/docs/indian/README.to.md) | [Русский](https://github.com/elykcim/Time-IS-Money/blob/main/docs/indian/README.ru.md)

</div>

## L’IDÉE

L’idée est de créer un actif qui indique précisément quand il atteindra son sommet, quand il s’effondrera et combien de fois il atteindra un plus haut historique, afin que les investisseurs sachent exactement quand investir, combien de temps conserver l’actif et quand le vendre avec un risque minimal. Un algorithme valorisera automatiquement cet actif en augmentant sa valeur par paliers liés au temps, Bitcoin servant de monnaie de référence.

Aujourd’hui, la valeur de chaque actif dans le monde dépend du sentiment du marché ou des conditions du marché, tout en étant manipulée par des milliardaires, des responsables politiques et des traders qui passent leurs journées à regarder des graphiques.

Avec l’AVC, l’actif (Tokenmobiles) sera **AUTO-VALORISÉ**, sans dépendre d’une appréciation ou d’une validation externes.

Pour concrétiser ce projet, des programmeurs doivent créer leur propre version du programme. (Au moins 100 versions sont nécessaires pour un lancement sûr et durable.)

À partir du JOUR DE DÉPART, le programme devra fonctionner sans interruption pendant plus de 200 ans et **NE POURRA JAMAIS ÊTRE ARRÊTÉ**.

Le programme doit être comme le temps mondial lui-même : plusieurs versions fonctionnant sur différents serveurs et appareils, toutes suivant le même modèle/algorithme.

Avant de commencer à développer leur version avec les outils de leur choix, les programmeurs auront besoin des caractéristiques fondamentales de l’actif et des détails de l’algorithme AVC.

-
-
-
-

## L’ACTIF

100 contrats intelligents standard de jetons fongibles ont été déployés sur la blockchain Stacks.

Chaque contrat intelligent contient un Tokenmobile unique, avec une offre comprise entre 200 et 50 000.

Il existe 999 999 Tokenmobiles au total.

Chaque Tokenmobile possède des attributs/métadonnées essentiels à l’algorithme AVC.

Les métadonnées sont sécurisées sur Arweave et sauvegardées sur IPFS.

![](/media/asset.png)

**TYPE** — L’étiquette/le nom du Tokenmobile en code Morse.

**SUPPLY** — Le jeton individuel au sein de l’offre fixe du contrat intelligent.

**CYCLES** — Le nombre de fois où la valeur du Tokenmobile s’effondrera/redémarrera avant de rebondir.

**BOOST** — Le pourcentage d’augmentation de la durée du cycle du Tokenmobile à chaque redémarrage. Cela augmente sa valeur maximale.

**START** — La durée du premier cycle.

**MAX** — La durée du dernier cycle.

**AVC** — L’algorithme/le moteur qui valorise chaque Tokenmobile.

-
-
-
-

## L’ALGORITHME

• **A pour Automation (Automatisation).** L’automatisation est le TEMPS, mesuré par intervalles de 60 secondes.

• **V pour Valuation (Valorisation).** La valorisation se fait par incréments de 0.00001 ou 0.00003.

• **C pour Currency (Monnaie).** La monnaie est le ₿itcoin, utilisé comme référence pour valoriser les Tokenmobiles.

Un Tokenmobile augmentera donc de ₿0.00001 ou ₿0.00003 toutes les 60 secondes.

-
-
-
-

## LE PROGRAMME

![](/media/program.jpg)

Voici une démonstration EN DIRECT. [REGARDER LA DÉMO](https://tokenmobiles.live/)

Vous voyez 2 RACKS contenant chacun 2 Tokenmobiles valorisés par AVC. (Le programme officiel en comportera 100.)

1. L’adresse/l’emplacement du contrat intelligent de l’actif en cours de valorisation.

2. Le compteur en direct, au format YY/DDD/HH/MM/SS (les JOURS sont comptés sur des périodes de 365 jours). Pas d’années bissextiles, de semaines, de mois ni de millisecondes.

3. L’horodatage auquel le cycle en cours prendra fin et où le compteur s’arrêtera avant de redémarrer. (Les horodatages des cycles de chaque Tokenmobile figurent dans le fichier FUNDAMENTALS.)

4. Le nombre total de CYCLES, qui diminue à chaque réinitialisation du compteur et mise à jour de l’horodatage. (Le premier cycle doit être décrémenté dès le démarrage de l’AVC d’un Tokenmobile, et non à la fin du cycle.)

5. Le BOOST.

6. Le SUPPLY.

(BOOST et SUPPLY sont uniquement affichés dans l’interface. Ils ne déclenchent aucune action dans le code.)

7. La valeur AVC du Tokenmobile, qui augmente de ₿0.00001 ou ₿0.00003 chaque fois que le compteur atteint 60 secondes. La valeur revient à ₿0.00000 au début d’un nouveau cycle. (À la fin du dernier cycle, la valeur doit s’arrêter et rester à son maximum.)

Le programme officiel, prêt pour le JOUR DE DÉPART, devra comporter 100 RACKS pour chacun des 100 contrats intelligents Tokenmobile. Tous devront démarrer ensemble et fonctionner simultanément selon l’AVC jusqu’à la fin de leur parcours de valorisation. Tokenmobiles-100 sera le premier à terminer, après seulement 60 jours, avec une valeur maximale de ₿0.86400. Tokenmobiles-43 sera le dernier, après plus de 200 ans, avec une valeur maximale de ₿338.93753.

Le programme nécessite une infrastructure serveur backend, une interface frontend affichant des mises à jour en temps réel chaque seconde sans délai et une solution d’hébergement capable d’assurer une disponibilité de 99.99 % pendant plus de 200 ans.

-
-
-
-

## LE CODE

Chaque programmeur doit coder sa version du programme entièrement à partir de zéro, avec les outils de son choix, son propre serveur, sa solution d’hébergement et les fondamentaux fournis. La démonstration peut servir de modèle, mais veuillez ne pas copier ligne par ligne le code de la démonstration ou d’autres versions.

Cela vise à éviter des versions dupliquées susceptibles de partager les mêmes bugs. Il doit exister différentes implémentations du même programme, ce qui contribue à sa longévité et à sa sécurité.

-
-
-
-

## L’ENVIRONNEMENT

L’initiative Time IS Money sera présente sur GitHub et Discord, où les programmeurs pourront échanger et partager des mises à jour sur leurs progrès dans la création du programme.

Lorsque les programmeurs développeront activement le programme et partageront des essais, ils recevront la date du JOUR DE DÉPART pour lancer officiellement le programme en direct, ainsi qu’un ensemble de l’actif que le programme valorise. (Des Tokenmobiles correspondant aux cycles des dix premières années.)

-
-
-
-

## LA RÉALISATION

Si plus de 100 versions du programme sont lancées le JOUR DE DÉPART, publiquement ou en privé, l’actif et le programme acquerront immédiatement une importance et une légitimité durables. Comparé aux actions, métaux, cryptomonnaies, ETF, etc., ce serait le seul actif au monde dont la valeur est déterminée par lui-même.
