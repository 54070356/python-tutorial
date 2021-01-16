FROM python:3.7

RUN pip3 install --no-cache-dir \
    Flask==1.1.2 -i https://pypi.douban.com/simple \
    requests==2.24.0 -i https://pypi.douban.com/simple \
    uwsgi==2.0.18 -i https://pypi.douban.com/simple


RUN mkdir /usr/src/app
WORKDIR /usr/src/app/


COPY service.py ./
COPY ./entrypoint.sh ./uwsgi.sh ./health-check.sh ./

# 配置health策略
HEALTHCHECK --start-period=150s --interval=20s --timeout=5s --retries=3 CMD ./health-check.sh

# Entrypoint that reads the shell ENV variables as config flags
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
