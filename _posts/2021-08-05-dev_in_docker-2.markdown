---
layout: post
title:  "Dev in docker 2"
date:   2021-08-05 10:35:24 +0200
categories: software
---
# Dev in Docker without going insane

## Tl;dr
Developing in docker is designed to make your life better but done the wrong way this workflow can seem to be very slow. I share here some crucial modifications to [my original dev in docker post](https://braaannigan.github.io/software/2020/07/26/dev_in_docker.html) that enhance the dev in docker experience. These changes are to specify the right base image and to cache pip installations.

## What are the main headaches of dev in docker?

The main headache of developing in docker can be that you frequently rebuild the image that you are working in. This rebuilding can be a time-consuming task if your image build requires downloading lots of third-party packages such as python installations or third-party packages installed with pip. However, if you choose your image carefully and use new innovations introduced recently by Docker then the time-cost of this process is minimal.

## Choosing the right image

The base of any Docker image is some flavour of linux kernel be that ubuntu, alpine, arch and so on. However, for your particular application you may know that your software stack will focus around a particular language such as python or julia. 

You can specify your stack in the Dockerfile by choosing your favourite linux kernel and then installing the language you need. For example, if you have a debian kernel such as ubuntu and want to run in python then you can run 
```Dockerfile
FROM ubuntu:16.0.4
RUN apt-get update && apt-get install python
```

There are a number of problems with this approach. The first problem is that as we have to run ```apt-get update``` to get a live package list this step can't be cached and so Docker will run the whole command each time we build the image. The second problem is that we are not specifying which version of python we want and so the version will change over time when the same Dockerfile is re-run.

A better way of developing in Docker in this case is to use a python base image with a specified version for example starting your Dockerfile with

```
FROM python:3.8.8
```
In this case each build will use the python 3.8.8 image from the official python account on dockerhub. This provides certainty about the python version you are running.  

As well as locking down the version the other advantage is that the python 3.8.8 base image will be downloaded and cached the first time you build your image from your Dockerfile. When you close your image and rebuild it Docker can use the cached image and so you will have much faster image rebuilds than if you use the ```apt-get install``` method above.

## Caching your third-party packages
Installing many third-party packages can be an even bigger time sink than installing a single language into your image. If you have say ten python packages in your `requirements.txt` file this can translate into downloading and installing dozens of packages via pip.

Until the most recent releases of Docker, however, there was no way of caching these downloaded packages. Indeed, even in the current version of Docker these packages are not cached by default. Help is at hand as caching can now be enabled by a simple modification of the standard pip installation command to:
```Dockerfile
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
```
There is a lot to digest in this `RUN` command so we'll go through it bit by bit. The first thing to note is the end of the command where you run `pip install -r requirements.txt` just as you did before. The second thing to note is the part immediately following the `RUN` command `--mount=type=cache`. This strange command tells Docker that it is going to do some caching. The last thing to note is `target=/root/.cache/pip`. This command tells Docker that it is the pip folder it is caching in the root directory inside the container.

The first time you build your image with this command the build will proceed much as it always did by downloading each package required by pip and then installing them all.  However, on each subsequent build the download step will be replaced by a much faster retrieval from your local cache and so Docker can get quickly to the install step.

## Putting it altogether

If I'm starting a simple project at the moment my Dockerfile would look something like this:
```Dockerfile
FROM python:3.8.8
WORKDIR /usr/src/app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
```

So in this Dockerfule I 
1. choose a sensible base image
2. specify my working directory 
3. copy my `requirements.txt` file into the image
4. pip install the image. 

As in [my original dev in Docker post](https://braaannigan.github.io/software/2020/07/26/dev_in_docker.html) I accompany this Dockerfile with a bash script to actually build the image. This script looks something like this
```bash
#Target is the command line option and can be 'dev', 'lab'
TARGET=$1

DOCKER_BUILDKIT=1 docker build -t your-image-name .

if [ "${TARGET}" == "dev" ]; then
# Mount the local directory so can track changes in Git
docker run -it -rm  -v $(pwd):/usr/src/app  your-image-name:latest /bin/bash
fi
# If you want to run a jupyter notebook in the image
if [ "${TARGET}" == "lab" ]; then
docker run -it -p 8888:8888  your-image-name:latest /bin/bash
fi
```
To build the image and run the container in `dev` mode I then simply in the command line run:
```bash
bash deploy.sh dev
```

The main differences from the earlier iteration are 
1. I am no longer using multi-stage builds unless I am aiming to do a cloud deploy 
2. I have added an `-rm` command into `docker run`. This is a clean-up command that removes the container's filesystem after you exit the interactive session. This clean-up operation reduces the accumulation of old containers in memory 
3. the two runtime options are `dev` and `lab`. The `dev` option is for running your code in the command line or ipython in the container. The `lab` option is for running a jupyter notebook inside the container. In the case you use the `lab` option you also open up a port to communicate the a port inside the container so that you can have a jupyter notebook from the container that runs in your browser as normal. 

## Docker versioning

The set of practices set out here are the default in current (mid-2021) versions of Docker - in particular the caching of pip installations. However, if you are using an earlier version of Docker you had to specify an environment variable called `DOCKER_BUILDKIT` to enable these features - [see my original dev in Docker post for the usage of DOCKER_BUILDKIT](https://braaannigan.github.io/software/2020/07/26/dev_in_docker.html). In addition on the first line of your Dockerfike you had to include
```Dockerfile
# syntax=docker/dockerfile:experimental
```



