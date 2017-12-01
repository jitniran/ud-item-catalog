from flask import Flask
from views.category import category
from views.item import item

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(category)
app.register_blueprint(item)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)