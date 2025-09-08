# Nutze ein offizielles Python-Image als Basis
FROM python:3.10-slim

# Lege ein Arbeitsverzeichnis fest
WORKDIR /app

# Erstelle ein virtuelles Umfeld (venv) an einem festen Ort
RUN python -m venv /opt/venv

# Setze die PATH-Variable, damit Python und Pip vom venv-Pfad verwendet werden
ENV PATH="/opt/venv/bin:$PATH"

# Kopiere die Abhängigkeitsdatei ins Container-Image
COPY requirements.txt ./

# Installiere die Python-Abhängigkeiten in das venv
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Rest des Projektcodes ins Container-Image
COPY . .

# Definiere den Standardbefehl
CMD [ "python", "main.py" ]