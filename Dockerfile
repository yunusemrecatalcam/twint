FROM continuumio/miniconda3:4.5.4
#RUN apk add binutils libc-dev
COPY ./requirements.txt /app/requirements.txt
RUN cd /app; pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "ban.py"]