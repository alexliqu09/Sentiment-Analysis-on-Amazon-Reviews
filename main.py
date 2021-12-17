# docker build -t bert
# docker run -t -p 5000:5000 --name betocontainer bert


import streamlit as st
from controller import controller

if __name__ == "__main__":
    Radio = st.sidebar.radio("Select", ("Home", "Beto", "MBert", "About"))
    if Radio == "Home":
        st.markdown(
            "<h1 style='text-align: center; color: black;'><center>Applying BERT Fine Tuning to SentimentClassification on Amazon Reviews.</center></h1>",
            unsafe_allow_html=True,
        )
        st.title("About the work")
        st.markdown(".....")
        st.title("Spanish BERT")
        st.markdown(".....")
        st.title("Multilingual BERT: ")
        st.markdown("....")

    if Radio == "Beto":
        st.text_input("")
        st.markdown(
            "<h1 style='text-align: center; color: blue;'> Spanish BERT </h1>",
            unsafe_allow_html=True,
        )
        st.header("Press the buttom to predict your senteces.")
        frase = st.text_input("Ingrese una frase")
        buttom = st.button("Beto")
        if buttom:
            st.text(controller.prediction(frase, "beto"))

    if Radio == "MBert":
        st.text_input("")
        st.markdown(
            "<h1 style='text-align: center; color: blue;'> Multilingual BERT </h1>",
            unsafe_allow_html=True,
        )
        st.header("Press the buttom to predict your senteces.")
        frase = st.text_input("Ingrese una frase")
        buttom = st.button("MBert")
        if buttom:
            st.text(controller.prediction(frase, "mbert"))

    if Radio == "About":
        st.markdown(
            "<h1 style='text-align:left; color: black;'><center>About</center></h1>",
            unsafe_allow_html=True,
        )
        st.title("Me")
        st.markdown(
            "I am researcher of Deep Learning. I think the AI is the present and future of technology development. \n My motivation to carry out this project is because I want to deep in the Image Processing\n"
        )
        st.title("Contact me")
        st.markdown(
            "If want to contact me, you should see: \n My [Email](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=alexander.lique.l@uni.pe) \n My [Github](https://github.com/alexliqu09),\n My [Twitter](https://twitter.com/lique_alex)"
        )
