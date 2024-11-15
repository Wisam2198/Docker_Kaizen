# Utiliser une image de base Python
FROM python:3.9-slim

# Mettre à jour les paquets et installer pip (si nécessaire)
RUN apt-get update && apt-get install -y python3-pip

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances du projet
RUN pip3 install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . .

# Créer le dossier reports
RUN mkdir -p /app/reports

# Spécifier la commande pour démarrer l'application
CMD ["python3", "conversion.py"]
