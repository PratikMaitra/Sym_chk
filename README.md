# Symptom Checker Tool (`Sym_Chk`)

## Description

Sym_Chk ( Symptom Checker Tool ) is a healthcare application that allows users to extract a list of positively identified signs and symptoms from clinical text. It was built using the Flask and spacy python packages. The tool uses a custom fine-tuned BioBERT model( en_ner_biobert_symptom - https://huggingface.co/pmaitra/en_biobert_ner_symptom ) which is available on Hugging Face. It also makes use of the Stanza library`s negation detection feature and the simcin mapping of the Nimble Miner app. The application was built as part of a research study on symptom identification of clinical notes of patients suffering from AML.


## Prerequisites
Before you begin, ensure you have either of the following :

- A working python installation with pip or conda (preferably a conda installation)
- Docker installed on your machine.

## Using the Model without the tool

If you only want to use the underlying fine-tuned BioBERT NER model you can find the model link,parameters and description on Hugging Face.
```bash
!pip install https://huggingface.co/pmaitra/en_biobert_ner_symptom/resolve/main/en_biobert_ner_symptom-any-py3-none-any.whl
```
The model requires the installation of the open-source spacy package along with the above model.

A sample use case is presented below.
```python

import spacy
nlp = spacy.load("en_biobert_ner_symptom")

doc = nlp("He complained of dizziness and nausea during the Iowa trip.")

for ent in doc.ents:
  print(ent)
```

## Installation & Usage

### Using conda or pip

1. Open up a terminal and **Clone the Repository:**
   ```bash
   git clone https://github.com/PratikMaitra/Sym_Chk.git
   ```
2. Install the required python packages from the requirements.txt using pip or conda.
3. Run the app.py file.

### Using Docker (recommended)

1. **Build the Docker Image:**
 ```bash
 docker build -t sym_chk_app .
```
2. **Run the container:**
```bash
docker run -d -p 5000:5000 sym_chk_app
```
3. Open up your browser and go to "http://localhost:5000" to use the tool.



### License & Citation

This tool is licensed under the MIT open-source license. If you use this tool, please cite our paper **"Developing a BioBERT-based Natural Language Processing Algorithm for Acute Myeloid Leukemia Symptom Identification from Clinical Notes- Sena Chae, Pratik Maitra, Padmini Srinivasan "**. A complete list of citations and acknowledgements can be found in the aforementioned paper.

