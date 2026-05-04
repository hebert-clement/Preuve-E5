# Schémas Réseau et Évolution de l'Architecture
Ce dossier retrace l'évolution de l'infrastructure mise en place. Il permet de visualiser le passage d'un proxy simple à une solution multi-sites, en passant par l'étape de test du Load Balancing.

---
## 1. Architecture Initiale (Mission 1)
*Objectif : Sécuriser l'accès à un serveur unique via un tunnel HTTPS.*
```mermaid
graph LR
    Client["💻 Client (Internet)"] -->|Port 443 - HTTPS| Proxy["🛡️ Reverse Proxy<br>(X.X.X.120)"]
    Proxy -->|Port 80 - HTTP| Backend["🖥️ Serveur Backend 1<br>(X.X.X.2)"]

    style Proxy fill:#FF0000,stroke:#333,stroke-width:2px,color:#fff
    style Backend fill:#0090FF,stroke:#333,stroke-width:2px,color:#fff
```
## 2. Architecture de Test : Load Balancing (Mission 2 - V1)
*Objectif : Répartir la charge entre trois serveurs identiques (Haute Disponibilité).*
```mermaid
graph TD
    Client["💻 Client"] -->|Requêtes| Proxy["⚖️ Apache Load Balancer"]
    
    subgraph "Cluster : backendcluster"
        Proxy -->|Répartition 1/3| B1["🖥️ Backend 1<br>(X.X.X.2)"]
        Proxy -->|Répartition 1/3| B2["🖥️ Backend 2<br>(X.X.X.160)"]
        Proxy -->|Répartition 1/3| B3["🖥️ Backend 3<br>(X.X.X.129)"]
    end

    style Proxy fill:#FF0000,stroke:#333,stroke-width:2px,color:#fff
    style B1 fill:#0090FF,stroke:#333,color:#fff
    style B2 fill:#0090FF,stroke:#333,color:#fff
    style B3 fill:#0090FF,stroke:#333,color:#fff
```
## 3. Architecture Finale : Multi-sites (Mission 2 - V2)
Objectif : Aiguiller les flux vers des services différents en fonction de l'URL demandée (VirtualHosts).
```mermaid
graph LR
    C["💻 Client"] -->|A : vanderbilt.cloud-services.fr| P["🛡️ Reverse Proxy"]
    C -->|B : visor.cloud-services.fr| P
    C -->|C : hkvision.cloud-services.fr| P

    P -->|Redirection A| S1["🖥️ Serveur IIS<br>(X.X.X.2)"]
    P -->|Redirection B| S2["🖥️ Serveur Hikvision 2<br>(X.X.X.160)"]
    P -->|Redirection C| S3["🖥️ Serveur Vanderbilt 3<br>(X.X.X.129)"]

    style P fill:#FF0000,stroke:#333,stroke-width:2px,color:#fff
    style S1 fill:#0090FF,stroke:#333,color:#fff
    style S2 fill:#0090FF,stroke:#333,color:#fff
    style S3 fill:#0090FF,stroke:#333,color:#fff
```
## Analyse du changement (V1 vers V2)
Le passage de la V1 (Load Balancing) à la V2 (Multi-sites) a été décidé suite à l'analyse des contenus : les serveurs backends hébergeant des services différents, la répartition de charge était incohérente. L'utilisation des VirtualHosts permet une gestion granulaire et précise de chaque application.

---
[⬅️ Retour au tableau de bord](../README.md)
