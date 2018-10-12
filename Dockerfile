FROM python:3

ADD app.py /
ADD model.sav /

RUN pip install flask
RUN pip install flask_cors
RUN pip install requests
RUN pip install sklearn

CMD ["python", "./app.py"]