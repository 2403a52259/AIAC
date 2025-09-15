import re

def extract_mentions_hashtags(text):
    """
    Extracts mentions (@username) and hashtags (#topic) from the given text.
    
    Rules:
    - Case-insensitive, results returned in lowercase.
    - Punctuation around tags is ignored.
    - Returns two lists: mentions and hashtags.
    
    Args:
        text (str): Input text
    
    Returns:
        tuple: (mentions, hashtags)
    """
    # Regex: word boundary, @ or #, then alphanumeric/underscore chars
    mention_pattern = r'@([a-zA-Z0-9_]+)'
    hashtag_pattern = r'#([a-zA-Z0-9_]+)'

    mentions = re.findall(mention_pattern, text)
    hashtags = re.findall(hashtag_pattern, text)

    # Normalize to lowercase
    mentions = [m.lower() for m in mentions]
    hashtags = [h.lower() for h in hashtags]

    return mentions, hashtags

tests = [
    "Hello @alice check #AI and #Python with @Bob",
    "Wow!! Thanks, @John_Doe!!! Learning #MachineLearning, #AI.",
    "Multiple @ALICE, @alice, and hashtags #Python #PYTHON.",
    "Punctuation test: (#AI), [@User], {#Data}, end@User.",
    "No tags here, just plain text.",
]

for t in tests:
    m, h = extract_mentions_hashtags(t)
    print(f"Input: {t}\n -> mentions={m}, hashtags={h}\n")