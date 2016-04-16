---
layout: post
title:  "Python repo for MITgcm"
date:   2016-04-12 16:35:24 +0200
categories: code intro
---
### What's out there?
This week I opened a [repo](https://github.com/braaannigan/mitgcm_python)
with python code for analysing MITgcm output that I've
been working on.  I've just started using python in the last few months, so I
doubt that it's a particularly sophisticated set of code.  However, I decided to open
it up after doing a search for MITgcm code on github.com and discovering that
there is a very limited amount of code out there.  
[Ryan Abernathey](https://github.com/rabernat/MITgcm_parallel_analysis)
has put together what looks like a very nice package for analysing
outputs in parallel.  [Ed Doddridge](https://bitbucket.org/edoddridge/mitgcm/)
has a nice object-oriented set of code for analysing the output in serial. Beyond that
there a limited array of code from the offical website at
[mitgcm.org](http://mitgcm.org/viewvc/MITgcm/MITgcm/utils/python/MITgcmutils/MITgcmutils/).
I decided to make my repo with the idea that there are probably people out there
looking for ideas about how to write their own code and who may be able to
give me some input into what I'm doing.

### Flat-bottomed
I decided to develop my own package primarily to help me learn to code in
python.  I also wanted code that is tailored to the particular type of
model configuration that I've been working with recently: doubly-periodic
domains with uniform Cartesian grids in the horizontal and flat bottoms. Code
written for this kind of set-up can save a lot of time as it only needs
the first two grid points in a tile to generate the horizontal grid and a single
column of the vertical grid spacings to generate the vertical grid.  I'll add
options for slightly more complicated grids as and when I need them.  The code
is written so that specified outputs and coordinate ranges - in x,y,z and time - can
be loaded.  This greatly reduces the amount of reading that must be done.

### Easy plotting
One aim of the code is to allow rapid reading and plotting of the model
output, whether you're working in a jupyter notebook or from a
python command line interpreter.  This is particularly useful in the early
stages of running experiments when a visual check of the model output - including
derived fields such as vorticity or stratification - is useful.  I hope to add
more functionality for animations and 3D plotting in the future.


### Classless
I've used matlab for the last few years rather than an object-oriented language.
That's probably one reason why the code currently returns numpy data structures
rather than a class approach that returns an object.
