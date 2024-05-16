from flask import app, Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from model_handler import get_predictions
from utils import get_preprocessed_images, images_to_tensors

app = Flask(__name__)
CORS(app)
@app.errorhandler(Exception)
def handle_exception(e):
    code = 500
    message = str(e)
    if isinstance(e, HTTPException):
        message = e.description
        code = e.code
    return jsonify(error=message), code

@app.route('/diagnose', methods=['POST'])
def get_diagnosis():
    try:
        images_binaries = request.files.to_dict(flat = False).values()
        preprocessed_images = get_preprocessed_images(images_binaries)
        tensor = images_to_tensors(preprocessed_images)
        bowel, extravsation, kidney, liver, spleen = get_predictions(tensor)
        return {
            'bowel' : bowel,
            'extravsation': extravsation,
            'kidney': kidney,
            'liver': liver,
            'spleen': spleen
        }
    except Exception as e:
        raise e
