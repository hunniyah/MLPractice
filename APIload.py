import requests

def getRandomUser():
    url="https://randomuser.me/api/"
    try:
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            user_info=data['results'][0]
            gender=f"{user_info['gender']}"
            name=f"{user_info['name']['title']} {user_info['name']['first']} {user_info['name']['last']}"
            city=f"{user_info['location']['city']}"
            country=f"{user_info['location']['country']}"
            email=f"{user_info['email']}"
            username=f"{user_info['login']['username']}"
            password=f"{user_info['login']['password']}"

            print("name:",name)
            print("gender:",gender)
            print("city:",city)
            print("country:",country)
            print("email:",email)
            print("username:",username)
            print("password:",password)
        else:
            print(f"Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
getRandomUser()