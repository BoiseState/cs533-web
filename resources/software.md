# Software and Installation

Most of the software you will need is available through Anaconda, a distribution of scientific
software for Python (and R). It is the easiest way to install Python with the packages we need. The
one additional piece of software we will need is Git.

We are using **Python 3.8** (or newer — Python 3.9 is fine) in this class.  Older versions of Python
may work, but I will be testing my example code and instructions with Python 3.8.

:::{ltip}Department Computers
If you want to use the department's computer lab for your work, see the [Onyx setup instructions](onyx-install) as well
as the instructions for [remotely using Onyx](onyx.md).
:::

[VSC]: http://code.visualstudio.com/

## Required Software

Our primary software is:

-  [Anaconda Python](https://www.anaconda.com/distribution/) (install this in your Onyx home directory for use there)

To complete assignments on department computers, you also need:

-  An SSH client (MobaXterm for Windows, `ssh` on Mac or Linux)
-  The [Boise State VPN](https://bsuvpn-offcampus.boisestate.edu/) for convenient access to Onyx nodes

For building more advanced workflows, there are many text editors you can use.
I use [Visual Studio Code][VSC], which has very good [remote editing support](https://code.visualstudio.com/docs/remote/remote-overview)
and also directly supports Jupyter notebooks (although I do not use this feature much).

The rest of this document walks through some details.

## About Conda

Anaconda (and Miniconda, described at the end of this document) is a scientific software distribution.
It is built around the Conda package manager.

Conda installs precompiled binary versions of software, including but not limited to Python
packages. The versions of Scientific Python software distributed through Conda are compiled against
more optimized versions of the core math libraries than the packages available through standard
Python channels (the Python Package Index).

When you are looking online for instructions for Python software, it will usually tell you to
install it with `pip`. However, since we are using Conda, it works better to install the Conda
version of a package (with `conda`) if possible. It will usually, but not always, have the same name
as the Python package. You can search for Conda packages on [anaconda.org](https://anaconda.org).

## Installing Anaconda Python

!!! note Platform Support

    The full Anaconda distribution works on x86_64 platforms - most Windows and Linux computers, and Macs
    with Intel processors.  If you have a Mac with an M1 processor, or an ARM-based Linux computer, go to
    the [miniconda instructions](miniconda) and use the Miniforge installer.

To install Anaconda on your computer:

1.  Download the appropriate installer for your platform from [Anaconda Python](https://www.anaconda.com/distribution/).

    If your computer has a 64-bit operating system (most do, *except* for Windows on ARM platforms like the Surface X),
    download the 64-bit version of Anaconda.  Make sure you get the Python 3 verision (it is the default).

2.  Run the installer.

(miniconda)=
## Saving Space with Miniconda

We don't need all of Anaconda.  If you want to save disk space, [Miniconda][] is a much smaller
distribution that just contains Python and the Conda package manager, so you can install the
packages you need yourself.  [Miniforge][] is an equivalent community-maintained distribution
that has support for more hardware platforms (including Linux and Mac on ARM-based chips).

[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[miniforge]: https://github.com/conda-forge/miniforge

1.  [Download the installer][miniconda] for your platform and run it.  On M1 Macs and ARM-based Linux, get the
    appropriate installer from [miniforge][].

2.  Install the base packages we will need:

        conda install pandas scipy scikit-learn notebook ipython \
            seaborn statsmodels

## Additional Packages

I use {py:mod}`seedbank` in many of my examples for seeding the random number generator. Seedbank is not currently available through the main Anaconda channel, so you will needt
to install it with `pip`:

    pip install seedbank

Do this *after* installing your other packages with `conda`, so seedbank doesn't try to pull in a non-Conda NumPy.

It is fine to use `pip` to install packages that are not available in Conda.  It also works to use it to install packages that are, but I do not recommend this, particularly for core compute packages such as `numpy`, `scipy`, and `scikit-learn` — the versions in Conda are more optimized.

## Installing Git and Command-Line Tools

We will be using Git later in the semester.

To install Git, the instructions differ based on your platform:

-   On Windows, [download and run the installer](https://git-scm.com/).
-   On macOS, install Xcode from the App Store.
-   On Linux, install `git` from your package manager.

(onyx-install)=
## Installing on Onyx

Unlike a lot of other software, Anaconda is designed to be installed separately by each user.

To setup on Anaconda on Onyx, you need to download the installer and run it on Onyx (or an Onyx node).
Once you have set it up on any Onyx node, it will be available across Onyx, no matter which node you log in to.
Due to Onyx's network file system performance, I recommend using Miniconda.

You can do this with:

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    /bin/bash Miniconda3-latest-Linux-x86_64.sh
    rm Miniconda3*.sh

This will install Miniconda (which by default will also configure your shell to activate the Miniconda environment).
Log out and log back in to Onyx and Conda will be active.
Install the base packages:

    conda install pandas scipy scikit-learn notebook ipython \
            seaborn statsmodels

Onyx already has Git installed.

## Using Anaconda

On Linux and Mac, the installer will, by default, modify your Bash startup scripts to activate Anaconda.

On Windows, it will install a separate ‘Anaconda Prompt’ and ‘Anaconda PowerShell’ that you can use from the start menu.

