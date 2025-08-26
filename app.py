from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bank Marketing ML API is working!"

@app.route('/health')
def health():
    return {"status": "healthy"}

@app.route('/predict', methods=['POST'])
def predict():
    # Add your ML model prediction logic here
    data = request.get_json()
    
    # Example prediction logic (replace with your actual ML model)
    # For now, just echo back the received data
    return jsonify({
        'prediction': 'approved', 
        'confidence': 0.85,
        'received_data': data
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)