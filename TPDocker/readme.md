# explication de docker et ses commandes:
### image Docker:
Une image c'est comme une classe (en java), qui fonctionnera de la même manière partout où on l'utilise (si on a docker de fonctionnel).
L'image va être
### conteneur Docker:
le conteneur est comme une instance d'une classe (en java). Il peut être appelé via le réseau.
les ports:
permet de lier le conteneur a l'hote pour appeler une application en réseau.

La conteneurisation permet de pouvoir appeler de n'importe où les conteneurs et donc leurs applications.

## les commandes dans le dockerfile:
la commande FROM:
la fonction pour appeler une image qui servira de base a l'application
la commande run:
(on peut en faire plusieurs) commande pour créer l'application.
la commande copy:
permet de copier vers la position indiquée
la commande expose:
c'est pour spécifier le port qu'on va utiliser
la commande cmd:
commande que l'on veut executer dans le conteneur

## les commandes dans le terminal/ cmd
docker build permet de faire une image depuis le conteneur indiqué
docker run permet d'instancier une image
docker exec pour lancer une commande sur le conteneur
docker ps pour savoir quels sont les conteneurs qui tournent
docker images pour afficher les images qu'on a recup

## exemple d'execution :
sudo docker build -t [nom du fichier]:01 .
sudo docker run -d -p 5000:5000 [nom du fichier]:01
sudo docker exec -it [le retour du run] /bin/bash
sudo docker logs [id renvoyé par le build]

tout supprimer sudo docker system prune -a && sudo docker images purge