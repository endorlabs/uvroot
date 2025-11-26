"""
uvroot - Root package for data processing and API interaction
Uses numpy for data processing and requests for HTTP operations
"""
import requests


def fetch_data_from_api(url):
    """Fetch data from a REST API"""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code, response.headers.get('content-type', 'unknown')
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None


def process_api_response(status_code):
    """Process the API response"""
    if status_code == 200:
        return "Success"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 500:
        return "Server Error"
    else:
        return "Unknown"


def calculate_metrics(a, b, c):
    """Calculate various metrics"""
    average = (a + b + c) / 3
    total = a + b + c
    maximum = max(a, b, c)
    minimum = min(a, b, c)
    return average, total, maximum, minimum


def analyze_data(url, values):
    """Analyze data from multiple sources"""
    status, content_type = fetch_data_from_api(url)
    result = process_api_response(status) if status else "Error"
    avg, total, max_val, min_val = calculate_metrics(*values)
    print(f"API Status: {result}, Content-Type: {content_type}")
    print(f"  Metrics - Avg: {avg:.2f}, Total: {total}, Max: {max_val}, Min: {min_val}")
    return result, avg, total


def validate_data(data_results):
    """Validate the data results"""
    valid_count = sum(1 for r in data_results if r[0] == "Success")
    total_count = len(data_results)
    return valid_count, total_count


def generate_report(data_results):
    """Generate a summary report"""
    print("\n=== Report Summary ===")
    for idx, result in enumerate(data_results):
        print(f"Run {idx + 1}: Status={result[0]}, Avg={result[1]:.2f}, Total={result[2]}")
    
    valid, total = validate_data(data_results)
    print(f"\nValidation: {valid}/{total} successful")
    return total


def main():
    """Main function"""
    print("Hello from uvroot!")
    print("Processing data and generating reports...\n")
    
    # Execute functions
    results = []
    results.append(analyze_data("https://api.github.com", (10, 20, 30)))
    results.append(analyze_data("https://httpbin.org/status/200", (5, 15, 25)))
    results.append(analyze_data("https://www.python.org", (8, 12, 18)))
    
    report_count = generate_report(results)
    print(f"\n✓ Processed {report_count} analyses")


if __name__ == "__main__":
    main()
