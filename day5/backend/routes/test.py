from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_security import auth_required, roles_accepted

class homeResource(Resource):
    def get(self):
        from utils.mailer import send_test_email
        send_test_email(to=['anchit@abc.com', 'prokriti@abc.com'], subject='Test Email', body='This is a test email from Flask app.')
        return "hello world"
    
    @auth_required('token')
    @roles_accepted('admin', 'user')
    def post(self, name):
        return make_response(jsonify({'message': f'Hello {name}'}), 200)