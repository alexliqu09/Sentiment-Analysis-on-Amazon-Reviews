<h1><center><b>Applying BERT Fine Tuning to Sentiment Classification on Amazon Reviews</b></center></h1>

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

- [Beto]()
- [MBert]()

<h2><b>Run the work in local</b></h2>

If you want to proof the work ,  you should run the following commands:

* First , Install requeriments file:

```
pip install -r requirements.txt
```

* Second , download the Weights [here]() and put them in this directory 

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

docker build -t bert

#RUN container
docker run -t -p 5000:5000 --name betocontainer bert
```
open http://localhost:5000.




If you find useful our work , please cite this paper:
```
@inproceedings{lique,
  title={Applying BERT Fine Tuning to Sentiment Classification on Amazon Reviews},
  author={Lique, Alexander and Vásquez, Diego and Rios, Manuel },
  year={2021}
}
```