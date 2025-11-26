# Callgraph Testing - Source Code Summary

This document summarizes the source code added to all packages for callgraph testing.

## Packages Updated

### 1. **uvroot** (Root Package)
- **Location**: `/main.py`
- **Features**: 
  - API data fetching using `requests` library
  - Response processing and validation
  - Metrics calculation (average, total, max, min)
  - Data analysis and report generation
- **Libraries**: `requests`
- **Function Call Depth**: 3-4 levels

### 2. **membery**
- **Location**: `/membery/main.py`
- **Features**:
  - JSON configuration parsing
  - String processing and text analysis
  - Word and character counting
  - Results saving to JSON file
- **Libraries**: `json`, `os`
- **Function Call Depth**: 3 levels

### 3. **memberz**
- **Location**: `/memberz/main.py`
- **Features**:
  - Mathematical statistics (mean, variance, std deviation)
  - Data normalization (0-1 range)
  - Function application (sqrt, log, exp, sin)
  - Dataset aggregation
- **Libraries**: `math`
- **Function Call Depth**: 4 levels

### 4. **t1**
- **Location**: `/t1/main.py`
- **Features**:
  - Matrix operations using numpy
  - Matrix multiplication
  - Statistical computations
  - Linear algebra operations
- **Libraries**: `numpy` (optional fallback)
- **Function Call Depth**: 3-4 levels

### 5. **t2**
- **Location**: `/t2/main.py`
- **Features**:
  - URL parsing and domain extraction
  - International domain name encoding (IDNA)
  - Domain validation
  - URL statistics generation
- **Libraries**: `idna`
- **Function Call Depth**: 3-4 levels

### 6. **t100/pkg1**
- **Location**: `/t100/pkg1/main.py`
- **Features**:
  - File system scanning and analysis
  - Directory information gathering
  - Size formatting (bytes to human-readable)
  - Python environment inspection
- **Libraries**: `os`, `sys`
- **Function Call Depth**: 3 levels

### 7. **t100/pkg2**
- **Location**: `/t100/pkg2/main.py`
- **Features**:
  - Date/time operations
  - Timestamp formatting (multiple formats)
  - Time delta calculations
  - Business days computation
  - Date sequence generation
- **Libraries**: `datetime`, `time`
- **Function Call Depth**: 4 levels

### 8. **t1/t11** (Nested Package)
- **Location**: `/t1/t11/main.py`
- **Features**:
  - Custom data structures (DataProcessor class)
  - Data sorting and filtering
  - Statistical computations
  - Multi-dataset processing pipeline
- **Libraries**: Standard library only
- **Function Call Depth**: 4-5 levels

### 9. **t1/t11/t111** (Deeply Nested Package)
- **Location**: `/t1/t11/t111/main.py`
- **Features**:
  - Regular expression pattern matching
  - Email and number extraction
  - Text sanitization
  - Pattern replacement
  - Format validation (email, phone, URL)
- **Libraries**: `re`
- **Function Call Depth**: 4 levels

### 10. **t100** (Standalone Project)
- **Location**: `/t100/main.py`
- **Features**:
  - Random number generation
  - Data shuffling and sampling
  - Statistical analysis
  - Multi-simulation runner
  - Dataset comparison
- **Libraries**: `random`
- **Function Call Depth**: 3-4 levels

## Running the Code

Each package can be run independently:

```bash
# Root package
python main.py

# Member packages
python membery/main.py
python memberz/main.py

# Workspace members
python t1/main.py
python t2/main.py

# Standalone packages
python t100/main.py
python t100/pkg1/main.py
python t100/pkg2/main.py

# Nested packages
python t1/t11/main.py
python t1/t11/t111/main.py
```

## Testing Callgraphs

All packages now have:
- Multiple function calls with 3-5 levels of call depth
- Various library usage for realistic callgraphs
- Different patterns (procedural, OOP, pipeline)
- Error handling and validation
- Rich function interactions

You can now apply your callgraph tools to analyze these packages!

## Key Features for Callgraph Analysis

1. **Multiple call chains**: Each package has functions that call other functions in a hierarchy
2. **Different patterns**: Mix of procedural, OOP, and pipeline patterns
3. **Library usage**: External libraries (requests, numpy, idna) and standard library
4. **Cross-function dependencies**: Functions depend on results from other functions
5. **Conditional paths**: Some functions have different execution paths
6. **Data flow**: Clear data flow from input → processing → output

## Notes

- All code is functional and can be executed
- Some packages have optional dependencies (numpy, idna) with fallback behavior
- Code includes error handling where appropriate
- Each package demonstrates different programming patterns

