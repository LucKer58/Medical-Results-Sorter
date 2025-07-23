import json
from src.preprocessor import Preprocessor

# Load your cardiology data
with open('data/raw/cardiology_abstracts.json', 'r') as f:
    data = json.load(f)

# Get the raw text
raw_text = data['abstracts']

# Test the splitting
processor = Preprocessor(raw_text)
abstracts = processor.split_abstracts()

print(f"Number of splits: {len(abstracts)}")
print("\nFirst 200 characters of each split:")
for i, abstract in enumerate(abstracts[:5]):  # Show first 5
    print(f"\n--- Split {i+1} ---")
    print(abstract[:200] + "...")
