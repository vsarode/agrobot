from agrobot.scripts.pick_list import get_pick_list
from agrobot.utils.resource import Resource
from flask.globals import current_app as app


class Picklist(Resource):
    def post(self, id):
        picklist = get_pick_list()
        app.config["SELECTED_PICKLIST"] = picklist.get(id)
        return True
