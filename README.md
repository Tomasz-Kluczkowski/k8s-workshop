# k8s-workshop
Basics of Kubernetes - workshop

## Project initial setup

```shell
cd ~/dev
git clone https://github.com/Tomasz-Kluczkowski/k8s-workshop.git
cd k8s-workshop
pyenv virtualenv k8s-workshop
pyenv activate k8s-workshop
pip install -r requirements.txt
```

## Start local server in debug mode

```shell
flask --debug run
```

## Test the 1 and only route '/'
- go to your browser
- enter `http://127.0.0.1:5000`
- does it show `Hello, World!` ?

## Creating a docker image
- Create a file called `Dockerfile` in the root of the project 

```shell
touch Dockerfile
```

- Fill it in starting with image base

```shell
FROM python:3.10.2-slim
```

- build the image once you have completed the Dockerfile

```shell
docker build -t hello-world-app:1.0.0 .
```

- the image will be stored in your local docker registry which is good for now.

- we can push it to public docker repo in docker hub, all we need is for you to have an account
- register you account here if you don't have one: https://hub.docker.com/signup
- login to your docker account locally

```shell
docker login
```

- type username and password as requested in the terminal.
- to be able to push to docker hub we need to tag the existing image

```shell
docker tag hello-world-app:1.0.0 <your-docker-username>/hello-world-app:1.0.0
```

- push your image to docker hub

```shell
docker push <your-docker-username>/hello-world-app:1.0.0
```
