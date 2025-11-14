import requests
from pprint import pprint

def main():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    json = response.json()
    
    for user in json:
        if user["id"] == 2:
            print("Usuario con id 2 encontrado")

if __name__ == "__main__":
    main()