FROM python:3.9-slim

WORKDIR /model 

COPY ./requeriments.txt /model/requeriments.txt
COPY ./controller.py /model/controller.py
COPY ./main.py /model/main.py
COPY ./model.py /model/model.py
COPY ./Betoweight.pth /model/Betoweight.pth
COPY ./MBertweight.pth /model/MBertweight.pth

RUN pip install --no-cache-dir --upgrade -r /model/requeriments.txt

EXPOSE 5000

CMD ["streamlit", "run", "main.py"]

