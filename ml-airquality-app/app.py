from flask import Flask, request, render_template
import joblib

app = Flask(__name__, template_folder='template')

# Load the trained model
model = joblib.load('model/RandomForest.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect and validate inputs
        features = []
        for k in ['PM2.5', 'PM10', 'NO2', 'SO2', 'O3', 'CO', 'City']:  # ✅ Added 'CO'
            val = request.form.get(k)
            if val is None or val == '':
                return f"<h2>Error: Missing input for {k}</h2><br><a href='/'>Back</a>"
            features.append(float(val))
        prediction = model.predict([features])[0]
        return f"<h2 style='text-align:center;'>Predicted Air Quality: <b>{prediction}</b></h2><br><a href='/'>Back</a>"
    except Exception as e:
        return f"<h2>Error: {e}</h2><br><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

