import time
import random
import sys

# Increase recursion limit if needed (good practice for algorithm labs)
sys.setrecursionlimit(20000)

def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm
    Time Complexity: O(log log n) average, O(n) worst case
    Space Complexity: O(1)
    """
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        
        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons
            
        # Interpolation formula to estimate probe position
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1, comparisons

def binary_search(arr, target):
    """Binary Search for comparison"""
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons

def performance_analysis():
    """Generates datasets of various sizes and compares IS and BS performance"""
    sizes = [1000, 5000, 10000, 50000, 100000]
    
    print("-" * 75)
    print(f"{'Size':>10} {'IS Time (ms)':>14} {'BS Time (ms)':>14} {'IS Comparisons':>16} {'BS Comparisons':>16}")
    print("-" * 75)
    
    for size in sizes:
        # Generate a uniformly distributed sorted array
        arr = sorted(random.sample(range(size * 10), size))
        # Pick a random target from the array to guarantee it exists
        target = arr[random.randint(0, size - 1)]
        
        # Interpolation Search timing over 100 iterations for accuracy
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = ((time.perf_counter() - start) / 100) * 1000
        
        # Binary Search timing over 100 iterations for accuracy
        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = ((time.perf_counter() - start) / 100) * 1000
        
        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp_is:>16} {comp_bs:>16}")
    print("-" * 75)

if __name__ == "__main__":
    # --- Demonstration on a small sample array ---
    print("=== Sample Demonstration ===")
    sample_arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    sample_target = 35
    
    print(f"Array: {sample_arr}")
    print(f"Searching for: {sample_target}")
    
    idx, comps = interpolation_search(sample_arr, sample_target)
    print(f"Found at index: {idx}, Comparisons: {comps}\n")
    
    # --- Performance Analysis ---
    print("=== Performance Analysis ===")
    performance_analysis()