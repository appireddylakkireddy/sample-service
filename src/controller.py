from flask import Flask,request,jsonify
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/v1/api', methods=['POST'])
def postSomeThing():
    content = request.json
    name = content['name']
    logger.info('name: %s',name)
    return "Hello  this service is up and running  %s" %name

@app.route("/")
def hello():
    return "Hi this service is up and running!"
