<p align="center">
<img src="https://i.imgur.com/Jj740Yd.png" alt="logo" height="150"/>
</p>

<h1 align="center">
Harvard CS50’s Introduction to Programming with Python — CS50P Final Project
</h1>

![Language](https://img.shields.io/badge/Language-Python-gold)

<p align="center">
<img src="https://certificates.cs50.io/f744f695-0532-4c77-9e52-ff02f0197bc6.png?size=letter"/>
</p>



# Agriculture Information System
 For video demo click [here!](https://youtu.be/g5Utf0XnGHs)
>[!IMPORTANT]
>The inspiration behind this program stems from my father‘s agricultural expertise and his dedication to his work. The insights and information provided within this project are largely influenced by his knowledge and experience in the field. For the best results, it is **highly** advised to consult with your local agricultural authorities.

## About
This project is developed as final project for [Harvard CS50’s Introduction to Programming with Python](https://www.harvardonline.harvard.edu/course/cs50s-introduction-programming-python).

The Agriculture Information System is designed to provide accessible and convenient access to vital agricultural insights, catering to individuals interested in farming and agriculture.

Key functionalities are:

| Command | Function |
| :---: | --- |
| `1` | Determine seed quantity |
| `2` | Find suitable fertiliser |
| `3` | Crop suggestions for your area |
| `4` | Recommended cultivation and harvest times |
| `5` | Daily weather forecast |
| `Q` | Quit|

- **Determine seed quantity**: Determine the optimal seed quantity required for your agricultural endeavors.

- **Find suitable fertiliser**: Access comprehensive details about widely used fertilizers, including types, usage instructions, and recommendations.

- **Crop suggestions for your area**: Receive personalized crop recommendations based on your geographic location.

- **Recommended cultivation and harvest times**: Gain insights into the ideal timing for planting and harvesting specific crops.

- **Daily weather forecast**: Stay updated with tailored weather forecasts for your region, facilitating informed decision-making in agricultural planning.

This project aims to simplify agricultural decision-making processes and enhance productivity for farmers and agriculture enthusiasts.

## How to use
-  Two functions on this project relies on two distinct APIs: [OpenWeatherMap API](https://openweathermap.org/api) and [RapidAPI](https://rapidapi.com/aptitudeapps/api/koppen-climate-classification/). To use them, you'll need to sign up for both APIs and obtain your own API keys. Then, insert your OpenWeatherMap API key where `"YOUR_API_KEY"` is indicated in the `forecast` function, and do the same for your RapidAPI key within the `get_climate` function.
- Since `match` statements require `Python 3.10` or newer, ensure you have at least `Python 3.10` installed.
- Install the modules listed in `requirements.txt` file by executing `pip install (module name)` in your IDE's terminal or command prompt and make sure you download the right versions.
- You can execute the project either by running `python3 project.py` or by using the _Run Python File_ in [VSCode](https://code.visualstudio.com/docs/python/python-tutorial#:~:text=support%20for%20Linting.-,Run%20Python%20code,right%20side%20of%20the%20editor.&text=Select%20one%20or%20more%20lines,a%20part%20of%20a%20file.).
- After running the file, the following will be displayed:
```
Welcome To Agriculture Information System...
This system is solely focused on giving basic information about agriculture.
Please enter your name: 
```
- Simply enter you name and system will prompt the following:
```
(Name), what would you like to do?
╒═══╤═══════════════════════════════════════════╕
│ 1 │ Determine seed quantity                   │
├───┼───────────────────────────────────────────┤
│ 2 │ Find suitable fertilizer                  │
├───┼───────────────────────────────────────────┤
│ 3 │ Crop suggestions for your area            │
├───┼───────────────────────────────────────────┤
│ 4 │ Recommended cultivation and harvest times │
├───┼───────────────────────────────────────────┤
│ 5 │ Daily weather forecast                    │
├───┼───────────────────────────────────────────┤
│ Q │ Quit                                      │
╘═══╧═══════════════════════════════════════════╛
Enter: 
```
- When you enter `1`, you’ll be prompted to input a crop name and the cultivation area in square meters (m²). Once you’ve provided this information, the system will calculate the amount of kilograms of seed you need to purchase for your specified area.
- When you enter `2`,  you’ll be prompted to input a crop name. Once you’ve provided this information, system will provide you with basic fertiliser information. 
- When you input `3`, you'll be prompted to input your city (or state) and country, separated by only a comma (e.g., Istanbul,Turkey). After providing this information, the system will display crop suggestions tailored to your area.
- When you enter `4`, you’ll be prompted to input a crop name. After providing this information, you will see the recommended cultivation and harvest times.
- When you enter `5`, you’ll be prompted to input your city (or state) and country, separated by only a comma (e.g., Istanbul,Turkey). After providing this information, the system will display daily weather forecast in your area.
- When you enter `Q`, you will just quit the system with the following displaying on the screen:
```
Exiting...
Made by Elif Nazli Ertuğrul.
```


- Also system will prompt you `Do you want to continue? (y/n):` after you’ve successfully gotten what you look for.
  - Enter `y` if you wish to proceed.
  - Enter `n` if you do not wish to proceed.

>[!NOTE]
>This project can provide information only for **wheat, beet, corn, sunflower and barley**.

## License
This project is licensed under the **Apache License** - see the [LICENSE](LICENSE) file for details.

<h1 align=center>This was CS50.
