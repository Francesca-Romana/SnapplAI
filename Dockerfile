# Immagine base: Python 3.12 versione leggera
FROM python:3.12-slim

# Cartella di lavoro dentro il container
WORKDIR /app

# Copia prima solo requirements e installa dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice
COPY . .

# Comando che parte quando lanci il container
CMD ["python", "main.py"]
