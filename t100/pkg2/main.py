"""
pkg2 - Date/time operations and data formatting
"""
import datetime
import time


def get_current_timestamp():
    """Get current timestamp in various formats"""
    now = datetime.datetime.now()
    iso_format = now.isoformat()
    unix_timestamp = time.time()
    
    return now, iso_format, unix_timestamp


def format_datetime(dt):
    """Format datetime in multiple ways"""
    formats = {
        'date': dt.strftime('%Y-%m-%d'),
        'time': dt.strftime('%H:%M:%S'),
        'datetime': dt.strftime('%Y-%m-%d %H:%M:%S'),
        'weekday': dt.strftime('%A'),
        'month': dt.strftime('%B')
    }
    
    return formats


def calculate_time_delta(start_date, end_date):
    """Calculate difference between two dates"""
    delta = end_date - start_date
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    
    return days, hours, minutes


def process_dates(date_strings):
    """Process multiple date strings"""
    results = []
    
    for date_str in date_strings:
        try:
            dt = datetime.datetime.fromisoformat(date_str)
            formatted = format_datetime(dt)
            results.append({
                'original': date_str,
                'parsed': dt,
                'formatted': formatted
            })
        except ValueError:
            print(f"Invalid date format: {date_str}")
    
    return results


def analyze_timestamps(results):
    """Analyze timestamp data"""
    if not results:
        return None
    
    dates = [r['parsed'] for r in results]
    earliest = min(dates)
    latest = max(dates)
    
    days, hours, minutes = calculate_time_delta(earliest, latest)
    
    print(f"Date range analysis:")
    print(f"  Earliest: {earliest.strftime('%Y-%m-%d')}")
    print(f"  Latest: {latest.strftime('%Y-%m-%d')}")
    print(f"  Span: {days} days, {hours} hours, {minutes} minutes")
    
    return earliest, latest, days


def generate_date_sequence(start_date, num_days):
    """Generate a sequence of dates"""
    dates = []
    current = start_date
    
    for i in range(num_days):
        dates.append(current)
        current = current + datetime.timedelta(days=1)
    
    return dates


def format_date_sequence(dates):
    """Format and display date sequence"""
    print("\nDate sequence:")
    for idx, date in enumerate(dates[:5]):  # Show first 5
        formatted = format_datetime(date)
        print(f"  {idx + 1}. {formatted['date']} ({formatted['weekday']})")
    
    if len(dates) > 5:
        print(f"  ... and {len(dates) - 5} more")
    
    return len(dates)


def calculate_business_days(start_date, end_date):
    """Calculate business days between two dates"""
    current = start_date
    business_days = 0
    
    while current <= end_date:
        if current.weekday() < 5:  # Monday = 0, Sunday = 6
            business_days += 1
        current += datetime.timedelta(days=1)
    
    return business_days


def main():
    """Main function"""
    print("Hello from pkg2!")
    print("Date and time processing tool\n")
    
    # Get current timestamp
    print("=== Current Timestamp ===")
    now, iso, unix = get_current_timestamp()
    print(f"ISO format: {iso}")
    print(f"Unix timestamp: {unix:.0f}")
    
    # Format current datetime
    print("\n=== Datetime Formatting ===")
    formats = format_datetime(now)
    for key, value in formats.items():
        print(f"  {key}: {value}")
    
    # Process sample dates
    print("\n=== Date Processing ===")
    sample_dates = [
        "2025-01-01T00:00:00",
        "2025-06-15T12:30:00",
        "2025-12-31T23:59:59"
    ]
    
    results = process_dates(sample_dates)
    earliest, latest, span = analyze_timestamps(results)
    
    # Generate date sequence
    print("\n=== Date Sequence ===")
    sequence = generate_date_sequence(earliest, 10)
    count = format_date_sequence(sequence)
    
    # Calculate business days
    business_days = calculate_business_days(earliest, latest)
    print(f"\nBusiness days in range: {business_days}")
    
    print("\n✓ Date processing complete")


if __name__ == "__main__":
    main()
