# Symptom Checker Tool (`Sym_Chk_Tl`)

## Description

Sym_Chk_Tl ( Symptom Checker Tool ) is a healthcare application that allows users to extract a list of positively identified signs and symptoms from clinical text. It was built using the Flask and spacy python packages. 

The tool uses a custom fine-tuned BioBERT model( en_ner_biobert_symptom).

Hugging Face Link -https://huggingface.co/pmaitra/en_biobert_ner_symptom  

The application was built as part of a research study on symptom identification from clinical notes.


## Prerequisites
Before you begin, ensure you have either of the following :

- A working python installation
- Pip or Conda

## Using the Model without the tool

If you only want to use the underlying fine-tuned BioBERT NER model you can find the model parameters ,description and its sample use-case on Hugging Face.
```bash
!pip install https://huggingface.co/pmaitra/en_biobert_ner_symptom/resolve/main/en_biobert_ner_symptom-any-py3-none-any.whl
```
The model requires the installation of the open-source spacy package along with the above.

A sample use case is presented below.
```python

import spacy
nlp = spacy.load("en_biobert_ner_symptom")

doc = nlp("He complained of dizziness and nausea during the Iowa trip.")

for ent in doc.ents:
  print(ent.text)
```

## Installation & Usage

### Using conda or pip

1. Open up a terminal and clone the repository:
   
   ```bash
   git clone https://github.com/PratikMaitra/Sym_Chk.git
   ```
   
2. Install the required python packages from the requirements.txt using pip or conda.
   
   ```bash
   cd Sym_Chk
   ```
   For pip use,
   ```bash
   pip install -r requirements.txt
   ```
   If you are using conda,
   
   ```bash
   conda create --name sym_chk_env --file requirements.txt
   ```
   
4. Run the app.py file.

   ```bash
   python app.py
   ```
5. Open up your browser and go to "http://localhost:5000" to use the tool.


### Citation

If you use this tool, please cite our paper **"Leveraging Natural Language Processing for Symptom Identification in Acute Myeloid Leukemia using Clinical Notes from Electronic Health Record - Sena Chae, Pratik Maitra et al"**. 

A complete list of citations and acknowledgements can be found in the aforementioned paper.

