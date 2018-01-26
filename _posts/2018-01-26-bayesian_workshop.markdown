---
layout: post
title:  "Bayesian workshop"
date:   2018-01-26 10:35:24 +0200
categories: bayesian
---
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

# Introduction to Bayesian statistics workshop
The workshop materials will be in both python and R.  I will be focusing on the
python code in the workshop and so I have provided installation instructions
for python below.  I'm assuming that R users already use R and have it installed.
If you already have Anaconda installed then you can skip to the Virtual Environment
section.

# Python installation
There may be a version of python installed on your system already.  However,
to make sure that we are all using the same version we will use
the Anaconda distribution of python.  If you have never downloaded Anaconda,
you go to the page below (changing the operating system if necessary)
and download the **python 3** version.

https://www.anaconda.com/download/

The anaconda installer may ask your permission to do various things such as
appending to your .bashrc file during installation.  
You can agree to all the points it asks.

If you are using windows you then open the Anaconda prompt (you can search for
Anaconda prompt from the Start menu).  All of the commands set out
below occur in the terminal (mac/unix) or the Anaconda prompt (windows),
rather than inside python.

For mac/linux you need to start a new terminal
session once Anaconda is installed.

In the terminal/Anaconda prompt enter
```
conda info
```
to check that conda is available.  ```conda``` is the command line utility that
will allow you to manage virtual environments.  You can learn more
about ```conda``` [here](http://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/).


# Virtual environment
It is good programming practice to create 'virtual environments' on your
machine.  A virtual environment is like a 'walled-off' installation of a
program -- such as python -- on your machine.  
Using a virtual environment lets you play around
with different installation set-ups on the same machine.  For example, you might
have one virtual environment that holds the set up for one project
that you started a couple of years ago while you have another virtual environment
that has the most recent version of the packages for a new project.

For this workshop, we will create a virtual environment called 'bayes'
that has the packages that we need for the workshop installed.

You can create this environment using the conda virtual environment manager by running the following command
in the terminal (mac/linux) or the Anaconda prompt (windows):
```
conda create -n bayes python=3.6.1 ipython jupyter scipy pystan pandas scikit-learn xarray holoviews bokeh seaborn
```
Say yes to any questions the installer asks.


This command 1) creates an environment called 'bayes', 2) sets python 3.6.1 as the
python version and then 3) installs the packages listed from ipython:seaborn.  

You can then 'activate' (switch-to) this virtual environment with the command:
```
source activate bayes
```
or in windows

```
activate bayes
```

You should see 'bayes' now appearing at the start of the command prompt.

You can deactivate and return to your root environment with the command:
```
source deactivate bayes
```
or in windows:
```
deactivate bayes
```

In mac/linux you can set default virtual environment by adding a line to your
 .bashrc file.  This file lives in your home directory.  It may have a slightly
 different name on your system.  You can find it by moving to your home directory
 ```
 cd ~
 ```
 and listing all the files, including the files beginning with . such as .bashrc
 that are normally hidden:
 ```
 ls - a .*
```
You set the default environment for new terminal windows by adding a line to the .bashrc file:
```
source deactivate bayes
```

# ipython kernel
We will be using interactive jupyter notebooks in the workshop.  
You need to make sure that the notebook sees the python installation
in the ```bayes``` virtual environment.  
You do this with the command
```
python -m ipykernel install --user --name bayes --display-name "bayes"
```

# Test installation
You can test whether the installation has worked by opening a jupyter notebook.  In the command line enter:
```
jupyter notebook
```

A notebook should then open in your web browser.  Click the 'new' button
on the top right and see if 'python bayes' is listed as an option.  
If not, then let me know.

Finally, to make sure everything is installed correctly, run the test notebook.
Navigate to [this page in your web browser](https://raw.githubusercontent.com/braaannigan/explore_data/master/_00_installation_check.ipynb)

Click ctrl + s to save the file as ```_00_installation_check.ipynb```.

Navigate to the directory where you saved this .ipynb file from your terminal.  
Check that you have activated the bayes environment - it should say ```bayes```
at the start of your command prompt. If not, activate ```bayes``` with:
```
source activate bayes
```
or in the Anaconda prompt in windows

```
activate bayes
```
and then open a jupyter notebook with the command
```
jupyter notebook
```

Open the file: ```_00_installation_check.ipynb```.

Follow the instructions to see if the model fits and the plot appears at the end.
It might take a couple of minutes to run everything.

Contact me if there are any problems.
