#Conexion al API de Linkedin
from linkedin_api import Linkedin 
from dotenv import load_dotenv
import os


load_dotenv()
email = os.getenv('LINKEDIN_EMAIL')
password = os.getenv('LINKEDIN_PASSWORD')


api = Linkedin(email, password)


# Metodo extractor de perfiles
def get_profile(profile):
    try:
        return api.get_profile(profile)
    except Exception as e:
        print(f"Error al obtener el perfil: {e}")
      
        return None