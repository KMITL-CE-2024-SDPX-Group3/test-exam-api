from flask import Flask, jsonify, abort

api_app = Flask(__name__)


@api_app.route('/')
def index():
    return "SDPX Exam"


@api_app.route("/is_prime/<number>", methods=['GET'])
def is_prime(number: str):
    try:
        number: int = int(number)
        if number < 2:
            return jsonify({
                "result": False
            })

        for i in range(2, number):
            if number % i == 0:
                return jsonify({
                    "result": False
                })

        return jsonify({
            "result": True
        })
    except ValueError:
        # If the conversion fails, return a 400 Bad Request
        abort(400, description="Invalid input: parameter must be a number")
        return None


if __name__ == '__main__':
    api_app.run()
