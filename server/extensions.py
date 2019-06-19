from flask_jwt_extended import JWTManager
from flask_caching import Cache
from flask_cors import CORS

jwt = JWTManager()
cache = Cache()
cors = CORS()
