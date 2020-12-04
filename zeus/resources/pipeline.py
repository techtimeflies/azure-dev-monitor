from zeus.resources.base_resource import Resource
from zeus import config, request_builder as rb

class Pipeline(Resource):

    cnf=config.get_instance()

    def __init__(self):
        super().__init__("pipelines", self.cnf.get_setting("API-VERSION", "DEFAULT"))

    def get_list(self):
        return rb.get(f"pipelines?{self.api}")
    
def get_instance():
    return Pipeline()