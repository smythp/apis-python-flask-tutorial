# Flask API Prototype

This repository contains instructions for setting up a prototype API in Flask. It's designed to be used in conjunction with the tutorial on creating web APIs with Python and Flask on the Programming Historian. website.

## Creating the Prototype

1\. Install [Python 3](https://www.python.org/downloads/).
2\. Open the command line. In OSX, click the finder on the top left of your desktop (the magnifying glass) and type `terminal`. The terminal should be the first application that appears. On Windows, click the Start menu icon and type `cmd` in the search box, then press `Enter`.
3\. Install Flask using the pip package manager by entering this command in the command line:

	pip install flask
	
You should see some output letting you know that Flask was installed successfully.
4\. Create a new folder in your home directory. On OSX, that's `/Users/$YOUR_NAME`, where `$YOUR_NAME` is your username on the computer. On Windows, that should be `C:\Users\$YOUR_NAME`. Call it `api_prototype`.
5\. In the `api_prototype` folder, create a new file called `run.py` using your text editor of choice. (I recommend TextWrangler on OSX or Notepad++ on Windows.)
6\. In the `run.py` file, type the following:

```python
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "Hello, world!"

app.run()
```
7\. On the command line, move into the `api_prototype` folder with the `run.py` file in it with the command:

	cd api_prototype
	
8\. Run the `run.py` file, which should start the Flask server, file with the command:

	python run.py
	
Your output should look like this:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open your browser and visit the link given above, [http://127.0.0.1:5000](http://127.0.0.1:5000/). You should see

	Hello, world!
	
which is the return value of the `hello()` function in the script.
9\. Now that we have our `Hello, world!` example running, let's add some pretend data to the application.

Add the following before teh `app.run()` portion of your script:

```python

