#COPY FROM teamshadi/mf-dataentry:Dockerfile

# to test: > docker run -it --entrypoint /bin/sh python:alpine
FROM python:alpine
RUN apk --update add git gcc musl-dev g++ freetds-dev
RUN pip3 install pew


# -i arguments copied from requirements.txt
# Reason for not using the requirements.txt is that in Dockerfile
# after a COPY, layers are not cached
RUN pew new \
  --python=python3 \
  -d \
  -i Django==1.10.5 \
  -i progressbar33==2.4 \
  ffa-cdr-admin

# This takes so long, just doing it on a new line
RUN pew in ffa-cdr-admin pip install git+https://github.com/pymssql/pymssql.git

WORKDIR /var/lib/ffa-cdr-admin
COPY . .

# required manual files. Check README.md for more details
RUN test -f importMarketflow.sh


# continue
RUN chmod +x /var/lib/ffa-cdr-admin/docker-entry.sh

ENTRYPOINT /var/lib/ffa-cdr-admin/docker-entry.sh




