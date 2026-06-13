from flask import Flask, render_template, request
import pickle
import pandas as pd
import warnings

# Hide sklearn warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Create DataFrame with same column names used during training
        data = pd.DataFrame([{
            'MolLogP': float(request.form['MolLogP']),
            'MolWt': float(request.form['MolWt']),
            'NumRotatableBonds': float(request.form['NumRotatableBonds']),
            'AromaticProportion': float(request.form['AromaticProportion'])
        }])

        # Prediction
        prediction = model.predict(data)[0]

        return render_template(
            "index.html",
            prediction=round(prediction, 4)
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)