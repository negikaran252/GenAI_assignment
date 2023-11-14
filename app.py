from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from dict import language_code_dict,voice_data_dict
from helper import image_ocr, text_to_speech, text_translation

app = Flask(__name__)

languages = []
for key in language_code_dict.keys():
    languages.append(key)


@app.route("/")
def home_page():
    return render_template('index.html', languages=languages)

@app.route("/translate",methods=['POST'])
def translated():
    file = request.files['file']
    language = request.form.get('language')
    filename = secure_filename(file.filename)
    file.save(os.path.join("static/"+filename))
    target_text=image_ocr("static/"+filename)
    lang_code=language_code_dict[language]
    translated_text=text_translation(target_text,lang_code)
    speech_code=""
    if language in voice_data_dict.keys():
        speech_code=voice_data_dict[language]
    else:
        return "Model doesn't support language to translate"
    audio_file = text_to_speech(translated_text,speech_code)    
    return render_template('translate.html',image="static/"+filename,text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
