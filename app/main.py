from flask import Flask
from flask_restplus import Api
from service import api_namespace as api_namespace_jokes


SERVICE_NAME = "Joke service"
app = Flask(SERVICE_NAME)

api = Api(app,
          title=SERVICE_NAME,
          description='A web service to collect jokes',
          doc="/doc")
api.add_namespace(api_namespace_jokes)


if __name__ == "__main__":
    app.logger.info(f"Service {api.title} started.")
    app.run(host='127.0.0.1', debug=True, port=80)