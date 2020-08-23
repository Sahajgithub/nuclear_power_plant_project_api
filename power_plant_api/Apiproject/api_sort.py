from flask import Flask,request
import json


app = Flask(__name__)



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

    skipped=(current_page-1)*page_size

    power_plants = json.dumps(newlist[skipped:skipped+page_size])
    return power_plants

if __name__ == '__main__':
    app.run(debug=True, port=5000)