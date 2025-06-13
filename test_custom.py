from pattern_extractor import extract_generalized_patterns

def test_my_data():
    # Put your custom keys here
    custom_keys = [
        "users.0.id",
        "users.1.name",
        "users.2.email",
        "orders.0.items.3.price",
        "orders.0.items.3.quantity",
        "orders.2.total",
        "products.10.name",
        "products.12.price",
        "users.10.id"     
    ]
    
    print(f"Testing {len(custom_keys)} custom keys:")
    for key in custom_keys:
        print(f"  {key}")
    
    patterns = extract_generalized_patterns(custom_keys)
    
    print(f"\nGenerated {len(patterns)} patterns:")
    for pattern in sorted(patterns):
        print(f"  {pattern}")
    
    # Calculate some stats
    total_keys = len(custom_keys)
    print(f"\nAnalysis:")
    print(f"  Total input keys: {total_keys}")
    print(f"  Unique patterns: {len(patterns)}")
    print(f"  Compression ratio: {len(patterns)/total_keys:.2%}")

if __name__ == "__main__":
    test_my_data()