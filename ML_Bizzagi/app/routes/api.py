from flask import Blueprint, request, jsonify
import app.models.ml_predict as ml
import pandas as pd

blueprint_ml = Blueprint('ml_api', __name__, url_prefix='/ml')

@blueprint_ml.route('/predict', methods=['POST'])
def ml_predict():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No file selected for uploading'}), 400

    if file and file.filename.endswith('.csv'):
        try:
            # Try Read CSV
            df = pd.read_csv(file)
            print(df.head())
            
            response = {
                'message': 'File received successfully',
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'message': f'Error processing file: {str(e)}'}), 500
    else:
        return jsonify({'message': 'Invalid file format. Please upload a CSV file.'}), 400

@blueprint_ml.route('/status/<task_id>', methods=['GET'])
def get_status(task_id):
    task = process_csv.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result
        }
    else:
        response = {
            'state': task.state,
            'status': str(task.info)
        }
    return jsonify(response)
