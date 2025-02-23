# models/country_model.py

from database.db import get_db_connection

class CountryModel:

    @staticmethod
    def get_all_countries():
        """
        Récupérer tous les pays de la base de données.
        """
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Country")
            countries = cursor.fetchall()
            return countries
        except Exception as e:
            print(f"Erreur lors de la récupération des pays : {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def get_country_by_id(country_id):
        """
        Récupérer un pays par son ID.
        """
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Country WHERE IdCountry = %s", (country_id,))
            country = cursor.fetchone()
            return country
        except Exception as e:
            print(f"Erreur lors de la récupération du pays : {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def add_country(data):
        """
        Ajouter un nouveau pays à la base de données.
        """
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            sql = """
                INSERT INTO Country (IdCountry, Country, Continent, Region, Death, Serious_Critical)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data['IdCountry'], data['Country'], data['Continent'], data['Region'], data['Death'], data['Serious_Critical']
            ))
            connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de l'ajout du pays : {e}")
            connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def update_country(country_id, data):
        """
        Mettre à jour les informations d'un pays existant.
        """
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            sql = """
                UPDATE Country
                SET Country = %s, Continent = %s, Region = %s, Death = %s, Serious_Critical = %s
                WHERE IdCountry = %s
            """
            cursor.execute(sql, (
                data['Country'], data['Continent'], data['Region'], data['Death'], data['Serious_Critical'], country_id
            ))
            connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de la mise à jour du pays : {e}")
            connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def delete_country(country_id):
        """
        Supprimer un pays de la base de données.
        """
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Country WHERE IdCountry = %s", (country_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Erreur lors de la suppression du pays : {e}")
            connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()