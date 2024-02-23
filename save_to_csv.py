'''
import csv

def save_to_csv(table_data):
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

    # Prepare fieldnames
    fieldnames = ['Article Number', 'Section', 'Topic', 'Length', 'Style', 'Generated text']

    # Add article number to each row of table_data
    for row in table_data:
        row['Article Number'] = article_number
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
        {'Section': 'Value 1', 'Topic': 'Value 2', 'Length': 'Value 3', 'Style': 'Value 4', 'Generated text': 'Value 5'}
    ]

    save_to_csv(table_data)
'''


import csv

def save_to_csv(table_data):
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

    # Prepare fieldnames
    fieldnames = ['Article Number', 'Section', 'Topic', 'Length', 'Style', 'Generated text']

    # Add article number to each row of table_data
    for row in table_data:
        row['Article Number'] = article_number
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
        {'Section': 'Value 1', 'Topic': 'Value 2', 'Length': 'Value 3', 'Style': 'Value 4', 'Generated text': 'Value 5'}
    ]

    save_to_csv(table_data)
