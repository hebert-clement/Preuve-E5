# Documentation Technique et Bilans

Ce dossier centralise toutes les procédures d'installation, les configurations spécifiques et les bilans d'expériences liés au projet Reverse Proxy.

---

## Sommaire des documentations

### Mission 1 : Mise en place du socle
* **[Procédure d'installation](./procedure-installation-apache.md)** : Guide étape par étape pour l'installation d'Apache2, l'activation des modules proxy et la génération du certificat SSL.

### Mission 2 - V1 : Équilibrage de charge (Archive)
* **[Configuration Load Balancing](./configuration-load-balancing.md)** : Documentation sur la tentative de mise en place d'un cluster avec l'algorithme `byrequests`. *Note : Cette solution a été archivée car les serveurs backends hébergeaient des services différents.*

### Mission 2 - V2 : Proxy Multi-sites (Solution Finale)
* **[Configuration Multi-URL](./configuration-multi-url.md)** : Documentation finale expliquant l'aiguillage par VirtualHosts et le diagnostic des redirections IIS.

### Mission 3 : Mise à jour Auto
* **[Configuration Mise è jours Auto](./maintenance-automatique.md)** : Documentation finale expliquant le proceder de mise a jour Auto.

### Mission 4 : Mise à jour Auto
* **[Configuration d'une centralisation des logs](./centralisation-logs.md)** : Documentation finale expliquant la configuration de Graylog.
---

## Ressources et Sources externes

Pour mener à bien ces missions, je me suis appuyé sur les documentations suivantes :

* **[Documentation officielle Apache](https://httpd.apache.org/docs/current/fr/mod/mod_proxy.html)** : Détails sur le module `mod_proxy`.
* **[Guide IONOS - Reverse Proxy](https://www.ionos.fr/digitalguide/serveur/configuration/configuration-apache-en-reverse-proxy/)** : Tutoriel de base pour la configuration initiale.
* **[Guide pour activer Unattended Upgrade](https://linuxblog.io/how-to-enable-unattended-upgrades-on-ubuntu-debian/)** : Tutoriel de base pour la configuration initiale.
* **[Documentation officielle Docker](https://docs.docker.com/)** : tutoriel sur l'installation de docker et de sa maintenance.

---
[⬅️ Retour au tableau de bord](../README.md)
