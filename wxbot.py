from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
deepThought = ChatBot("zhaoge")
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
deepThought.train("chatterbot.corpus.chinese")  # 语料库
bot = Bot(cache_path=True)
my_group = bot.groups().search('王炸')[0]
my_group.send("大家好,我是人工智障")
#tuling = Tuling(api_key='40c5d77747494193b13ec1ab1a6f6c20')
@bot.register(my_group, except_self=False)
def reply_my_friend(msg):
    print(msg)
    return deepThought.get_response(msg.text).text  # 使用机器人进行自动回复
embed()