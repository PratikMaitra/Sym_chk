# Symptom Checker Tool (`Sym_Chk`)

## About
The Symptom Checker Tool allows users to input clinical notes and extract a list of signs and symptoms detected from the entered text. It was built using Flask,spacy and is based on a custom fine-tuned BioBERT model. It also makes use of the Stanza library`s negation detection and the simclin set of Nimble Miner. The tool was built as part of a research study on symptom identification of patient notes.

## Features
- Limit of 1000 characters for the input clinical note. 
- Extraction of signs and symptoms alogn with their categories from the entered text.
- Can discard negated signs and symptoms
- Licensed under MIT License..
- Citations and acknowledgment section provided below.

## Prerequisites
Before you begin, ensure you meet either of the following requirements:

- Working python installation(preferably a conda installation)
- Docker installed on your machine.


## Installation & Usage

### Using conda or pip

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PratikMaitra/Sym_Chk.git
   ```
2. Install the required python packages from the requirements.txt using pip or conda.

### Using Docker

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

This tool is licensed under the MIT open-source license. If you use this tool, please cite our paper **"Developing a BioBERT-based Natural Language Processing Algorithm for Acute Myeloid Leukemia Symptom Identification from Clinical Notes-Sena Chae, Pratik Maitra, Padmini Srinivasan"**. Full citations and acknowledgements can be found in the paper.

