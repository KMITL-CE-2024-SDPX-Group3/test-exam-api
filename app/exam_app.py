from flask import Flask, jsonify, abort

api_app = Flask(__name__)


@api_app.route('/')
def index():
    return "SDPX Exam"


@api_app.route("/is2honor/<x>", methods=['GET'])
def is_prime(x: str):
    try:
        x: float = float(x)
        if x <= 3.5 and x >= 3.25:
            return jsonify({
                "result": True
            })
        return jsonify({
            "result": False
        })
    except ValueError:
        # If the conversion fails, return a 400 Bad Request
        abort(400, description="Invalid input: parameter must be a number")
        return None


@api_app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400


if __name__ == '__main__':
    api_app.run()
