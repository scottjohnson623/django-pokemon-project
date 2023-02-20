FROM --platform=linux/amd64 python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api/
COPY start.sh /start.sh

RUN pip install -r requirements.txt
ADD . /api
RUN ls -all
CMD ["/start.sh"]
