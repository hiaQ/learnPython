#!/user/bin/env python
#coding:utf-8

dict = {
        'Hello'                       : 'Hello',
        'Nice to meet you'            : 'Nice to meet you,too',
        'Which fruit do you like best': 'I like apple very much',
        'How old are you'             : '20 years old',
        'You are handsome'            : 'Thank you'
        }
#t--train 训练机器人对话；c--chat 同机器人聊天；l--leave 让机器人离开
flag = 'c' #让机器人默认是聊天状态
work = True  #让机器人默认是工作的

print 'Hi, my name is Python.'
print 'Do you want chat with me?'
while flag == 'c' or 't':
    flag = raw_input(unicode("你可以选择跟我聊天(c)还是训练我对话(t),或是让我离开(l)?(c/t/f)",'utf-8').encode('gbk'))  #聊天或训练状态时循环执行
    #训练状态时
    if flag == 't':
    	question = raw_input(unicode("请输入问题(key):",'utf-8').encode('gbk')) #获取输入作为key
    	answer = raw_input(unicode('请输入回答(value):','utf-8').encode('gbk')) #获取输入作为value
    	dict[str(question)] = str(answer)   #向字典中存入键值对
    	print u'训练成功'
    	print u"现在我已经会%d个问题了" % len(dict)
    	continue;
    #聊天状态时
    elif flag == 'c':
    	if len(dict) == 0:
    		print u"现在我还不会任何问题，请先训练我"
    		continue;
    	chat_word = raw_input(unicode('谢谢你跟我聊天，你想对我说点什么呢？','utf-8').encode('gbk'))
    	#遍历整个字典
    	for key in sorted(dict.keys()):
    		if str(chat_word) == key:
    			work = True
    			print dict[key]
    			break
    		else:
    			work = False
    	#如果机器人为不工作状态，打印提示信息，并重置工作状态为True
    	if work == False:
    		print u'抱歉，这句话我还不会回答'
    		work = True
    #执行离开操作时，打印提示信息
    elif flag == 'l':
    	print u"好的，再见！"
    	break
    else:
    	print u"请输入提示的指令"
    	continue