from flask import jsonify

def available(result):
    return jsonify({'available': result})