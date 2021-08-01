
# create an API hosted as heroku app
# the API accepts 16 key valuer pairs
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

# return prediction price
app = Flask(__name__)

# a route for the 'hompepage', to begin work with flask and check if is alive
@app.route("/", methods=["GET"])
@api.doc(description='alive!')
class status(Resource):
def home(self):
    result = {
        'status': True,
        'message': 'alive!'
    }
    return jsonify(result), 200
    # need return content and request code



# a route for predict
@app.route("/predict", methods=['POST'] )
def predict(item: Proprety):
    proprety = dict(item)
    return {'price' : predict(preprocess(property))}


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)  # TODO: set debug = False before deployment

