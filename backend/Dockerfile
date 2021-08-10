FROM python:3.9-slim-buster

WORKDIR /app/

# 更新apt-get 镜像源
RUN sed -i s@http://deb.debian.org@http://mirrors.aliyun.com@g /etc/apt/sources.list
RUN sed -i s@http://security.debian.org@http://mirrors.aliyun.com@g /etc/apt/sources.list

# 解决 https://stackoverflow.com/a/54939919/14080578
RUN apt-get install tzdata -y

COPY requirements.txt /app/
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip config set global.extra-index-url https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install pip==19.3
RUN pip install gunicorn gevent==20.9.0

COPY . .

RUN python manage.py collectstatic
RUN ls static/
RUN mkdir /static
RUN cp -r  static/* /static/

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 9000

ENTRYPOINT exec /docker-entrypoint.sh $0 $@
CMD ["run","web"]