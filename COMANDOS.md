## Después de creado el repositorio de forma manual hacemos lo siguiente:
- git init
git add .
git commit -m "Proyecto de automatización de despliegue en GCR"
## Vinculamos nuestro repositorio local con el remoto en GitHub y le damos el nombre de origin
git remote add origin https://github.com/KevinInoCol/Automatizacion-Deploy-en-GCR-de-GCP.git

## Tu repo probablemente usa "main" como rama principal
git branch -M main

## Hacemos el push al repositorio remoto en GitHub 
git push -u origin main
## Si da error al momento de subir como un "remote: Invalid username or password" y "fata: Authentication failed for ..". Entonces ve al:
https://github.com/settings/tokens





# Suele pasar que te confundiste en algo, digamos que erraste en el cicd.yaml:
- git status
- git add .github/workflows/cicd.yaml
- git commit -m "cicd.yaml take 3"

- git push






# --------------------------- Comandos típicos para Despliegue manual -----------------------

## Paso 0: Vinculación
gcloud init

## Paso 1: Creación del repositorio de Artifact Registry
gcloud artifacts repositories create repo-project-kkk-fastapi --repository-format docker --project project-mlops-10-streamlit --location us-central1

## Paso 2: Crear la imagen de mi APLICACION y subir al repositorio
gcloud builds submit --config=cloudbuild.yaml --project project-mlops-10-streamlit

## Paso 3: Comando para despliegue o ejecución de la imagen en el repositorio
gcloud run services replace service.yaml --region us-central1 --project project-mlops-10-streamlit

## Paso 4: OPCIONAL, Dar permisos de acceso a mi APLICACION. ESTO SE EJECUTA UNA SOLA VEZ
gcloud run services set-iam-policy servicio-fastapi-kevin-inofuente gcr-service-policy.yaml --region us-central1 --project project-mlops-10-streamlit