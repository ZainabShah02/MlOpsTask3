import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model from the pickle file
with open('iris_classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get feature values from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Make a prediction using the loaded model
        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(features)[0]

        # Map the numerical prediction to the flower species
        # species_mapping = {
        #     0: 'Iris-setosa',
        #     1: 'Iris-versicolor',
        #     2: 'Iris-virginica'
        # }
        # predicted_species = species_mapping[prediction]

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', error_message=str(e))

if __name__ == '__main__':
    app.run(debug=True,port=5000)
