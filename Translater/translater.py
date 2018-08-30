from flask import (
    Flask, render_template, url_for, jsonify, request
)

from Translater.src.online.youdao import youdao

app = Flask("muji_translater")


@app.route('/translate', methods=['GET', 'POST'])
def index():
    return render_template("trans.html")


@app.route('/get_trans', methods=['POST',])
def get_trans():
    if request.method == "POST":
        if request.form['method'] == 'youdao':
            text = request.form['text']
            """
                现在只是一个没处理过的dict，如下
                :input: test
                :return: {'translation': ['测试'], 'basic': {'us-phonetic': 'tɛst', 'phonetic': 'test', 'uk-phonetic': 'test', 'explains': ['n. 试验；检验', 'vt. 试验；测试', 'vi. 试验；测试', 'n. (Test)人名；(英)特斯特']},
                    'query': 'test', 
                    'errorCode': 0, 
                    'web': [{'value': ['测试', '测验', '检验'], 'key': 'Test'}, {'value': ['Test Drive', 'Test Drive', '无限狂飙'], 'key': 'Test Drive'}, {'value': ['测试员', '测试工程师', '软件测试工程师'], 'key': 'Test Engineer'}]}
                该怎么返回再商量
            """
            return jsonify(youdao(text))
    
        elif request.form['method'] == "baidu":
            pass
        elif request.form['method'] == 'jinshan':
            pass
        elif request.form['method'] == 'google':
            pass
        elif request.form['method'] == 'offline':
            pass

    return jsonify({"test": "测试，检测，尝试(如果你看到了这串数据，就代表你的参数走进了异次元)"})
