# Definition of Done (DoD)

Pour qu'une tâche soit considérée comme "Terminée", elle doit valider les critères suivants :

1. **Code Review** : Le code a été relu et approuvé par au moins un pair (si applicable).
2. **Tests Passés** :
    - Tous les tests unitaires (PyTest) passent avec succès.
    - Pas de régressions identifiées.
3. **Qualité du Code** :
    - Le code respecte les standards PEP 8 (vérifié par `flake8`).
    - Pas de "linting errors" critiques.
4. **Docker** :
    - L'image Docker se construit sans erreur.
    - La taille de l'image finale est inférieure à 100 MB.
    - Le conteneur démarre et répond au Health Check.
5. **CI/CD** :
    - Le pipeline GitHub Actions est au vert (Status: Success).
    - Les scans de sécurité (Trivy) ne remontent pas de vulnérabilités critiques.
