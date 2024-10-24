# Utiliser une image de base légère pour Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de dépendances dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/reports

# Copier tout le code du projet dans le conteneur
COPY . .

# Exposer le port (si ton application a besoin d'un port, par exemple pour une API Flask)
# EXPOSE 5000

# Spécifier la commande pour démarrer l'application
CMD ["python", "conversion.py"]
