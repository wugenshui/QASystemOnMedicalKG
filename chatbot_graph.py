#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()
        # 症状缓存
        self.symptom = []
        # 疾病缓存
        self.disease = ''
        # 上一次的问题，未回答完成会进行累加
        self.lastquestion = ''

    def chat_main(self, sent):
        answer = '您好，我是小勇医药智能助理，希望可以帮到您。如果没答上来，可联系https://liuhuanyong.github.io/。祝您身体棒棒！'
        res_classify = self.classifier.classify(sent)
        print(res_classify)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        print(res_sql)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            if not final_answers['data']:
                # 旧版问答
                return '\n'.join(final_answers)
            else:
                # 新版问答
                if final_answers['last'] != None:
                    self.lastquestion = final_answers['last']
                    print('set self.lastquestion:' + self.lastquestion)
                return final_answers['data']
            
            

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        # 记录上一次的问题
        handler.lastquestion += question + ' '
        answer = handler.chat_main(handler.lastquestion)
        print('小勇:', answer)

