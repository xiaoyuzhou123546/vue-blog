from flask import Flask
from flask_cors import *

app = Flask(__name__)

CORS(app,supports_credentials=True)

# r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
# CORS(app, resources=r'/*')


from app import routes