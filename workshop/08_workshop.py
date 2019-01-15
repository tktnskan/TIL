from flask import Flask
app = Flask(__name__)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    dictionary={
        'apple': '사과',
        'banana': '바나나',
        'watermelon': '수박'
    }
    if word in dictionary.keys():
        a = dictionary[word]
        return (f'{word} 은(는) {a}')
    else:
        return (f'{word} 은(는) 나만의 단어장에 없는 단어입니다!')
    
app.run(debug = True)