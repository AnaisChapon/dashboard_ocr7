import subprocess
import os

# Définir le port pour l'API Flask et le dashboard Streamlit
api_port = "5000"
dashboard_port = "8000"

# Lancer l'API Flask
api_process = subprocess.Popen(["python", "api_complet_light.py"], env=dict(os.environ, PORT=api_port))
print(f"API Flask lancée sur le port {api_port}")

# Lancer le dashboard Streamlit
dashboard_process = subprocess.Popen(["streamlit", "run", "dashboard_complet_light.py", "--server.port", dashboard_port])
print(f"Dashboard Streamlit lancé sur le port {dashboard_port}")
