# Chatroom Docker

Ce projet est un serveur de chatroom simple, exécuté dans un conteneur Docker. Il permet aux utilisateurs de se connecter et d'envoyer des messages à travers un port configurable.

Le projet utilise un fichier `.env` pour définir des variables d'environnement qui configurent le serveur de chatroom :

- **CHAT_PORT** : Définit le port sur lequel le serveur écoute. Par défaut, le port est **8888**.
- **MAX_USERS** : Définit le nombre maximal d'utilisateurs autorisés dans la salle de chat. Par défaut, il est défini sur **10** utilisateurs.


Pour construire l'image Docker, exécutez la commande suivante :

```
docker-compose build
```

Ensuite pour lancer le serveur en arrière plan:

```
docker-compose up-d 
```

Pour arrêter le serveur : 

```
docker-compose down
```





