from flask import Flask, request,render_template
from flask_cors import cross_origin
from weather import weath
import dialogflow

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/weather',methods=['POST'])

def webhook():
    req = request.get_json(silent=True)
    intent = req.get('queryResult').get('intent').get('displayName')
    if intent=='Weather':
        x = req.get('queryResult').get('parameters').get('geo-city')

        response = weath(x)
        return response
    else:
        return {'fulfillment':'intent not matched'}

if __name__=='__main__':
    app.run(debug=True)


