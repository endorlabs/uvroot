"""
t11 - Data structures and algorithm operations
"""


class DataProcessor:
    """Process and manage data structures"""
    
    def __init__(self):
        self.data = []
        self.cache = {}
    
    def add_item(self, item):
        """Add item to data structure"""
        self.data.append(item)
        return len(self.data)
    
    def get_items(self):
        """Get all items"""
        return self.data.copy()
    
    def clear(self):
        """Clear all data"""
        self.data.clear()
        self.cache.clear()


def create_processor():
    """Create and initialize data processor"""
    processor = DataProcessor()
    return processor


def populate_data(processor, items):
    """Populate processor with data"""
    count = 0
    for item in items:
        processor.add_item(item)
        count += 1
    
    print(f"Added {count} items to processor")
    return count


def sort_data(data):
    """Sort data in multiple ways"""
    sorted_asc = sorted(data)
    sorted_desc = sorted(data, reverse=True)
    
    return sorted_asc, sorted_desc


def filter_data(data, threshold):
    """Filter data based on threshold"""
    above = [x for x in data if x > threshold]
    below = [x for x in data if x <= threshold]
    
    return above, below


def analyze_data_structure(processor, threshold):
    """Analyze data structure contents"""
    data = processor.get_items()
    
    if not data:
        print("No data to analyze")
        return None
    
    sorted_asc, sorted_desc = sort_data(data)
    above, below = filter_data(data, threshold)
    
    print(f"Data analysis:")
    print(f"  Total items: {len(data)}")
    print(f"  Min: {min(data)}, Max: {max(data)}")
    print(f"  Above {threshold}: {len(above)}, Below: {len(below)}")
    print(f"  Sorted (asc): {sorted_asc[:5]}...")
    
    return sorted_asc, above, below


def compute_statistics(data):
    """Compute statistical measures"""
    if not data:
        return None, None, None
    
    total = sum(data)
    average = total / len(data)
    median_idx = len(data) // 2
    sorted_data = sorted(data)
    median = sorted_data[median_idx]
    
    return total, average, median


def process_multiple_datasets(datasets):
    """Process multiple datasets"""
    results = []
    
    for idx, dataset in enumerate(datasets):
        print(f"\n--- Dataset {idx + 1} ---")
        processor = create_processor()
        populate_data(processor, dataset)
        
        threshold = sum(dataset) / len(dataset)
        analysis = analyze_data_structure(processor, threshold)
        
        if analysis:
            total, avg, median = compute_statistics(dataset)
            print(f"  Stats: total={total}, avg={avg:.2f}, median={median}")
            results.append((total, avg, median))
    
    return results


def aggregate_results(results):
    """Aggregate results from multiple datasets"""
    if not results:
        return None
    
    total_sum = sum(r[0] for r in results)
    avg_of_avgs = sum(r[1] for r in results) / len(results)
    
    print(f"\n=== Aggregated Results ===")
    print(f"Total sum across all datasets: {total_sum}")
    print(f"Average of averages: {avg_of_avgs:.2f}")
    
    return total_sum, avg_of_avgs


def run_pipeline(datasets):
    """Run complete data processing pipeline"""
    print("Running data processing pipeline...")
    
    results = process_multiple_datasets(datasets)
    aggregated = aggregate_results(results)
    
    return aggregated


def main():
    """Main function"""
    print("Hello from t11!")
    print("Data structure and algorithm operations\n")
    
    # Create sample datasets
    datasets = [
        [10, 25, 30, 15, 40, 35, 20, 45, 50, 28],
        [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
        [100, 200, 150, 175, 225, 250, 300, 275, 325, 350],
        [3, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    ]
    
    # Run pipeline
    result = run_pipeline(datasets)
    
    if result:
        print(f"\n✓ Pipeline complete - processed {len(datasets)} datasets")
    else:
        print("\n✗ Pipeline failed")


if __name__ == "__main__":
    main()
