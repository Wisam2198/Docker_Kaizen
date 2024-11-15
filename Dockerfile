# Utiliser l'image officielle de Python 3.9
FROM python:3.9-slim

# Mettre à jour les paquets et installer pip (si nécessaire)
RUN apt-get update && apt-get install -y python3-pip

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 8080 (si nécessaire)
EXPOSE 8080

# Lancer l'application (si nécessaire)
CMD ["python", "app.py"]
