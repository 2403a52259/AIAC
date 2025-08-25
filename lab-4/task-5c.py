import re
from collections import Counter

def find_most_frequent_word(paragraph):
    """
    Find the most frequently used word in a paragraph.
    
    This function demonstrates few-shot prompting with 3 examples:
    1. Basic text processing
    2. Handling punctuation and special characters
    3. Managing edge cases like empty strings
    
    Args:
        paragraph (str): Input paragraph to analyze
        
    Returns:
        tuple: (most_frequent_word, frequency_count)
    """
    
    # Example 1: Basic text processing
    # Input: "The quick brown fox jumps over the lazy dog"
    # Expected: ("the", 2) - "the" appears twice
    
    # Example 2: Handling punctuation and special characters
    # Input: "Hello, world! How are you today? I'm doing great!"
    # Expected: ("hello", 1) - "hello" appears once after processing
    
    # Example 3: Managing edge cases
    # Input: "   " (empty or whitespace-only)
    # Expected: (None, 0) - no words found
    
    # Step 1: Convert to lowercase
    text_lower = paragraph.lower()
    
    # Step 2: Remove punctuation using regex
    # Remove all characters that are not letters, numbers, or spaces
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    
    # Step 3: Tokenize words (split by whitespace)
    words = text_clean.split()
    
    # Step 4: Handle edge case - empty paragraph
    if not words:
        return None, 0
    
    # Step 5: Count word frequencies
    word_counts = Counter(words)
    
    # Step 6: Find the most frequent word
    most_frequent_word = word_counts.most_common(1)[0]
    
    return most_frequent_word[0], most_frequent_word[1]

# Test the function with the examples from the prompts
def test_examples():
    """Test the function with the examples mentioned in the prompts"""
    
    print("Testing few-shot prompting examples:")
    print("=" * 50)
    
    # Example 1: Basic text processing
    example1 = "The quick brown fox jumps over the lazy dog"
    result1 = find_most_frequent_word(example1)
    print(f"Example 1: '{example1}'")
    print(f"Result: {result1}")
    print()
    
    # Example 2: Handling punctuation and special characters
    example2 = "Hello, world! How are you today? I'm doing great!"
    result2 = find_most_frequent_word(example2)
    print(f"Example 2: '{example2}'")
    print(f"Result: {result2}")
    print()
    
    # Example 3: Managing edge cases
    example3 = "   "
    result3 = find_most_frequent_word(example3)
    print(f"Example 3: '{example3}' (empty/whitespace)")
    print(f"Result: {result3}")
    print()
    
    # Additional test case
    example4 = "Python is amazing! Python programming is fun. I love Python."
    result4 = find_most_frequent_word(example4)
    print(f"Example 4: '{example4}'")
    print(f"Result: {result4}")

if __name__ == "__main__":
    test_examples()