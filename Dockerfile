FROM gcr.io/google_appengine/python

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ADD . /app

CMD ["python3","keepAlive"]