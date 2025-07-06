from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Spam Detection API is running!"

if __name__ == '__main__':
    app.run(debug=True)
