from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '21BCS7837'

if __name__ == '__main__':
    app.run(debug=True)
