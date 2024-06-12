import json
from urllib.parse import urlparse
from app import get_profile
import boto3
import os
from dotenv import load_dotenv
load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_table_name = os.getenv('AWS_TABLE_NAME')

os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Obtener la referencia de la tabla existente
table = dynamodb.Table(aws_table_name)


# Lista de palabras clave
keywords = [
    "software", "ingeniería de sistemas", "systems engineering", "system engineer",
    "ingeniería de software", "ingeniero de software", "ingeniera de software",
    "software engineering", "hardware", "internet", "cloud", "computing",
    "machine learning", "data science", "cybersecurity", "networking", "blockchain",
    "big data", "augmented reality", "internet of things", "robotics", "automation",
    "devops", "mobile applications", "web development", "development", "e-commerce",
    "quantum", "computer vision", "natural language processing", "tech startups",
    "fintech", "healthtech", "edtech", "software as a service", "platform as a service",
    "infrastructure as a service", "telecommunications", "semiconductors", "biometrics",
    "computación", "nube", "aprendizaje automático", "ciencia de datos", "datos",
    "ciberseguridad", "redes", "internet de las cosas", "robótica", "automatización",
    "aplicaciones móviles", "desarollo de software", "desarollo web", "comercio electrónico",
    "computación cuántica", "tecnología de la información", "visión por computadora",
    "procesamiento de lenguaje natural", "startups tecnológicas", "software como servicio",
    "infraestructura como servicio", "telecomunicaciones", "biometría", "system", "developer",
    "programmer", "data", "analyst", "architect", "tester", "qa", "sistemas", "desarrollador",
    "programador", "analista de datos", "diseñador", "informática", "tecnología", "technology",
    "nanotechnology", "nanotecnología", "inteligencia artificial", "ciencia", "transformación digital",
    "fullstack", "frontend", "backend", "full-stack", "front-end","back-end","ux", "seguridad", "aplicaciones", "móviles",
    "realidad virtual", "científico de datos", "gestor de proyectos", "embebidos", "información",
    "digitales", "ecommerce", "virtualización", "contenedores", "reality",  "network", "security", "applications", "mobile",
    "automation",   "containers"
]

# Lista de palabras clave específicas adicionales para la segunda verificación
specific_keywords = [
    "ingeniería de sistemas", "systems engineering", "system engineer",
    "ingeniería de software", "ingeniera de software", "software engineering",
    "ingeniero de software", "software engineer", "ingeniero de sistemas",
    "ingeniera de sistemas", "systems engineer"
]

university_name = "Universidad de Cartagena - Colombia"

#funcion que verifica la palabra clave esta dentro 
def has_keyword(industry_name, keywords):
    industry_name_lower = industry_name.lower()
    return any(keyword in industry_name_lower for keyword in keywords)


def validate_profile(profile):
    validator = 0
    cartagena_university = False
    if 'industryName' in profile:    
        if (has_keyword(profile['industryName'], keywords)):
            if(has_keyword(profile['industryName'], specific_keywords)):
                validator += 1
            validator += 1
             

    if 'headline' in profile:    
        if(   has_keyword(profile['headline'], keywords)):
            if(has_keyword(profile['headline'], specific_keywords)):
                validator += 1
            validator += 1
             
    if 'summary' in profile:
        if(  has_keyword(profile['summary'], keywords)):
            if(has_keyword(profile['summary'], specific_keywords)):
                validator += 1
            validator += 1
            

    for experience in profile['experience']:
        if 'title' in experience:
            if( has_keyword(experience['title'], keywords)):
                if(  has_keyword(experience['title'], specific_keywords)):
                 validator += 1
                validator += 1

    #Validación principal si pertenece a la universidad de Cartagena
    for education in profile['education']:
        if 'schoolName' in education:
            if( university_name in education['schoolName'] ): 
                cartagena_university = True 
        if 'fieldOfStudy' in education:                        
            if(  has_keyword(education['fieldOfStudy'], keywords)): 
                validator += 4
              


    if(cartagena_university):
        return validator
    else:
        return 0


with open('profiles.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


count_profiles_validates = 0
for profile in data:
    parsed_url = urlparse(profile['Profile_link'])
    user_name = parsed_url.path.split('/in/')[-1]
    user = get_profile(user_name)
    if not user:
        continue
    number_validations = validate_profile(user)
    if(number_validations is not None and int(number_validations) >= 4):
        profile_data = {
            'public_id': user.get('public_id', ''),
            'userName': user.get('public_id', ''),
            'firstNames': user.get('firstName', ''),
            'lastNames': user.get('lastName', ''),
            'student': user.get('student', False),  
            'headline': user.get('headline', ''),
            'summary': user.get('summary', ''),
            'industryName': user.get('industryName', ''),
            'birthDate': user.get('birthDate', {}),
            'locationName': user.get('locationName', ''),
            'geoCountryName': user.get('geoCountryName', ''),
            'geoLocationName': user.get('geoLocationName', ''),
            'validation_number': number_validations,
            'experience': [
                {
                    'position': exp.get('title', ''),
                    'company': {
                    'companyName': exp.get('companyName', ''),
                           'industries': exp.get('company', {}).get('industries', [])
                    },
                    'timePeriod': exp.get('timePeriod', {})
                     
                      
                } for exp in user.get('experience', [])
            ],
            'education': [
                {
                    'degreeName': edu.get('degreeName', ''),
                    'fieldOfStudy': edu.get('fieldOfStudy'),
                    'timePeriod': edu.get('timePeriod', {}),
                       'university': {
                        'universityName': edu.get('school', {}).get('schoolName', ''),
                    }
                } for edu in user.get('education', [])
            ],
            'languages': user.get('languages', []),
            'certifications': [
                {
                    'name': cer.get('name', ''),
                    'authority': cer.get('authority', ''),
                    'timePeriod': cer.get('timePeriod', {}),
                    'url': cer.get('url'),
                    'company': {
                        'name': cer.get('company', {}).get('name', ''),
                        'universalName': cer.get('company', {}).get('universalName', '')
                    }

                } for cer in user.get('certifications', [])
            ],
            'skills': user.get('skills', [])
        }
        print()
        count_profiles_validates += 1
        table.put_item(Item=profile_data)
        print(profile_data['userName'], " - Profile inserted successfully. - number: ", count_profiles_validates)


print(count_profiles_validates)


