#!/bin/bash

err() {
    echo -e "\n\n\nERROR $@, aborting...\n\n\n"
    exit 1
}

WORKDIR="/path/to/Conda-install" # FIXME
echo -e "\nInstalling Conda from $WORKDIR..."
mkdir -vp $WORKDIR || err "creating Conda directory"
cd $WORKDIR

echo -e "\nDownloading installer:"
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh  || err "downloading Conda"

CondaDir="/path/to/installation/.conda" # FIXME
echo "Installing Conda in $CondaDir/"
time bash Miniforge3-Linux-x86_64.sh -b -p $CondaDir || err "installing Conda"
source $CondaDir/bin/activate || err "activating Conda"
conda init || err "initialising Conda"
conda config --set auto_activate_base false  # Don't show "(base) " prefix to prompt.  Setting stored in ~/.condarc.

# rm -f Miniforge3-Linux-x86_64.sh  ||  err "cleaning up"

