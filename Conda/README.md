# Setting up a Conda environment for the UU ML course

## Introduction
This directory provides the information needed to setup your Conda environment on your laptop in the case that you do not have one already installed. Note if you plan to use only the server for your work you can skip the rest.  
For further reading on Conda you can see [Nikhef documentation](https://kb.nikhef.nl/ct/Conda_environments.html) as well.  Furthermore, some introductory notes on the use of bash (command-line/shell), emacs (text editing),
(Python and) git can be found in
[GettingStartedWithBashEmacsPythonAndGit.pdf](../GettingStartedWithBashEmacsPythonAndGit.pdf).

We will use [Conda](https://docs.conda.io/), an open-source package- and environment-management system, to
setup an environment for our machine-learning course with the required packages.  Follow the steps below to
install Conda and setup an environment.

## Installing Conda
If you haven't installed Conda, you should do it now.  

### linux 

In order to do
so, you can download the following bash script, make it executable, and run it:
```
  wget https://raw.githubusercontent.com/MarcvdSluys/UU-ML-Cluster/master/install-conda.sh
  chmod u+x install-conda.sh
  ./install-conda.sh
```
This takes about 5 minutes and will install Conda.  Note that the installer
changes your settings in `~/.bashrc`.

### MacOS 

In order to do
so, you can download the following bash script, make it executable, and run it:
```
  wget https://raw.githubusercontent.com/agrelli/material/refs/heads/main/install-conda.sh
  chmod u+x install-conda.sh
  ./install-conda.sh
```
This takes about 5 minutes and will install Conda.  Note that the installer
changes your settings in `~/.bashrc`.
If you do not have wget (very likely) then 
```
  brew install wget
```
and try again.

## Creating a Conda environment for the machine-learning course
You will have to use a fresh bash shell to do this.  You can either close and open again, or type
```
  bash
```
Then download the configuration file and setup the Conda environment for the ML course:

### linux
```bash
  wget https://raw.githubusercontent.com/agrelli/material/refs/heads/main/course.yml
  conda env create -f course.yml
```
### MacOS
```bash
  wget https://raw.githubusercontent.com/agrelli/material/refs/heads/main/course_MacOs.yml
  conda env create -f course_MacOs.yml
```
This can take about 15 minutes.
Note: you need a specific .yml file for MacOs because the support for Cuda software package is discontinued. The .yml file given her offers a workaround to still be able to use Cuda functionalities. 

If all went well, you should see the instructions to activate and deactivate the `ml_gpu_env` Conda environment:
```bash
  conda activate ml_gpu_env
  conda deactivate
```
In case of problems, like environment not accepted, have a look to the first line of the .yml file. The proper environment name is there.

### Miscellanea

The environment you just installed is a base environment for ML developments on GPU/CPU. Note that, depending on how you decide to progress with your project, you might need additional packages. In this is the case, conda itself will suggest you the missing package and then, from your environment you can just type `conda install <package>`. If you need a specific version of the package then `conda install <package>=<x.y.z>` where x,y,z is the version (i.e 3.2.1). In case of problems you are encouraged to ask technical help to your TAs.

## How to connect to the server from UU network

In case you want to use the server, be aware that each group has a group username assigned that is simply the group name (i.e for group1 is `group1`). 
How to:
- Ask the TAs (or me) the server address and group passw
- from your laptop terminal: use SSH protocol (i.e `ssh -XY group1@<server address>`). At this point the group paswd will be required
- Once the ssh succeed your terminal is now the server terminal and you can work as if you would still be in your laptop
- In the server the conda environment is already installed so you nee just to type `conda activate ml_gpu_env`
- The location of the data on the server is under `/Volumes/ML2024_data/`

## How to connect to the server from other networks

The points of the previous section are still valid but before them you need an additional step
- If you are NOT in UU network then you need to connect before to gemini server `ssh -XY <your student number>@gemini.science.uu.nl`. The passwd is your usual solis passwd. From there execute all the steps of the previous section
