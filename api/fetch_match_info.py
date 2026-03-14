import requests

def get_match_info(api_key, match_id):
    
    url = f"https://api.cricapi.com/v1/match_info?apikey={api_key}&id={match_id}"

    response = requests.get(url)

    return response.json()