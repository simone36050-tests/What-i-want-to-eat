from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/food/<string:what>')
def food(what: str):
    return jsonify({
        'want_to_eat': False
    })

app.run()
