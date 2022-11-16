from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def handler():
    word = request.args.get('word')
    dictionary = {
        'cat' : 'кошка',
    }
    translation = dictionary.get(word, 'не найдено в словаре')
    return render_template(
        'first.html',
        word = word,
        translation=translation
    )
