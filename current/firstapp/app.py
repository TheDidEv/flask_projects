from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"Sum: {(num1 + num2)}"    

@app.route('/hadle_url_params')
def hendle_params():
    # return str(request.args)
    # greeting = request.args.get('greeting')
    
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting'] # required field for input
        name = request.args.get('name')
        return f"{name}, {greeting}"
    else:
        return "some parrametrs are missing"
    
    
# POST method
@app.route('/hello', methods=['POST'])
def hello():
    return "Hello world"

# multiple method
@app.route('/mult', methods=['GET', 'POST'])
def mult():
    if request.method == 'GET':
        return "You made a GET request", 200
    elif request.method == 'POST':
        return "You made a POST request", 200
    else:
        return "You make wrong request", 400


# Response example
@app.route('/resp_ex')
def res_ex():
    # response = make_response()
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    # response.body = {"asd": "asd2", "sd": "sa2"}
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)