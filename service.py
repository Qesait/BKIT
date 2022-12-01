from flask import Flask
from lucky_numbers import lucky_numbers


app = Flask(__name__)


@app.route("/")
def hello_world():
    html = """<h1>Returning the lucky numbers!</h1>
              <a href="https://oeis.org/A000959">The sequence in the OEIS<br></a>
              <a href="https://ru.wikipedia.org/wiki/Счастливое_число_(lucky_number)">Wikipedia</a>"""
    return html


@app.route('/num/<int:cnt>')
def get_fib(cnt):
    numbers = lucky_numbers()
    res = [next(numbers) for _ in range(cnt)]
    return res
