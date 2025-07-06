from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your pre-trained model (replace 'spam_model.joblib' with your actual model file)
model = joblib.load('spam_model.joblib')

@app.route('/')
def home():
    return "Email Spam Detection API is running."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        email_text = data.get('email')

        if not email_text:
            return jsonify({'error': 'No email text provided'}), 400

        # Prepare input for your model (adjust if your model needs vectorization or preprocessing)
        # Example: if your model expects a list of texts
        prediction = model.predict([email_text])

        # Assuming binary classification: 1=spam, 0=not spam
        result = 'spam' if prediction[0] == 1 else 'not spam'

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
