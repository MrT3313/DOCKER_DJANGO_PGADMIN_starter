# Dockerfile
#FROM python:latest as base
FROM python:3.9 as base

# SET: environment variables
## dont write .pyc files to disk -> dev environment stays clean
ENV PYTHONDONTWRITEBYTECODE 1
## send python output straight to terminal w/o being buffered (see in real time)
ENV PYTHONUNBUFFERED 1
## add (NOT REPLACE) files to the available path
ENV PATH="/scripts:${PATH}"

#FROM base as global_installs_and_updates
RUN apt-get update && \
    apt-get install -y
RUN pip install --upgrade pip

# TODO: multi stage build
#FROM global_installs_and_updates as build

# 👀 docker_workflow-compose is passing "src/app" directory as build context

# INSTALL: requirements
## V1
COPY ./requirements /app/requirements

FROM base as dev

COPY --from=base /app /app
RUN pip install -r /app/requirements/dev.txt

# maps static files to volumes
RUN mkdir -p /vol/app/static
RUN mkdir -p /vol/app/media
RUN chmod 755 /vol/app/static
RUN chmod 755 /vol/app/media

# COPY: application files to container
COPY . /app

# make all files inside /scripts directory executable
RUN chmod +x /app/scripts/*

# 🚨 needed for aws fargate
VOLUME /vol/app

# CHANGE: workdir to access manage.py
WORKDIR /app

#CMD ["entrypoint.sh"]

# TODO: ACTIVATE ENV --> notes below
#FROM base as env

FROM base as prod

COPY --from=base /app /app
RUN pip install -r /app/requirements/prod.txt

# maps static files to volumes
RUN mkdir -p /vol/app/static
RUN mkdir -p /vol/app/media
RUN chmod 755 /vol/app/static
RUN chmod 755 /vol/app/media

# COPY: application files to container
COPY . /app

# make all files inside /scripts directory executable
RUN chmod +x /app/scripts/*

# 🚨 needed for aws fargate
VOLUME /vol/app

# CHANGE: workdir to access manage.py
WORKDIR /app

#CMD ["entrypoint.sh"]















# 🚨 ACTIVATE: venv
# Can avoid conflicts with the underlying base img -> should not be an issue with alpine but can be with other base images
## TODO: when its working move install to run BLOCK above
#RUN apt-get install virtualenv -y
## V2
## last line: prevents from running the container as the root user
#RUN virtualenv venv && \
#    venv/bin/activate && \
#    venv/bin/pip install --upgrade pip && \
#    venv/bin/pip install -r ./app/requirements/prod.txt && \
#    adduser --disabled-password --no-create-home app

#ENV PATH="/venv/bin:$PATH"
#USER app

## V3
#RUN virtualenv venv
#
#RUN venv/bin/pip install --upgrade pip
#
#RUN venv/bin/activate && \
#	venv/bin/pip install -r ./app/requirements/prod.txt

## 🚨 DEFINE PATH - w/ virtual env
#ENV PATH='/scripts:/venv/bin:$PATH'



