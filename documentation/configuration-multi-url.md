# Configuration du Proxy Multi-sites (VirtualHosts)

## Évolution du besoin
Suite à une demande du tuteur, l'architecture initiale en "Load Balancing" (répartition de charge) a été modifiée pour une gestion "Multi-sites". L'objectif est d'attribuer une URL unique à chaque serveur backend pour une identification précise des services.

## Architecture Multi-URL
Le serveur Apache a été configuré avec trois **VirtualHosts** distincts sur le port 443 :

* **URL 1** : `visor.cloud-services.fr`      ➔ Backend : `X.X.X.2`
* **URL 2** : `hkvision.cloud-services.fr`   ➔ Backend : `X.X.X.160`
* **URL 3** : `vanderbilt.cloud-services.fr` ➔ Backend : `X.X.X.129`

## Configuration Technique
Pour réaliser cet aiguillage, j'ai utilisé la directive `ServerName` dans chaque bloc VirtualHost. Le proxy analyse l'en-tête HTTP "Host" envoyé par le navigateur pour déterminer vers quel serveur interne envoyer la requête.

## Sécurisation : Blocage de l'accès par IP
Afin de renforcer la sécurité de l'infrastructure, j'ai mis en place un blocage des requêtes qui n'utilisent pas les noms de domaine autorisés (VirtualHosts).

* **Objectif** : Empêcher la découverte du serveur par simple scan d'IP.
* **Méthode** : Utilisation d'un VirtualHost par défaut capturant le trafic sur l'IP, associé à une directive `ErrorDocument 403`.
* **Résultat** : L'utilisateur reçoit une page personnalisée "Accès Interdit" au lieu de la page par défaut d'Apache.

## Focus Technique : Proxying Avancé (Cas Hikvision)

Le serveur de caméras Hikvision présentait une difficulté technique majeure : il tentait de forcer le navigateur client à utiliser son adresse IP locale (`X.X.X.160`), contournant ainsi le domaine public du proxy.

### Problématiques rencontrées
* **Redirections forcées (302 Found)** : La caméra renvoyait des en-têtes HTTP "Location" contenant l'IP interne au lieu du nom de domaine.
* **IP "Hardcodée"** : L'adresse IP locale était présente directement dans le code source des fichiers JavaScript et XML, provoquant des ruptures de session dès la connexion.
* **Boucle de redirection (Infinite Loop)** : Un conflit de protocole (HTTP/HTTPS) générait une erreur de redirection infinie sur Firefox.

### Solutions et outils utilisés
1. **Analyse de flux (Troubleshooting)** : Installation et utilisation de `tcpdump` pour capturer le trafic en temps réel et identifier les fuites d'IP dans les en-têtes HTTP.
2. **Réécriture de contenu (`mod_substitute`)** :
    * Activation du filtrage sur les types MIME `text/javascript` et `application/xml`.
    * Remplacement dynamique de l'IP `X.X.X.160` par le domaine `hkvision.cloud-services.fr` dans tout le flux sortant.
3. **Double Chiffrement SSL** : Configuration d'Apache pour qu'il communique en HTTPS avec le backend (`SSLProxyEngine On`), tout en ignorant les alertes de certificats auto-signés via `SSLProxyCheckPeerCN Off`.
4. **Correction des en-têtes (Headers)** : Utilisation de `Header edit Location` pour réécrire les redirections 302 à la volée.

---

## Bilan de compétences - Conclusion de la Mission

### Compétences techniques validées
* **Diagnostic réseau avancé** : Capacité à utiliser des outils de capture de paquets (`tcpdump`) pour isoler un bug complexe.
* **Proxying de haut niveau** : Mise en place de réécriture de contenu (Data manipulation) et non plus seulement de l'aiguillage de trafic.
* **Gestion de la sécurité SSL/TLS** : Maîtrise des échanges sécurisés entre le proxy et les serveurs backend.

### Apports personnels
Cette mission m'a permis de comprendre que la mise en place d'un proxy ne se limite pas toujours à l'application de règles standards. Face à des matériels propriétaires (comme Hikvision), il est nécessaire de "hacker" le flux de données pour garantir une expérience utilisateur transparente et sécurisée. La résolution de ce problème a demandé de la rigueur et une analyse méthodique des échanges client-serveur.

---
[⬅️ Retour au tableau de bord](../README.md)
