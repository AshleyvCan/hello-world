

from flask import Flask, request
from resources.train_classifier import train
app = Flask(__name__)

@app.route('/train/<clf>', methods = ['POST'])
def train_classifier(clf):
    #data_api = os.environ['DATA_API']
    #data_json = request.get(data_api).json
    #data_json = request.get_json() # !! This can be replaced by comments above if prefered

    message = train(clf)
    return message

app.run(debug=True)
app.run(host='0.0.0.0', port=5000)