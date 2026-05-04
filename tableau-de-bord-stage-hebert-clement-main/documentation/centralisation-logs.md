# Mission 4 : Centralisation et Analyse de Logs avec Graylog

## 1. Présentation du besoin
Dans le cadre de l'exploitation du Reverse Proxy, il est devenu indispensable de centraliser les journaux d'événements (logs) pour :
* **Surveiller** la santé des services en temps réel.
* **Détecter** les tentatives d'intrusion ou les erreurs de configuration.
* **Auditer** les accès aux différents backends.

## 2. Choix Technologiques
Le choix s'est porté sur la Stack Graylog, déployée via Docker Compose pour bénéficier de l'isolation des processus et d'une gestion simplifiée des dépendances.

**Composants de la solution :**

* **Graylog 4.3 :** Serveur principal pour la réception, le traitement et la visualisation des logs.
* **OpenSearch 1.3.15 :** Moteur de recherche haute performance utilisé pour indexer et stocker les données.
* **MongoDB 4.4 :** Base de données NoSQL stockant les configurations (utilisateurs, streams, alertes).

**Alternative possible**

Il est possible d'utiliser une image de MongoDB faite par la communauté pour passez outre cette contrainte. La communauté a crée des image MongoDB qui n'utilise pas les instructions AVX. Cela vous permet d'utiliser la version 7.0 de Graylog avec MongoDB qui n'utilise pas d'instruction AVX.

vous pouvez utiliser l'image ghcr.io/fenio/mongodb-no-axv:7.0 par exemple

## 3. Contraintes Matérielles et Adaptations
Lors du déploiement, une contrainte technique majeure a été rencontrée : le processeur (CPU) de la machine hôte ne supporte pas les instructions **AVX**.

* **Le Problème** : Les versions officielles récentes de MongoDB (5.0+) et OpenSearch (2.x) requièrent impérativement l'AVX pour démarrer.
* **La Solution retenue** : Une stratégie de "downgrade" vers des versions stables et compatibles : MongoDB 4.4 et OpenSearch 1.3.15.
* **Alternative identifiée** : Pour utiliser des versions plus récentes de la stack (ex: MongoDB 7.0), il est possible de recourir à des images construites par la communauté (ex: `ghcr.io/fenio/mongodb-no-avx`). Ces images sont recompilées sans l'exigence AVX, offrant une plus grande flexibilité sur du matériel ancien.

## 4. Architecture de Notification (Relais SMTP)
Pour permettre à Graylog d'envoyer des alertes par mail malgré les restrictions réseau (port 25 bloqué), un relais Postfix a été configuré sur la VM hôte.
* **Configuration du Relais :** Redirection vers le relais interne 10.X.X.X.
* **Réécriture d'adresse :** Utilisation d'une table generic pour transformer l'adresse locale technique en une adresse mail valide (clement.hebert@linkt.fr), garantissant la délivrabilité.

## 5. Flux de Données et Ports Utilisés
Le système est configuré pour écouter sur plusieurs points d'entrée :
* **Interface Web :** Port 9000 (Redirigé vers le port 443 via le Reverse Proxy).
* **Entrée GELF :** Port 12201 (UDP/TCP) pour les logs structurés.
* **Entrée Syslog :** Port 1514 (UDP/TCP) pour les logs standards.

## 6. Persistance et Sécurité
* **Volumes :** Les données sont stockées dans des volumes Docker nommés (mongodb_data, os_data, graylog_data) pour éviter toute perte de données lors des mises à jour des conteneurs.
* **Secrets :** Le mot de passe administrateur est sécurisé via un hachage **SHA256** directement dans le fichier de configuration.

# Bilan Personnel
Cette mission m'a permis de maîtriser le cycle complet de gestion des logs, de l'installation de l'environnement Docker jusqu'à la résolution de conflits matériels spécifiques (AVX). J'ai également appris à configurer une chaîne de notification complexe impliquant un relais SMTP et de la réécriture d'en-têtes.

---
[⬅️ Retour au tableau de bord](../README.md)
