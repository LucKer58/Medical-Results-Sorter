import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import models.sklearn_logistic_regression as model
import json

with open('tests/test_abstracts.json', 'r', encoding='utf-8') as f:
    test_data = json.load(f)

class TestSpecialtyClassifier(unittest.TestCase):
    def test_batch_predict(self):
        clf = model.SpecialtyClassifier()
        # Prepare a dict: test_case_name -> text
        test_dict = {f"case_{i}": item["text"] for i, item in enumerate(test_data)}
        results = clf.batch_predict(test_dict)
        errors = []
        for i, item in enumerate(test_data):
            expected = item["label"]
            predicted = results[i]["predicted_specialty"]
            if predicted != expected:
                errors.append(f"case_{i}: expected {expected}, got {predicted}")
        if errors:
            self.fail("Mismatches found:\n" + "\n".join(errors))

if __name__ == '__main__':
    unittest.main()





