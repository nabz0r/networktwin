# 🌐 Exemples de Topologies Réseau

## 1. Topologie Entreprise Simple
```mermaid
graph TD
    Internet[Internet]
    Firewall[Firewall]
    Router[Routeur Principal]
    CoreSwitch[Switch Cœur]
    
    AccessSwitch1[Switch Accès Étage 1]
    AccessSwitch2[Switch Accès Étage 2]
    
    Serveur1[Serveur Web]
    Serveur2[Serveur BD]
    
    Poste1[Poste Travail 1]
    Poste2[Poste Travail 2]
    Poste3[Poste Travail 3]
    
    Internet --> Firewall
    Firewall --> Router
    Router --> CoreSwitch
    
    CoreSwitch --> AccessSwitch1
    CoreSwitch --> AccessSwitch2
    
    CoreSwitch --> Serveur1
    CoreSwitch --> Serveur2
    
    AccessSwitch1 --> Poste1
    AccessSwitch1 --> Poste2
    AccessSwitch2 --> Poste3
```

### Caractéristiques
- Firewall de protection
- Routeur central
- Switch cœur de réseau
- Séparation physique des étages
- Serveurs centralisés

## 2. Topologie Datacenter
```mermaid
graph TD
    CoreRouter[Core Router]
    Firewall1[Firewall 1]
    Firewall2[Firewall 2]
    
    AggSwitch1[Aggregation Switch 1]
    AggSwitch2[Aggregation Switch 2]
    
    ToRSwitch1[Top of Rack 1]
    ToRSwitch2[Top of Rack 2]
    ToRSwitch3[Top of Rack 3]
    
    Serv1[Serveur App 1]
    Serv2[Serveur App 2]
    Serv3[Serveur BD 1]
    Serv4[Serveur BD 2]
    Serv5[Serveur Cache]
    
    CoreRouter --> Firewall1
    CoreRouter --> Firewall2
    
    Firewall1 --> AggSwitch1
    Firewall2 --> AggSwitch2
    
    AggSwitch1 --> ToRSwitch1
    AggSwitch1 --> ToRSwitch2
    AggSwitch2 --> ToRSwitch3
    
    ToRSwitch1 --> Serv1
    ToRSwitch1 --> Serv2
    ToRSwitch2 --> Serv3
    ToRSwitch2 --> Serv4
    ToRSwitch3 --> Serv5
```

### Caractéristiques
- Architecture multiniveau
- Redondance des firewalls
- Switches d'agrégation
- Switches Top of Rack
- Séparation applicative

## 3. Réseau Campus
```mermaid
graph TD
    Internet[Internet]
    RouterPrincipal[Routeur Principal]
    
    SwitchDistribution1[Switch Distribution 1]
    SwitchDistribution2[Switch Distribution 2]
    
    SwitchAccesBA[Switch Accès Bâtiment A]
    SwitchAccesBB[Switch Accès Bâtiment B]
    SwitchAccesBC[Switch Accès Bâtiment C]
    
    ServeurCentral[Serveur Central]
    ServeurDNS[Serveur DNS]
    ServeurDHCP[Serveur DHCP]
    
    PostesA1[Postes A1]
    PostesA2[Postes A2]
    PostesB1[Postes B1]
    PostesC1[Postes C1]
    
    Internet --> RouterPrincipal
    RouterPrincipal --> SwitchDistribution1
    RouterPrincipal --> SwitchDistribution2
    
    SwitchDistribution1 --> SwitchAccesBA
    SwitchDistribution1 --> SwitchAccesBC
    SwitchDistribution2 --> SwitchAccesBA
    SwitchDistribution2 --> SwitchAccesBC
    
    SwitchDistribution1 --> ServeurCentral
    SwitchDistribution1 --> ServeurDNS
    SwitchDistribution2 --> ServeurDHCP
    
    SwitchAccesBA --> PostesA1
    SwitchAccesBA --> PostesA2
    SwitchAccesBC --> PostesB1
    SwitchAccesBA --> PostesC1
```

### Caractéristiques
- Interconnexion de plusieurs bâtiments
- Routeur principal
- Switches de distribution
- Switches d'accès
- Répartition géographique
- Services centralisés

## 4. Topologie Cloud Hybride
```mermaid
graph TD
    Internet[Internet]
    RouterEntreprise[Routeur Entreprise]
    Firewall[Firewall]
    
    SwitchLocal[Switch Local]
    ServeurLocal1[Serveur Local 1]
    ServeurLocal2[Serveur Local 2]
    
    GatewayCloud[Cloud Gateway]
    
    ServiceCloud1[Service Cloud App]
    ServiceCloud2[Service Cloud BD]
    ServiceCloud3[Service Cloud Backup]
    
    Internet --> RouterEntreprise
    RouterEntreprise --> Firewall
    Firewall --> SwitchLocal
    
    SwitchLocal --> ServeurLocal1
    SwitchLocal --> ServeurLocal2
    
    RouterEntreprise --> GatewayCloud
    
    GatewayCloud --> ServiceCloud1
    GatewayCloud --> ServiceCloud2
    GatewayCloud --> ServiceCloud3
```

### Caractéristiques
- Infrastructure locale
- Connexion cloud sécurisée
- Répartition des services
- Point d'accès unique

## 5. Topologie IoT
```mermaid
graph TD
    Internet[Internet]
    RouterPrincipal[Routeur Principal]
    GatewayIoT[Gateway IoT]
    
    SwitchLocal[Switch Local]
    
    CapteurTemp1[Capteur Température 1]
    CapteurTemp2[Capteur Température 2]
    CapteurHum1[Capteur Humidité 1]
    CapteurLum1[Capteur Luminosité 1]
    
    ServeurCollecte[Serveur Collecte IoT]
    ServeurAnalyse[Serveur Analyse]
    
    Internet --> RouterPrincipal
    RouterPrincipal --> GatewayIoT
    GatewayIoT --> SwitchLocal
    
    SwitchLocal --> CapteurTemp1
    SwitchLocal --> CapteurTemp2
    SwitchLocal --> CapteurHum1
    SwitchLocal --> CapteurLum1
    
    SwitchLocal --> ServeurCollecte
    ServeurCollecte --> ServeurAnalyse
```

### Caractéristiques
- Gateway IoT centralisée
- Collecte multi-capteurs
- Serveur de traitement
- Architecture modulaire

## Points Clés
- Chaque topologie répond à des besoins spécifiques
- Modularité et évolutivité
- Sécurité et redondance
- Adaptation aux contraintes métier

## Recommandations
- Adaptez la topologie à votre contexte
- Pensez à la sécurité et à la performance
- Prévoyez l'évolutivité
- Documentez vos choix d'architecture
