import csv
import re

def clean_csv_combined(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            cleaned_row = []  # Correct initialization of cleaned_row
            for field in row:
                # 1. Remove leading/trailing spaces
                field = field.strip()

                # 2. Handle commas within fields by enclosing in quotes
                if ',' in field and not (field.startswith('"') and field.endswith('"')):
                    field = '"' + field + '"'

                # 3. Insert comma in skills (generalized)
                field = re.sub(r'([a-zA-Z0-9]) ([A-Za-z0-9])', r'\1, \2', field)

                # 4. Remove non-printable characters
                field = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', field)

                # 5. Handle empty fields
                if not field:
                    field = ''  # or some default value like 'N/A'

                cleaned_row.append(field)
            writer.writerow(cleaned_row)

clean_csv_combined('jobs_data_cleaned2.csv', 'jobs_data_cleaned3.csv')
