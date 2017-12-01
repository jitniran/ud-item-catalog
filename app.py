from flask import Flask
from views.category import category
app = Flask(__name__)
app.register_blueprint(category)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)