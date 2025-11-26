"""
t111 - String manipulation and pattern matching
"""
import re


def sanitize_string(text):
    """Remove special characters from string"""
    # Remove non-alphanumeric except spaces
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return sanitized


def extract_numbers(text):
    """Extract all numbers from text"""
    numbers = re.findall(r'\d+', text)
    return [int(n) for n in numbers]


def extract_emails(text):
    """Extract email addresses from text"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails


def count_words(text):
    """Count words in text"""
    words = text.split()
    word_count = len(words)
    unique_words = len(set(word.lower() for word in words))
    
    return word_count, unique_words


def analyze_text_patterns(text):
    """Analyze various patterns in text"""
    sanitized = sanitize_string(text)
    numbers = extract_numbers(text)
    emails = extract_emails(text)
    word_count, unique_count = count_words(text)
    
    print(f"Text analysis:")
    print(f"  Words: {word_count} (unique: {unique_count})")
    print(f"  Numbers found: {numbers}")
    print(f"  Emails found: {emails}")
    print(f"  Sanitized length: {len(sanitized)}")
    
    return word_count, numbers, emails


def find_patterns(text, pattern):
    """Find all occurrences of a pattern"""
    matches = re.finditer(pattern, text)
    results = [(m.group(), m.start(), m.end()) for m in matches]
    
    return results


def replace_pattern(text, pattern, replacement):
    """Replace pattern in text"""
    replaced = re.sub(pattern, replacement, text)
    count = len(re.findall(pattern, text))
    
    print(f"Replaced {count} occurrences of pattern")
    return replaced, count


def process_text_data(texts):
    """Process multiple text samples"""
    results = []
    
    for idx, text in enumerate(texts):
        print(f"\n--- Text {idx + 1} ---")
        analysis = analyze_text_patterns(text)
        results.append(analysis)
    
    return results


def summarize_text_analysis(results):
    """Summarize text analysis results"""
    total_words = sum(r[0] for r in results)
    total_numbers = sum(len(r[1]) for r in results)
    total_emails = sum(len(r[2]) for r in results)
    
    print(f"\n=== Summary ===")
    print(f"Total words: {total_words}")
    print(f"Total numbers extracted: {total_numbers}")
    print(f"Total emails extracted: {total_emails}")
    
    return total_words, total_numbers, total_emails


def transform_text(text):
    """Apply various transformations to text"""
    upper = text.upper()
    lower = text.lower()
    title = text.title()
    
    # Replace multiple spaces with single space
    normalized = re.sub(r'\s+', ' ', text).strip()
    
    return {
        'upper': upper,
        'lower': lower,
        'title': title,
        'normalized': normalized
    }


def validate_format(text, format_type):
    """Validate text format"""
    patterns = {
        'email': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$',
        'phone': r'^\+?1?\d{9,15}$',
        'url': r'^https?://[^\s]+$',
        'number': r'^\d+$'
    }
    
    pattern = patterns.get(format_type, '.*')
    is_valid = bool(re.match(pattern, text))
    
    return is_valid


def batch_validate(texts, format_type):
    """Validate multiple texts"""
    valid_count = 0
    
    for text in texts:
        if validate_format(text, format_type):
            valid_count += 1
    
    print(f"Validation: {valid_count}/{len(texts)} valid {format_type}s")
    return valid_count


def main():
    """Main function"""
    print("Hello from t111!")
    print("String manipulation and pattern matching\n")
    
    # Sample texts with various content
    texts = [
        "Hello World! Contact us at support@example.com for help. Phone: 1234567890",
        "Python 3.11 is great! Email: admin@test.org or sales@company.com",
        "Order #12345 received. Total: $99.99. Tracking: ABC-123-XYZ",
        "Visit https://www.python.org for more info about Python programming"
    ]
    
    # Process texts
    print("=== Processing Text Data ===")
    results = process_text_data(texts)
    
    # Summarize
    total_w, total_n, total_e = summarize_text_analysis(results)
    
    # Test transformations
    print("\n=== Text Transformations ===")
    sample = texts[0]
    transforms = transform_text(sample)
    print(f"Original: {sample[:50]}...")
    print(f"Title case: {transforms['title'][:50]}...")
    
    # Test pattern replacement
    print("\n=== Pattern Replacement ===")
    replaced, count = replace_pattern(sample, r'\d+', 'XXX')
    print(f"Result: {replaced[:60]}...")
    
    # Batch validation
    print("\n=== Format Validation ===")
    email_samples = ["support@example.com", "invalid.email", "admin@test.org"]
    valid = batch_validate(email_samples, 'email')
    
    print(f"\n✓ Processed {len(texts)} text samples")


if __name__ == "__main__":
    main()
