
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.specialties import MEDICAL_SPECIALTIES
import json

training_data = []

for specialty in MEDICAL_SPECIALTIES:
    processed_path = f'data/processed/{specialty}_abstracts_processed.json'
    with open(processed_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        abstracts = data['abstracts']
        for abstract in abstracts:
            training_data.append({"text": abstract, "label": specialty})

training_path = 'data/training/training_abstracts.json'
with open(training_path, 'w', encoding='utf-8') as l:
    json.dump(training_data, l, indent=2)