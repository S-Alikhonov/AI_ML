from model import model,loss,optimizer,model_reg,optimizer_reg
from data_handler import loadtrain,loadtest

def train(model_nn,loss,optimizer,epochs,lr):
    for epoch in range(epochs):
        print(f'runing epoch {epoch+1} out of {epochs} epochs:')
        for i, (x,y) in enumerate(iter(loadtrain)):
            optimizer.zero_grad() #setting grad as 0, to prevent grad accumualtion
            y_h = model_nn(x) #prediction
            loss_val = loss(y_h,y) # loss calc
            print(f'{i} iteration loss:\t {loss_val.item():.6f} ') 
            loss_val.backward() #backprop
            optimizer.step() #updating weights and biases

train(model_reg,loss,optimizer_reg,10,0.03)