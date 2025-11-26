"""
t100 - Standalone project for testing and utilities
"""
import random


def generate_random_numbers(count, min_val=1, max_val=100):
    """Generate random numbers"""
    numbers = [random.randint(min_val, max_val) for _ in range(count)]
    return numbers


def shuffle_list(items):
    """Shuffle a list randomly"""
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled


def sample_from_list(items, sample_size):
    """Sample random items from list"""
    if sample_size > len(items):
        sample_size = len(items)
    
    sampled = random.sample(items, sample_size)
    return sampled


def calculate_statistics(numbers):
    """Calculate basic statistics"""
    if not numbers:
        return None
    
    total = sum(numbers)
    mean = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'total': total,
        'mean': mean,
        'min': minimum,
        'max': maximum,
        'count': len(numbers)
    }


def analyze_random_data(count):
    """Generate and analyze random data"""
    numbers = generate_random_numbers(count)
    stats = calculate_statistics(numbers)
    
    print(f"Generated {count} random numbers")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Range: [{stats['min']}, {stats['max']}]")
    print(f"  Total: {stats['total']}")
    
    return numbers, stats


def compare_datasets(dataset1, dataset2):
    """Compare two datasets"""
    stats1 = calculate_statistics(dataset1)
    stats2 = calculate_statistics(dataset2)
    
    mean_diff = abs(stats1['mean'] - stats2['mean'])
    range_diff = abs((stats1['max'] - stats1['min']) - (stats2['max'] - stats2['min']))
    
    print(f"\nDataset comparison:")
    print(f"  Mean difference: {mean_diff:.2f}")
    print(f"  Range difference: {range_diff:.2f}")
    
    return mean_diff, range_diff


def run_simulations(num_simulations, data_size):
    """Run multiple random data simulations"""
    results = []
    
    for i in range(num_simulations):
        print(f"\n--- Simulation {i + 1} ---")
        numbers, stats = analyze_random_data(data_size)
        results.append(stats)
    
    return results


def aggregate_simulation_results(results):
    """Aggregate results from simulations"""
    avg_mean = sum(r['mean'] for r in results) / len(results)
    avg_total = sum(r['total'] for r in results) / len(results)
    
    print(f"\n=== Simulation Summary ===")
    print(f"Number of simulations: {len(results)}")
    print(f"Average mean: {avg_mean:.2f}")
    print(f"Average total: {avg_total:.2f}")
    
    return avg_mean, avg_total


def test_sampling():
    """Test various sampling operations"""
    print("\n=== Sampling Tests ===")
    
    items = list(range(1, 51))  # 1 to 50
    print(f"Original list: {items[:10]}... (50 items)")
    
    shuffled = shuffle_list(items)
    print(f"Shuffled: {shuffled[:10]}...")
    
    sample = sample_from_list(items, 10)
    print(f"Sample of 10: {sorted(sample)}")
    
    return shuffled, sample


def main():
    """Main function"""
    print("Hello from t100!")
    print("Random data generation and analysis\n")
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Run simulations
    print("=== Running Simulations ===")
    results = run_simulations(3, 20)
    
    # Aggregate results
    avg_mean, avg_total = aggregate_simulation_results(results)
    
    # Compare first two datasets
    if len(results) >= 2:
        dataset1 = generate_random_numbers(20)
        dataset2 = generate_random_numbers(20)
        compare_datasets(dataset1, dataset2)
    
    # Test sampling
    shuffled, sample = test_sampling()
    
    print(f"\n✓ All tests complete - {len(results)} simulations run")


if __name__ == "__main__":
    main()
