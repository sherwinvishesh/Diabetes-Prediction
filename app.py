from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Assuming your model expects features in this order:
# ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Define a route for the homepage to render the index.html template
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load the model and scaler from disk
    with open('knn_model.pkl', 'rb') as model_file:
        knn = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    
    # Use request.form.get() to avoid KeyErrors and ensure order
    input_features = [
        float(request.form.get('pregnancies')),
        float(request.form.get('glucose')),
        float(request.form.get('bloodpressure')),
        float(request.form.get('skinthickness')),
        float(request.form.get('insulin')),
        float(request.form.get('bmi')),
        float(request.form.get('diabetespedigreefunction')),
        float(request.form.get('age')),
    ]
    final_features = np.array(input_features).reshape(1, -1)
    final_features_scaled = scaler.transform(final_features)
    
    prediction = knn.predict(final_features_scaled)
    output = prediction[0]

    return render_template('index.html', prediction_text='Diabetes Prediction: {}'.format("Yes" if output == 1 else "No"))

if __name__ == "__main__":
    app.run(debug=True)
