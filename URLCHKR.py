import requests
url = input("Enter the url: ")
url ='http://'+url


def url_check(url):
    try:
        get = requests.get(url)
        if get.status_code == 200:
            print(f"{url} is reachable")
        elif get.status_code == 303:
            print(F"{url} is unreachable")
        elif get.status_code == 404:
            print(F"{url} currently down")
        elif get.status_code == 403:
            print(F"{url} is forbidden")
        elif get.status_code == 503:
            print(F"{url} under maintenance")
        else:
            print(f"{url} is not reachable, status code:{get.status_code}")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"{url} does not exist\n Error: {e}")

url_check(url)

