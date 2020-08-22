from flask import Flask,request
import json

app = Flask(__name__)


def data_access(country,status=None,type=None):
    power_list= [{1: country},{2: country}]
    return power_list

@app.route('/power_plant')
def power_plant():
    country = request.args.get('country')
    if(country==None):
        return "provide a country"

    status = request.args.get('status')
    type = request.args.get('type')

    power_plants = json.dumps(data_access(country), indent=10)
    return power_plants

if __name__ == '__main__':
    app.run(debug=True, port=5000)