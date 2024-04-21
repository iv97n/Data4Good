from flask import Flask, jsonify
import random

app = Flask(__name__)

# Endpoint to get random weather
@app.route('/weather')
def get_random_weather():
    weather_options = ["sunny", "cloudy", "rainy"]
    random_weather = random.choice(weather_options)
    return jsonify({"weather": random_weather})

if __name__ == '__main__':
    app.run(debug=True)