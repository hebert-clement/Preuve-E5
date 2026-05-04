# Maintenance Préventive : Mises à jour Automatiques

## Objectif
Assurer la sécurité et la stabilité des VMs en automatisant l'installation des mises à jour de sécurité Debian sans intervention manuelle.

## Solution Technique : Unattended-Upgrades
Le paquet `unattended-upgrades` a été installé et configuré pour :
* Télécharger et installer les correctifs de sécurité quotidiennement.
* Nettoyer les anciens paquets inutiles pour libérer de l'espace disque.
* Envoyer (optionnel) des notifications en cas d'erreur.

## Installation et Configuration
1. **Installation** : `sudo apt update && sudo apt install unattended-upgrades`
2. **Activation** : `sudo dpkg-reconfigure -plow unattended-upgrades`
3. **Fichiers modifiés** :
   * `/etc/apt/apt.conf.d/50unattended-upgrades` (Paramétrage des dépôts)
   * `/etc/apt/apt.conf.d/20auto-upgrades` (Fréquence des mises à jour)

---

## Bilan de compétences - Mission 3

### Compétences et Savoir-faire
* **Maintenance préventive** : Automatisation des tâches d'administration pour garantir la continuité de service.
* **Gestion de la sécurité** : Réduction de la fenêtre d'exposition aux vulnérabilités (failles 0-day).

### Apports de l'expériences
* Maîtrise de la gestion des paquets sous Debian.
* Compréhension des cycles de mise à jour système.

---
[⬅️ Retour au tableau de bord](../README.md)
