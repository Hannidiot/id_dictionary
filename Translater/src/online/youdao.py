# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:56:41 2018

@author: w1450
"""

# '''
# Created on 2018-5-26
#
# @author: yaoshuangqi
# '''

__all__ = ['youdao',]

import urllib.request
import urllib.parse
import json

class YoudaoFanyi():
    VERSION = 1.1
    URL = 'http://fanyi.youdao.com/openapi.do'
    KEY_FROM = 'Dic-EVE'
    KEY = '975360059'
    TYPE = 'data'
    # 可选值xml, json
    DOC_TYPE = 'json'
    def translate(self, text):
        """
        翻译方法，传入要翻译的文本，返回结果字典
        """
        # 参数
        params = {'keyfrom': self.KEY_FROM, 'key': self.KEY, 'type': self.TYPE, 'doctype': self.DOC_TYPE, 'version': self.VERSION ,'q': text}
        resp = urllib.request.urlopen(self.URL, urllib.parse.urlencode(params).encode(encoding='utf_8'))
        data = resp.read().decode("utf_8")
#        print('有道API翻译内容:%s'%data)
        return json.loads(data)

    def format_for_command(self, text):
        """
        为命令行格式化翻译结果
        """
        data = self.translate(text)
        # TODO：格式化字符串
        if data:
            print('有道翻译：')
            print('\t原文本：', data.get('query', text))
            translation = data.get('translation',None)
            explains = data['basic']['explains']
            if translation:
                for t in translation:
                    print('\t翻  译：', t)
                if explains:
                    print('\t解释：',explains)
            else:
                print('未找到该词')

def youdao(text):
    """
    
    :param text: 待翻译的文本
    :return: 返回一个字典，其中translation为翻译,basic - explains是解释
    """
    if text and text.strip() != '':
        return YoudaoFanyi().translate(text)

if __name__ == '__main__':
    while True:
        content = input('请输入翻译内容：')
        if content:
            print(youdao(content))
        else:
            print('有道翻译： \n\t提示：您已退出！！')
            break
