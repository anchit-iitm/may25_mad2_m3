from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String())

class test1(db.Model):
    clid = db.Column(db.Integer, primary_key=True)
    clname = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "hello world"

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about1/<name>')
def about1(name):
    return render_template('about.html', name=name)


@app.route('/querydata')
def querydata():
    data = test.query.all()
    return render_template('querydata.html', data=data)

@app.route('/savedata', methods=['GET', 'POST'])
def savedata():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        number = data.get('number')
        try:
            new_data = test(name=name, number=number)
            db.session.add(new_data)
            db.session.commit()
            return redirect(url_for('querydata'))
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500
    
    if request.method == 'GET':
        return render_template('savedata.html')
    
@app.route('/updatedata/<int:id>', methods=['GET', 'POST'])
def updatedata(id):
    data = test.query.filter_by(id=id).first()
    if request.method == 'POST':
        form_data = request.form
        data.name = form_data.get('name', data.name)
        data.number = form_data.get('number', data.number)
        try:
            db.session.commit()
            return redirect(url_for('querydata'))
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500
    if request.method == 'GET':
        return render_template('savedata.html', data=data)
    
@app.route('/deletedata/<int:id>', methods=['GET'])
def deletedata(id):
    data = test.query.filter_by(id=id).first()
    if request.method == 'GET':
        try:
            db.session.delete(data)
            db.session.commit()
            return redirect(url_for('querydata'))
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
    # db.create_all()