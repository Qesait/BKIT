from flask import Flask
from lucky_numbers import lucky_numbers


app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Returning the lucky numbers!</h1><a href="https://oeis.org/A000959">Последовательность на OEIS</a>'


@app.route('/num/<int:cnt>')
def get_fib(cnt):
    numbers = lucky_numbers()
    res = [next(numbers) for _ in range(cnt)]
    return res
