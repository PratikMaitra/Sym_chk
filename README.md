# Symptom Checker Tool (`Sym_Chk`)

## Description

Sym_Chk ( Symptom Checker Tool ) is a healthcare application that allows users to extract a list of positively identified signs and symptoms from clinical text. It was built using the Flask and spacy python packages. The tool uses a custom fine-tuned BioBERT model( en_ner_biobert_symptom - https://huggingface.co/pmaitra/en_biobert_ner_symptom ) which is available on Hugging Face. It also makes use of the Stanza library`s negation detection feature and the simcin mapping of the Nimble Miner app. The application was built as part of a research study on symptom identification of clinical notes of patients suffering from AML.

## Features
- Extraction of signs and symptoms along with their categories from the entered text.
- Can discard negated signs and symptoms
- Licensed under the open source MIT License..
- Citations and acknowledgment section provided below.

## Prerequisites
Before you begin, ensure you meet either of the following requirements:

- A working python installation with pip or conda (preferably a conda installation)
- Docker installed on your machine.

## Using the Model without the tool

If you want to only use the underlying fine-tuned BioBERT model you can find it on Hugging Face.
```bash
!pip install https://huggingface.co/pmaitra/en_biobert_ner_symptom/resolve/main/en_biobert_ner_symptom-any-py3-none-any.whl
```
The model requires the installation of the open-source spacy package.

Sample use case of the model using python.
```python

import spacy
nlp = spacy.load("en_biobert_ner_symptom")

doc = nlp("He complained of dizziness and nausea during the Iowa trip.")

for ent in doc.ents:
  print(ent)
```

## Installation & Usage

### Using conda or pip

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PratikMaitra/Sym_Chk.git
   ```
2. Install the required python packages from the requirements.txt using pip or conda.

### Using Docker (recommended)

1. **Build the Docker Image:**
 ```bash
 docker build -t sym_chk_app .
```
2. **Run the container:**
```bash
docker run -d -p 5000:5000 sym_chk_app
```
3. Go to your browser and type in "http://localhost:5000" to use the tool.



### License & Citation

This tool is licensed under the MIT open-source license. If you use this tool, please cite our paper **"Developing a BioBERT-based Natural Language Processing Algorithm for Acute Myeloid Leukemia Symptom Identification from Clinical Notes- Sena Chae, Pratik Maitra, Padmini Srinivasan "**. A complete list of citations and acknowledgements can be found in the aforementioned paper.

