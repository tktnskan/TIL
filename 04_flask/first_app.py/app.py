import random
import sys
import os
from flask import Flask, jsonify  #Flask 클래스 호출
from script import eng_dict
import csv


app = Flask(__name__)


@app.route('/')  # 조건부
def index():
    return 'Hi~!'

@app.route('/ssafy')
def ssafy():
    return 'Welcome to ssafy!'

@app.route('/pick_lotto')
def pick_lotto():
    a = sorted(random.sample(range(1,46),6))
    # return(f'오늘 당신의 로또번호는 {str(a)} 입니다.')
    return jsonify(
        {
            '오늘 당신의 로또번호는': f'{a}'
        }
    )

@app.route('/hi/<string:name>') # app은 flask 서버를 의미, route는 가는길, 
#()안은 주소(목적지), 목적지 도달시 밑에 정의되어 있는 함수 def hi(name)을 자동으로 실행
def hi(name):  # 소괄호 안에 argument를 지정해주어야 코드가 흐름,
    return(f'hi {name}!')

@app.route('/dictionary/<string:word>')
def dictionary(word):
    if word in eng_dict.keys():
        # return f'{word}는 ' + eng_dict[f'{word}']
        return f'{word} 는 {eng_dict[word]}'
    else:
        return f'{word}는 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':
    app.run(debug=True)
