from flask import Flask, request
import json
from power_plant_data_service.plant_data import power_plant_data

app = Flask(__name__)


@app.route('/')
def sorted_plants_country():
    page_size= request.args.get('page_size')

    if page_size is None:
        return "provide page size"

    current_page = request.args.get('current_page')

    if current_page is None:
        return "provide current page"

    current_page=int(current_page)
    page_size=int(page_size)

    newlist = sorted(power_plant_data(current_page, page_size), key=lambda k: k['Country'])

    power_plants = json.dumps(newlist, default=str)
    return power_plants


if __name__ == '__main__':
    app.run(debug=True, port=5000)