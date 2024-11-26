---
author: Tom Gotsman
date: 2024-10-08
title: Self Hosting Reflex with Docker
description: Hosting Reflex on your own infra using Docker for efficient containerization.
image: /blog/self-hosting-with-docker.webp
meta: [
    {
      "name": "keywords",
      "content": "
        docker containerization,
        self-hosting python apps,
        reflex deployment,
        containerized web applications,
        docker compose for web apps,
        python web app deployment,
        reflex and docker integration,
        devops for reflex applications,
        data manipulation in python,
        data-driven web apps,
        modern web application development,
        python data analysis tools,
        python data visualization,
        python fintech applications,
        python web development,
        reflex ecosystem,
        reflex web development,
      "
    },
]
---

```python exec
from pcweb.flexdown import markdown_with_shiki
```

Reflex offers a powerful way to build reactive web apps in pure Python, complete with one-line deployment for easy hosting. For those who want to self host on their own infra we'll explore how to leverage Docker to containerize and deploy your app, taking your Reflex app from development to production.


## Prerequisites 

This tutorial assumes you have a Reflex app ready for deployment and Docker Compose installed on your machine. If you haven't already, you can install Docker Compose by following the instructions on the [Docker website](https://docs.docker.com/compose/install/).



## Dockerizing Your Reflex App


There will only be 4 files needed to Dockerize your Reflex app:

1. `compose.yml`
2. `Dockerfile`
3. `web.Dockerfile`
4. `nginx.conf`

You need to create these files at the top level of your app, the same folder level as the `rxconfig.py` file. See below for an example folder structure:

```bash
\{app_name}
├── .web
├── assets
├── \{app_name}
│   ├── __init__.py
│   └── \{app_name}.py
├── compose.yml
├── Dockerfile
├── nginx.conf
├── web.Dockerfile
└── rxconfig.py

```


### compose.yml

The first file is the `compose.yml` file. This file will define the services that will be run in the Docker containers and makes them work together. Here is an example of a `compose.yml` file:


```yaml
services:
  backend:
    build:
      dockerfile: Dockerfile
    ports:
     - 8000:8000
    depends_on:
     - redis
  frontend:
    build:
      dockerfile: web.Dockerfile
    ports:
      - 3000:80
    depends_on:
      - backend
  redis:
    image: redis
```

```python exec
import reflex as rx
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header=rx.text("Explanation of the compose.yml file", color=rx.color("slate", 12), weight="regular"),
        content=markdown_with_shiki("""Here we define three services: `backend`, `frontend`, and `redis`. The `backend` service will run the Reflex app, the `frontend` service will run the web server, and the `redis` service will run the Redis server. The `depends_on` key specifies the order in which the services will be started.

The first to be run is the `redis` service. We use Redis for the state manager and it is good to put in its own container, so that its easy to differenatiate the resource usage from a cache and the actual web server. It pulls the docker image for redis and runs the image as a container. If we wanted a specific tag then we can specify it in the image key, i.e. `image: redis:7.4.0`.

As the `backend` service is dependent on the `redis` service, the `backend` service will not start until the all the services in the `depends_on` have started and have passed the health checks. The `backend` service will build the backend Docker image using the `Dockerfile` and run the image as a container. For the `ports` first `8000` is the external port, the one that we get access to from the docker container. The second number is internal port i.e. within Reflex.

Once the `backend` service has passed all the health checks, the `frontend` service image will be built using the Dockerfile `web.Dockerfile` and then run as a container. For the ports `3000` is the external port we access outside the container and it maps to port `80` for the internal port as this is where http resolves to because this is where nginx serves the application inside the container (we will explain what nginx is later in this blog).""", color=rx.color("slate", 12)),
    ),
    variant="ghost",
    collapsible=True,
)
```



### Dockerfile

The `Dockerfile` is used to build the Docker image for the Reflex app. Here is an example of a `Dockerfile`:

