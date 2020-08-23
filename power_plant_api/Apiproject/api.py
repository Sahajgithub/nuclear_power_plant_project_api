from flask import Flask, request
import json
from power_plant_data_service.plant_data import power_plant_data


app = Flask(__name__)


<<<<<<< HEAD:Apiproject/api.py

@app.route('/')
def sorted_plants_country():
    page_size= request.args.get('page_size')

    if(page_size == None):
        return "provide page size"

    current_page = request.args.get('current_page')

    if(current_page == None):
        return "provide current page"

    current_page=int(current_page)
    page_size=int(page_size)

    newlist = sorted(get_all_plants(), key=lambda k: k['country'])

    if(len(newlist)%page_size==0):
        max_no_of_pages = len(newlist)/page_size
    else:
        max_no_of_pages = abs(len(newlist)/page_size)+1

    if(current_page>max_no_of_pages):
        return "not enough data"
=======
@app.route('/power_plant')
def power_plant():
    country = request.args.get('country')

    if country is None:
        return "provide a country"
>>>>>>> 23335c9993a0c416f7165b56aa6fca04aba41990:power_plant_api/Apiproject/api.py

    skipped=(current_page-1)*page_size

<<<<<<< HEAD:Apiproject/api.py
    power_plants = json.dumps(newlist[skipped:skipped+page_size])
=======
    power_plants = json.dumps(power_plant_data(country, status, type), indent=10)
>>>>>>> 23335c9993a0c416f7165b56aa6fca04aba41990:power_plant_api/Apiproject/api.py
    return power_plants


if __name__ == '__main__':
    app.run(debug=True, port=5000)