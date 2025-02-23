# APIapp.py

from flask import Flask
from routes.country_routes import country_bp

app = Flask(__name__)

# Enregistrer le blueprint
app.register_blueprint(country_bp)

# Route d'accueil
@app.route('/')
def home():
    return "Bienvenue sur l'API Covid-19 !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
