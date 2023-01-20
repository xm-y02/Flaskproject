from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f')
@app.route('/f/<value>')
def f(value=""):
    return f"{value} Celsius is converted to {convert_celsius_to_fahrenheit(float(value))} Fahrenheit"


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
