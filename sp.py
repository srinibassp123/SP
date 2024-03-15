from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
    return '21BCS7837'

if _name_ == '_main_':
    app.run(debug=True)
