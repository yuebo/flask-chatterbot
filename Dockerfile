FROM python:3.7.4-stretch
RUN mkdir -p /root
ADD . /root
WORKDIR /root
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENV DB_URL sqlite:///db.sqlite3
ENV DB_ADAPTER chatterbot.storage.SQLStorageAdapter
COPY utils.py /usr/local/lib/python3.7/site-packages/chatterbot/utils.py
EXPOSE 5000
ENTRYPOINT ["python","app.py"]
