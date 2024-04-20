import requests


def fetch_and_display_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.text:
            try:
                data = response.json()

                print("Data retrieved successfully:")
                print(data)
            except ValueError:
                print("Error: Response is not in JSON format.")
        else:
            print("Error: Empty response received.")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)


api_url = "https://restcountries.com/v3.1/all"
fetch_and_display_data(api_url)
