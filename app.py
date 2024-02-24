from flask import Flask, render_template, request
from save_to_csv import save_to_csv  # Import the save_to_csv function

app = Flask(__name__)

# Initial data for the table
table_data = [
    {'Section': 'Value 1', 'Topic': 'Value 2', 'Length': 'Value 3', 'Generated text': 'Value 4'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Update table data with form data including the subcategory
        table_data[0]['Section'] = request.form['section']
        table_data[0]['Topic'] = request.form['topic']
        table_data[0]['Length'] = request.form['length']
        table_data[0]['Generated text'] = request.form['generated_text']
        
        # Save data to CSV file
        save_to_csv(table_data, request)
        
    return render_template('index.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