```dockerfile
FROM python:3.12


ENV REDIS_URL=redis://redis PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt


ENTRYPOINT ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "debug" ]
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header=rx.text("Explanation of the Dockerfile file", color=rx.color("slate", 12), weight="regular"),
        content=markdown_with_shiki("""We start from the python image of 3.12. 

Docker compose makes all the services accessible to each via their service name. Therefore `redis://` is the protocol, `redis` is the url and is easily accessible to all other services and therefore we access the redis container. If you are using a self hosted redis then you would put the actual url here instead of redis i.e. `REDIS_URL=redis://sjc04rdsdb01.your.cloud.provider.com`. `PYTHONUNBUFFERED=1` ensures that stdout and stderr go to the terminal.

`WORKDIR /app` sets the working directory inside the docker container. `COPY . .` copies everything from your current directory into the docker container.

The `ENTRYPOINT` is the command that is run when the container starts. In this case, we run the `reflex` command to start the Reflex app in production mode. The `--backend-only` flag tells Reflex to only run the backend server and not the frontend server. The `--loglevel` flag sets the log level to debug.""", color=rx.color("slate", 12)),
    ),
    variant="ghost",
    collapsible=True,
)
```


### web.Dockerfile

The `web.Dockerfile` is used to build the Docker image for the web server. Here is an example of a `web.Dockerfile`:

```dockerfile
FROM python:3.12 AS builder

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
RUN reflex export --frontend-only --no-zip

FROM nginx

COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header=rx.text("Explanation of the web.Dockerfile file", color=rx.color("slate", 12), weight="regular"),
        content=markdown_with_shiki("""We import `python:3.12` and build on top of it and the name of this build step is `builder` which we can then reference later as needed. The `WORKDIR`, `COPY`, `RUN pip install` commands are the same as in the `Dockerfile`. The `reflex export --frontend-only --no-zip` command exports the frontend assets to the `.web/_static` directory. The `builder` step encompasses all lines until we reach the next `FROM` statement. After this the `builder` step is complete and ready to be used in later steps.

`nginx` is an image that we import and there is no need for an entrypoint as we plan to utilize the existing one that comes with the image.

We now have `/app/.web/_static` in our builder from the reflex export command and we copy that into the location that nginx is looking to serve files from.

We update the nginx configuration to one that serves our files and has a proxy pass to the backend and place this config where nginx looks to read its configuration from.""", color=rx.color("slate", 12)),
    ),
    variant="ghost",
    collapsible=True,
)
```



### nginx.conf

The `nginx.conf` file is used to configure the Nginx web server. Here is an example of an `nginx.conf` file:

```nginx
server { 
 listen 80;
 listen  [::]:80;
 server_name frontend;


 error_page   404  /404.html;

 location /_event {
    proxy_set_header   Connection "upgrade";
    proxy_pass http://backend:8000;
    proxy_http_version 1.1;
    proxy_set_header   Upgrade $http_upgrade;
 }

 location /ping {
    proxy_pass http://backend:8000;
 }

 location /_upload {
    proxy_pass http://backend:8000;
 }

 location / {
   # This would be the directory where your Reflex app's static files are stored at
   root /usr/share/nginx/html;
 }

}
```

```python eval
rx.accordion.root(
    rx.accordion.item(
        header=rx.heading("Explanation of the nginx.conf file", color=rx.color("slate", 12), weight="regular", size='5'),
        content=markdown_with_shiki("""The `listen 80;` and `listen  [::]:80;` lines specify that the server should listen on port 80 ([::] is for ipv6).

The `location /_event` block is used to proxy websocket connections to the backend server. The `proxy_pass http://backend:8000;` line specifies that the requests should be forwarded to the `backend` service on port 8000. Anything that hits the frontend on the 3 pages (`/_event`, `/ping`, `/_upload`) are passed on to the backend and then the backend will respond and the front end will pass that straight back to the user. 

When a request doesn't match any of the specifically defined pages above, Nginx follows these steps:

It looks in the `/usr/share/nginx/html` directory, which is where your Reflex app's static files are stored. Nginx tries to match the request's `$uri` to a file in this directory. 

