import requests

def main():

    res=requests.get("http://data.fixer.io/api/latest?access_key=XXXXXXXXXXXX")

    if res.status_code!=200:
        raise Exception("Error API request unsuccessful")
    data=res.json()
    num=data["base"]
    print(num)

if __name__=="__main__":
    main()
