# Utilise une image Python de base
FROM python:3.13-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    build-essential

# Copier le code de l'application dans le conteneur
WORKDIR /app
COPY . .

# Créer et activer un environnement virtuel
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Installer pytest
RUN pip install pytest

# Exécuter les tests avec pytest
CMD ["pytest", "tests/"]
