from flask_restful import Resource
from flask import jsonify, request, make_response


class CeleryResource(Resource):
    def get(self):
        from utils.celery_tasks import printHello
        var1 = printHello.delay()
        while not var1.ready():
            pass
        if var1.failed():
            return make_response(jsonify({"message": "Celery task failed"}), 500)
        
        if var1.successful():
            return make_response(jsonify({"message": "Celery task has been executed", "result": var1.result, "id": var1.id}), 200)
        
class CeleryAddResource(Resource):
    def get(self, x=None, y=None):
        from utils.celery_tasks import add
        if x is None or y is None:
            return make_response(jsonify({"message": "x and y are required"}), 400)
        var1 = add.delay(x, y)
        while not var1.ready():
            pass
        if var1.failed():
            return make_response(jsonify({"message": "Celery task failed"}), 500)

        if var1.successful():
            return make_response(jsonify({"message": "Celery task has been executed", "result": var1.result, "id": var1.id}), 200)
        
class CeleryQueryResource(Resource):
    def get(self, a=None):
        from utils.celery_tasks import query_db
        if a is None:
            return make_response(jsonify({"message": "a is required"}), 400)
        var1 = query_db.delay(a)
        while not var1.ready():
            pass
        if var1.failed():
            return make_response(jsonify({"message": "Celery task failed"}), 500)

        if var1.successful():
            return make_response(jsonify({"message": "Celery task has been executed", "result": var1.result, "id": var1.id}), 200)
        
class CeleryEmailResource(Resource):
    def get(self):
        from utils.celery_tasks import send_email
        var1 = send_email.delay()
        while not var1.ready():
            pass
        if var1.failed():
            return make_response(jsonify({"message": "Celery task failed"}), 500)

        if var1.successful():
            return make_response(jsonify({"message": "Email sent successfully", "id": var1.id, 'result': var1.result}), 200)