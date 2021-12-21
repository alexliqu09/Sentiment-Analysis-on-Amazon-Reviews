# docker build -t bert
# docker run -t -p 5000:5000 --name betocontainer bert

#from pathlib import Path
import streamlit as st
import base64
from controller import controller

st.markdown(
    """
    <style>
        .logo-img{
            width:120%;
            height:auto;
        }
    </style>
    """,
    unsafe_allow_html=True    
)

if __name__ == "__main__":
    Radio = st.sidebar.radio("Select", ("Home", "Beto", "MBert", "About"))
    if Radio == "Home":
        st.markdown(
            """
            <h1><center><b>Applying BERT Fine Tuning to Sentiment Classification on Amazon Reviews</b></center></h1>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <h2><b>About this Work</b></h2>
            <p>
                Sentiment analysis has made great progress in recent years, due to the fact that companies want to have a better
                understanding of how their products are classified by their consumers. However, despite the great advances that 
                emerge in the field of artificial intelligence to solve this task, the most robust models are found in the English
                language. In the present work, we compare two Artificial Intelligence models that have monolingual and Multilingual 
                approaches, which are Spanish BERT and Multilingual BERT, models based on BERT's transformer Architecture, to which 
                the fine tuned technique was applied for the task of Sentiment analysis on the Amazon reviews dataset in Spanish using 
                the accuracy and F1 score metrics. Finally, it was found that the Spanish BERT model has the best results for the sentiment
                analysis task on the Amazon reviews dataset in Spanish.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            ---
            <h2><b>Pipeline</b></h2>
            
            <div class="container">
                <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open('src/pipeline.png', "rb").read()).decode()}">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
                If you find useful our work , please cite this paper:
                ```
                    @inproceedings{lique,
                    title={Applying BERT Fine Tuning to Sentiment Classification on Amazon Reviews},
                    author={Lique, Alexander and Vásquez, Diego and Rios, Manuel },
                    year={2021}
                    }
                ```
        """, unsafe_allow_html=True)

    if Radio == "Beto":
        st.text_input("")
        st.markdown(
            """
                <h1 style='text-align: center; color: blue;'> Spanish BERT </h1>
                <p>
                    "The Spanish language is one of the top 5 spoken languages in the world. Nevertheless, 
                     finding resources to train or evaluate Spanish language models is not an easy task. 
                     In this paper we help bridge this gap by presenting a BERT-based language model pre-trained 
                     exclusively on Spanish data. As a second contribution, we also compiled several tasks 
                     specifically for the Spanish language in a single repository much in the spirit of the 
                     GLUE benchmark. By fine-tuning our pre-trained Spanish model we obtain better results 
                     compared to other BERT-based models pre-trained on multilingual corpora for most of the 
                     tasks, even achieving a new state-of-the-art on some of them. We have publicly released our 
                     model, the pre-training data and the compilation of the Spanish benchmarks."
                </p>
                Extract here: 
                José Cañete et al. “Spanish Pre-Trained BERT Modeland Evaluation Data”. 
                
                Original Paper <a href="https://users.dcc.uchile.cl/~jperez/papers/pml4dc2020.pdf">here</a>

            """,
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
            """
            <h1 style='text-align: center; color: blue;'> Multilingual BERT </h1>
            <p>
                    "In this paper, we show that Multilingual BERT
                    (M-BERT), released by Devlin et al. (2019)
                    as a single language model pre-trained from
                    monolingual corpora in 104 languages, is
                    surprisingly good at zero-shot cross-lingual
                    model transfer, in which task-specific annotations
                    in one language are used to fine-tune the
                    model for evaluation in another language. To
                    understand why, we present a large number of
                    probing experiments, showing that transfer is
                    possible even to languages in different scripts,
                    that transfer works best between typologically
                    similar languages, that monolingual corpora
                    can train models for code-switching, and that
                    the model can find translation pairs. From
                    these results, we can conclude that M-BERT
                    does create multilingual representations, but
                    that these representations exhibit systematic
                    deficiencies affecting certain language pairs."
            </p>
                Extract here: Telmo Pires, Eva Schlinger, and Dan Garrette.“How  multilingual is Multilingual BERT?”. 

            <div>
                Original Paper <a href="https://arxiv.org/pdf/1906.01502.pdf">here</a>
            </div>
            """,
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
        st.title("Us")
        st.markdown(
            "We are researchers of Deep Learning. We think the AI is the present and future of technology development. \n Our motivation to carry out this project is because We want to deep in the Natural language Processing\n"
        )
        st.title("Contact Us")
        st.markdown(
            "If want to contact us, you should see: \n My [Email](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=alexander.lique.l@uni.pe) \n My [Github](https://github.com/alexliqu09),\n My [Twitter](https://twitter.com/lique_alex)"
        )
