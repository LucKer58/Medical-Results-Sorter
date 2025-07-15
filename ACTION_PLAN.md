# Medical Results Sorter - Action Plan

## Your Step-by-Step Guide

### 🎯 **TODAY - Task 1: Project Structure Setup (30 minutes)**

#### What to do:
1. Create these folders in your project:
   ```
   config/
   src/
   data/
   data/raw/
   data/processed/
   models/
   notebooks/
   tests/
   ```

2. Create these empty files:
   ```
   requirements.txt
   config/specialties.py
   src/__init__.py
   src/data_collector.py
   src/preprocessor.py
   src/classifier.py
   notebooks/exploration.ipynb
   ```

#### ✅ **You'll know you're done when:** 
Your project has the folder structure above.

---

### 🎯 **TODAY - Task 2: Virtual Environment (15 minutes)**

#### What to do:
1. Open terminal in your project folder
2. Run: `python -m venv medical_env`
3. Activate: `medical_env\Scripts\activate` (Windows)
4. Create requirements.txt with basic dependencies

#### Code to write in `requirements.txt`:
```
biopython==1.81
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
requests==2.31.0
matplotlib==3.7.2
jupyter==1.0.0
```

#### ✅ **You'll know you're done when:** 
Virtual environment is active and you can `pip install -r requirements.txt`

---

### 🎯 **TODAY - Task 3: Define Medical Specialties (45 minutes)**

#### What to code in `config/specialties.py`:
```python
MEDICAL_SPECIALTIES = {
    "cardiology": {
        "keywords": ["heart", "cardiac", "cardiovascular", "artery", "blood pressure"],
        "mesh_terms": ["Cardiology", "Heart Diseases", "Cardiovascular System"]
    },
    # Add the other 14 specialties...
}
```

#### Your research task:
- Find 5-10 keywords for each specialty
- Look up MeSH terms for each specialty on PubMed
- Think about medical abbreviations (ECG, MRI, etc.)

#### ✅ **You'll know you're done when:** 
You have all 15 specialties defined with keywords and MeSH terms.

---

### 🎯 **TOMORROW - Task 4: PubMed API Connection (2 hours)**

#### What to code in `src/data_collector.py`:
1. Function to connect to PubMed API
2. Function to search for abstracts by MeSH term
3. Function to download and parse abstracts
4. Function to save abstracts to JSON files

#### Your learning goals:
- Understand how PubMed E-utilities work
- Learn to handle API rate limits
- Practice error handling and retries

#### ✅ **You'll know you're done when:** 
You can download 10 abstracts for one specialty and save them.

---

### 🎯 **Day 3 - Task 5: Data Collection (3 hours)**

#### What to do:
1. Download 50 abstracts per specialty (750 total)
2. Save in organized JSON format
3. Basic data quality checks

#### Expected output:
```
data/raw/
├── cardiology_abstracts.json
├── neurology_abstracts.json
├── ...
```

#### ✅ **You'll know you're done when:** 
You have 750 medical abstracts saved locally.

---

### 🎯 **Day 4 - Task 6: Text Preprocessing (4 hours)**

#### What to code in `src/preprocessor.py`:
1. Text cleaning functions
2. Medical abbreviation handling
3. Feature extraction (TF-IDF)
4. Train/test split creation

#### Your coding challenges:
- How to handle medical abbreviations?
- How to clean noisy text?
- How to balance the dataset?

#### ✅ **You'll know you're done when:** 
You have clean, processed features ready for ML.

---

### 🎯 **Day 5-6 - Task 7: Simple Classifier (6 hours)**

#### What to code in `src/classifier.py`:
1. Keyword-based classifier (baseline)
2. TF-IDF + Logistic Regression
3. Model evaluation functions
4. Cross-validation

#### Your ML learning:
- How does TF-IDF work?
- What's precision vs recall?
- How to interpret confusion matrices?

#### ✅ **You'll know you're done when:** 
You have a working classifier with ~70%+ accuracy.

---

## 📚 **Learning Resources You'll Need:**

### For PubMed API:
- PubMed E-utilities documentation
- Biopython Entrez tutorial

### For Machine Learning:
- Scikit-learn documentation
- "Introduction to Statistical Learning" (free online)

### For Medical Terms:
- MeSH database browser
- Medical abbreviations list

---

## 🚀 **Daily Success Metrics:**

- **Day 1:** Project structure exists, dependencies installed
- **Day 2:** All specialties defined, first API call successful
- **Day 3:** 750 abstracts collected and saved
- **Day 4:** Clean data ready for ML
- **Day 5:** Working baseline classifier
- **Day 6:** Improved classifier with evaluation metrics

---

## 🆘 **When You Get Stuck:**

1. **API Issues:** Check PubMed status, verify your query syntax
2. **Data Problems:** Start with just 2-3 specialties first
3. **ML Confusion:** Begin with the simplest possible model
4. **Code Errors:** Use print statements and small test cases

**Remember:** Each task builds on the previous one. Don't skip ahead!

---

## 🎉 **End Goal:**
By the end of next week, you'll have a working medical text classifier that you coded yourself!
