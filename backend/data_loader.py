import requests

def fetch_meteor_events():
    url = "https://www.amsmeteors.org/members/api/open_api/get_events"
    
    response = requests.get(url)
    data = response.json()
    
    return data