import requests
url=f"https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
if response.status_code==200:
    joke_data=response.json()
    print("Setup:",joke_data["setup"])
    print("PunchLine:",joke_data["punchline"])
   
else:
    print("Error",response.status_code)
    
          
