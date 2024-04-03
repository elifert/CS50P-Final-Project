import requests, tabulate, time
from geopy.geocoders import Nominatim


class InvalidInputError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return super().__str__()


class Crop:
    crops = {
        "wheat": {
            "cultivation time": "october 15th to 30th",
            "harvest time": "july 15th"
        },
        "beet": {
            "cultivation time": "april 15th",
            "harvest time": "october 20th"
        },
        "corn": {
            "cultivation time": "april 20th",
            "harvest time": "september 30th"
        },
        "sunflower": {
            "cultivation time": "may 1st",
            "harvest time": "september 15th"
        },
        "barley": {
            "cultivation time": "october 15th to 30th",
            "harvest time": "july 7th",
        },
    }

    def __init__(self, crop_name: str, cultivation_area: int):
        self.crop_name = crop_name
        self.cultivation_area = cultivation_area

    @property
    def crop_name(self):
        return self._crop_name

    @crop_name.setter
    def crop_name(self, crop_name: str):
        if crop_name in Crop.crops:
            self._crop_name = crop_name
        else:
            raise InvalidInputError("Crop you entered is not available at the moment.")

    def calculate(self):
        if self.crop_name == "wheat":
            return f"for bread wheat {(self.cultivation_area / 1000) * 22}, for durum wheat {(self.cultivation_area / 1000) * 25}"
        elif self.crop_name == "beet":
            return (self.cultivation_area / 1000) * 0.5
        elif self.crop_name == "corn":
            return (self.cultivation_area / 1000) * 2.8
        elif self.crop_name == "sunflower":
            return (self.cultivation_area / 1000) * 5
        elif self.crop_name == "barley":
            return (self.cultivation_area / 1000) * 32
        else:
            return None

    def fertiliser(self):
        return """
        DAP 18-46-0 (Diammonium Phosphate Fertilizer)\n
        Most preferred base fertiliser by farmers as it provides adequate amount of phosphorus nutrition and nitrogen.\n
        It's perfect for any kind of crop.\n
        You must apply approx. 20 kilograms per decare.
        ---------------------------------------
        UREA 46-0-0
        One of the most preferred fertilisers.\n
        Urea is widely used in the agricultural sector both as a fertiliser and animal feed additive.\n
        It's affordable, eco-friendly and has good adaptability.
        ---------------------------------------
        For best results:
        Consult local agricultural resources and specialists for specific
        recommendations on fertiliser varieties and growing practices in your area.
        """

    def cultivation_time(self):
        return Crop.crops[self.crop_name]["cultivation time"]

    def harvest_time(self):
        return Crop.crops[self.crop_name]["harvest time"]


def main():
    menu()
    name = input().title()
    animate_texts(f"{name}, what would you like to do?")
    table()
    while True:
        option = input()
        try:
            match option:
                case "1":
                    while True:
                        try:
                            crop = Crop(input("Enter the crop name: "), int(input("Enter your cultivation area in square meters (m²): ")))
                            print(f"You need to buy {crop.calculate()} kilograms of seed")
                            if ans := quit_or_continue():
                                animate_texts(f"{name}, what would you like to do?")
                                table()
                                break
                            else:
                                animate_texts("Exiting...\nMade by Elif Nazli Ertuğrul.")
                                break
                        except InvalidInputError as msg:
                            print(msg, f"\nAvailable crops are: {list_crops()}", sep="")
                        except ValueError:
                            print("Please enter a valid number.")
                    if ans:
                        continue
                    else:
                        break

                case "2":
                    while True:
                        try:
                            crop = Crop(input("Enter the crop name: "), None)
                            print(crop.fertiliser())
                            if ans := quit_or_continue():
                                animate_texts(f"{name}, what would you like to do?")
                                table()
                                break
                            else:
                                animate_texts("Exiting...\nMade by Elif Nazli Ertuğrul.")
                                break
                        except InvalidInputError as msg:
                            print(msg, f"\nAvailable crops are: {list_crops()}", sep="")
                    if ans:
                        continue
                    else:
                        break

                case "3":
                    while True:
                        try:
                            city_and_country = input("Please enter your city and country, separated by comma: ").title()
                            if climate := get_climate(city_and_country):
                                print("You can cultivate:", ", ".join(key for key in return_crop(climate.lower())))
                            else:
                                raise InvalidInputError("Location you entered does not have a defined Köppen classification.")
                            if ans := quit_or_continue():
                                animate_texts(f"{name}, what would you like to do?")
                                table()
                                break
                            else:
                                animate_texts("Exiting...\nMade by Elif Nazli Ertuğrul.")
                                break
                        except InvalidInputError as msg:
                            print(msg)
                    if ans:
                        continue
                    else:
                        break

                case "4":
                    while True:
                        try:
                            crop = Crop(input("Enter the crop name: "), None)
                            print(f"Best cultivation time for {crop.crop_name} is {crop.cultivation_time().upper()}")
                            print(f"Best harvest time for {crop.crop_name} is {crop.harvest_time().upper()}")
                            if ans := quit_or_continue():
                                animate_texts(f"{name}, what would you like to do?")
                                table()
                                break
                            else:
                                animate_texts("Exiting...\nMade by Elif Nazli Ertuğrul.")
                                break
                        except InvalidInputError as msg:
                            print(msg, f"\nAvailable crops are: {list_crops()}", sep="")
                    if ans:
                        continue
                    else:
                        break

                case "5":
                    while True:
                        try:
                            city, country = input("Please enter your city and country, separated by comma: ").split(",")
                            if forecast(city, country):
                                for keys, values in forecast(city, country).items():
                                    print(f"{keys}: {values}")
                                if ans := quit_or_continue():
                                    animate_texts(f"{name}, what would you like to do?")
                                    table()
                                    break
                                else:
                                    animate_texts("Exiting...\nMade by Elif Nazli Ertuğrul.")
                                    break
                            else:
                                raise InvalidInputError("City and country you entered is not valid.")
                        except ValueError:
                            print("Invalid input format. Please enter city and country separated by comma.")
                        except InvalidInputError as msg:
                            print(msg, "\nPlease enter valid city and country", sep="")
                    if ans:
                        continue
                    else:
                        break

                case "Q":
                    animate_texts("Exiting...\nMade by Elif Nazli Ertuğrul")
                    break

                case _:
                    raise InvalidInputError("Invalid option. Try again.")
        except InvalidInputError as msg:
            print(msg)
            table()
            pass


