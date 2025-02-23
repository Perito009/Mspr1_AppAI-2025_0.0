# routes/country_routes.py

from flask import Blueprint, jsonify
import mysql.connector

# Créer un blueprint pour les routes liées aux pays
country_bp = Blueprint('country', __name__, url_prefix='/country')

# Config de la BDD
db_config = {
    'host': 'localhost',
    'user': 'root',      # Remplace par ton utilisateur MySQL
    'password': 'Root', # Remplace par ton mot de passe MySQL
    'database': 'dbCovid19DataViz'
}

# Route GET pour récupérer tous les pays
@country_bp.route('/', methods=['GET'])
def get_all_countries():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Country")
        countries = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(countries)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
