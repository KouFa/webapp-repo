from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def start():
    return "Hello Wor-kable!"

@app.route('/health')
def healthCheck():
    return jsonify(
                    message="OK",
                    category="success",
                    status=200
                )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)



