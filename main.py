import streamlit as st 
from model import BERT

class LoadModel():
    def __init__(self):
        self.beto = BERT(3, "dccuchile/bert-base-spanish-wwm-cased", 'Betoweight.pth')
        self.mbert = BERT(3, "bert-base-multilingual-cased", 'MBertweight.pth')

    def getModels(self):
        return self.beto, self.mbert

load = LoadModel()

if __name__ == "__main__":
    beto, mbert  = load.getModels()

    Radio =st.sidebar.radio("Select",("Home","Beto","mBert","About"))
    
    if  Radio=='Home':
        st.title("About the work")

    if Radio=='Beto':
        print(beto.sentiment_classification('me gusta'))

    if Radio=='mBert':
        print(beto.sentiment_classification('me gusta'))

    if Radio=='About':                
                st.markdown("<h1 style='text-align:left; color: red;'> About </h1>", unsafe_allow_html=True)
                st.title("Me")
                st.markdown("I am researcher of Deep Learning. I think the AI is the present and future of technology development. \n My motivation to carry out this project is because I want to deep in the Image Processing \n and also I wanted to learn about the culture and apply the data of Japan. \n")
                st.title("Contact me")
                st.markdown("If want to contact me ,you should see: \n My Email is [here](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=alexander.lique.l@uni.pe) \n My Github is [here](https://github.com/alexliqu09),\n My Twitter is [here](https://twitter.com/lique_alex)")