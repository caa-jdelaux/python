import requests
import os
#COMMENT IMPORTER REQUESTS
#pip install requests

def lambda_handler(event, context):
    client_id = os.environ['amzn1.application-oa2-client.648cc1592a3e4c228a634b9b3ee79900']
    client_secret = os.environ['amzn1.oa2-cs.v1.775b1819bd1cbf34eacf41ff47e71910eda3e278395a1e85e9e5e18e5b44e482']
    refresh_token = os.environ['Atzr|IwEBIHRbyYnW1J1FKWwWkGdBM0MeHc1oFPt5jzExRqH48lkR60UEgRi00XLhe8NkvpKP2MsPYXuRkFWPh4mxauOHY_XGb-LXuy791zTcyX5beSwx-27YQ-QGx5FEOt6n5F9aygUwuFcMLUb4mVaXPFP5f0exuB7vMmqWXfATwuwLTlURHoVxBrVe_gkEvzjf-zLuz9hBPG9LG3JPGKR0qDrBWoTg-xpnj_FzWYrJrfBHIugyxS6AM0KjjOMl7tY_Sycn0AYerReJVb3MwV35I-UV4zHw09vgfRlRqjgAZSW0JyWu084ikey66N-oL46VSSUbTEjSxW9Mr2UhvIXAtp920GyHSDW1pVXfnE5hdDbftRX2lpwtVkpFFoEdEKYxJXOHOzJQ-2YEeCpuYDSbWVOeB2Yy1Z0VCIv91NGpCByZ9-WFAGaoS9ob4tzwAftrECisbaEJpbs1RUpkVlJEEf9eqMvKVq4RL1uM1mPzUwi43884A_qIdGH7sCHw3Fy8qrE3kOrD0NvqManTeqhe3RTzAD_f3cF0-_BOirpXIwrsRtg2LWPpmxObN8TKFFFvIGHtAOFWaXdYAWkvBUigxrKknXwBtCzgeIIrDc0n8cABGKiTcwJBsIh24PTq2fclEOWh7PCGOj_wDEsmyjDaqwBTv2kpuklEgGfpkAfpP5GACOyohn6pIItvbulE0Lkj6BdDgcC4iHSyU09hOZT5UDov57Y9xbm1ANOTEDxasD3Z-EFi5tX5f5Wpp7XGXOnbbL6fscE']
    routine_id = os.environ['NZK4WBezTbmw4XQkWhSn3Q']

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

