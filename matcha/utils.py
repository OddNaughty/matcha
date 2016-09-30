from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # print(g.logged_user)
        if g.get('user', None) is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
#
# def next(f):
#     @wraps(f)
#     def decorate(*args, **kwargs):
#         next_url = request.args.get('next', None)
#         if next_url is not None:
#             k = f(*args, **kwargs)
#             return redirect(next_url)
#     return decorate