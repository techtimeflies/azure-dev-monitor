from azuredevmonitor.resources.base_resource import Resource
from azuredevmonitor import config, request_builder as rb
import logging

class Pipeline(Resource):

    cnf = config.get_instance()
    logger = logging.getLogger(__name__)

    def __init__(self):
        super().__init__("pipelines", self.cnf.get_setting("API VERSION", "DEFAULT"))

    def get_list(self):
        self.logger.info("getting pipelines")
        data = rb.get(f"pipelines?{self.api}")

        if data:
            count = data.json()["count"]
            values = data.json()["value"]

            self.logger.info(f"found {count}")

            self.enumerate_pipelines(values)

        return data
        
    def enumerate_pipelines(self, data):
        for x in data:
            self.logger.info(f"id:{x['id']}, name:{x['name']}, url:{x['url']}")

def get_instance():
    return Pipeline()

    