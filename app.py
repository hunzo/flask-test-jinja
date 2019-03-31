from flask import Flask,render_template
import json
import requests

URL_APIs = "http://PATH_TO_URL_APIs"

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def TEST():
    return render_template('render_test.html', name = 'TESSSSSSSSSSSSSSSST')

@app.route('/callapi')
def call_api():
    url = URL_APIs
    r = requests.get(url)
    json_obj = json.loads(r.text)
    print(json_obj)
    # print(type(json))
    return render_template('render_palo.html', result = json_obj, name ='Palo Results' )


if __name__ == "__main__":  
    app.run(host='0.0.0.0', debug=True)
