from flask import Flask
from flask_mongoengine import MongoEngine
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'python_flask',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)