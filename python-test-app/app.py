from flask import Flask
from prometheus_client import start_http_server, Counter
import os

app = Flask(__name__)
REQUESTS = Counter('hello_worlds_total', 'Numar total de accesari')

@app.route('/')
def hello():
    REQUESTS.inc()
    return "Salut Mihai! Aplicatia ruleaza in K8s si e monitorizata."

if __name__ == '__main__':
    # Pornim exportatorul de metrici pe portul 8000
    start_http_server(8000)
    # Aplicatia ruleaza pe 5000
    app.run(host='0.0.0.0', port=5000)
