import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.specialties import MEDICAL_SPECIALTIES
import json

class PubMedDataCollector:


    def __init__(self):
        self.base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

    
    def search_papers(self, mesh_term, count):

        search_url = f'{self.base_url}?db=pubmed&term={mesh_term}[Mesh]&retmax={count}&retmode=json'
        response = requests.get(search_url)
        data = response.json()

        paper_ids = data['esearchresult']['idlist']
        return paper_ids

    
    def get_abstracts(self, paper_ids):
        if not paper_ids:
            return ""

        fetch_base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
        id_joiner = ','.join(paper_ids)
        fetch_url = f'{fetch_base_url}?db=pubmed&id={id_joiner}&retmode=text&rettype=abstract'

        response = requests.get(fetch_url)
        
        return response.text
    
    def collect_for_specialties(self):

        for specialty_name in MEDICAL_SPECIALTIES.keys():
            mesh_terms = MEDICAL_SPECIALTIES[specialty_name]['mesh_terms']
            abstracts_per_term = 50 // len(mesh_terms)
        
            all_ids = []
            for mesh_term in mesh_terms:
                ids = self.search_papers(mesh_term, abstracts_per_term)
                all_ids.extend(ids)
            
            abstracts = self.get_abstracts(all_ids)
            data = {'speciality': specialty_name, 'abstracts': abstracts}
            with open(f'data/raw/{specialty_name}_abstracts.json', 'w') as f:
 
                json.dump(data, f)

if __name__ == "__main__":
    collector = PubMedDataCollector()
    collector.collect_for_specialties()