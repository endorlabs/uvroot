"""
pkg1 - File system operations and path manipulation
"""
import os
import sys


def get_directory_info(path):
    """Get information about a directory"""
    if not os.path.exists(path):
        return None, None, None
    
    total_files = 0
    total_dirs = 0
    total_size = 0
    
    try:
        for entry in os.scandir(path):
            if entry.is_file():
                total_files += 1
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_dirs += 1
    except PermissionError:
        pass
    
    return total_files, total_dirs, total_size


def format_size(size_bytes):
    """Format bytes to human readable size"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def analyze_directory(path):
    """Analyze directory contents"""
    files, dirs, size = get_directory_info(path)
    
    if files is None:
        print(f"Directory not found: {path}")
        return None
    
    formatted_size = format_size(size)
    print(f"Directory: {path}")
    print(f"  Files: {files}, Directories: {dirs}")
    print(f"  Total size: {formatted_size}")
    
    return files, dirs, size


def get_python_info():
    """Get Python interpreter information"""
    version = sys.version.split()[0]
    executable = sys.executable
    platform = sys.platform
    
    print(f"Python {version} on {platform}")
    print(f"  Executable: {executable}")
    
    return version, platform


def check_environment():
    """Check environment variables"""
    important_vars = ['PATH', 'HOME', 'USER', 'SHELL']
    env_info = {}
    
    for var in important_vars:
        value = os.environ.get(var, 'Not set')
        env_info[var] = value
        # Print only first 50 chars for PATH
        display_value = value[:50] + '...' if len(value) > 50 else value
        print(f"  {var}: {display_value}")
    
    return env_info


def scan_paths(paths):
    """Scan multiple paths"""
    results = []
    
    for path in paths:
        result = analyze_directory(path)
        if result:
            results.append(result)
    
    return results


def summarize_scan(results):
    """Summarize scan results"""
    total_files = sum(r[0] for r in results)
    total_dirs = sum(r[1] for r in results)
    total_size = sum(r[2] for r in results)
    
    print(f"\n=== Scan Summary ===")
    print(f"Total Files: {total_files}")
    print(f"Total Directories: {total_dirs}")
    print(f"Total Size: {format_size(total_size)}")
    
    return total_files, total_dirs, total_size


def main():
    """Main function"""
    print("Hello from pkg1!")
    print("File system analysis tool\n")
    
    # Get Python info
    print("=== Python Environment ===")
    version, platform = get_python_info()
    
    # Check environment
    print("\n=== Environment Variables ===")
    env_info = check_environment()
    
    # Analyze current directory and parent
    print("\n=== Directory Analysis ===")
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    
    paths_to_scan = [current_dir]
    if parent_dir != current_dir:
        paths_to_scan.append(parent_dir)
    
    results = scan_paths(paths_to_scan)
    
    if results:
        summarize_scan(results)
    
    print("\n✓ Analysis complete")


if __name__ == "__main__":
    main()
