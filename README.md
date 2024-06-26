# DataExtractor-LinkedinProfiles

## Descripción

**DataExtractor-LinkedinProfiles** es una herramienta diseñada para extraer y procesar datos de perfiles de LinkedIn. Este proyecto es útil para la recopilación de información de perfiles con fines de análisis, investigación de mercado, y más.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal utilizado para el desarrollo del script.
- **DynamoDB**: Base de datos para almacenar la información extraída.
- **BeautifulSoup**: Librería para el web scraping.
- **Requests**: Librería para hacer solicitudes HTTP.
- **Boto3**: SDK de Amazon para interactuar con DynamoDB.
- **python-dotenv**: Para cargar variables de entorno.
- **python3-linkedin**: Cliente de LinkedIn para Python.

## Variables de Entorno

Para configurar el proyecto, es necesario definir las siguientes variables de entorno en un archivo .env basado en el archivo .env.example incluido:

```bash
LINKEDIN_USERNAME: Tu nombre de usuario de LinkedIn.
LINKEDIN_PASSWORD: Tu contraseña de LinkedIn.
AWS_ACCESS_KEY_ID: Tu clave de acceso de AWS.
AWS_SECRET_ACCESS_KEY: Tu clave secreta de AWS.
AWS_TABLE_NAME: Nombre de la tabla de DynamoDb.
```

### Ejemplo de .env:

```bash
LINKEDIN_USERNAME=iusplays@gmail.com
LINKEDIN_PASSWORD=micontra123
AWS_ACCESS_KEY_ID=LFTW7wdasLFTW7wwq2
AWS_SECRET_ACCESS_KEY=NuH1ANwasñ231ANNuHN
AWS_TABLE_NAME=StudentsCartagenaU
```

## Instalación

### Clona el repositorio:

```bash
git clone https://github.com/iLuisOlivares/DataExtractor-LinkedinProfiles.git
cd DataExtractor-LinkedinProfiles
```

##### Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

##### Dependencias Importantes:

Asegúrate de tener instaladas las siguientes librerías:

```bash
pip install requests beautifulsoup4 boto3 python-dotenv python3-linkedin
```

##### Configura las variables de entorno:

Crea un archivo .env en el directorio raíz del proyecto.
Copia el contenido de .env.example a .env y actualiza con tus credenciales.

##### Inicializa la base de datos:

```bash
python createDB.py
```

##### Ejecuta el script principal para iniciar la extracción de datos:

Para procesar y leer los perfiles extraídos:

```bash
python read_process_profiles.py
```

##### Estructura del Proyecto

- app.py: Script principal que contiene el metodo para acceder a perfiles de linkedin
- createDB.py: Script para inicializar la tabla de DynamoDB.
- read_process_profiles.py: Script para procesar y leer los datos de los perfiles extraídos.
- profiles.json: Archivo donde se almacenan temporalmente los datos extraídos del web scraping y exportar perfiles validos a la BD.
- .env: archivo de configuración de variables de entorno.
- .env.example: Ejemplo de archivo de configuración de variables de entorno.
- README.md: Documentación del proyecto.
- requeriment.txt: archivo con las dependencias necesarías.

### Autores

- Luis Olivares Puello
- Cesar Leiva Acuña

### Licencia

Este proyecto está bajo la Licencia MIT.
