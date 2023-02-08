from flask import Flask, request
import requests

def get_weather(zip_code):
    # API endpoint to get the weather information
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?appid=7b0af02a47ef146da5725d73b655fb00&zip={zip_code}"

    # Make a GET request to the endpoint
    response = requests.get(endpoint)
    return response.json()


app = Flask(__name__)

@app.route("/weather", methods=["GET"])
def get_weather_service():
    zip_code = request.args.get("zip_code")
    print("zip_code",zip_code)
    # You can use any API or database to get the zip code based on the city name.
    # For demonstration purposes, we'll use a fake API endpoint that returns the city name as its zip code.
    weather_stats = get_weather(zip_code)
    return {"weather_stats": weather_stats}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
    