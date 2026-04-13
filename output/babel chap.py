# Babel Chap Script

import sys
from babel.numbers import format_decimal, format_currency
from babel.dates import format_date, format_doi

def main():
    # Check if arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python chap.py <bibliography_file>")
        sys.exit(1)

    bib_file = sys.argv[1]

    # Initialize output filename
    out_filename = f"{bib_file.split('.')[0]}.md"

    # Read bibliography file
    with open(bib_file, 'r') as f:
        bib_text = f.read()

    # Format citations
    citations = []
    for line in bib_text.split('\n'):
        if '@bibliography' not in line and '@cite' not in line:
            continue
        # Assuming citation format is @cite{<citation>}
        citation = line.strip().split('{')[1].strip('}')
        citations.append(citation)

    # Format bibliography entries
    formatted_bibs = []
    for bib in citations:
        if 'doi' in bib:
            formatted_bibs.append(format_doi(bib))
        elif 'date' in bib:
            formatted_bibs.append(f"Published on {format_date(bib['date'])}")
        else:
            formatted_bibs.append(f"{bib['title']}: {format_currency(bib.get('price', ''), 'USD')}")
    # Join formatted bibliography entries
    formatted_bib_text = '\n'.join(formatted_bibs)

    # Write output file
    with open(out_filename, 'w') as f:
        f.write(formatted_bib_text)

if __name__ == '__main__':
    main()