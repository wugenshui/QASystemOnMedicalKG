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
        self.FINISH_WORD = ['下一轮', '新的疾病']

    def chat_main(self, sent):
        answer = '您好，我是小勇医药智能助理，希望可以帮到您。祝您身体棒棒！'
        self.log('实际查询语句：' + sent)
        res_classify = self.classifier.classify(sent)
        self.log('提取参数：' + str(res_classify))
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        self.log('转化SQL：' + str(res_sql))
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            if final_answers['last'] != None:
                self.disease = ''
                self.lastquestion = final_answers['last']
                if final_answers['last'] != '':
                    self.disease = final_answers['last']
            return final_answers['data']

    def isFinish(self, sent):
        for wd in self.FINISH_WORD:
            if wd in sent:
                self.disease = ''
                self.lastquestion = ''
                print('*' * 100)
                print('您好，我是小勇医药智能助理，希望可以帮到您。祝您身体棒棒！')
                return True
        return False
    
    def log(self, msg):
        a = 1
        #print(msg)
            
            

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        if not handler.isFinish(question):
            if handler.disease == '':
                # 未确定疾病前记录上一次的问题
                handler.lastquestion += question + ' '
                answer = handler.chat_main(handler.lastquestion)
            else:
                answer = handler.chat_main(handler.disease + question)
            print('小勇:', answer)

