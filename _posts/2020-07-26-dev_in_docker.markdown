---
layout: post
title:  "Dev in docker"
date:   2020-07-26 10:35:24 +0200
categories: software
---
# Dev in Docker

## Tl;dr
Use multi-stage builds and virtual environments to rapdily build and re-build your docker images.

Note: my post is inspired by this post by [Itamar Turing-Trauring](https://pythonspeed.com/articles/multi-stage-docker-python/) where you can see more detail on these ideas and some alternative approaches. 

I've also been trying to digest this great talk on [Dockerfile best practices](https://www.youtube.com/watch?v=JofsaZ3H1qM&t=1087s) and this [article on best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

## Why should you dev in Docker?

Docker containers are like a mini operating system that you can run on your computer. Developing inside these containers has many advantages for anyone doing data analysis. The containers provide isolated environments so that you can have different software stacks for different projects without them interfering with each other. Unlike python virtual environments these containers cover the operating system as well as the analysis software. This depth of the stack becomes particularly import when using more complicated software such as deep learning libraries like Tensorflow or PyTorch that have dependencies in C++ and CUDA that make them much more brittle and sensitive to the exact version of any packages you use. 

Docker containers are also great for collaboration and reproducibility. As you choose the operating system inside the container it no longer matters whether other users are running a different Linux distribution, MacOS or even Windows. It is also straightforward to share the containers either by using a Dockerfile (just a text file with docker commands for setting up the container) or a docker image hosted on Dockerhub. 


## Why does it seem like a pain to dev in Docker?

If you hear all of this and decide you'll give developing in Docker a go, you'll probably find it a frustrating experience. You might find that you have to frequently rebuild the docker image and it takes ages each time to do so. In addition, you might find that you now have to keep track of changes to the same files both on your regular system and in the container.

## What are the goals for developing in Docker?

Developing in docker we want:
- to have a consistent and isolated runtime for our analysis
- to have a docker container that you can run in just a few second after the initial build
- to be able to track changes to your scripts using Git during development
- to be able to package everything up when you are ready to share without needing a new Dockerfile.

## Let's cut to the chase
So we ca acheive all of this with the following Dockerfile. We'll discuss the associated bash script below.
```
## First stage of build for dev
FROM python:3.8-slim-buster as dev
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Create a python virtual env so we can install in dev image and copy to test and deploy
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt

# Second stage of build for sharing
FROM dev as share
# Copy over the installed python packages from dev
COPY --from=dev /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY training.py ./
```

## Use a multi-stage build
The first point is that we use a multi-stage build. The first image is called ```dev``` and the second image is called ```share```. We develop in ```dev```. In this image we don't copy our script ```training.py``` to the image as we're going to mount that file from our file system when we do ```docker run``` (see bash script below). Mounting ```training.py``` means that we can edit it as normal but the changes will be reflected inside the running container.

When we're ready to share the image with someone else we build the ```share``` image. In this image we need ```training.py``` to be included in the image as the other user won't be able to access it on our file system.

## Use a virtual environment
When we build the ```dev``` image we copy the ```requirements.txt``` file listing all of our python dependencies into the container and run ```pip install -r requirements.txt``` to install these python packages into the container. By creating a virtual environment with ```RUN python -m venv /opt/venv``` and adding it to the path with ```ENV PATH="/opt/venv/bin:$PATH"``` we ensure that all of these packages are installed into the virtual environment.  

Using a virtual environment doesn't make much difference when we are working in the ```dev``` image. Instead, the virtual environment comes in handy when we build the ```share``` image. In this case we use a command to copy the virtual environment directory from the ```dev``` image over to the ```share``` image ```COPY --from=dev /opt/venv /opt/venv```.
This means that we have copied over all of the installed packages with no need to re-install them with ```pip```.

## Think about the order of the Dockerfile
To be able to rapidly re-build your docker image means knowing how often the commands on different lines are changed and how often the files that you ```COPY``` into the image change.  Basically, if there have been no changes in the sequence of commands and the underlying files have not changed then you can re-build the image quickly because docker uses its cache. HOwever, when you change a command that is ```RUN``` or a file that you ```COPY``` then docker re-runs that line and all subsequent lines. This means that you should put lines that will change rarely earlier in the dockerfile and lines that change regularly at the bottom.

There is an additional complication with the lines containing ```requirements.txt``` and the ```pip``` installation. As these can be quite slow you generally want these to be as early in the Dockerfile as possible. However, early in development I sometimes find that these change quite regularly. However, I may also have a single huge download -- generally PyTorch -- that occupies 90%+ of the time but rarely changes. In this case I might do the ```pip ``` install of PyTorch early in the Dockerfile and then place the requirements.txt in a more appropriate place later in the sequence.

## Deploy with bash
To run your image in interactive mode you can use the following bash script
```
#Target can be 'dev', 'share' as per Dockerfile stage names
TARGET=$1

DOCKER_BUILDKIT=1 docker build -t your-image-name --target ${TARGET} .

if [ "${TARGET}" == "dev" ]; then
# Mount the local directory so can track changes in Git
docker run -it  -v $(pwd):/usr/src/app  your-image-name:latest /bin/bash
fi

if [ "${TARGET}" == "share" ]; then
docker run -it   your-image-name:latest /bin/bash
fi
```
You run this script from the command line as ```bash deploy.sh dev``` or ```bash deploy.sh share``` (where ```dev``` and ```share``` correspond to the names of the multi-stage builds in the Dockerfile).

The main difference from standard practice in the ```docker build``` command is the ```--target``` option. This specifies how far through the multi-stage build in the Dockerfile the script should proceed. In addition, we are setting an inline environment variable (i.e. an environment variable that only applies to the command that follows).This is ```DOCKER_BUILDKIT=1``` and tells docker to use its new BuildKit method for building images that is faster and produces smaller images.

If you provide the ```dev``` option to deploy.sh then you mount your local directory into the container with ```$(pwd):/usr/src/app```. When the container starts running you can run ```ls``` in the command line to check that all of your files are there.

