from flask import Blueprint, request, current_app
from functools import wraps
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if token was included in request
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 403
        try:
            # Verify web token
            data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        except:
            return {
                "message": "Invalid web token"
            }, 403

        return f(data, *args, **kwargs)
    return decorated