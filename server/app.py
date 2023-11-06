#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# Add your views here



if __name__ == '__main__':
    app.run(port=5555, debug=True)