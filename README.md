# pysherlock

pysherlock is a Python library for dealing with web scraping using images, it's a Python application of the rendertron headless browser API originally written in JavaScript, it also has a lot of other features.

[GitHub repo link to RenderTron](https://github.com/GoogleChrome/rendertron)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pysherlock.

```bash
pip install pysherlock
```

## Usage

```python
#Example 1
from pysherlock import web_ss
web_ss("https://makeareadme.com") #Website passed as argument

#Example 2
from pysherlock import weather
weather("Bangalore")

#Example 3
from pysherlock import wiki
wiki("Barack Obama")

#Example 4
from pysherlock import qrgen
qrgen("https://www.google.com")
```
## Output

1.)Image saved in the directory.
![Image](https://www.online-convert.com/downloadfile/774e33dc-f681-4be7-be1d-75e000988b6e/a200f859-e1ac-4915-89a8-33d64ef7cc78)

2.) {'Temp': '24°C', 'Time': 'Saturday 10:40 am', 'Sky': 'Mostly cloudy', 'Other': '.'} #To get specific data use weather.get method as it is a dictionary.

3.) Gives output from the Barack Obama Page wikipedia.

4.) A QR code, when scanned leads to google, is saved in the current directory.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Roadmap

1. Translator feature

### Issues and Suggestions
Open an issue or email me at quantechlxxi.corp@gmail.com


