---
layout: default
visible: 1
---

# Python installation
Python may be installed on your system already.  However, we will be using the Anaconda distribution of python.  To get this, you go to the page below (changing the operating system if necessary) and download the **python 3** version.
https://www.anaconda.com/download/#linux
The anaconda installer may ask your permission to do various things such as appending to your .bashrc file during installation.  You can agree to all the points it asks.

All of the commands listed below occur in the terminal (mac/unix) or the Anaconda prompt (windows),
rather than inside python.

# Virtual environment
It is good programming practice to create 'virtual environments' on your machine.  A virtual environment is like a 'walled-off' installation of a program on your machine.  Using a virtual environment lets you play around with different installation set-ups on the same machine (similar to having different versions of matlab on the same machine).

For this workshop, we will create a virtual environment called 'work3' that has the packages that we need for the workshop installed.

In mac/linux, you can create this environment using the conda virtual environment manager by running the following in the command line:
```
conda create -n work3 python=3.6.1 ipython jupyter scipy numba xarray dask holoviews bokeh seaborn
```

In windows you need to run all commands in the Anaconda prompt (search for Anaconda from the Start menu).

This command 1) creates an environment called 'work3', 2) sets python 3.6.1 as the
python version and then 3) installs the packages listed from ipython:seaborn.  

You can then 'activate' (switch-to) this virtual environment with the command:
```
source activate work3
```
or in windows

```
activate work3
```

You should see 'work3' now appearing at the start of the command prompt.

You can deactivate and return to your root environment with the command:
```
source deactivate work3
```
or in windows:
```
deactivate work3
```

# ipython kernel
We will be using interactive jupyter notebooks in the workshop.  
You can make sure that the notebook sees the python installation in the ```work3``` virtual environment.  
You do this with the command
```
python -m ipykernel install --user --name work3 --display-name "python work3"
```

# Test installation
You can test whether the installation has worked by opening a jupyter notebook.  In the command line enter:
```
jupyter notebook
```

A notebook should then open in your web browser.  Click the 'new' button on the top right and see if 'work3' is listed as an installation.  If not, then let me know.

Finally, to make sure everything is installed correctly, run the test notebook.
Navigate to [this page in your web browser](https://raw.githubusercontent.com/braaannigan/explore_data/master/workshop_installation_check.ipynb)

Click ctrl + s to save the file as workshop_installation_check.ipynb.

Navigate to the directory where you saved the .ipynb file from your terminal.  
Check that you have activated the work3 environment and then open a jupyter notebook with the command
```
jupyter notebook
```

Open the workshop_installation_check.ipynb with the 'work3' kernel - making sure that you .

Execute the two cells​ by pressing shift-enter.  The first cell imports the necessary
packages.  The second cell checks that the package versions are up-to-date.
