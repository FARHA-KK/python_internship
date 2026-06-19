import requests

url=f"https://api.github.com/users/octocat"
response=requests.get(url)

if response.status_code==200:
    user_data=response.json()
    print("Name:",user_data["name"])
    print("Location:",user_data["location"])
    print("Public repositories:",user_data["public_repos"])
else:
    print("Error ",response.status_code)
        