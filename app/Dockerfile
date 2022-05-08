FROM python:3.9-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNbUFFERED 1


# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev zlib-dev libjpeg jpeg-dev py3-pillow py3-cffi py3-brotli pango-dev fontconfig ttf-freefont font-noto terminus-font

# Install dependencies
RUN pip install -U pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
