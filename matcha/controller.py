from flask import request


def do_register():
    errors_messages = {"email": "This is not a valid email"}
    errors = errors_messages
    print(request.form)
    return errors