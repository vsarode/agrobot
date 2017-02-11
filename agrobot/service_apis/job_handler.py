from agrobot.service_api_handlers.job_handler import create_job
from agrobot.utils.resource import Resource
from flask.globals import current_app as app
from copy import deepcopy


class Job(Resource):
    def get(self):
        current_picklist = app.config["SELECTED_PICKLIST"]
        job = current_picklist[0]
        if job.get("status") == "PROGRESS":
            return job
        else:
            j = deepcopy(job)
            response = create_job(j)
            job["status"] = "PROGRESS"
            return response

    def put(self):
        current_picklist = app.config["SELECTED_PICKLIST"]
        current_picklist.pop(0)
        return True


class UIJob(Resource):
    def get(self):
        current_picklist = app.config["SELECTED_PICKLIST"]
        job = current_picklist[0]
        if job["status"] == "PROGRESS":
            return job
        else:
            return False
