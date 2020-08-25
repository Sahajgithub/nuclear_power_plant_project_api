from flask import Flask, request
import json
from power_plant_data_service.plant_data import specific_power_plant_data


app = Flask(__name__)


@app.route('/power_plant')
def power_plant():

    country = request.args.get('country')
    status = request.args.get('status')
    type = request.args.get('type')

    if country is None:
        return "Provide a country"

    power_plants = json.dumps(specific_power_plant_data(country, status, type), default=str)

    return power_plants


if __name__ == '__main__':
    app.run(debug=True, port=5000)
