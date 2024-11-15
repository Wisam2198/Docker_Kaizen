FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Créer le dossier de rapports
RUN mkdir -p /app/reports

# Copier le code source dans l'image Docker
COPY . .

# Exposer le port si nécessaire
# EXPOSE 5000

CMD ["python", "conversion.py"]
