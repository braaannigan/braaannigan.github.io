---
layout: post
title:  "Dev in docker"
date:   2020-07-26 10:35:24 +0200
categories: software
---

## Why should you dev in Docker?

Docker containers are like a mini operating system that you can run on your computer. Developing inside these containers has many advantages for anyone doing data analysis. The containers provide isolated environments so that you can have different software stacks for different projects without them interfering with each other. Unlike python virtual environments these containers cover the operating system as well as the analysis software. This depth becomes particularly import when using more complicated software such as deep learning libraries like Tensorflow or PyTorch that have dependencies in C++ and CUDA that make them much more brittle and sensitive to the exact version of any packages you use. 

Docker containers are also great for collaboration and reproducibility. As you choose the operating system inside the container it no longer matters whether other users are running a different Linux distribution, MacOS or even Windows. It is also straightforward to share the containers either by using a Dockerfile (just a text file with docker commands for setting up the container) or a docker image hosted on Dockerhub.  

## Why does it seem like a pain to dev in Docker?

If you hear all of this and decide you'll give developing in Docker a go, you'll probably find it a frustrating experience. You might find that you have to frequently rebuild the docker image and it takes ages each time to do so. In addition, you might find that you now have to keep track of changes to the same files both on your regular system and in the container.