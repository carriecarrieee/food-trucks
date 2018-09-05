# Show Open Food Trucks
Show Open Food Trucks is a simple command-line program that prints out a list of food trucks that are open at the current date, when the program is being run. It will print a list of 10 trucks at a time, prompting for input from the user before displaying the next 10 (or fewer if there are fewer than 10 remaining), and so on until there are no more food trucks to display.

### Data
The San Francisco government’s website has a public data source of [food trucks](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b "Data Schema"). The San Francisco Data API was used to make requests to the data source [here](https://dev.socrata.com/foundry/data.sfgov.org/bbb8-hzi6 "Mobile Food Schedule").

### Technology
This program was created in Python 2.7. It is optional to set up and activate a python virtual environment:
```python
virtualenv env
source env/bin/activate
```
There is only one dependency, listed in `requirements.txt`. You can install this with:
```python
pip install -r requirements.txt
```
Alternatively, you can also directly install the requests package:
```python
pip install requests
```

To run the program, simply run the following command:
```python
python show_open_food_trucks.py
```

### Version 2.0
In a later version, this simple program could be expanded into a full-scale web application, which would have a front-end component to it, complete with HTML/CSS/Javascript files that can contribute to a polished graphical user interface that is more interactive. For example, with a command-line program that must use a command-line interpreter (CLI), the user only interacts with the program by either executing the program or pressing `Enter` to allow a subsequent set of 10 rows to be displayed. With a web application, it would be possible to build in continuous/infinite scrolling or clicking to the next page that shows the next 10 entries. To run the program at another time, the CLI program requires running the program again (`python show_open_food_trucks.py`), whereas a full scale web app can have built-in features that seamlessly allow users to search for open trucks again and again.

A web application would allow for the use of buttons and clicks of the mouse, images, animation, colors, fonts, icons, videos--through HTML/CSS/Javascript code that is linked up with the python code--while the CLI program is text/keyboard only.
