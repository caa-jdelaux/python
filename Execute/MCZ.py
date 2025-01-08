import requests
import os
#COMMENT IMPORTER REQUESTS
#pip install requests

def lambda_handler(event, context):
    client_id = os.environ['CLIENT-ID']
    client_secret = os.environ['CLIENT-SECRET']
    refresh_token = os.environ['REFRESH-TOKEN']
    routine_id = os.environ['ROUTINE-ID']

    # Obtenir un nouveau token d'accès
    token_url = "https://api.amazon.com/auth/o2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(token_url, data=data)
    access_token = response.json()["access_token"]

    # Exécuter la routine
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    url = f"https://api.amazonalexa.com/v1/routines/{routine_id}/trigger"
    response = requests.post(url, headers=headers)

    return {
        'statusCode': response.status_code,
        'body': 'Routine exécutée avec succès' if response.status_code == 200 else 'Échec de l\'exécution de la routine'
    }

