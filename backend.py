from constants import api_key
import requests


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={api_key}"
    response = requests.get(url)
    print(response)
    data = response.json()
    print(data)
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    print(filtered_data)
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
