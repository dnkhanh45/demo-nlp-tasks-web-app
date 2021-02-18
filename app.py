import os
from flask import Flask, render_template, request, flash, url_for, send_file
from flaskext.markdown import Markdown
from final.en import gensim_text, gtts_en, nltk_text, pytesseract_en, pyttsx3_en, spacy_text, speech_recognition_en, \
    stanzaen_text, textblob_text # , transformers_text
from final.vi import gtts_vi, pytesseract_vi, pyttsx3_vi, pyvi_text, speech_recognition_vi, stanzavi_text, \
    underthesea_text

app = Flask(__name__)
Markdown(app)
app.secret_key = b'This is my secret key! Its type must be byte'

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/gtts_pyttsx3_vi', methods=["GET", "POST"])
def gtts_pyttsx3_vi_rout():
    if request.method == 'POST':
        text = request.form['text']
        vi_gtts_filename = gtts_vi.gtts_vi_prc(text)
        vi_pyttsx3_filename = pyttsx3_vi.pyttsx3_vi_prc(text)
        return render_template('gtts_pyttsx3_vi_result.html', text=text, vi_gtts_filename=vi_gtts_filename,
                               vi_pyttsx3_filename=vi_pyttsx3_filename)
    return render_template('gtts_pyttsx3_vi.html')


@app.route('/download_gtts_vi/<fn>')
def download_gtts_vi(fn):
    return send_file(fn, as_attachment=True)


@app.route('/download_pyttsx3_vi/<fn>')
def download_pyttsx3_vi(fn):
    return send_file(fn, as_attachment=True)


@app.route('/gtts_pyttsx3_en', methods=["GET", "POST"])
def gtts_pyttsx3_en_rout():
    if request.method == 'POST':
        text = request.form['text']
        en_gtts_filename = gtts_en.gtts_en_prc(text)
        en_pyttsx3_filename = pyttsx3_en.pyttsx3_en_prc(text)
        return render_template('gtts_pyttsx3_en_result.html', text=text, en_gtts_filename=en_gtts_filename,
                               en_pyttsx3_filename=en_pyttsx3_filename)
    return render_template('gtts_pyttsx3_en.html')


@app.route('/download_gtts_en/<fn>')
def download_gtts_en(fn):
    return send_file(fn, as_attachment=True)


@app.route('/download_pyttsx3_en/<fn>')
def download_pyttsx3_en(fn):
    return send_file(fn, as_attachment=True)


@app.route('/pytesseract_vi', methods=["GET", "POST"])
def pytesseract_vi_rout():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('pytesseract_vi.html')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('pytesseract_vi.html')
        fn = file.filename
        if '.' in fn and fn.split('.', 1)[1].lower() in {'png', 'jpg'}:
            file.save(os.path.join(r'D:\files\vi\pytesseract', fn))
            text = pytesseract_vi.pytesseract_vi_prc(fn)
            return render_template('pytesseract_vi_result.html', text=text)
        else:
            flash('Not suitable file')
            return render_template('pytesseract_vi.html')
    return render_template('pytesseract_vi.html')


@app.route('/pytesseract_en', methods=["GET", "POST"])
def pytesseract_en_rout():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('pytesseract_en.html')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('pytesseract_en.html')
        fn = file.filename
        if '.' in fn and fn.split('.', 1)[1].lower() in {'png', 'jpg'}:
            file.save(os.path.join(r'D:\files\en\pytesseract', fn))
            text = pytesseract_en.pytesseract_en_prc(fn)
            return render_template('pytesseract_en_result.html', text=text)
        else:
            flash('Not suitable file')
            return render_template('pytesseract_en.html')
    return render_template('pytesseract_en.html')


@app.route('/speechrecognition_vi', methods=["GET", "POST"])
def speechrecognition_vi_rout():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('speechrecognition_vi.html')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('speechrecognition_vi.html')
        fn = file.filename
        if '.' in fn and fn.split('.', 1)[1].lower() == 'wav':
            file.save(os.path.join(r'D:\files\vi\speech_recognition', fn))
            text = speech_recognition_vi.speech_recognition_vi_prc(fn)
            return render_template('speechrecognition_vi_result.html', text=text)
        else:
            flash('Not suitable file')
            return render_template('speechrecognition_vi.html')
    return render_template('speechrecognition_vi.html')


