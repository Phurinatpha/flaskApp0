from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '79c39690efaf2fd90101c64261bb95df427e226f6b976d86'
from app import views  # noqa
