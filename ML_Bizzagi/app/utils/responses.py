from flask import jsonify

def success_response(data, message="Success", status_code=200):
    return jsonify({"status": "success", "message": message, "data": data}), status_code

def error_response(message="Error", status_code=500):
    return jsonify({"status": "error", "message": message}), status_code