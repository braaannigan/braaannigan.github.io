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
The workshop materials will be in python using a package called PyMC3.
You can install the software needed using the Anaconda python distribution.
If you already have Anaconda installed then you can skip to the Virtual Environment
section below.

# Python installation
There may be a version of python installed on your system already.  However,
it is unlikely that it will be up-to-date enough for the
workshop software to run with that software.  

To make sure that we are all using the same software we will use
the Anaconda distribution of python.  If you have never downloaded Anaconda,
you go to [this page](https://www.anaconda.com/download/
) and download the **python 3** version.

The anaconda installer may ask your permission to do various things such as
appending to your .bashrc file during installation. You can agree to all the points it asks.

For **mac/linux** you need to start a new terminal
session once Anaconda is installed.

If you are using **windows** you open the Anaconda prompt (you can search for
"Anaconda prompt" from the Start menu).  **All of the commands** set out
below occur in the terminal (mac/linux) or the Anaconda prompt (windows),
rather than inside python.

To check that the installation has worked, enter in the terminal/Anaconda prompt
```
conda info
```
This will display some information about the version of ```conda``` that you
are using.  In this case ```conda``` is the command line utility that
will allow you to manage the packages that are installed in your
virtual environments.  If you are interested you
can learn more about what ```conda``` does [in this blog post](http://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/).


# Virtual environment
It is good practice to create virtual environments on your
machine.  A virtual environment is like a 'walled-off' installation of a
program -- such as python -- on your machine.  Using a virtual environment lets you play around
with different software set-ups on the same machine.  For example, you might
have one virtual environment that holds the set-up for one project
that you started a couple of years ago with older versions of package.
When you start a new project you create a new virtual environment with
more recent version of packages without disturbing the older project.
You can then switch between these environments with a single command.

For this workshop, we will create a virtual environment called 'bayes'. This
virtual environment will have the packages that we need for the workshop installed.

You can create this environment and install the necessary packages using  
conda by running the following command
in the terminal (mac/linux) or the Anaconda prompt (windows):
```
conda create -n bayes python=3.6.1 ipython jupyter scipy pymc3 pandas scikit-learn xarray holoviews bokeh seaborn
```
Answer yes to any questions the installer asks.


This command 1) creates an environment called 'bayes', 2) sets python 3.6.1 as the
python version and then 3) installs the packages listed from ipython:seaborn.  

You can then 'activate' (switch-to) this virtual environment from
the terminal in mac/linux with the command:
```
source activate bayes
```
or in windows from the Anaconda prompt

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

# Ipython kernel for the Jupyter notebooks
We will be using interactive jupyter notebooks in the workshop.  You need to
make sure that the notebook sees the python installation
in the ```bayes``` virtual environment.  
You do this with the command
```
python -m ipykernel install --user --name bayes --display-name "bayes"
```

# Test the installation
You can test whether the installation has worked by opening a jupyter notebook.  
In the terminal (mac/linux) or the Anaconda prompt (windows) enter:
```
jupyter notebook
```

A notebook should then open in your web browser.  Click the 'new' button
on the top right and check that 'bayes' is listed as an option amongst the
kernels.  If bayes does not appear, then open a new terminal and try running the
ipython kernel creation command again.  If that fails then let me know.

Finally, to make sure everything is installed correctly, run the test notebook.
Navigate to [this page in your web browser](https://raw.githubusercontent.com/braaannigan/explore_data/master/_00_installation_check.ipynb).

Click ctrl + s and save the file as ```_00_installation_check.ipynb```.

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

You may get an error message saying that the xarray package has not been found.
In this case you should close down the notebook in the browser and in
the command line.  You then run
```
pip install xarray
```
and try again to open a notebook and run ```_00_installation_check.ipynb```.

Contact me if there are any problems.
