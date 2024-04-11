import jwt  # Import PyJWT library
from time import time

# Generate tokens 
def generate_token(token_payload,token_secret,expiration_time=30*24*60*60):
     # Add expiration time to the payload
    token_payload['exp'] = int(time()) + expiration_time
    token = jwt.encode(token_payload, token_secret, algorithm='HS256')
    return token

# Verify JWT token
def verify_jwt_token(token,token_secret):
    try:
        # Decode the token using the secret key
        payload = jwt.decode(token, token_secret, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None