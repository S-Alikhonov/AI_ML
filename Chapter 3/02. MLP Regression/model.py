import torch
from torch import nn
from torch.optim import Adam
from data_handler import loadtest,loadtrain



#for timeseries
input_dim = 35
hidden = [14,7]
model = nn.Sequential(
    nn.Linear(input_dim,hidden[0]),
    nn.ReLU(),
    nn.Linear(hidden[0],hidden[1]),
    nn.ReLU(),
    nn.Linear(hidden[1],1)
)
optimizer = Adam(model.parameters(),lr=0.001)


#for regular calssification
input_dim_reg = 7
hidden_reg = [5,3]
model_reg = nn.Sequential(
    nn.Linear(input_dim_reg,hidden_reg[0]),
    nn.ReLU(),
    nn.Linear(hidden_reg[0],hidden_reg[1]),
    nn.ReLU(),
    nn.Linear(hidden_reg[1],1)
)
optimizer_reg = Adam(model_reg.parameters(),lr=0.001)

loss = nn.MSELoss()

