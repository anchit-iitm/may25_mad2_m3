from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about1/<name>')
def about1(name):
    return render_template('about.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)