import csv

def save_to_csv(table_data, request):
    # Read existing data from CSV file
    existing_data = []
    try:
        with open('data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = list(reader)
    except FileNotFoundError:
        pass

    # Increment article number
    article_number = len(existing_data) + 1

    # Prepare fieldnames including the new 'Tag' column
    fieldnames = ['Article Number', 'Section', 'Subcategory', 'Topic', 'Length', 'Style', 'Generated text', 'Links', 'Visits', 'Click on links']

    # Add article number and tag to each row of table_data
    for row in table_data:
        row['Article Number'] = article_number
        row['Subcategory'] = request.form['subcategory']  # Assuming the subcategory is passed through the form
        article_number += 1

    # Combine existing data with new data
    updated_data = existing_data + table_data

    # Write updated data to CSV file
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write updated data
        for row in updated_data:
            # Filter out keys not present in fieldnames
            filtered_row = {key: row[key] for key in fieldnames if key in row}
            writer.writerow(filtered_row)


if __name__ == '__main__':
    # Sample table_data, you should replace this with your actual data
    table_data = [
        {'Section': 'Value 1', 'Topic': 'Value 2', 'Length': 'Value 3', 'Style': 'Value 4', 'Generated text': 'Value 5', 'Links': 'Link 1', 'Visits': '10', 'Click on links': '5'}
    ]

    save_to_csv(table_data)
