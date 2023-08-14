from flask import Flask, render_template, request
from model import apply
from postprocessing import classify_terms

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_entities = []
    entity_categories = {}
    categories_string = ""
    input_text = ""
    
    if request.method == 'POST':
        input_text = request.form.get('input_text', '').strip()
        if "reset" in request.form:
            input_text = ""
        elif "apply" in request.form:
            entities = apply(input_text)
            entity_categories = classify_terms(entities)
            extracted_entities = list(entity_categories.keys())
            categories_string = "\n".join([", ".join(entity_categories[entity]) for entity in extracted_entities])

    return render_template('index.html', extracted_entities=extracted_entities, categories_string=categories_string, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
