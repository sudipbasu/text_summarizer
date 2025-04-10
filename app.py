import nltk
from nltk.tokenize import word_tokenize
from flask import Flask, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
nltk.download('punkt_tab')

app = Flask(__name__)

def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join(str(sentence) for sentence in summary)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        summary = summarize_text(input_text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)
