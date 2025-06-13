# Dynamic Regex Pattern Generalization

A robust tool for extracting and generalizing regex patterns from structured dot-separated keys commonly found in logs, flattened JSONs, and event payloads.

## Problem Overview

When processing structured data keys like `users.0.id`, `orders.12.items.3.price`, we need to:
- Identify recurring structural patterns
- Replace numeric indices with regex patterns
- Generalize similar patterns when appropriate
- Support downstream use cases like schema inference and alert grouping

## Solution Architecture

### Two-Phase Approach

**Phase 1: Basic Pattern Extraction**
- Parse dot-separated keys into segments  
- Replace numeric segments with `\d+` regex
- Properly escape special regex characters
- Deduplicate identical patterns

**Phase 2: Advanced Generalization**
- Group patterns by structural similarity (same prefix, different final segment)
- Apply frequency-based generalization rules
- Replace final segments with `\w+` when appropriate

### Generalization Rules

- **< 75% frequency**: Keep patterns separate (insufficient similarity)
- **75-95% frequency**: Generalize final segment to `\w+` (optimal generalization)  
- **≥ 95% frequency**: Keep patterns separate (assume intentional specificity)

## Installation & Usage

```bash
git clone https://github.com/vaibhavsharma3070/genlift-take-home-repo.git
cd genlift-take-home-repo
python -m pytest tests/
```

### Basic Usage
```python
from pattern_extractor import extract_generalized_patterns

keys = [
    "users.0.id",
    "users.1.name", 
    "orders.12.items.3.price"
]

patterns = extract_generalized_patterns(keys)
print(patterns)
# {'users\\.\\d+\\.id', 'users\\.\\d+\\.name', 'orders\\.\\d+\\.items\\.\\d+\\.price'}
```

### Testing & Validation

**Run Full Test Suite:**
```bash
python -m pytest test_pattern_extractor.py -v
```

**Run Example Demonstrations:**
```bash
python examples.py
```

**Test with Custom Data:**
```bash
python test_custom.py
```

**Test 75-95% Generalization:**
```bash
python test_75_95_percent.py
```

**Create Your Own Test:**
```python
# Create test_my_data.py
from pattern_extractor import extract_generalized_patterns

def test_my_scenario():
    custom_keys = [
        # Add your keys here
        "api.v1.users.123.profile",
        "api.v1.users.456.settings",
        "database.connections.5.status"
    ]
    
    print(f"Testing {len(custom_keys)} custom keys:")
    for key in custom_keys:
        print(f"  {key}")
    
    patterns = extract_generalized_patterns(custom_keys)
    
    print(f"\nGenerated {len(patterns)} patterns:")
    for pattern in sorted(patterns):
        print(f"  {pattern}")

if __name__ == "__main__":
    test_my_scenario()
```

**Performance Benchmarking:**
```bash
python benchmark.py
```

## Implementation Details

The core algorithm handles several edge cases:
- Special regex characters in static segments (dots, brackets, etc.)
- Nested numeric indices at multiple levels
- Mixed data structures with varying depths
- Performance optimization for large key sets

## Testing Strategy

Comprehensive test suite covering:
- Basic pattern extraction accuracy
- Advanced generalization logic
- Edge cases and malformed inputs
- Performance benchmarks
- Real-world data scenarios

## Performance Characteristics

- **Time Complexity**: O(n * m) where n = number of keys, m = average key length
- **Space Complexity**: O(n) for pattern storage