# Mission : Création d'une Weathermap de supervision (Grafana)

## Objectif
Concevoir une cartographie dynamique du réseau (Weathermap) pour visualiser en temps réel l'état des liens et le trafic entre les différents équipements de l'infrastructure.

## Réalisation Technique
L'outil utilisé est **Grafana** avec le plugin Weathermap, alimenté par des données provenant de **Prometheus**.

### Points clés de la configuration :
* **Modélisation** : Création de nœuds (équipements) et de liens (interfaces réseau).
* **Requêtes PromQL** : Mise en place de calculs pour afficher le débit en bits par seconde et le taux d'utilisation en pourcentage.
  * *Exemple de calcul* : `(rate(if_in_octets{...}[5m]) * 8) / if_speed{...} * 100`.
* **Indicateurs visuels** : Utilisation d'une échelle de couleurs pour identifier immédiatement les saturations ou les pertes de paquets (ping loss).

## Preuves et Livrables
* **[Documentation Utilisateur](./documentation/)** : Guide complet sur la prise en main et la configuration des nœuds/liens.
* **[Dashboards finaux](./captures-weathermap/)** Visualisations des différents segments du réseau.

---
