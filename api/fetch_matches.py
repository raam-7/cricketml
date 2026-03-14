import requests

def get_matches(api_key):
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={api_key}&offset=0"
    
    response = requests.get(url)
    data = response.json()

    matches = []

    for match in data["data"]:
        matches.append({
            "id": match["id"],
            "name": match["name"],
            "status": match["status"]
        })

    return matches


if __name__ == "__main__":
    API_KEY = "1a959976-f70e-41e2-a241-c3d8a3266037"
    matches = get_matches(API_KEY)

    for m in matches:
        print(m)


