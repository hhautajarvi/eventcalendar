from flask import Flask
from os import getenv
import locale

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["TEMPLATES_AUTO_RELOAD"] = True
locale.setlocale(locale.LC_TIME, 'fi_FI.UTF-8')

import routes