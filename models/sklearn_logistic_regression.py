import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

class SpecialtyClassifier:
    def __init__(self, train_path='data/training/training_abstracts.json'):
        with open(train_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.texts = [item['text'] for item in data]
        self.labels = [item['label'] for item in data]
        self.vectorizer = TfidfVectorizer(
            max_features=3000, ngram_range=(1,2), min_df=2, max_df=0.85, stop_words='english'
        )
        self.X = self.vectorizer.fit_transform(self.texts)
        self.y = self.labels
        self._fit_models()

    def _fit_models(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        param_grid = {'C': [0.1, 1, 10], 'max_iter': [1000, 2000]}
        svc = LinearSVC(class_weight='balanced')
        grid = GridSearchCV(svc, param_grid, cv=3, n_jobs=-1)
        grid.fit(X_train, y_train)
        self.best_svc = grid.best_estimator_

        self.rf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
        self.rf.fit(X_train, y_train)

        y_pred_svc = self.best_svc.predict(X_test)
        y_pred_rf = self.rf.predict(X_test)
        svc_report = classification_report(y_test, y_pred_svc, output_dict=True)
        rf_report = classification_report(y_test, y_pred_rf, output_dict=True)

        self.best_model_per_class = {}
        for cls in self.best_svc.classes_:
            svc_f1 = svc_report.get(cls, {}).get('f1-score', 0)
            rf_f1 = rf_report.get(cls, {}).get('f1-score', 0)
            self.best_model_per_class[cls] = 'svc' if svc_f1 >= rf_f1 else 'rf'

    def predict(self, text):
        new_X = self.vectorizer.transform([text])
        svc_decision = self.best_svc.decision_function(new_X)
        svc_idx = svc_decision.argmax()
        svc_pred = self.best_svc.classes_[svc_idx]
        rf_proba_arr = self.rf.predict_proba(new_X)[0]
        rf_idx = rf_proba_arr.argmax()
        rf_pred = self.rf.classes_[rf_idx]
        svc_conf = abs(svc_decision[0][svc_idx]) if svc_decision.ndim == 2 else abs(svc_decision[svc_idx])
        rf_conf = rf_proba_arr[rf_idx]
        if svc_conf >= rf_conf:
            return svc_pred, "LinearSVC"
        else:
            return rf_pred, "RandomForest"

    def batch_predict(self, abstracts_dict):
        results = []
        for test_case, abstract in abstracts_dict.items():
            pred, model = self.predict(abstract)
            results.append({
                "test_case": test_case,
                "abstract": abstract,
                "predicted_specialty": pred,
                "model": model
            })
        return results

    def export_predictions(self, results, filename='test_predictions.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["test_case", "abstract", "predicted_specialty", "model"])
            writer.writeheader()
            for row in results:
                writer.writerow(row)

# Example usage:
if __name__ == "__main__":
    from tests.test_results import test_befunde
    clf = SpecialtyClassifier()
    results = clf.batch_predict(test_befunde)
    clf.export_predictions(results)

