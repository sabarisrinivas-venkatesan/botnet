from flask import Flask
import sys

app = Flask(__name__)

@app.route('/c2/url')


def parseurl():
    f = open("url.txt","r")
    return (f.readline())

if __name__ == '__main__':
    app.run()