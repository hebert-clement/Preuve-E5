# Mise en place d’un reverse proxy Apache sous Linux

## Contexte
Dans le cadre de mon stage, j’ai été amené à installer et configurer un serveur **reverse proxy** afin de centraliser l’accès à un serveur web interne.  
Cette tâche m’a permis de renforcer mes compétences en **administration Linux**, **configuration Apache** et **gestion des services réseau**.

---

## Objectif
Mettre en place un serveur reverse proxy HTTP permettant :
- de rediriger les requêtes clientes vers un serveur backend,
- de mieux maîtriser la gestion des accès,
- de comprendre le fonctionnement des échanges HTTP côté serveur.

---

## Environnement technique
- Système : Linux Debian
- Serveur web : Apache2
- Type d’architecture : Reverse Proxy
- Réseau : Local

---

## Étapes de configuration

### 1. Installation du serveur Apache
Installation du serveur Apache2 à l’aide du gestionnaire de paquets :

```bash
sudo apt update
sudo apt install apache2 -y
```
### 2. Activation des modules nécessaires

Activation des modules Apache requis pour le fonctionnement du reverse proxy :
```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_balancer
sudo a2enmod lbmethod_byrequests
sudo systemctl restart apache2
```
Ces modules permettent à Apache de relayer les requêtes HTTP vers un serveur distant.

### 3. Configuration du reverse proxy
**Création du fichier de configuration**  
Un fichier de configuration dédié est créé dans le répertoire des sites disponibles :
```bash
sudo nano /etc/apache2/sites-available/reverse-proxy.conf
```
**Configuration du VirtualHost**  
Configuration du virtual host permettant la redirection des requêtes vers le serveur backend :
```bash
<VirtualHost *:80>
    ServerAdmin admin@example.com
    ServerName mon-proxy.local

    ProxyRequests Off
    ProxyPreserveHost On

    ProxyPass / http://backend_server/
    ProxyPassReverse / http://backend_server/

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
### 4. Activation du site
Activation du site et rechargement de la configuration Apache :
```bash
sudo a2ensite reverse-proxy.conf
sudo systemctl reload apache2
```

## Résultat obtenu
Les requêtes HTTP envoyées vers mon-proxy.local sont correctement redirigées vers le serveur backend.

- Le serveur Apache joue le rôle d’intermédiaire entre les clients et le serveur cible.
- La configuration est fonctionnelle et stable dans un environnement local.
- 
### Note théorique : Pourquoi un Reverse Proxy ?
Durant cette mission, j'ai dû assimiler la différence fondamentale entre :
- Un **Proxy** : Agit pour le compte des clients (sortant vers Internet).
- Un **Reverse Proxy** : Agit pour le compte des serveurs (entrant depuis Internet).
C'est cette configuration "Reverse" que j'ai mise en œuvre pour sécuriser l'accès à mon serveur backend et centraliser la gestion du certificat SSL.

## Compétences développées
Cette activité m’a permis de :

- comprendre le rôle et le fonctionnement d’un reverse proxy,
- configurer des services Apache via des fichiers VirtualHost,
- utiliser les modules Apache liés au proxy,
- renforcer mes compétences en administration système Linux,
- manipuler et structurer des configurations réseau professionnelles.

## Conclusion

La mise en place de ce reverse proxy Apache m’a permis d’acquérir des compétences concrètes en administration de serveurs et en architecture web.
Cette expérience constitue une base solide pour la gestion de services web et la sécurisation des accès dans un environnement professionnel.

## Bilan personnel & Analyse (Référentiel E5)

### Lacunes identifiées et besoins en formation
* **Théorie des flux** : Au début de la mission, j'ai dû effectuer des recherches théoriques pour bien distinguer le rôle d'un **Proxy** (protection du client) et d'un **Reverse Proxy** (protection et gestion du serveur).
* **Protocoles et Sécurité** : J'ai rencontré des difficultés lors de la mise en place de la redirection automatique du **HTTP vers le HTTPS**. Cela m'a permis de comprendre le fonctionnement des codes de redirection (301/302) et la configuration des ports 80 et 443.

### Apports de l'expérience
* **Diagnostic réseau** : Utilisation des outils de développement du navigateur et des logs Apache pour identifier pourquoi une redirection ne fonctionnait pas.
* **Compétence technique** : Maîtrise de la réécriture d'URL et des directives de redirection sécurisée.

### Focus sur la sécurisation (HTTPS)
* **Certificat Auto-signé** : Conformément aux consignes de la mission, j'ai généré et mis en place un certificat auto-signé. 
* **Lien avec la formation** : Cette manipulation a permis de réinvestir les notions vues en cours sur l'utilitaire `openssl` et la gestion des hôtes virtuels sur le port 443.
* **Résultat** : Chiffrement des flux entre le client et le proxy validé (malgré l'alerte de sécurité normale pour un certificat non signé par une autorité publique).
---
[⬅️ Retour au tableau de bord](../README.md)
