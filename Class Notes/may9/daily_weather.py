#
# Simple historical weather tool
#
import urllib.request
import json
import datetime


def get_daily_weather_data(city: str, state: str, country: str,
                           datestart: str, dateend: str, api_key) -> dict:
    # Create the URL following the web API documentation
    url_name = "https://api.weatherbit.io/v2.0/history/daily?city=" + city + \
               "," + state + "&country=" + country + "&start_date=" + \
               datestart + "&end_date=" + dateend + "&key=" + api_key
    # Perform the request
    request = urllib.request.Request(url_name)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response.close()
    api_data_obj = json.loads(response_data)
    return api_data_obj


if __name__ == "__main__":
    USER_API_KEY = "9c605351de014c7aab50b15eeaef6e14"
    city = input("Enter city           : ")
    state = input("Enter state          : ")
    country = input("Enter country        : ")
    filename_out = input("Filename to save data: ")
    dateend = datetime.date.today()
    datestart = dateend - datetime.timedelta(days=365)
    weather_data = get_daily_weather_data(city, state, country,
                                          str(datestart), str(dateend),
                                          USER_API_KEY)
    file_out = open(filename_out, "w")
    json.dump(weather_data, file_out)
    file_out.close()
