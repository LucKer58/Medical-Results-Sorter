import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.specialties import MEDICAL_SPECIALTIES
import json

class Preprocessor:
    def __init__(self, text):
        self.text = text

    
    def split_abstracts(self):
        # Split at the start of each numbered abstract (e.g., '\n1. ', '\n2. ', etc.)
        text = '\n' + self.text.lstrip()
        abstracts = re.split(r'\n(?=\d+\. )', text)
        abstracts = [a.strip() for a in abstracts if a.strip()]
        return abstracts
    
    
    def clean_text(self, text):
        text = text.lower()
        # Keep letters, numbers, spaces, and periods
        text = re.sub(r'[^a-z0-9\.\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def format_all(self):
        # Main method: split abstracts and clean each as a single text block
        abstracts = self.split_abstracts()
        cleaned_abstracts = [self.clean_text(a) for a in abstracts]
        return cleaned_abstracts

if __name__ == "__main__":
    for specialty in MEDICAL_SPECIALTIES:
        raw_path = f'data/raw/{specialty}_abstracts.json'
        processed_path = f'data/processed/{specialty}_abstracts_processed.json'
        with open(raw_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        raw_text = data['abstracts']
        processor = Preprocessor(raw_text)
        cleaned_abstracts = processor.format_all()
        processed_data = {
            "specialty": specialty,
            "abstracts": cleaned_abstracts
        }
        with open(processed_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=2)
