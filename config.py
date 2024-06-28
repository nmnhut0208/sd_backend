import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()
SERVICE_NAME = os.getenv('SERVICE_NAME', '/backend')
# TRUEID_URL = os.getenv('TRUEID_URL', 'https://ttxt-api-stag.trueid.vn/face/v1.0/match-sdk')
# TRUEID_TOKEN = os.getenv('TRUEID_TOKEN', 'Bearer abcdefghijklmnopqrstuvwxyz')
# YOLOV8_MODEL_PATH = os.getenv('YOLOV8_MODEL_PATH', 'weights/yolov8n-face.onnx')
# YOLOV8_CONF_THRES = float(os.getenv('YOLOV8_CONF_THRES', 0.45))
# YOLOV8_NMS_THRES = float(os.getenv('YOLOV8_NMS_THRES', 0.5))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_MAX_SIZE_BYTES = int(os.getenv('LOG_MAX_SIZE_BYTES', 20*1024*1024))
LOG_MAX_LENGTH_FIELD = int(os.getenv('LOG_MAX_LENGTH_FIELD', 256))
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'logs/access.log')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'mydatabase')
URL_PREFIX = os.getenv('URL_PREFIX', 'https://aiwrapapi-ixuh.onrender.com/aiwapi/v1')
USERNAME = os.getenv('USERNAME', 'vtdadmin')
PASSWORD = os.getenv('PASSWORD', 'vtd@123!@#')
USERNAME_MONGO = os.getenv('USERNAME_MONGO', 'root')
PASSWORD_MONGO = os.getenv('PASSWORD_MONGO', 'vtd@123!@#')
ADD_MONGO = os.getenv('ADD_MONGO', 'localhost:27017')
DATABASE_URL = "mongodb://%s:%s@%s/?authSource=admin" % (
        quote_plus(USERNAME_MONGO), quote_plus(PASSWORD_MONGO),quote_plus(ADD_MONGO))
MAX_RETRIES = int(os.getenv('MAX_RETRIES', 10))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', 5))

# "mongodb://%s:%s@%s/?authSource=admin" % (
#         quote_plus("root"), quote_plus("vtd@123!@#"),quote_plus("localhost:27017"))