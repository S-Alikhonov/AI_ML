from model import Model,train_model
from prep import loader,tokenize,prep
from chats_patterns import chats
import torch
from torch import nn

#pairs, voca, tags
pairs,voca,tags = prep(chats)

#embedded inputs and labels
x_train,y_train = tokenize(pairs,voca,tags)

#dataloader
trainloader = loader(x_train,y_train,batchsize=2)

#embedded imput size is the same as voca length
input_dim = len(voca)
#output dimension is the same as number of unique tags
out_dim = len(tags)
hidden1=24
hidden2=12
#model
model = Model(input_dim,hidden1=hidden1,hidden2=hidden2,out_dim=out_dim)

#optimizer
optimizer = torch.optim.Adam(model.parameters(),lr=0.003)

#criterion
criterion = nn.CrossEntropyLoss()

#training
# train_model(model=model,
#     dataloader=trainloader,
#     optimizer=optimizer,
#     criterion=criterion,
#     epochs=1000)


