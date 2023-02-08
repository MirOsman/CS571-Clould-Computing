from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/zipcode", methods=["GET"])
def get_zipcode():
    city = request.args.get("city")
    print("city",city)
    # You can use any API or database to get the zip code based on the city name.
    # For demonstration purposes, we'll use a fake API endpoint that returns the city name as its zip code.
    city_zip_code_dict = {
        "fremont": 94538,
        "dublin": 94532
    }
    zip_code = city_zip_code_dict[city]
    res = requests.get("http://localhost:9000/weather?zip_code=94538")
    data = res.json()
    print("res", res.json())
    
    return {"weather_stats": data["weather_stats"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
