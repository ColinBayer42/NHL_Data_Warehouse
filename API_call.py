import requests

def API_Call(endpoint):
# declare API URL as constant
    API_URL = "https://statsapi.web.nhl.com/api/v1/"
    response = requests.get(API_URL + endpoint, params={"Content-Type": "application/json"})
    data = response.json()
    return(data)
    