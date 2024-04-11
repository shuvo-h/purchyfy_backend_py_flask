from flask import jsonify

def sendRes(status_code,data=None,meta=None,message="",isSuccess=True,errors=None):
    response = {
        'success': isSuccess,
        'message': message if message else "Done",
        'meta': meta,
        'data': data,
        "errors":errors
    }
    return jsonify(response), status_code

