from train import voca,tags,input_dim,out_dim,hidden1,hidden2
import torch
from model import Model
from chats_patterns import chats
from prep import input_prep
import random

state = torch.load('med_bot.pth')
bot_model = Model(in_dim=input_dim,hidden1=hidden1,hidden2=hidden2,out_dim=out_dim)
bot_model.load_state_dict(state)


bot = 'Medbot'
print("let's have a convo, (to exit type 'quit' )")
with torch.no_grad():
    bot_model.eval()
    while True:
        text = input('You:')
        if text == 'quit':
            print('Hope you found what you want. ')
            break
        x_test = input_prep(text,voca)
        x_test = torch.tensor(x_test,dtype=torch.float)
        x_test = x_test.view(1,-1)
        out = bot_model.forward(x_test)
        _,pred = torch.max(out,1)
        tag = tags[pred.item()]
        for intent in chats['intents']:
                if tag == intent['tag']:
                    print(f"{bot}: {random.choice(intent['responses'])}")
    



