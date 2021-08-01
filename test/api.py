
# create an API hosted as heroku app
#the API accepts 16 key valuer pairs
# "data": {
#     "area": int,
#     "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
#     "rooms-number": int,
#     "zip-code": int,
#     "land-area": Optional[int],
#     "garden": Optional[bool],
#     "garden-area": Optional[int],
#     "equipped-kitchen": Optional[bool],
#     "full-address": Optional[str],
#     "swimming-pool": Optional[bool],
#     "furnished": Optional[bool],
#     "open-fire": Optional[bool],
#     "terrace": Optional[bool],
#     "terrace-area": Optional[int],
#     "facades-number": Optional[int],
#     "building-state": Optional[
#       "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"

from flask import Flask, jsonify, request
import json
import pickle


#return prediction price
app = Flask(__name__)

# a route for the hompepage, to begin work with flask
@app.route("/", methods=["GET", "POST"])
def index():
    #need return content and request code
    return '<h1>Welcome to my app</h1>', 200

#a route for predict
@app.route("/predict", methods=['GET'] )
def predict():

    #goals :
    # parse values
    # use request object to get the current request query args
    request.args.get ("area", '')
    request.args.get("property-type", '')


    #make prediction
    prediction = predict_result([    key       ])#TODO fill
    if prediction is not None:
        #return prediction as a json response
        result = {"prediction": prediction } #TODO: fix the True as correct value
    else:
        return 'Error making prediction ', 400
    #return a dict in json
    return jsonify(result), 200

def predict_result(instance):
    #unpickle
    infile = open('prediction.p', 'rb' )
    key =pickle.load(infile)
    infile.close()

    #traverse predic based on the instance
    try:
        return prediction = sklearn.predict #TODO correct hardcode
    except:
    #soemething goes wrong, return None
        return None
if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)# TODO: set debug = False before deployment





# url= "eliza-app.herokuapp.com/predict?=area=int&lproprety-type="""
#
# response = requests.get(url)
# # check the response's status code
# print ('status code:', response.status_code)
# if response.status_code == 200:
#     #succes
#     json_object = json.loads(response.txt)
#     prediction = json_object["prediction"]


# app = Flask(__name__)
#
# @app.route('/')
# def home():
#    return 'Hello World'
#
# @app.route('/<name>')
# def user(name):
#     return f"Hello {name}!"
#
#
# if __name__ == '__main__':
#    app.run(port=5000)