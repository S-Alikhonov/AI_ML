import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

header = st.container()
plots = st.container()

with header:
    st.title('play more to understand more...')
    st.subheader('\n'*3)
    st.subheader('here you can play with mean and standard deviation of the distribution of men\'s height ')

    
    
with plots:
    st.text('I will use some user input via sliders')
    st.title('\n'*5)
    sel_col, display_col = st.columns(2)
    def normal(x, mean, std):
        return 1/np.sqrt(2*np.pi*(std**2))*np.exp(-(x-mean)**2/(2*std**2))
    x = np.linspace(120,250,1000)
    mean = sel_col.slider('choose value for distribution mean',min_value=110,max_value=190,value=160,step=10)
    std = sel_col.slider('choose value for standard deviation',min_value=10,max_value=40,value=10,step=5)
    fig,ax = plt.subplots(figsize=(10,8))
    ax.plot(x,normal(x,mean,std),linewidth=3)
    ax.set_title("men's height distrbitution\n")
    plt.grid()
    display_col.write(fig)
