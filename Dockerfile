FROM gcr.io/google_appengine/python

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN pip3 install requests

ADD . /app

CMD ["python3","keepAlive.py"]