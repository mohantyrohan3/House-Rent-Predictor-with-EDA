from flask import Flask, request, jsonify , render_template
import util
app = Flask(__name__)
@app.route('/')
def home():
    util.load_saved_artifacts()
    return render_template('index.html')



@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.load_saved_artifacts()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/ahmedabad_model', methods=['POST'])
def predict_home_price_ahmedabad():
    bedroom = int(request.form['bedroom'])
    area = float(request.form['area'])
    bathroom = int(request.form['bathroom'])

    response = jsonify({
        'estimated_price':util.get_estimated_price_ahmedabad(bedroom,area,bathroom)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/Mumbai_model', methods=['POST'])
def predict_home_price_mumbai():
    bedroom = int(request.form['bedroom'])
    area = float(request.form['area'])
    bathroom = int(request.form['bathroom'])

    response = jsonify({
        'estimated_price':util.get_estimated_price_mumbai(bedroom,area,bathroom)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/Delhi_model', methods=['POST'])
def predict_home_price_delhi():
    bedroom = int(request.form['bedroom'])
    area = float(request.form['area'])
    bathroom = int(request.form['bathroom'])

    response = jsonify({
        'estimated_price':util.get_estimated_price_delhi(bedroom,area,bathroom)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/Bangalore_model', methods=['POST'])
def predict_home_price_bangalore():
    bedroom = int(request.form['bedroom'])
    area = float(request.form['area'])
    bathroom = int(request.form['bathroom'])

    response = jsonify({
        'estimated_price':util.get_estimated_price_bangalore(bedroom,area,bathroom)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/Kolkata_model', methods=['POST'])
def predict_home_price_kolkata():
    bedroom = int(request.form['bedroom'])
    area = float(request.form['area'])
    bathroom = int(request.form['bathroom'])

    response = jsonify({
        'estimated_price':util.get_estimated_price_kolkata(bedroom,area,bathroom)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
