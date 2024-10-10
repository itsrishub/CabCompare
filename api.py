from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()


def getcsrf():
    # return BeautifulSoup(requests.get('https://ride.guru').content, 'html.parser').find('input', {'name': 'csrfmiddlewaretoken'})['value']
    session = requests.Session()
    session.get('https://ride.guru')
    return session.cookies.get_dict()

def search(query: str):
    return requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json?types=district,postcode,place,neighborhood,address,poi&autocomplete=true&limit=10&proximity=77.663587,12.994375&access_token=pk.eyJ1IjoiY2hyaXNoYXdlcyIsImEiOiJjbGNpbGV0dmc0M21xM29tb2syZHE3YmU4In0.Vse1fk7Oga4WpeJsWIH28w').json()

def compare():
    return 0

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get")
def read_item():
    # return {"csrf": getcsrf()}
    return getcsrf()

@app.get("/search/{query}")
def read_item(query: str):
    return search(query)