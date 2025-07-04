from flask import Flask, request, redirect, url_for
from models import db, test, test1
from config import devConfig

app = Flask(__name__)
app.config.from_object(devConfig)

db.init_app(app)

@app.route('/')
def home():
    return "hello world"

@app.route('/about/<name>')
def about1(name):
    return {"name": name}

@app.route('/querydata')
def querydata():
    data = test.query.all()
    if not data:
        return {'message': 'No data found'}, 404
    dbData = []
    for item in data:
        dbData.append({
            'id': item.id,
            'name': item.name,
            'number': item.number
        })
    print(dbData)
    return {'message': 'Data fetched successfully', 'data': dbData}

@app.route('/savedata', methods=['POST'])
def savedata():
    data = request.json
    name = data.get('name')
    number = data.get('number')
    try:
        new_data = test(name=name, number=number)
        db.session.add(new_data)
        db.session.commit()
        return {'message': 'Data saved successfully', 'data': {'id': new_data.id, 'name': name, 'number': number}}, 201
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {e}", 500

    
@app.route('/updatedata/<int:id>', methods=['POST'])
def updatedata(id):
    data = test.query.filter_by(id=id).first()
    form_data = request.json
    data.name = form_data.get('name', data.name)
    data.number = form_data.get('number', data.number)
    try:
        db.session.commit()
        return {'message': 'Data updated successfully', 'data': {'id': data.id, 'name': data.name, 'number': data.number}}, 200
    except Exception as e:
        db.session.rollback()
        return f"An error occurred: {e}", 500
    

@app.route('/deletedata/<int:id>', methods=['GET'])
def deletedata(id):
    data = test.query.filter_by(id=id).first()
    if request.method == 'GET':
        try:
            db.session.delete(data)
            db.session.commit()
            return {'message': 'Data deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500
        
@app.route('/test1', methods=['POST', 'GET'])
def test1_route():
    if request.method == 'POST':
        data = request.json
        clname = data.get('clname')
        if not clname:
            return {'message': 'clname is required'}, 400
        try:
            new_data = test1(clname=clname)
            db.session.add(new_data)
            db.session.commit()
            return {'message': 'Data saved successfully', 'data': {'clid': new_data.clid, 'clname': clname}}, 201
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500
    if request.method == 'GET':
        data = test1.query.all()
        if not data:
            return {'message': 'No data found'}, 404
        dbData = [{'clid': item.clid, 'clname': item.clname} for item in data]
        return {'message': 'Data fetched successfully', 'data': dbData}

@app.route('/test1/<int:clid>', methods=['PUT', 'GET', 'DELETE'])
def test1_detail(clid):
    data = test1.query.filter_by(clid=clid).first()
    if not data:
        return {'message': 'Data not found'}, 404

    if request.method == 'GET':
        return {'message': 'Data fetched successfully', 'data': {'clid': data.clid, 'clname': data.clname}}

    if request.method == 'PUT':
        form_data = request.json
        data.clname = form_data.get('clname', data.clname)
        try:
            db.session.commit()
            return {'message': 'Data updated successfully', 'data': {'clid': data.clid, 'clname': data.clname}}, 200
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500

    if request.method == 'DELETE':
        try:
            db.session.delete(data)
            db.session.commit()
            return {'message': 'Data deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run()