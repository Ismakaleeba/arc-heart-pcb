import csv
import os

INPUT_CSV = 'bom_input.csv'      # Replace with your actual input file or KiCad export
OUTPUT_DIR = 'bom_output'
OUTPUT_CSV = os.path.join(OUTPUT_DIR, 'bom_cleaned.csv')

def generate_bom():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    components = {}

    # Read input CSV
    with open(INPUT_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            part = row.get('Part Number', '').strip()
            desc = row.get('Description', '').strip()
            qty = int(row.get('Quantity', '0'))

            if part in components:
                components[part]['Quantity'] += qty
            else:
                components[part] = {
                    'Description': desc,
                    'Quantity': qty
                }

    # Write cleaned BOM
    with open(OUTPUT_CSV, 'w', newline='') as csvfile:
        fieldnames = ['Part Number', 'Description', 'Quantity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for part, data in components.items():
            writer.writerow({
                'Part Number': part,
                'Description': data['Description'],
                'Quantity': data['Quantity']
            })

    print(f"BOM generated at {OUTPUT_CSV}")

if __name__ == '__main__':
    generate_bom()
