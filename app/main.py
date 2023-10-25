from flask import Flask
from auth_token import token_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ExampleKey'

@app.route('/')
def hello():
    return 'hi! verify your jwt by making a request to /test with this format: Authorization <token>'

@app.route('/test', methods=['POST'])
@token_required
def test_jwt(data):
    return {"message": data}

if __name__ == '__main__':
    app.run(debug=True)