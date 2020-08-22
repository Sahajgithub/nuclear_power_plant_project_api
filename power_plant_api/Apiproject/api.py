from flask import Flask, request
import json
from power_plant_data_service.plant_data import power_plant_data

app = Flask(__name__)


@app.route('/power_plant')
def power_plant():
    country = request.args.get('country')

    if country is None:
        return "provide a country"

    status = request.args.get('status')
    type = request.args.get('type')

    power_plants = json.dumps(power_plant_data(country, status, type), indent=10)
    return power_plants


if __name__ == '__main__':
    app.run(debug=True, port=5000)