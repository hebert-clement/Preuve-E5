# Audit et Optimisation du Référencement

## Objectif du TP
Réaliser l'audit technique d'un site existant pour identifier les freins au référencement naturel et proposer des axes d'amélioration basés sur les standards du web et les critères SEO modernes.

## Méthodologie
L'analyse a été effectuée à l'aide de l'outil **W3C Markup Validation Service** et une inspection manuelle basée sur les piliers du SEO.

---

## Rapport d'Audit : `index.html`

### Structure Métadonnées
* **Balises Meta** : La description actuelle est trop générique et les mots-clés sont absents.
  * *Amélioration* : Rédiger une meta-description incitative de 150 caractères et enrichir la balise `<title>` avec une phrase descriptive plutôt qu'une suite de mots.
* **Données Structurées** : Absence totale de balisage JSON-LD.
  * *Amélioration* : Implémenter des schémas pour aider les moteurs de recherche à comprendre le type de contenu.

### Sémantique et Contenu Visible
* **Hiérarchie** : Utilisation de multiples balises `<h1>`, ce qui fragmente la compréhension du sujet principal.
  * *Amélioration* : Conserver un seul `<h1>` unique et structurer le reste avec des `<h2>` et `<h3>`.
* **Maillage interne** : Les ancres de liens sont trop vagues.
  * *Amélioration* : Utiliser des textes d'ancres descriptifs intégrant des mots-clés.
* **Performance** : Utilisation de `@import` pour le CSS, ce qui ralentit le rendu.
  * *Amélioration* : Remplacer par des balises `<link>` pour un chargement parallèle.

### Accessibilité et Mobilité
* **Images** : Absence d'attributs `alt`.
  * *Amélioration* : Ajouter des descriptions textuelles pour l'accessibilité et le référencement image.
* **Responsive Design** : Absence de la balise `viewport`. Le site n'est pas adapté aux mobiles.
  * *Amélioration* : Ajouter `<meta name="viewport" content="width=device-width, initial-scale=1">` et utiliser un framework comme Bootstrap pour le responsive.

### Expérience Utilisateur
* **Sémantique** : Trop grande dépendance aux balises `<div>`.
  * *Amélioration* : Utiliser les balises sémantiques `<header>`, `<nav>`, `<main>`, `<section>`, et `<footer>`.

---
[⬅️ Retour au tableau de bord](../../README.md)
