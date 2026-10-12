# Gameplay — brouillon de travail

- [[GameDesignDocument/Gameplay/Genre|Genre]]

Genre

Hack'n'slash, Action-RPG, Exploration.

Univers et contexte narratif

L'histoire se déroule dans la région fictive de Markyo, un univers mêlant les influences de Marseille et de Tokyo.

Le joueur incarne Natanael, un jeune homme aspirant à devenir rōnin, qui arrive à Markyo dans l'espoir de faire fortune.

Au cours de son aventure, il rencontre Emmanuel, un épicier indien qui cache une autre identité : celle d'un ingénieur talentueux. Emmanuel a conçu une arme expérimentale, la Pistoblade, dont les fonctionnalités peuvent être progressivement débloquées et améliorées grâce à des investissements financiers.

Cependant, Emmanuel est lourdement endetté auprès de Steezy, un puissant parrain du crime local.

Pour aider Emmanuel à rembourser ses dettes et financer les améliorations de la Pistoblade, Natanael accepte d'accomplir différentes missions, l'entraînant peu à peu dans les affaires criminelles de Markyo.

Le remboursement de la dette relève du scénario et avance avec les missions principales. L'argent du joueur reste disponible pour les achats de coups et de slots ; le remboursement n'entraîne pas de prélèvement sur cet argent.

Concept du jeu

FranceTokyo est un Action-RPG orienté hack'n'slash et exploration. Le joueur évolue dans un univers original où les combats, l'accomplissement de missions et la recherche d'argent constituent les principaux moteurs de progression.

L'argent gagné permet notamment d'améliorer la Pistoblade, de débloquer de nouvelles capacités et de faire évoluer le style de combat du protagoniste.


visual style art-direction, cel-shading, tokyo vibe futuriste, low poli 

Direction artistique — palette Marseille + Tokyo (brouillon) :

Direction retenue pour les premiers essais : une ville méditerranéenne lumineuse avec des détails urbains japonais et futuristes. Les façades chaudes, la pierre claire, le bleu de la mer et le street-art se mêlent aux enseignes verticales lumineuses et aux éléments technologiques. Le rendu reste en low poly et cel-shading.

| Couleur | Code | Usage proposé |
|---|---|---|
| Pierre claire | `#F2E3C6` | Façades, sols |
| Bleu mer | `#237FBA` | Mer, volets |
| Terre cuite | `#C96A4A` | Murs, toitures |
| Bleu encre | `#1B263B` | Ombres, métal |
| Jaune soleil | `#F2BC57` | Lumière, détails |
| Rose néon | `#E84B9A` | Enseignes, technologie |

Les teintes méditerranéennes occupent les grandes surfaces ; les touches néon restent ponctuelles. Pour le cel-shading, chaque couleur se décline en ombre, couleur de base et lumière. Les proportions et les déclinaisons restent à tester dans les décors.

![[GameDesignDocument/Gameplay/Palette-Marseille-Tokyo.svg]]

