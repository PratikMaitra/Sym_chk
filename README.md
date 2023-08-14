Symptom Checker App (Sym_Chk)
Introduction
The Symptom Checker App allows users to input clinical text and get potential symptoms detected from the text. Built using Flask and backed by the BioBERT model, the app offers high accuracy and easy-to-use UI.

Features
User-friendly interface to input clinical text.
Limit of 1000 characters for input to ensure prompt processing.
Extraction of potential symptoms from the input text.
Categorization of detected symptoms.
Licensed under MIT License.
Prerequisites
Before you begin, ensure you have met the following requirements:

Docker installed on your machine.
Basic knowledge of how to run Docker containers.
Installation & Usage
Using Docker
Clone the Repository:

bash
Copy code
git clone https://github.com/PratikMaitra/Sym_Chk.git
Navigate to the Directory:

bash
Copy code
cd Sym_Chk
Build the Docker Image:

Copy code
docker build -t sym_chk_app .
Run the Docker Container:

arduino
Copy code
docker run -d -p 5000:5000 sym_chk_app
Access the App:
Open your browser and go to http://localhost:5000.

License & Citation
This tool is licensed under the MIT open-source license. If you use this tool, please cite the paper "Developing a BioBERT-based Natural Language Processing Algorithm for Acute Myeloid Leukemia Symptom Identification from Clinical Notes". Full citations and acknowledgements can be found in the paper.
