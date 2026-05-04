# Configuration de l'Équilibrage de Charge (Load Balancing)

## Architecture du Cluster
Pour cette mission, j'ai mis en place un cluster de serveurs pour garantir la disponibilité et répartir la charge de travail.

* **Nom du cluster** : `backendcluster`
* **Nœud 1** : `X.X.X.2`
* **Nœud 2** : `X.X.X.160`
* **Nœud 3** : `X.X.X.129`

**Algorithme utilisé :** `byrequests`. Ce mode répartit les requêtes de manière équitable entre les nœuds (Round Robin), envoyant chaque nouveau visiteur vers le serveur suivant dans la liste.

---

## Analyse et Justification du Choix Technologique

### Pourquoi avoir abandonné le Load Balancing ?
Initialement, j'avais envisagé une solution de répartition de charge (**Load Balancing**). Cependant, après analyse des serveurs backends et validation auprès de mon tuteur, il est apparu que les trois serveurs hébergent des services **totalement différents** (contenus distincts).

Le Load Balancing n'est utilisé que lorsque plusieurs serveurs hébergent exactement le même site pour répartir le trafic. Utiliser un cluster ici aurait été une erreur technique car l'utilisateur aurait été envoyé aléatoirement sur l'un des trois services différents.

### La solution : Le Proxy Multi-sites (VirtualHosts)
La solution retenue est donc la configuration par **VirtualHosts**. Elle permet au Reverse Proxy d'analyser l'en-tête HTTP `Host` envoyé par le navigateur du client :
1. Le client demande une URL spécifique (ex: `[app1.linkt.local](https://visor.cloud-services.fr/)`).
2. Le Proxy lit cette demande grâce à la directive `ServerName`.
3. Le Proxy aiguille la requête vers le serveur backend correspondant à cette URL précise.

**Résultat** : Un point d'entrée unique (le Proxy) pour trois services distincts et sécurisés.

---

## Résolution de problèmes (Troubleshooting)

### Problème : Redirection automatique vers `/index.asp`
Lors des tests, l'URL était automatiquement complétée par `/index.asp`, ce qui brisait la transparence de la navigation pour l'utilisateur final.

### Analyse et Diagnostic
1. **Identification de la source** : En testant le serveur Backend **X.X.X.2** en direct, j'ai constaté que ce serveur (sous IIS) forçait la redirection vers sa page par défaut.
2. **Analyse des flux** : L'utilisation de l'inspecteur réseau a confirmé que le serveur Windows envoyait une instruction de redirection que le Proxy Apache suivait par défaut.

### Solution mise en œuvre
* **Ajustement des directives** : Modification des directives `ProxyPass` et `ProxyPassReverse` dans le fichier `reverse-proxy.conf`.
* **Réécriture d'en-tête** : Configuration d'Apache pour tenter de masquer le chemin interne envoyé par IIS et maintenir l'URL racine pour l'utilisateur.
* **Note sur les limites** : N'ayant pas accès à l'administration de la VM Windows, la résolution a été concentrée sur la configuration du Reverse Proxy Apache.

---

## Bilan de compétences - Mission 2

### Compétences et Savoir-faire
* **Mise en place de la haute disponibilité** : Configuration d'un cluster pour répartir les requêtes sur trois nœuds.
* **Gestion des algorithmes de répartition** : Maîtrise de la directive `lbmethod=byrequests`.
* **Sécurisation des flux** : Intégration du cluster dans un environnement sécurisé HTTPS avec certificat auto-signé.

### Lacunes identifiées et besoins en formation
* **Interactions Proxy/Backend** : Compréhension de l'impact des configurations par défaut des serveurs de destination (IIS) sur le proxy.
* **Limites d'accès** : Apprentissage de la gestion d'incidents dans un environnement où l'accès à certains équipements est restreint (VM Windows inaccessible).

### Apports de l'expérience
* **Analyse de flux** : Utilisation avancée de l'inspecteur réseau du navigateur pour le diagnostic.
* **Adaptabilité** : Recherche de solutions alternatives au niveau d'Apache pour compenser des paramètres de serveurs tiers.

---
[⬅️ Retour au tableau de bord](../README.md)