@app.route('/speechrecognition_en', methods=["GET", "POST"])
def speechrecognition_en_rout():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return render_template('speechrecognition_en.html')
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('speechrecognition_en.html')
        fn = file.filename
        if '.' in fn and fn.split('.', 1)[1].lower() == 'wav':
            file.save(os.path.join(r'D:\files\en\speech_recognition', fn))
            text = speech_recognition_en.speech_recognition_en_prc(fn)
            return render_template('speechrecognition_en_result.html', text=text)
        else:
            flash('Not suitable file')
            return render_template('speechrecognition_en.html')
    return render_template('speechrecognition_en.html')


@app.route('/pyvi_vi', methods=["GET", "POST"])
def pyvi_vi_route():
    if request.method == 'POST':
        text = request.form['text']
        pos_tags = pyvi_text.pyvi_prc(text)
        return render_template('pyvi_vi_result.html', text=text, pos_tags=pos_tags)
    return render_template('pyvi_vi.html')


@app.route('/underthesea_vi', methods=["GET", "POST"])
def underthesea_vi_route():
    if request.method == 'POST':
        text = request.form['text']
        uvdoc = underthesea_text.underthesea_prc(text)
        return render_template('underthesea_vi_result.html', text=text, pos_tags=uvdoc.pos_tags,
                               ner_text=uvdoc.ner_text,
                               classify_result=uvdoc.classify_result, sentiment_result=uvdoc.sentiment_result)
    return render_template('underthesea_vi.html')


@app.route('/stanzavi_vi', methods=["GET", "POST"])
def stanzavi_vi_route():
    if request.method == 'POST':
        text = request.form['text']
        stvdoc = stanzavi_text.vinlp(text)
        return render_template('stanzavi_vi_result.html', text=text, stvdoc=stvdoc)
    return render_template('stanzavi_vi.html')


@app.route('/gensim_en', methods=["GET", "POST"])
def gensim_en_route():
    if request.method == 'POST':
        text = request.form['text']
        summa = gensim_text.gensim_prc(text)
        return render_template('gensim_en_result.html', text=text, summa=summa)
    return render_template('gensim_en.html')


@app.route('/spacy_en', methods=["GET", "POST"])
def spacy_en_route():
    if request.method == 'POST':
        text = request.form['text']
        spedoc = spacy_text.spacy_prc(text)
        return render_template('spacy_en_result.html', text=text, doc=spedoc.doc, deps=spedoc.deps, ent=spedoc.ent)
    return render_template('spacy_en.html')


@app.route('/nltk_en', methods=["GET", "POST"])
def nltk_en_route():
    if request.method == 'POST':
        text = request.form['text']
        nedoc = nltk_text.nltk_prc(text)
        return render_template('nltk_en_result.html', text=text, pos_tags=nedoc.pos_tags, lemmas=nedoc.lemmas,
                               sentiment_result=nedoc.sentiment_result)
    return render_template('nltk_en.html')


@app.route('/textblob_en', methods=["GET", "POST"])
def textblob_en_route():
    if request.method == 'POST':
        text = request.form['text']
        tedoc = textblob_text.textblob_prc(text)
        return render_template('textblob_en_result.html', text=text, doc=tedoc.doc, lemmas=tedoc.lemmas,
                               sentiment_result=tedoc.sentiment_result)
    return render_template('textblob_en.html')


@app.route('/stanzaen_en', methods=["GET", "POST"])
def stanzaen_en_route():
    if request.method == 'POST':
        text = request.form['text']
        stedoc, ner_text = stanzaen_text.stanzaen_prc(text)
        senti = {
            0: "negative",
            1: "neutral",
            2: "positive"
        }
        return render_template('stanzaen_en_result.html', text=text, stedoc=stedoc, ner_text=ner_text, senti=senti)
    return render_template('stanzaen_en.html')


#@app.route('/transformers_en', methods=["GET", "POST"])
#def transformers_en_route():
#    if request.method == 'POST':
#        text = request.form['text']
#        sa = transformers_text.sa(text)
#        sentiment_result = sa[0]['label']
#        return render_template('transformers_en_result.html', text=text, sentiment_result=sentiment_result)
#    return render_template('transformers_en.html')


if __name__ == '__main__':
    app.run(debug=True)
