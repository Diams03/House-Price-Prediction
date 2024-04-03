from flask import jsonify,request,Flask
import util 

app=Flask(__name__)

@app.route('/get_locations_name', methods=['GET'])
def get_locations_name():
    response=jsonify({
        'location':util.get_locations_name()
    })
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=="__main__":
    print("starting flask server for price prediction")
    util.loads_artifacts()
    app.run()