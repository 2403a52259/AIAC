import re
def validate_indian_mobile(mobile_number):
    """
    Validate Indian mobile number. 
    Args:
        mobile_number (str): The mobile number to validate   
    Returns:
        bool: True if valid Indian mobile number, False otherwise    
    Rules:
        - Must be 10 digits
        - Must start with 6, 7, 8, or 9
        - May include optional country code (+91 or 91)
        - Strips spaces, dashes, and parentheses before validation
    """
    # Strip spaces, dashes, and parentheses
    cleaned_number = re.sub(r'[\s\-\(\)]', '', str(mobile_number))
    # Pattern for Indian mobile number validation
    # Optional country code (+91 or 91) followed by 10 digits starting with 6-9
    pattern = r'^(\+91|91)?[6-9]\d{9}$'
    # Check if the cleaned number matches the pattern
    if re.match(pattern, cleaned_number):
        return True
    else:
        return False
# Test cases
if __name__ == "__main__":
    # Valid numbers
    test_cases = [
        "9876543210",           # 10 digits starting with 9
        "+919876543210",        # With +91 country code
        "919876543210",         # With 91 country code
        "6789012345",           # Starting with 6    
    ]
    # Invalid numbers
    invalid_cases = [
        "1234567890",           # Doesn't start with 6-9
        "987654321",            # Only 9 digits
        "98765432101",          # 11 digits
        "+91987654321",         # Country code + 9 digits
        "987654321a",           # Contains letter    
    ]
    print("Testing Valid Indian Mobile Numbers:")
    print("=" * 40)
    for number in test_cases:
        result = validate_indian_mobile(number)
        print(f"{number:20} -> {result}")   
    print("\nTesting Invalid Numbers:")
    print("=" * 40)
    for number in invalid_cases:
        result = validate_indian_mobile(number)
        print(f"{number:20} -> {result}")
