FROM python:3.9.13

RUN ln -sf /usr/share/zoneinfo/Asia/Beijing/etc/localtime

RUN echo 'Asia/Beijing' >/etc/timezone

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY run.py /code/fake

EXPOSE 50001

ENV ENV="local"

CMD ["python", "fake/run.py"]
