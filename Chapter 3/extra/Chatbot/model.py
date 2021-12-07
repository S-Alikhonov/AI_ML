import torch
from torch import nn
import torch.nn.functional as F
import numpy as np

class Model(nn.Module):
    def __init__(self,in_dim,hidden1,hidden2,out_dim):
        super(Model,self).__init__()
        self.fc1 = nn.Linear(in_dim,hidden1)
        self.fc2 = nn.Linear(hidden1,hidden2)
        self.fc3 = nn.Linear(hidden2,out_dim)
    
    def forward(self,x):
        z = F.relu(self.fc1(x))
        z = F.relu(self.fc2(z))
        out = self.fc3(z)

        return out

def train_model(model,dataloader,optimizer,criterion,epochs):
    for epoch in range(epochs):
        losses = []
        print(f'running {epoch+1} out of {epochs} epochs')

        for x,y in dataloader:
            optimizer.zero_grad()
            y = torch.tensor(y,dtype=torch.long)
            x = torch.tensor(x,dtype=torch.float)
            out = model.forward(x)
            loss = criterion(out,y)
            loss.backward()
            optimizer.step()
            losses.append(loss.item())


        print(f'\ttraining loss: {np.mean(losses):.6f}')
    name = 'med_bot.pth'
    torch.save(model.state_dict(),name)
    print(f'the last loss: {np.mean(losses):.6f} ')
    print(f'Model trained successfully as [{name}]')