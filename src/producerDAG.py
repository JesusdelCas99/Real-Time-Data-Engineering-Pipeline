import requests


def getUserInfo():

    response = requests.get("https://randomuser.me/api/")
    data = response.json()

    userInfo = {
        'username': data['results'][0]['login']['username'],
        'password': data['results'][0]['login']['password'],
        'name': data['results'][0]['name']['first'],
        'phone': data['results'][0]['phone'],
        'email': data['results'][0]['email'],
        'city': data['results'][0]['location']['city'],
        'state': data['results'][0]['location']['state'],
        'country': data['results'][0]['location']['country']
    }

    return userInfo


if __name__ == "__main__":
    userInfo = getUserInfo()

    print(userInfo)