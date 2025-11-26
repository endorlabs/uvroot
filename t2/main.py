"""
t2 - URL parsing and text processing operations
"""
try:
    import idna
    HAS_IDNA = True
except ImportError:
    HAS_IDNA = False
    print("Warning: idna not available")


def encode_domain(domain):
    """Encode domain name to ASCII"""
    if HAS_IDNA:
        try:
            encoded = idna.encode(domain)
            return encoded.decode('ascii')
        except Exception as e:
            print(f"Encoding error: {e}")
            return domain
    return domain


def decode_domain(ascii_domain):
    """Decode ASCII domain to Unicode"""
    if HAS_IDNA:
        try:
            return idna.decode(ascii_domain)
        except Exception as e:
            print(f"Decoding error: {e}")
            return ascii_domain
    return ascii_domain


def validate_domain(domain):
    """Validate domain name format"""
    if not domain:
        return False
    
    parts = domain.split('.')
    if len(parts) < 2:
        return False
    
    return all(part and part[0] != '-' and part[-1] != '-' for part in parts)


def process_url(url):
    """Process and parse URL"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Extract domain
    domain = url.split('//')[-1].split('/')[0].split(':')[0]
    
    is_valid = validate_domain(domain)
    encoded = encode_domain(domain) if is_valid else domain
    
    print(f"URL: {url}")
    print(f"  Domain: {domain}, Valid: {is_valid}")
    print(f"  Encoded: {encoded}")
    
    return domain, encoded, is_valid


def analyze_urls(urls):
    """Analyze multiple URLs"""
    results = []
    valid_count = 0
    
    for url in urls:
        domain, encoded, is_valid = process_url(url)
        results.append({
            'url': url,
            'domain': domain,
            'encoded': encoded,
            'valid': is_valid
        })
        if is_valid:
            valid_count += 1
    
    return results, valid_count


def generate_statistics(results):
    """Generate statistics from URL analysis"""
    total = len(results)
    valid = sum(1 for r in results if r['valid'])
    
    print(f"\nStatistics:")
    print(f"  Total URLs: {total}")
    print(f"  Valid: {valid}")
    print(f"  Invalid: {total - valid}")
    
    return total, valid


def save_report(results):
    """Save analysis report"""
    print("\n=== URL Analysis Report ===")
    for idx, result in enumerate(results, 1):
        status = "✓" if result['valid'] else "✗"
        print(f"{idx}. {status} {result['domain']}")
    return len(results)


def main():
    """Main function"""
    print("Hello from t2!")
    print("Processing URLs and domain names...\n")
    
    # Sample URLs including international domains
    urls = [
        "example.com",
        "https://www.python.org",
        "github.com/user/repo",
        "münchen.de",
        "café.fr",
        "invalid",
        "https://sub.domain.example.com:8080/path"
    ]
    
    print("Analyzing URLs...")
    results, valid_count = analyze_urls(urls)
    
    print("\n" + "="*50)
    total, valid = generate_statistics(results)
    
    report_count = save_report(results)
    
    print(f"\n✓ Processed {report_count} URLs ({valid_count} valid)")


if __name__ == "__main__":
    main()
