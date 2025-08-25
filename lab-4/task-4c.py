import csv

def analyze_csv(csv_file):
    """
    Read a CSV file and return statistics about rows and words.
    
    Args:
        csv_file (str): Path to the CSV file
        
    Returns:
        dict: Dictionary containing total rows, empty rows, and total words
    """
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    total_rows = len(rows)
    empty_rows = sum(1 for row in rows if not any(cell.strip() for cell in row))
    total_words = sum(len(cell.split()) for row in rows for cell in row if cell.strip())
    
    return {
        'total_rows': total_rows,
        'empty_rows': empty_rows,
        'total_words': total_words
    }

# Example usage
if __name__ == "__main__":
    # Test with a sample CSV file
    result = analyze_csv('sample.csv')
    print(f"Total rows: {result['total_rows']}")
    print(f"Empty rows: {result['empty_rows']}")
    print(f"Total words: {result['total_words']}")