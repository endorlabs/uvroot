"""
t1 - Array operations and matrix computations using numpy
"""
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("Warning: numpy not available")


def create_matrix(rows, cols):
    """Create a random matrix"""
    if HAS_NUMPY:
        return np.random.rand(rows, cols)
    else:
        return [[0] * cols for _ in range(rows)]


def matrix_multiply(a, b):
    """Multiply two matrices"""
    if HAS_NUMPY:
        return np.dot(a, b)
    else:
        return a  # Fallback


def compute_statistics(matrix):
    """Compute matrix statistics"""
    if HAS_NUMPY:
        mean = np.mean(matrix)
        std = np.std(matrix)
        sum_val = np.sum(matrix)
        return mean, std, sum_val
    else:
        return 0, 0, 0


def process_matrix(matrix):
    """Process matrix with various operations"""
    mean, std, sum_val = compute_statistics(matrix)
    print(f"Matrix stats: mean={mean:.3f}, std={std:.3f}, sum={sum_val:.3f}")
    
    if HAS_NUMPY:
        transposed = np.transpose(matrix)
        return transposed, mean, std
    else:
        return matrix, mean, std


def linear_algebra_ops(matrix1, matrix2):
    """Perform linear algebra operations"""
    if HAS_NUMPY:
        product = matrix_multiply(matrix1, matrix2)
        trans1, mean1, std1 = process_matrix(matrix1)
        trans2, mean2, std2 = process_matrix(matrix2)
        
        print(f"Product shape: {product.shape}")
        return product, mean1, mean2
    else:
        return matrix1, 0, 0


def validate_matrices(matrices):
    """Validate matrix dimensions"""
    if not HAS_NUMPY:
        return True
    
    valid = all(isinstance(m, np.ndarray) for m in matrices)
    print(f"Validation: {len(matrices)} matrices, all valid: {valid}")
    return valid


def run_analysis(size):
    """Run complete matrix analysis"""
    print(f"\n--- Analysis with {size}x{size} matrices ---")
    
    m1 = create_matrix(size, size)
    m2 = create_matrix(size, size)
    
    if validate_matrices([m1, m2]):
        product, mean1, mean2 = linear_algebra_ops(m1, m2)
        print(f"Means: matrix1={mean1:.3f}, matrix2={mean2:.3f}")
        return product
    return None


def main():
    """Main function"""
    print("Hello from t1!")
    
    if not HAS_NUMPY:
        print("Numpy not available - limited functionality")
        return
    
    print("Running matrix operations...\n")
    
    # Run analyses with different sizes
    sizes = [3, 5, 10]
    results = []
    
    for size in sizes:
        result = run_analysis(size)
        if result is not None:
            results.append(result)
    
    print(f"\n✓ Completed {len(results)} analyses")


if __name__ == "__main__":
    main()