def get_climate(city_and_country):
    geolocator = Nominatim(user_agent="LonAndLan")
    location = geolocator.geocode(city_and_country)
    url = "https://koppen-climate-classification.p.rapidapi.com/classification"
    headers = {
        "X-RapidAPI-Key": "YOUR_API_KEY", # Insert your RapidAPI Key 
        "X-RapidAPI-Host": "koppen-climate-classification.p.rapidapi.com",
    }
    response_climate = requests.get(
        url,
        headers=headers,
        params={"lat": location.latitude, "lon": location.longitude},
    )
    climate_data = response_climate.json()
    if "error" not in climate_data:
        return climate_data["classification"]
    else:
        return None


def return_crop(climate):
    data = []
    climates = {
        "wheat": ["cfa", "cfb", "csa", "csb", "dfa", "dfb", "dwa"],
        "beet": ["cfa", "csa", "cfb", "csb", "cfc", "dfb"],
        "corn": ["cfa", "cfb", "csa", "csb", "dfb", "dfa"],
        "sunflower": ["cfa", "cfb", "csb", "dfa", "dfb", "bs"],
        "barley": ["cfa", "cfb", "csa", "csb", "dfa", "dfb", "dwa", "bs"],
    }

    for crop in climates:
        for crop_climate in climates[crop]:
            if crop_climate == climate:
                data.append(crop)
    return data if data else None


def forecast(city, country):
    api_key = "YOUR_API_KEY" # Insert your OpenWeather API
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    url = base_url + city + "," + country + "&appid=" + api_key
    response = requests.get(url, params={"units": "metric"})
    data = response.json()
    if response.status_code == 200:
        precipitation_rate = data["rain"]["1h"] if "rain" in data else 0
        data = {
            "Description": data["weather"][0]["description"],
            "Temperature": f"{data['main']['temp']} °C",
            "Humidity": f"{data['main']['humidity']} %",
            "Wind speed": f"{data['wind']['speed']} m/s",
            "Precipitation rate": f"{precipitation_rate * 100} %",
        }
        return data
    else:
        return None


def animate_texts(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


def menu():
    sentences = [
        "Welcome To Agriculture Information System...\n",
        "This system is solely focused on giving basic information about agriculture.\n",
        "Please enter your name: ",
    ]

    for sentence in sentences:
        animate_texts(sentence)


def table():
    options = [
        [1, "Determine seed quantity"],
        [2, "Find suitable fertilizer"],
        [3, "Crop suggestions for your area"],
        [4, "Recommended cultivation and harvest times"],
        [5, "Daily weather forecast"],
        ["Q", "Quit"],
    ]

    print("\n", tabulate.tabulate(options, tablefmt="fancy_grid"), sep="")
    print("Enter: ", end="")


def quit_or_continue():
    while True:
        answer = input("Do you want to continue? (y/n): ").lower()
        try:
            if answer == "y":
                return True
            elif answer == "n":
                return False
            else:
                raise InvalidInputError("Invalid input. Expected 'y' or 'n'.")
        except InvalidInputError as msg:
            print(msg)


def list_crops():
    return ", ".join(key for key in Crop.crops.keys())


if __name__ == "__main__":
    main()