Références visuelles : [Le Panier, Marseille](https://www.marseille-tourisme.com/decouvrez-marseille/culture-et-patrimoine/les-111-quartiers-marseillais/le-quartier-du-panier/) et [Shibuya, Tokyo](https://www.gotokyo.org/en/story/walks-and-tours/shibuya/index.html).

targent audience et tone: ado, humouristique, serieux

Player fantasy / Core experience: 
nerveux combo satisfaisant 

- combos aérien
- 2 armes en 1 (donc possibilité de combiner les armes pour réaliser les combos, et faire des combos par arme)
- recolte d'argent qui te permet de changer (acheter) ton coup de base (ou le suivant) du combos
- système de style qui te permet gagner des dégâts (boss ou ennemi de base) qui augmente la barre de stagger (bar de choc) donc combats "plus facile" (joueur récompenser en fonction de son rang du style qui va de C to SSS) la bar de stagger n'augmente que si il est de style S ou plus courament
- bruit (sons des animations, armes, vent, pas, etc...)  fait maison

5.8 cel-shading
Action RPG 3D avec timing
Hack'n slash
DMC/bayonetta/MH
Mécanique de changer les combos
Nerveux rapide
Zone petite/moyenne
Pas Open World
Patterne d'ennemi qui répond au gameplay 
du joueur (genre MHRISE/SUNBREAK)

![[GameDesignDocument/Gameplay/image.png]]

Patterne des ennemis :
enemies simples : attaque basiques, facile a combo

miniboss : résiste offre un minimum de challenge

Boss : gros patterne travaillé 

des comportement différents en fonction de la jauge de stagger

patterne plus agressif (marqué par un cri) a 50% de jauge de stagger

faires les modèles 3D toi meme

un ou 2 miniboss par niveau

Target

PC puis console Switch, Switch 2 playstation X-Box

malgré le manque de bruitage tout est fait main

boom boom bomm
swish swash swoosh

Scope : 2 grands niveaux explorables connectés + une arène de boss

## Missions, achats et progression — brouillon

- Les deux niveaux explorables sont connectés. Les missions structurent la progression du joueur dans ces espaces.
- Le jeu comporte des missions principales et des missions secondaires.
- L'argent gagné grâce aux missions permet d'acheter des coups et des slots pour développer les possibilités de la Pistoblade.
- La progression des achats doit être cadrée avec le nombre de missions et leurs récompenses dans ce périmètre.
- Pour le PoC : 3 slots au départ au sol comme en l'air. Le joueur peut acheter un quatrième slot au sol ; le combo aérien conserve ses 3 slots.
- La progression jusqu'à 8 slots et les achats de slots aériens restent des pistes pour la suite du jeu, hors périmètre du PoC.

### Périmètre des combos pour le PoC

- Au sol : 3 à 4 coups, avec le quatrième slot facultatif et commun aux modes épée et pistolet.
- En l'air : 3 coups pour chaque mode, avec une configuration séparée de celle du sol.
- Pour utiliser le quatrième slot au sol, le joueur peut acheter Estoc d'approche pour l'épée et Salve en éventail pour le pistolet. Ces followers s'ajoutent aux followers de départ, sans doublon.
- Le catalogue actuel permet de tester la personnalisation, l'achat d'un slot supplémentaire et l'alternance des armes dans ce périmètre.

### Missions prévues pour le PoC

- 4 missions principales au total dans les deux niveaux connectés et l'arène de boss.
- Les missions principales 1 à 3 servent à découvrir l'univers de Markyo et à aider Emmanuel à récupérer de l'argent pour rembourser sa dette.
- Le remboursement avance dans le scénario avec ces missions. Cette progression s'arrête à la mission 4, où Steezy veut tuer Emmanuel.
- La quatrième mission principale est le combat contre le boss final du PoC, dans l'arène prévue : un samouraï en armure, homme de Steezy. Steezy en a assez d'Emmanuel et veut le faire tuer ; le joueur affronte ce samouraï pour empêcher la mise à mort d'Emmanuel.
- 6 missions secondaires au total, réparties dans l'ensemble des deux niveaux.
- Chacune des missions secondaires peut être refaite à l'infini.
- Les histoires et les objectifs jouables des missions 1 à 3 ci-dessous sont retenus pour le PoC. Les durées et les conditions précises d'accès restent à cadrer ; les attaques et le comportement du samouraï en armure seront cadrés plus tard.

#### Missions principales 1 à 3 — retenues pour le PoC

Ces missions utilisent les deux niveaux déjà prévus, les rats et le Cerbère. Emmanuel porte les échanges narratifs ; les clients et fournisseurs peuvent rester hors champ. Les caisses sont des objets fixes avec lesquels le joueur interagit, leur récupération ou leur livraison étant représentée par l'état de mission.

**Mission 1 — Les rats font crédit**

- Lieu : la boutique d'Emmanuel et une cour de stockage du premier niveau.
- Histoire : Natanael cherche son premier travail à Markyo. Emmanuel doit honorer une commande, mais des rats ont envahi sa réserve et il ne peut plus accéder à ses marchandises. Il prête la Pistoblade à Natanael pour régler le problème : « Mes clients prennent à crédit, les rats se servent directement. »
- Déroulement : parler à Emmanuel, rejoindre la réserve, éliminer le groupe de rats, puis revenir lui annoncer que le passage est libre.
- Réussite : tous les rats de la mission sont éliminés et le joueur reparle à Emmanuel.
- Suite narrative : Emmanuel peut honorer sa commande et effectuer un premier remboursement dans le scénario. Il rémunère Natanael et lui confie un autre travail. Cette mission fait découvrir les alentours de la boutique et les premiers combats.

**Mission 2 — Le colis qui aboie**

- Lieu : un dépôt du port dans le deuxième niveau, accessible depuis le premier.
- Histoire : une marchandise qu'Emmanuel a déjà commandée attend au dépôt. Il compte la revendre pour continuer à rembourser Steezy, mais un Cerbère a fait du lieu son repaire. Le fournisseur a laissé la caisse et refuse de revenir la chercher.
- Déroulement : accepter la mission chez Emmanuel, passer dans le deuxième niveau, rejoindre le dépôt, vaincre le Cerbère, interagir avec la caisse et revenir voir Emmanuel.
- Réussite : le Cerbère de la mission est vaincu, la caisse est récupérée dans l'état de mission et le joueur reparle à Emmanuel.
- Progression : le premier passage au niveau 2 débloque le launcher avec Coupe montante offerte, conformément à la règle déjà retenue.
- Suite narrative : Emmanuel récupère la marchandise et prépare une vente importante. Il croit encore pouvoir arranger les choses avec Steezy. Cette mission fait découvrir le deuxième quartier et le Cerbère.

**Mission 3 — La dernière livraison**

- Lieu : une autre zone du port dans le deuxième niveau, avec retour à la boutique du premier niveau.
- Histoire : Emmanuel a trouvé un acheteur pour sa marchandise. Il promet à Natanael que cette vente lui permettra de souffler. Le point de livraison est occupé par des rats et un Cerbère ; Natanael doit dégager la zone pour que l'acheteur puisse récupérer la commande.
- Déroulement : accepter la mission chez Emmanuel, rejoindre le point de livraison, éliminer les ennemis présents, interagir avec la caisse de livraison, puis retourner à la boutique.
- Réussite : les ennemis de la mission sont éliminés, la livraison est validée et le joueur reparle à Emmanuel.
- Suite narrative : la vente réussit, mais Emmanuel reçoit un message de Steezy : « Garde ta monnaie. C'est ta tête que je veux maintenant. » Cette menace prépare la rupture avec Steezy et l'arrêt du remboursement dans le scénario à la mission 4. Emmanuel apprend qu'un samouraï en armure vient le tuer ; la mission 4 amène Natanael à affronter cet homme dans l'arène de boss.

Base de réalisation commune : dialogues courts avec Emmanuel, objectifs de déplacement, élimination d'ennemis, interactions avec des caisses fixes et validation au retour à la boutique. Les récompenses du joueur suivent l'échelle de prix et de récompenses proposée ; le remboursement reste un élément du scénario.

Les missions secondaires du PoC sont des contrats de chasse répétables.

- Objectif : vaincre une cible ou un groupe d'ennemis dans une zone donnée.
- Les six contrats réutilisent les types d'ennemis prévus pour le PoC, en variant les cibles, leur nombre et leur emplacement dans les deux niveaux.
- Boucle : accepter un contrat, affronter les cibles, valider automatiquement leur élimination et recevoir la récompense. Reprendre le contrat réinitialise ses cibles pour permettre une nouvelle chasse.
- Le cadrage détaillé des six chasses est reporté à plus tard, lorsque le bestiaire offrira une variété d'ennemis suffisante. Les cibles, quantités, emplacements, conditions d'accès, durées et récompenses seront précisés à ce moment-là.

### Coups de départ et déblocages

- Le combo de départ au sol comporte 3 coups : un beginner, un follower et un finisher.
- Le combo de départ aérien comporte également 3 coups : un beginner, un follower et un finisher.

Coups possédés et équipés au départ pour chaque mode :

| Configuration | Mode | Beginner | Follower | Finisher |
|---|---|---|---|---|
| Sol | Épée | Entaille vive | Balayage latéral | Frappe lourde |
| Sol | Pistolet | Tir direct | Tir perçant | Salve concentrée |
| Air | Épée | Entaille aérienne | Estoc aérien | Frappe plongeante |
| Air | Pistolet | Tir aérien | Tir traversant | Tir descendant |

- Aucun launcher n'est possédé au départ. Au niveau 2, la mécanique de launcher se débloque et Coupe montante est offerte et équipée par défaut pour le mode épée, afin de pouvoir l'utiliser immédiatement.
- Les autres launchers sont achetables dans la boutique d'Emmanuel à partir du niveau 2 ; chaque variante doit être achetée pour pouvoir l'équiper et l'utiliser.
- Le slot du coup spécial Arme 1 + Arme 2 doit être acheté dans la boutique d'Emmanuel. Le spécial est indisponible avant cet achat et s'utilise au sol comme en l'air une fois débloqué.

### Première échelle de prix et de récompenses — proposition à valider

Montants exprimés en unités de monnaie, dont le nom reste à choisir. Cette échelle sert de base pour cadrer la progression ; les valeurs seront ajustées avec le nombre et la durée des missions, le catalogue retenu et les tests du prototype.

| Élément | Montant proposé | Type |
|---|---|---|
| Mission principale | 1 000 | Récompense |
| Mission secondaire | 500 | Récompense |
| Beginner ou follower supplémentaire | 500 | Prix d'achat |
| Finisher ou launcher supplémentaire | 800 | Prix d'achat |
| Slot du coup spécial | 2 500 | Prix d'achat |
| Passage de 3 à 4 slots au sol | 2 000 | Prix d'achat |

- Pour le PoC, seul le quatrième slot au sol est achetable. Sa longueur équipée reste commune à l'épée et au pistolet ; la configuration aérienne conserve 3 slots.
- Les slots sont des achats à préparer sur plusieurs missions. Les coups supplémentaires restent accessibles plus tôt, pour développer les choix du joueur dans ses slots existants.
- Avec la récompense de référence de 1 000 unités, une première mission principale permet d'acheter des coups supplémentaires. Le quatrième slot coûte 2 000 unités, soit deux récompenses principales économisées sans autre dépense.
- Avec les récompenses proposées, les trois premières missions principales et les six missions secondaires réussies une fois chacune rapportent 6 000 unités, hors autres sources d'argent. Ce calcul sert de repère pour les achats avant le boss du PoC.
- À titre d'exemple, le quatrième slot au sol (2 000 unités), Estoc d'approche (500) et Salve en éventail (500) coûtent ensemble 3 000 unités et permettent d'équiper 4 coups dans les deux modes au sol. Ajouter le slot du spécial (2 500) porte le total à 5 500 unités, avec 500 unités restantes sur ce repère de 6 000.
- La répétition des missions secondaires permet de continuer à financer les achats. Le rythme de progression dépendra de leur durée et des récompenses retenues.
- La progression attendue avant la quatrième mission principale, ainsi que le rythme des achats via les missions secondaires, restent à cadrer avec les tests du prototype.

### Piste de progression jusqu'à 8 slots — hors PoC

- Pour la suite du jeu, la capacité pourrait progresser jusqu'à 8 slots, beginner et finisher inclus, avec des achats séparés pour le sol et l'air.
- Les slots supplémentaires resteraient facultatifs. Atteindre 8 coups équipés demanderait 6 followers distincts pour chaque mode dans la configuration concernée ; ces coups supplémentaires relèvent de la suite du jeu.

| Passage envisagé | Prix proposé |
|---|---|
| De 4 à 5 slots | 3 000 |
| De 5 à 6 slots | 5 000 |
| De 6 à 7 slots | 8 000 |
| De 7 à 8 slots | 12 000 |

Avec le prix proposé de 2 000 unités pour le quatrième slot, passer de 3 à 8 slots coûterait 30 000 unités pour une configuration, soit 60 000 pour le sol et l'air, hors achats de coups. Ces montants sont conservés comme pistes pour la suite du jeu.

### Boutique d'Emmanuel

- La boutique d'Emmanuel se trouve dans le premier niveau.
- Le joueur achète les coups et les slots auprès d'Emmanuel.
- Tout achat est définitif pour la partie : un coup ou un slot acheté reste débloqué et n'a pas à être racheté.
- Les coups et slots possédés sont enregistrés avec la progression du joueur aux checkpoints et restaurés avec la sauvegarde chargée.
- Retirer ou remplacer un coup dans un combo ne fait pas perdre ce coup ; il reste possédé.
- Les launchers supplémentaires s'achètent dans cette boutique à partir du niveau 2. Coupe montante est offerte lors du déblocage de la mécanique.
- Le slot du coup spécial fait partie des achats de la boutique. Il coûte un peu plus cher que le premier slot supplémentaire de combo : prix de départ proposé de 2 500 unités, contre 2 000 pour passer de 3 à 4 slots. Ces montants restent à tester pour l'équilibrage.
- La boutique permet également de modifier la configuration des combos.
- Le joueur peut aussi modifier ses combos depuis un menu, uniquement en dehors des combats. La modification de la configuration est indisponible pendant un combat.
- Rééquiper les coups déjà possédés est gratuit.

À cadrer ensemble :

- Durée et conditions précises d'accès des missions principales du PoC. Les missions 1 à 3 sont retenues ; la mission 4 oppose le joueur au samouraï en armure de Steezy, dont le comportement de combat sera cadré plus tard.
- Détail des 6 chasses : cadrage reporté jusqu'à ce que le bestiaire offre une variété d'ennemis suffisante.
- Récompenses des missions et éventuelles autres sources d'argent liées aux combats et à l'exploration.
- Catalogue supplémentaire à acheter et rythme des achats de coups et de slots.
- Sélection des variantes de launchers à produire pour le PoC.

## Notes de combat — pistes à tester (brouillon)

Base de réflexion pour les combos au sol et aériens. Les règles et le périmètre restent à valider en prototype.

Les coups se répartissent en quatre catégories : beginner, follower, finisher et launcher.

- Combo au sol : enchaîner plusieurs attaques en alternant librement les deux armes actuellement équipées, avec un index de combo partagé.
- Launcher simple : projeter l'ennemi en l'air, pendant que le personnage reste au sol.
- Launcher avec suivi : projeter l'ennemi et faire monter le personnage avec lui pour poursuivre le combat en l'air.
- Combo aérien : enchaîner des attaques lorsque le personnage est en l'air, y compris après un saut normal, avec une configuration séparée de celle du combo au sol. Pour le PoC, le combo aérien conserve 3 slots. L'achat de slots aériens supplémentaires est une piste pour la suite du jeu. Une première liste de coups est proposée dans le catalogue provisoire ci-dessous.
- Attaque plongeante : attaquer vers le sol depuis les airs. Première piste dans le catalogue : un finisher aérien qui fait descendre le joueur et la cible. Effet à l'impact à tester.
- Attaques au pistolet : une vraie branche offensive du combo, avec des coups propres à chaque index et des finishers. Le mode pistolet de la gunblade reste à courte portée, avec seulement un peu plus d'allonge que le mode épée. Les deux modes sont pensés pour le combat proche. Chaque coup doit apporter un intérêt dans l'enchaînement : dégâts, portée, zone touchée, placement ou effet sur la cible. Premières pistes dans le catalogue provisoire ci-dessous, à valider en prototype.
- Tir de soutien éventuel (à décider) : un tir simple sur une touche dédiée, dont l'action reste la même quel que soit l'index du combo. Il pourrait maintenir temporairement l'ennemi en l'air ; ralentir aussi la chute du personnage reste optionnel. Ce tir serait indépendant de l'index partagé et ne le ferait pas avancer.

Commandes manette (repères PlayStation) :

Le jeu est pensé pour la manette, avec les commandes suivantes.

| Commande | Action |
|---|---|
| Carré | Attaque de l'Arme 1 |
| Triangle | Attaque de l'Arme 2 |
| Carré + Triangle simultanément | Spécial Arme 1 + Arme 2, disponible après l'achat de son slot chez Emmanuel |
| Stick à l'opposé de la cible + Carré ou Triangle | Launcher équipé avec l'Arme 1 ou l'Arme 2 ; Coupe montante offerte au niveau 2, autres variantes à acheter chez Emmanuel |
| Rond | Esquive, au sol comme en l'air |
| Croix (X) | Saut |
| R1 | Verrouillage manuel d'une cible |
| Flèches directionnelles | Changement de cible |

Défense, points de vie et mort :

- Esquive : mécanique de défense retenue, utilisable au sol et en l'air avec la même commande et le même principe.
- L'esquive remet l'index partagé du combo à 0. Le prochain coup est le beginner de l'arme choisie.
- Chaque esquive fait perdre un rang de style.
- L'esquive accorde 10 frames d'invulnérabilité sur une référence de 60 FPS, soit environ 0,167 seconde. Cette durée reste constante quelle que soit la fréquence d'affichage. C'est la valeur de départ à tester pour le PoC.
- L'esquive interrompt immédiatement toute attaque en cours dès l'appui sur Rond, au sol comme en l'air. Cette règle s'applique aux beginners, followers, finishers, launchers et au coup spécial, pour conserver le caractère nerveux du combat.
- Parade : piste à envisager après le PoC, ajout encore incertain.
- Points de vie classiques : subir des dégâts réduit les PV ; atteindre 0 PV entraîne la mort.
- À la mort : affichage d'un écran Game Over, puis chargement de la sauvegarde du dernier checkpoint, qui restaure l'état du joueur, du monde et de la progression au moment de son enregistrement.

Checkpoints et sauvegarde — base retenue pour le PoC :

- Un checkpoint correspond à une sauvegarde de l'état du jeu à un instant donné.
- Pour l'instant, une sauvegarde est créée au changement de zone ou au début d'une mission. Les emplacements précis des checkpoints seront décidés plus tard.
- La sauvegarde enregistre l'état du joueur, notamment sa position, ses PV, son argent, ses coups et slots possédés et ses configurations de combat.
- Elle enregistre également l'état du monde et la progression du joueur, notamment l'état des ennemis et des missions et les déblocages déjà obtenus.
- Charger le dernier checkpoint restaure cet état enregistré. La progression réalisée depuis ce checkpoint revient à l'état sauvegardé ; les PV et l'argent sont également ceux enregistrés à ce moment-là.

Ciblage manuel avec verrouillage automatique en l'absence de sélection :

- Le joueur peut sélectionner manuellement un ennemi. Cette cible a priorité sur le ciblage automatique.
- Sans cible sélectionnée manuellement, le jeu choisit automatiquement un ennemi à viser.
- Les coups qui rapprochent le joueur utilisent la cible active, au sol comme en l'air.
- Piste de sélection automatique à tester : privilégier un ennemi proche dans la direction où regarde le personnage.
- Piste à tester : conserver la cible automatique pendant l'enchaînement pour éviter de changer d'ennemi à chaque coup.

Caméra — piste à tester en prototype :

- Sans verrouillage manuel, la caméra suit le joueur, qui peut l'orienter librement. Le ciblage automatique n'ajuste que légèrement le cadrage.
- Avec verrouillage manuel, la caméra vise un point entre le joueur et l'ennemi pour les garder visibles ensemble. Elle pivote progressivement et recule légèrement lorsque leur écart augmente.
- En combat aérien, elle accompagne la montée et la descente du joueur et de sa cible pour garder le combo lisible.
- Les mouvements de caméra sont lissés pour éviter les changements brusques lors d'un rapprochement, d'un launcher ou d'un changement de cible.
- Pour le PoC : tester un cadrage simple avec une distance de verrouillage limitée, dans une arène dégagée. Les réglages et la gestion des situations plus difficiles restent à travailler après ce premier test.

Catégorie launcher — configuration séparée :

- Aucun launcher n'est possédé au départ. Au niveau 2, Coupe montante est offerte et équipée par défaut pour le mode épée lors du déblocage de la mécanique. Les autres launchers s'achètent chez Emmanuel à partir de ce niveau avant de pouvoir être équipés et utilisés.
- Les launchers forment une catégorie à part, distincte des beginners, followers et finishers du combo équipé. Ils projettent l'ennemi en l'air, avec ou sans suivi du personnage.
- Ils sont configurables dans un emplacement dédié, séparé des slots du combo équipé.
- Ils sont utilisables uniquement au sol, pendant un combo déjà commencé, après un beginner ou un follower. Ils ne peuvent pas être déclenchés depuis le repos, pendant un finisher ou après celui-ci.
- Une seule commande directionnelle est retenue pour le launcher.
- Commande : orienter le stick de déplacement à l'opposé de la cible active et appuyer sur Arme 1 (Carré) ou Arme 2 (Triangle). La référence est la position de la cible choisie manuellement ou par le ciblage automatique.
- Les combos classiques et l'alternance lame/pistolet restent accessibles avec les commandes normales.
- Un launcher réinitialise l'index partagé à 0. Le prochain coup du combo normal est donc un beginner.
- Étendre les commandes directionnelles après avoir testé la fluidité et la facilité d'utilisation du launcher.

Précision sur les combos des deux armes équipées :

- Les combos de chaque arme partagent le même index : ils avancent dans un seul enchaînement commun.
- Pour le PoC, le combo commence avec 3 slots. Le joueur peut acheter un quatrième slot au sol ; la configuration aérienne conserve 3 slots. La progression jusqu'à 8 slots reste une piste pour la suite du jeu.
- Le quatrième slot au sol est facultatif : le joueur peut conserver un combo de 3 coups même après l'avoir acheté.
- L'épée et le pistolet utilisent toujours le même nombre de slots actifs. L'activation des slots facultatifs est commune aux deux modes : leurs finishers sont placés au même index.
- Le combo équipé utilise trois types de coups :
  - Beginner : premier coup du combo, remplaçable uniquement par un autre beginner.
  - Follower : coup intermédiaire, remplaçable uniquement par un autre follower.
  - Finisher : dernier coup du combo, remplaçable uniquement par un autre finisher.
- Au départ et dans le combo aérien du PoC : 1 beginner + 1 follower + 1 finisher. Au maximum au sol dans le PoC : 1 beginner + 2 followers + 1 finisher. La piste de 8 slots pour la suite du jeu correspond à 1 beginner + 6 followers + 1 finisher.
- Les slots supplémentaires utilisés ajoutent des followers entre le beginner et le finisher.
- Un même follower ne peut être équipé qu'une fois dans un combo normal. Chaque slot follower utilisé doit contenir un coup distinct pour l'arme correspondante. Pour le PoC, ce follower peut aussi être choisi dans la configuration séparée du spécial ; cette autorisation est provisoire.
- À chaque étape, le joueur peut choisir le coup de l'une ou de l'autre arme équipée.
- Chaque arme a ses propres coups de combo, y compris ses finishers. Choisir le pistolet à une étape doit être un vrai choix offensif, avec un coup différent de celui de la lame.
- Alterner les armes conserve l'avancement du combo. Après le coup 1 à l'épée, utiliser le pistolet joue son coup 2.
- Un beginner ou un follower fait avancer l'index même s'il ne touche aucun ennemi ; un finisher raté remet l'index à 0.
- Prendre un coup remet l'index partagé à 0. Le prochain coup du combo est le beginner de l'arme choisie.
- Dépasser le délai autorisé entre deux attaques remet l'index partagé à 0. La durée et le point de départ de ce délai restent à régler en prototype.
- Le finisher est le dernier coup du combo, joué avec l'arme choisie pour cette dernière étape.
- Tout finisher terminé remet l'index partagé à 0 (premier slot, beginner), qu'il appartienne au combo équipé ou au coup spécial. Le prochain coup est le beginner de l'arme choisie.
- Chaque finisher a une utilité propre. Le choix du dernier coup dépend de ce que le joueur veut obtenir dans la situation ; les premières propositions d'effets figurent dans le catalogue provisoire ci-dessous.

Exemples avec les 3 slots de départ : épée 1 (beginner) → pistolet 2 (follower) → épée 3 (finisher), ou épée 1 (beginner) → pistolet 2 (follower) → pistolet 3 (finisher). Le joueur peut aussi rester sur la même arme pendant tout l'enchaînement.

Configuration aérienne séparée :

- Le joueur compose son combo aérien indépendamment de son combo au sol.
- La longueur du combo aérien est également commune à l'épée et au pistolet, mais peut être différente de celle du combo au sol.
- Pour le PoC, la configuration aérienne conserve ses 3 slots, même après l'achat du quatrième slot au sol. Pour la suite du jeu, les achats de slots aériens resteraient séparés de ceux du sol.
- Un saut normal permet d'utiliser le combo aérien ; projeter la cible avec un launcher n'est pas une condition obligatoire.
- Le saut réinitialise l'index partagé à 0 : le combo aérien repart sur le beginner de l'arme choisie.
- L'atterrissage réinitialise aussi l'index partagé à 0 : le combo au sol repart sur le beginner de l'arme choisie.
- Le stick seul ne permet pas de déplacer le personnage en l'air. Les déplacements aériens sont liés aux coups utilisés ou à l'esquive. Les coups aériens permettent notamment de se rapprocher d'une cible distante.
- Pendant l'animation d'une attaque aérienne, la chute du joueur est suspendue : il reste à sa hauteur, sauf si le coup prévoit un déplacement vertical. À la fin de l'animation, sa chute reprend.
- Certaines attaques font monter le personnage en l'air avec la cible ; d'autres ne font pas monter le personnage. Le passage en l'air dépend donc aussi des effets du coup utilisé.
- Chaque coup du joueur qui touche un ennemi en l'air réinitialise sa chute : l'ennemi recommence à retomber depuis sa hauteur actuelle. Entre deux coups, sa chute reprend normalement.
- Les dégâts de la traînée du Tir orbital réinitialisent également la chute de l'ennemi à chaque application. La traînée dure 2 secondes.
- Certains finishers aériens amènent la cible au sol : cet effet de descente prend le dessus sur la réinitialisation habituelle de sa chute.
- D'autres finishers aériens laissent le joueur en l'air après leur exécution.
- Tout finisher aérien remet l'index partagé à 0, même lorsque le joueur reste en l'air.
- Le rythme des coups permet donc d'entretenir la présence de la cible en l'air. Les paramètres de chute et le rythme des attaques restent à équilibrer en prototype.
- Chaque ennemi possède un comportement aérien distinct. Ses paramètres de chute et ses réactions aux coups et aux projections sont à définir individuellement pour l'équilibrage.

Coup spécial Arme 1 + Arme 2 :

- Le spécial se débloque par l'achat de son slot dans la boutique d'Emmanuel. Il est indisponible avant cet achat ; le prix de départ proposé est de 2 500 unités.
- Cet emplacement est séparé des slots du combo équipé.
- Déclenchement avec les commandes Arme 1 + Arme 2 ensemble.
- Le spécial enchaîne un follower puis un finisher.
- Son follower et son finisher sont configurables séparément du combo équipé. Le joueur choisit un follower pour le premier coup du spécial et un finisher pour le second.
- Pour le PoC, un follower déjà équipé dans le combo normal peut aussi être choisi pour le spécial. Cette règle est provisoire et conserve l'interdiction des doublons à l'intérieur du combo normal.
- Le spécial est utilisable au sol et en l'air, avec la même commande et les mêmes conditions d'enchaînement.
- Le spécial aérien possède sa propre configuration : un follower et un finisher choisis parmi les coups aériens, indépendamment du spécial au sol et du combo aérien équipé.
- Il est utilisable uniquement pendant un combo déjà commencé, après un beginner ou un follower. Il ne peut pas être déclenché depuis le repos ni après un finisher.
- Le finisher du spécial remet l'index à 0, comme tout autre finisher.
- Une esquive peut interrompre immédiatement le spécial avant sa fin ; elle remet l'index à 0 comme toute esquive.

Recharge du spécial — règle retenue pour le PoC :

- Cooldown : 5 secondes, commun aux configurations au sol et en l'air.
- Le cooldown commence dès le déclenchement du spécial et continue même si le joueur l'interrompt avec une esquive.
- Un indicateur affiche la disponibilité du spécial et sa recharge.

Exemples : beginner du combo équipé → Arme 1 + Arme 2 → follower du spécial → finisher du spécial → retour à l'index 0 ; ou beginner → follower(s) du combo équipé → Arme 1 + Arme 2 → follower du spécial → finisher du spécial → retour à l'index 0.

Exemples de passages au combat aérien :

- Saut normal (index remis à 0) → beginner du combo aérien équipé → suite du combo aérien.
- Combo au sol avec alternance lame/pistolet → launcher directionnel avec suivi (index remis à 0) → combo aérien avec alternance lame/pistolet → finisher de l'arme choisie.

Le catalogue provisoire ci-dessous propose des coups aériens et une attaque plongeante en finisher. Ces propositions restent à tester.

Intérêt pour la Pistoblade : construire un enchaînement en choisissant entre les coups de la lame et du pistolet à chaque étape. Le pistolet doit apporter sa propre richesse offensive. Pistes pour ses coups : salves, tirs perçants ou attaques accompagnées d'un déplacement, à tester. La variété des attaques et l'alternance épée/pistolet alimentent le rang de style selon les règles ci-dessous.

Précisions sur le style et les deux modes de la gunblade :

- Une jauge de points de style fait progresser les rangs : C → B → A → S → SS → SSS.
- À 0 point de style, aucun rang ne s'affiche. Tant que la jauge contient des points, C est le rang affiché le plus bas.
- Un coup qui touche rapporte des points de style. Un coup raté ne rapporte rien, même s'il fait avancer le combo selon les règles de l'index.
- La variété apporte un bonus : alternance épée/pistolet, passages entre le sol et les airs, et utilisation de différents coups. Le joueur peut aussi monter son style en restant sur une seule arme.
- Répéter toujours le même enchaînement rapporte progressivement moins de points de style.
- Un finisher réussi apporte un bonus de style pour récompenser le fait d'aller au bout de l'enchaînement.
- Après un court délai sans toucher d'ennemi, la jauge de style baisse progressivement et peut atteindre 0. Le délai et la vitesse de baisse restent à régler en prototype.
- Prendre un coup fait perdre immédiatement un rang de style, comme chaque esquive.
- Au rang C, une esquive ou un coup reçu vide toujours la jauge de style : elle passe à 0 et aucun rang ne s'affiche.
- Le rang de style augmente les dégâts infligés.
- Mode épée : le bonus de style s'accompagne d'un effet visuel d'explosion.
- Mode pistolet : le style apporte une portée supplémentaire, en plus de sa portée de base supérieure à celle de l'épée. La façon de rendre ce bonus visible reste à définir.
- Les rangs concernés, les valeurs des bonus et les coups affectés restent à préciser.
- L'effet visuel d'explosion est prévu ; un éventuel effet sur la zone touchée ou d'autres propriétés de l'attaque reste à décider.

### Ennemis prévus pour le PoC — brouillon

Le bestiaire du PoC comprend trois types d'ennemis :

- Samouraï : le samouraï en armure, homme de Steezy, est le boss de la mission principale 4.
- Rats.
- Cerbère.

Chaque type d'ennemi possède ses propres attaques, qui seront cadrées plus tard.

Ennemis et stagger — règles et pistes :

- Hors stagger, la possibilité de projeter un ennemi dépend de son type et de sa résistance à la projection. Ces propriétés restent à définir pour chaque ennemi.
- Les ennemis normalement projetables peuvent être envoyés en l'air sans avoir besoin d'être en stagger.
- Première piste : les ennemis simples pourraient être facilement projetables même sans stagger. Pour les ennemis résistants, miniboss ou boss, la projection pourrait être réservée à la fenêtre de stagger.
- Seuls les coups réussis au rang S, SS ou SSS font monter la jauge de stagger des ennemis touchés.
- Si le joueur redescend sous S, le stagger déjà accumulé reste conservé. Ses coups cessent de faire monter la jauge jusqu'à ce qu'il atteigne à nouveau S ou un rang supérieur.
- Lorsque sa jauge de stagger est pleine, l'ennemi est temporairement étourdi : son attaque en cours est interrompue et il ne peut plus riposter pendant cette fenêtre.
- Pendant cet étourdissement, les ennemis habituellement non projetables ou fortement résistants à la projection deviennent temporairement projetables en l'air. Un launcher peut exploiter cette fenêtre pour ouvrir un combo aérien.
- Pendant l'étourdissement, les coups réussis infligent toujours des dégâts et rapportent du style selon les règles habituelles, mais ne font plus monter la jauge de stagger.
- À la fin de la fenêtre de stagger, la jauge de l'ennemi revient à 0 et peut être remplie à nouveau.
- Si l'ennemi est encore en l'air à la fin de cette fenêtre, le combo aérien continue selon les règles habituelles. L'ennemi retrouve sa résistance normale à la projection lorsqu'il touche le sol.
- La durée de l'étourdissement est définie selon l'ennemi et reste à régler en prototype.

### Premier catalogue de coups — propositions pour le brouillon

Les coups possédés et équipés au départ sont fixés dans la section « Coups de départ et déblocages ». Coupe montante est offerte au niveau 2 lors du déblocage des launchers. Les autres coups du catalogue sont des propositions à acheter ensuite ; les launchers supplémentaires s'achètent chez Emmanuel à partir du niveau 2. Les noms et effets restent à discuter et à tester. Cette liste ne constitue pas un engagement à produire tous ces coups. Les dégâts, portées, cadences et prix restent à équilibrer.

La portée des coups de pistolet reste courte : ils touchent un peu plus loin que l'épée, tout en restant adaptés aux combos à proximité des ennemis. Cette intention vaut au sol comme en l'air.

Les réactions aux projections et aux impacts dépendent du comportement propre à chaque ennemi. Les bonus de style déjà décrits s'appliquent selon les règles qui seront retenues ; l'explosion visuelle de l'épée ne donne pas automatiquement un effet de zone à tous ses coups.

#### Coups au sol

| Catégorie | Mode | Nom provisoire | Effet proposé | Intérêt dans le combo |
|---|---|---|---|---|
| Beginner | Épée | Entaille vive | Frappe rapide au contact sur la cible devant le joueur. | Commencer rapidement un enchaînement à courte portée. |
| Follower | Épée | Estoc d'approche | Avance vers la cible puis frappe avec la pointe. | Réduire la distance créée pendant le combat. |
| Follower | Épée | Balayage latéral | Coupe en arc devant le joueur et peut toucher plusieurs ennemis proches. | Choisir de toucher un groupe plutôt que de se déplacer vers une seule cible. |
| Finisher | Épée | Frappe lourde | Coup puissant concentré sur une cible au contact. | Terminer l'enchaînement avec des dégâts concentrés sur un ennemi. |
| Beginner | Pistolet | Tir direct | Tir ciblé à courte portée, avec un peu plus d'allonge que l'épée. | Commencer un combo sur une cible légèrement hors de portée de la lame. |
| Follower | Pistolet | Tir perçant | Projectile qui traverse plusieurs ennemis alignés sur une courte distance. | Exploiter leur alignement pour atteindre plusieurs cibles proches. |
| Follower | Pistolet | Salve en éventail | Plusieurs tirs répartis devant le joueur à courte portée. | Couvrir un groupe dispersé devant le joueur ; chaque cible reçoit une partie de la salve. |
| Finisher | Pistolet | Salve circulaire | Le joueur tourne sur lui-même en tirant à 360° autour de lui pour toucher plusieurs cibles proches. | Terminer le combo en attaquant les ennemis qui entourent le joueur. |
| Finisher | Pistolet | Salve concentrée | Plusieurs tirs dirigés sur une même cible proche. | Concentrer les dégâts du finisher avec une petite marge de portée par rapport à l'épée. |

La Salve en éventail poursuit le combo en touchant un groupe devant le joueur. La Salve circulaire est proposée en finisher pour les ennemis autour du joueur, en alternative à la Salve concentrée sur une seule cible.

#### Coups aériens

Ces coups se configurent dans le combo aérien séparé. Le stick ne déplace pas le joueur en l'air ; les déplacements indiqués ci-dessous font partie de l'attaque.

| Catégorie | Mode | Nom provisoire | Effet proposé | Intérêt dans le combo |
|---|---|---|---|---|
| Beginner | Épée | Entaille aérienne | Petite avancée vers la cible suivie d'une frappe au contact. | Ouvrir le combo aérien en rejoignant une cible proche. |
| Follower | Épée | Estoc aérien | Déplacement vers une cible plus éloignée, puis attaque avec la pointe. | Rattraper la distance pendant un enchaînement aérien. |
| Finisher | Épée | Frappe plongeante | Le joueur descend en frappant et entraîne la cible vers le sol. | Choisir de ramener le combat au sol. |
| Finisher | Épée | Coupe suspendue | Large frappe au contact qui laisse le joueur en l'air à la fin du coup. | Toucher des ennemis proches et terminer le combo sans forcer le retour au sol. |
| Beginner | Pistolet | Tir aérien | Tir ciblé depuis les airs à courte portée. | Ouvrir le combo aérien sur une cible légèrement hors de portée de la lame. |
| Follower | Pistolet | Tir traversant | Projectile qui traverse des cibles proches alignées dans sa trajectoire. | Toucher plusieurs ennemis proches depuis une position aérienne. |
| Finisher | Pistolet | Tir descendant | Impact qui projette la cible vers le sol tandis que le joueur reste en l'air. | Ramener la cible au sol en conservant la position aérienne du joueur. |
| Finisher | Pistolet | Rafale aérienne | Rafale concentrée sur une cible proche ; le joueur reste en l'air après le coup. | Concentrer les dégâts avec un peu plus d'allonge que l'épée, sans imposer une projection vers le sol. |

Les coups réussis réinitialisent la chute de l'ennemi selon la règle aérienne. Les finishers qui ramènent la cible au sol appliquent leur effet de descente. Chaque finisher remet l'index à 0, y compris lorsque le joueur reste en l'air.

#### Launchers configurables séparément

Coupe montante est offerte et équipée par défaut pour le mode épée au niveau 2, lors du déblocage de la mécanique. Les autres launchers ci-dessous sont à acheter chez Emmanuel à partir du niveau 2. Ils sont utilisables uniquement au sol. Ces premières variantes occupent l'emplacement dédié aux launchers et se déclenchent pendant un combo après un beginner ou un follower, hors finisher. Commande : stick à l'opposé de la cible active + Arme 1 (Carré) ou Arme 2 (Triangle). Chaque launcher remet l'index à 0.

| Catégorie | Mode | Nom provisoire | Effet proposé | Intérêt dans le combo |
|---|---|---|---|---|
| Launcher | Épée | Coupe montante | Projette la cible en l'air ; le joueur reste au sol. | Mettre la cible en l'air tout en conservant sa position au sol. |
| Launcher | Épée | Ascension | Projette la cible et fait monter le joueur avec elle. | Passer directement du combat au sol au combo aérien. |
| Launcher | Pistolet | Tir de projection | Tir à courte portée qui projette la cible en l'air ; le joueur reste au sol. | Projeter une cible légèrement hors de portée du launcher à l'épée. |
| Launcher | Pistolet | Tir orbital | Tir à courte portée qui projette la cible en l'air et laisse une traînée circulaire dans les airs pendant 2 secondes. Chaque application de dégâts de la traînée à la cible réinitialise sa chute. | Ajouter des dégâts persistants et entretenir la présence de la cible en l'air pendant la poursuite du combat. |

La traînée du Tir orbital dure 2 secondes et inflige des dégâts à la cible. Chaque application de dégâts réinitialise sa chute : l'ennemi recommence à retomber depuis sa hauteur actuelle. Les valeurs des dégâts et leur fréquence restent à définir et à tester.

#### Pistes pour le spécial Arme 1 + Arme 2

Le spécial contient un follower puis un finisher, configurés séparément du combo normal. Pour le PoC, il est provisoirement autorisé de choisir pour le spécial un follower déjà équipé dans le combo normal. Sa configuration aérienne utilise les coups aériens du catalogue, avec la même autorisation provisoire de partager un follower.

| Follower proposé | Finisher proposé | Intérêt de l'enchaînement |
|---|---|---|
| Estoc d'approche | Salve concentrée | Rejoindre la cible avec la lame puis concentrer les dégâts du pistolet. |
| Tir perçant | Frappe lourde | Toucher des ennemis alignés puis finir au contact sur une cible déjà à portée de l'épée. |

Ces exemples sont des pistes au sol. En l'air, le joueur utilise le follower et le finisher de sa configuration spéciale aérienne. Au sol comme en l'air, le spécial se déclenche après un beginner ou un follower, puis remet l'index à 0 après son finisher.

Points à préciser plus tard :

- Attaques propres du samouraï, des rats et du Cerbère.
- Timing des enchaînements entre attaques et comportement des appuis anticipés.
- Esquive : direction et distance du déplacement, et comportement de la chute pendant l'esquive aérienne.
- Invulnérabilité de l'esquive : placement de la fenêtre d'invulnérabilité dans l'animation à préciser.
- Ciblage : comportement du verrouillage et du changement de cible, portée de détection automatique et perte du verrouillage lorsque la cible est vaincue ou trop éloignée.
- Caméra : réglages du cadrage et du lissage, distance maximale de verrouillage, gestion des murs et des obstacles, et comportement lorsque la cible passe derrière le joueur.
- Durée et point de départ du délai autorisé entre deux attaques du combo.
- Équilibrage du prix et du rythme d'achat du quatrième slot au sol pour le PoC. La progression jusqu'à 8 slots relève de la suite du jeu.
- Effet des autres transitions sol/air sur l'index, hors saut, launcher et atterrissage.
- Validation des coups aériens de départ et sélection des alternatives du catalogue à retenir pour le PoC, avec un combo aérien de 3 slots.
- Équilibrage du maintien aérien : chute de l'ennemi, intervalle entre les coups et comportement selon les types d'ennemis.
- Launchers : sélection des variantes supplémentaires à produire pour chaque mode et équilibrage de leurs effets ; Coupe montante est offerte au niveau 2, les autres launchers retenus sont à acheter à partir de ce niveau.
- Équilibrage du spécial avec les coups du catalogue du PoC et essais de la réutilisation provisoire d'un follower du combo normal.
- Spécial : équilibrage du prix de son slot et essais du cooldown retenu de 5 secondes.
- Sélection des coups de chaque mode et validation de leurs effets et de leur utilité en prototype.
- Bonus de dégâts et de portée liés au style, seuils d'activation et effets visuels associés.
- Stagger : valeurs des gains par coup et durée de l'étourdissement selon l'ennemi.
- Style : valeurs des gains et des bonus, seuils des rangs, détection des enchaînements répétés, délai et vitesse de baisse. Application de la perte d'un rang : points conservés aux rangs supérieurs à C.
- Décider si un tir de soutien séparé est utile. Si retenu : définir sa touche, sa durée et les limites du maintien aérien, pour éviter de suspendre une cible indéfiniment.
- Validation du finisher plongeant proposé, de son effet à l'impact et de la transition vers le combat au sol.
- Sélection du catalogue supplémentaire à acheter et modalités de remplacement pour chaque catégorie.
- Priorité du prototype : tester les combos de départ définis au sol et en l'air, l'achat du quatrième slot au sol, l'alternance lame/pistolet avec l'index partagé, les finishers, le saut et l'esquive. Le combo aérien reste à 3 coups. Intégrer le déblocage du launcher au niveau 2 avec Coupe montante offerte, l'achat des launchers supplémentaires et l'achat du slot du spécial dans la boutique d'Emmanuel. Le tir de soutien séparé et le ralentissement de la chute du personnage restent des pistes optionnelles.


