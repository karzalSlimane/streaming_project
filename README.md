# Projet de Pipeline de Streaming de Données en Temps Réel

## Description du Projet

Ce projet vise à concevoir et déployer un pipeline de données en temps réel utilisant des technologies modernes telles que Kafka, PySpark, MongoDB, Cassandra et Streamlit. Le pipeline collecte des données, les traite en temps réel, les stocke dans des bases de données distribuées et fournit une visualisation interactive des résultats. L'objectif est d'analyser et de suivre en temps réel les utilisateurs et leurs comportements.

### Technologies Utilisées

- **Kafka** : Pour l'ingestion des données en temps réel via des topics.
- **PySpark Structured Streaming** : Pour traiter les flux de données en temps réel.
- **MongoDB** : Pour le stockage des données brutes.
- **Cassandra** : Pour le stockage des données agrégées et la gestion des requêtes rapides.
- **Streamlit** : Pour créer un tableau de bord interactif et surveiller les résultats.
- **Docker et Docker Compose** : Pour orchestrer et déployer l'ensemble du pipeline dans des conteneurs.

## Architecture

Le pipeline de données est constitué de plusieurs étapes clés :

1. **Ingestion des Données** : Les données sont produites et envoyées dans des topics Kafka par un producteur Kafka.
2. **Traitement des Données** : Les flux de données sont consommés par PySpark Structured Streaming pour effectuer des transformations en temps réel et calculer des agrégats.
3. **Stockage** :
   - Les données brutes sont stockées dans **MongoDB** pour garantir une flexibilité maximale.
   - Les agrégats sont insérés dans **Cassandra** pour permettre des requêtes rapides et scalables.
4. **Visualisation et Monitoring** : Un tableau de bord interactif est développé avec **Streamlit** pour afficher les résultats en temps réel et fournir une supervision du pipeline.
5. **Tests et Optimisation** : Des tests unitaires sont exécutés pour assurer la stabilité et les performances du système. Des mécanismes de surveillance sont mis en place pour suivre l’état des services et optimiser le pipeline.

## Prérequis

- **Docker** : Pour créer et gérer des conteneurs.
- **Docker Compose** : Pour orchestrer les services multiples.
- **Python 3.x** : Pour exécuter les scripts de traitement de données.
- **Kafka**, **PySpark**, **MongoDB**, **Cassandra**, **Streamlit** doivent être configurés et accessibles via Docker.

## Installation

### 1. Cloner le dépôt

Clonez le dépôt GitHub dans votre répertoire local :

```bash
git clone https://github.com/karzalSlimane/projet-streaming.git
cd projet-streaming
