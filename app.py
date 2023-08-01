"""
This module contains the functions that operate as the controller
for the flask application. The functions in this module are helper
functions to support the features of the flask application.
"""

from attm.utility_module import traverse_json
from flask import Flask, flash, request, json, render_template, redirect, url_for

# Create the application object
app = Flask(__name__, root_path='attm')
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET'])
def index():
    """
    Render the index page of the flask application.
    """
    return render_template(
        'index.html.jinja',
        page_title='Home',
        dread_score_form_data=[],
        avg_score_list=[])

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calculate the average DREAD score based on the form data received.
    """
    # Load form data from request
    form_data = json.loads(request.form['original_dread_score_form_data'])

    # Initialize total scores for each DREAD category
    total_scores = {field: 0 for field in ['damage_potential', 'affected_users', 'reproducibility', 'exploitability', 'discoverability']}
    
    # Sum scores from form data
    for element in form_data:
        for field in total_scores.keys():
            total_scores[field] += int(request.form[f"{field}_{element['index']}"])
            
    # Calculate average scores
    average_scores = {field: total/len(form_data) for field, total in total_scores.items()}
    
    # Format average scores for display
    avg_score_list = [{'name': name.replace('_', ' ').title(), 'avg_score': score} for name, score in average_scores.items()]

    # Render the page with the calculated scores
    return render_template(
        'index.html.jinja',
        page_title='Home',
        dread_score_form_data=json.loads(request.form['original_dread_score_form_data']),
        avg_score_list=avg_score_list,
        tree_data=json.loads(request.form['original_tree_data']))

@app.route('/upload', methods=['POST'])
def file_upload():
    """
    Handle the uploading of a JSON file, extract attack tree data and DREAD score data from it.
    """
    if request.method == 'POST':
        user_file_upload_data = request.files['user_file_upload_data']
        if user_file_upload_data.filename == '':
            flash('No file selected for uploading')
        elif user_file_upload_data and user_file_upload_data.filename.endswith('.json'):
            data = json.load(user_file_upload_data)
            tree_data = [data]

            # Traverse the JSON to extract DREAD score form data
            dread_score_form_data = []
            traverse_json(data, dread_score_form_data)

            flash('File successfully uploaded')
            return render_template(
                'index.html.jinja',
                page_title='Home',
                tree_data=tree_data,
                dread_score_form_data=dread_score_form_data)
        else:
            flash('Allowed file types are json')

    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=3000, debug=True)
