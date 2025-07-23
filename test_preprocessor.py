import json
import os
from src.preprocessor import Preprocessor

# Create processed directory if it doesn't exist
os.makedirs('data/processed', exist_ok=True)

# Load your cardiology data
with open('data/raw/cardiology_abstracts.json', 'r') as f:
    data = json.load(f)

# Get the raw text
raw_text = data['abstracts']

# Test the full preprocessing pipeline
processor = Preprocessor(raw_text)
processed_abstracts = processor.format_all()

print(f"Processed {len(processed_abstracts)} abstracts")

# Show a few examples in more detail

# Show a few examples in more detail
for i, abstract in enumerate(processed_abstracts[:5]):
    if abstract:
        print(f"\n--- Abstract {i+1} ---")
        print(f"Excerpt (first 300 chars): {abstract[:300]}...")
    else:
        print(f"\n--- Abstract {i+1} [EMPTY] ---")


# Count how many have actual content (non-empty strings)
valid_count = sum(1 for a in processed_abstracts if a.strip())
print(f"\nFound {valid_count} non-empty abstracts out of {len(processed_abstracts)}")

# Save the processed data
processed_data = {
    "specialty": data['speciality'],
    "abstracts": processed_abstracts
}

with open('data/processed/cardiology_abstracts_processed.json', 'w') as f:
    json.dump(processed_data, f, indent=2)
    
print("\nProcessed data saved to data/processed/cardiology_abstracts_processed.json")