Here's how it works for a request to `myapp.com/home/user`:
a. The `$uri` becomes `home/user`
b. Nginx combines the root directory with the `$uri` where root is `/usr/share/nginx/html` so the path is `/usr/share/nginx/html/uri/index.html`
c. Subbing in the `$uri` parameter it looks for a file at: `/usr/share/nginx/html/home/user/index.html`

If Nginx finds a file at this path, it serves it to the user. If no file is found, Nginx returns a 404 (Not Found) page.""", color=rx.color("slate", 12)),
    ),
    variant="ghost",
    collapsible=True,
)
```



## Running Your Dockerized Reflex App (locally)

To run your Dockerized Reflex app, navigate to the top level of your app and run the following command:

```bash
docker compose up 
```

Now check out `localhost:3000`.

```md alert warning
# Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
If the docker desktop app is not running, you will see this error message. Make sure the docker desktop app is running before you run the dockerization command.
```

When you make changes to your app and want the changes to be reflected in the docker containers you will need to rebuild the images using docker compose with the build flag:

```bash
docker compose up --build
```



## Deploying your dockerized app to a remote server 

*Note*: the following commands were used on a EC2 Amazon Linux vm, your commands may differ slightly.

To deploy your Dockerized Reflex app to a remote server, you will need to push your Docker images to a container registry like Docker Hub or Amazon ECR. Once your images are in the registry, you can pull them onto your remote server and run them using Docker Compose.

Here are the steps to deploy your Dockerized Reflex app to a remote server:

1- Build and tag your image 

```bash
docker build . -f Dockerfile -t 83????????86.dkr.ecr.us-west-2.amazonaws.com/example_app/backend:v0.1 --platform linux/amd64
```
`example_app` is the name of the repository. `-f` is used to specify the file that we want to build into an image. `-t` is for tagging and is used to name the docker image. After the colon is our tag, which we normally use to do versioning.

`--platform linux/amd64` is setting what platform this docker image will run on, this may differ depending on what machine you are going to host this on. 

2- Push image to your remote repository

```bash
docker push 83????????86.dkr.ecr.us-west-2.amazonaws.com/example_app/backend:v0.1 
```

Ensure that you authenticate with your remote repository, for AWS it may look something like this:

```bash
docker login -u AWS -p $(aws ecr get-login-password --region us-west-2) 83???????86.dkr.ecr.us-west-2.amazonaws.com
```

Now repeat the commands above with the `web.Dockerfile` to build and push these to the remote repository.

*Note* you will likely need to update your `web.Dockerfile` to include the `API_URL` for the hostname of where you are hosting

```dockerfile
FROM python:3.12 AS builder

WORKDIR /app

COPY . .
ENV API_URL=http://ec2-XX-XXX-XXX-XX.us-west-2.compute.amazonaws.com
RUN pip install -r requirements.txt
RUN reflex export --frontend-only --no-zip


FROM nginx


COPY --from=builder /app/.web/_static /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
```


### Update the compose.yml file

3- Add an updated the `compose.yml` file to pull the images from the remote repository to your remote host.


```dockerfile
services:
  backend:
    image: XXXXXX.dkr.ecr.us-west-2.amazonaws.com/example_app/backend:v0.1
    entrypoint: ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "debug" ]
    depends_on:
     - redis
  frontend:
    image: XXXXX.dkr.ecr.us-west-2.amazonaws.com/example_app/frontend:v0.1
    ports:
      - 80:80
    depends_on:
      - backend
  redis:
    image: redis
```

4- In side your EC2 Machine run the following commands (ignoring the comments):

```bash
# add your compose.yml here
vi compose.yml

# become root
sudo su 
# install docker
yum install docker -y 
# download docker-compose
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose 
# make docker-compose executable 
chmod +x /usr/local/bin/docker-compose
# check to make sure docker-compose is working
docker-compose version
# output: Docker Compose version v2.29.7

# start docker
systemctl start docker

# configure aws for accessing private ecr
aws configure
# here you will have to provide your access key id and secret access key

# login with docker using our ecr creds
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin xxxxxx.dkr.ecr.us-west-2.amazonaws.com

# start up the app
docker-compose up -d
```



