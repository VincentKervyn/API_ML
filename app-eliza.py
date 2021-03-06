from flask import Flask, request, jsonify
import pandas as pd
import joblib
import traceback



from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "It's alive, alive !"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        ds = pd.DataFrame(json_)

        query = preprocess(ds)


        pred_price = list(predict(query))
        response = {"Price": list(pred_price)}
        return jsonify(response)
    except:
        return jsonify({"trace": traceback.format_exc()})


@app.route('/predict', methods=['GET'])
def format_data():
    return """<xmp>
                data format for the POST request:
                {
                    "data": {
                            "type": "APARTMENT" | "HOUSE", 
                            "rooms-number": int,
                            "area": int,                                                     
                            "kitchen_equipped": bool 0 | 1,
                            "furnished": bool  0 | 1,
                            "fireplace": bool  0 | 1,
                            "terrace": bool  0 | 1,
                            "terrace-area": int,
                            "garden": bool 0 | 1,
                            "garden-area": int,
                            "land_surface": int,
                            "facade_count": int,                            
                            "swimming_pool": bool 0 | 1,
                            "building_condition": "TO_BE_DONE_UP" | "TO_RENOVATE" | "GOOD" | "JUST_RENOVATED" | "AS_NEW" | "TO_RESTORE"
                            "Province":"LUXEMBOURG" | "HAINAUT" | "FLANDRE-OCCIDENTALE" | "LIEGE" | "FLANDRE-ORIENTALE" | "BRUXELLES" | "BRABANT FLAMAND" | "ANVERS" | "BRABANT WALLON" | "LIMBOURG" | "NAMUR"
                            "Region":"WALLONIE" | "VLAANDEREN" | "BRUXELLES"
                    }
                }
                </xmp>"""


if __name__ == '__main__':
    # You want to put the value of the env variable PORT if it exist (some services only open specifiques ports)
    port = int(os.environ.get('PORT', 5000))
    # Threaded option to enable multiple instances for
    # multiple user access support
    # You will also define the host to "0.0.0.0" because localhost will only be reachable from inside de server.
    app.run(host="0.0.0.0", threaded=True, port=port)