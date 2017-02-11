from os.path import dirname, abspath

import django;

django.setup()
from django.db import close_old_connections

from flask import Flask
from flask.ext import restful
from agro_db.settings.pool import init_pool

from flask.ext.cors import CORS

close_old_connections()
init_pool()

app = Flask(__name__)
CORS(app)
app.auth_header_name = 'X-Authorization-Token'
app.root_dir = dirname(dirname(abspath(__file__)))

api = restful.Api(app)
app.logger.info("Setting up Resources")

from agrobot.service_apis.ping import Ping
from agrobot.service_apis.job_handler import Job, UIJob
from agrobot.service_apis.picklist import Picklist

api.add_resource(Ping, '/agrobot/ping/')
api.add_resource(Picklist, '/agrobot/picklist/<int:id>')
api.add_resource(Job, '/agrobot/givejob/')
api.add_resource(UIJob, '/agrobot/givejob/ui/')

app.logger.info("Resource setup done")
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=9846)
