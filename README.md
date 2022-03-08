<h1><center><b>Applying BERT Fine Tuning to Sentiment Classification on Amazon Reviews</b></center></h1>

<h2><b>Abstract</b></h2>
<p>
Sentiment analysis has made great progress in recent years, due to the fact that companies want to have a better
understanding of how their products are classified by their consumers. However, despite the great advances that 
emerge in the field of artificial intelligence to solve this task, the most robust models are found in the English
language. In the present work, we compare two Artificial Intelligence models that have monolingual and Multilingual approaches, which are Spanish BERT and Multilingual BERT, models based on BERT's transformer Architecture, to which the fine tuned technique was applied for the task of Sentiment analysis on the Amazon reviews dataset in Spanish using the accuracy and F1 score metrics. Finally, it was found that the Spanish BERT model has the best results for the sentiment analysis task on the Amazon reviews dataset in Spanish.
</p>

this paper is available [here](https://drive.google.com/file/d/1Ynn2NR7MOCsaZdNGo7CRDZSjcTAEE-br/view?usp=sharing)

<h2><b>Pipeline</b></h2>
<p>
<center>
    <br>
    <img src="src/pipeline.png" width="750px" height="300px">
    </br>
</center>
</p>


<h2><b>Prerequisites</b></h2>

* Linux / Window
* Python3
 

<h2><b>Clone this Repository</b></h2>

```
git clone https://github.com/alexliqu09/Sentiment-Analysis-on-Amazon-Reviews.git
```

<h2><b>Train model</b></h2>

If you want to train the models use the colab Notebooks

- [Beto](Beto.ipynb)
- [MBert](MBert.ipynb)

<h2><b>Run the work in local</b></h2>

If you want to proof the work ,  you should run the following commands:

* First , Install requeriments file:

```
pip install -r requeriments.txt
```

* Second , download the Weights of [Beto](https://drive.google.com/file/d/12BDzmBHhKgLkHmq-3DbZfmyNGtFF_cnh/view?usp=sharing) & [MBERT](https://drive.google.com/file/d/1CuNLZ0LbFhZbcNBN2hMSb354BKZLgRtR/view?usp=sharing) and put them in this directory 

* Third , Start Streamlit server:
```
streamlit run main.py
```
* Note:
```
Local host : http://localhost:8501 
Network URL:  http://192.168.0.5:8501
```

<h2><b>Run with Docker 🐋</b></h2>


```
#Bulding docker image 

docker build -t bert .

#RUN container
docker run -t -p 5000:5000 --name betocontainer bert
```
open http://172.17.0.2:8501




If you find useful our work , please cite this paper:
```
@inproceedings{@lvrBERT,
  title={Applying BERT Fine Tuning to Sentiment Classification on Amazon Reviews},
  author={Lique, Alexander and Vásquez, Diego and Rios, Manuel },
  year={2021}
}
```

Please cite the following paper (arXiv) if you found this dataset useful:
```
@inproceedings{marc_reviews,
    title={The Multilingual Amazon Reviews Corpus},
    author={Keung, Phillip and Lu, Yichao and Szarvas, György and Smith, Noah A.},
    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
    year={2020}
}
```


