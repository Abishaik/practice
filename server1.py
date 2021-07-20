from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():

    return 'This Is Shown using SERVER 1'

app.run(host='0.0.0.0', port=5000)
