# Experiment-Workflow: Introduction
This repository is a basic, example experiment which intends to replicate my workflow when it comes to creating reproducable reports. The current backbone of my work is Quarto, which is a very useful publishing system that works with python, julia and R. It basically lets you convert your jupyter notebook/R markdown code into multiple formats. Here are a few:
- Interactive html file
- Latex pdf
- Latex beamer slidehow
- docx word document
- ppt Microsoft powerpoint slideshow.

Among others!

What drew me to quarto is that it has the potential to dynamically generate experimental reports, where the figures are created directly from your results, and inline coding lets you automatically change parameter values based upon the experiment you are interested in presenting.

The intention of this repository is to demonstrate a completely reproducable experiment, which I hope you can get some ideas from and perhaps even innovate upon. 

As you may have noticed, my example is completely in python. But, a lot of the basic concepts covered in this repository apply to R. It seems that Quarto is  a lot more suited for R in general, so there may be things you can do in R with Quarto that you can't do in python. I have found that the [quarto guide][https://quarto.org/docs/guide/] has been an invaluable resource in making this. quarot might be quite niche, so I have found that LLMs haven't given me very useful answers, or I have had to heavily modify the ones they have with info from the guide. Maybe it's a skill issue on my part?

## Installing Quarto

Quarto is not a package, and so it must be installed into your system directly. The installation files can be found [here][https://quarto.org/docs/get-started/].

I will run over a basic installation tutorial for your virtual machine, which is highly recommended. You can install quarto on windows too, but I haven't done that yet. Let me know if you have done it and it works. 

First, head to the link provided above and install a file whick looks something like this:
```
quarto-1.9.37-linux-amd64.deb

```
Then, head over to your downloads folder and open up your terminal. You can do this by right clicking, then in the context menu select `Open in Terminal`. Alternatively, you can open the terminal and 'cd' into the downloads folder. Once there, run the 'debian package get' command `dpkg` with the `-i` flag and the filename as a super user:
```
sudo dpkg -i quarto-1.9.37-linux-amd64.deb
```
# The Experiment

The experiment example is quite trival, it's not really an experiment at all! All it does is sample noisy observations from a test function (that you can change) from $k$ equally spaced locations. The noise is Gaussian $\epsilon \sim N(0,\tau)$, and $\tau$ can be changed. The experimental parameters are

| Parameter | Range | Descp
| -------- | ------- | ------- |
| $k$ | Integer $>0$ | Number of equally spaced locations |
| $\tau$ | Float $>0$ | Scale of the Gaussian noise on observations |
| function_id | $\{0,1\}$ | Function id from `test_utils.py`. There are only two. |
| seed | Integer $>0$ | RNG seed |

The generated report displays the config's parameters, the test function equation and the results plotted against truth.

## Initialisation
Before you do anything, you need to initialise the python environment that's been prepared for the experiment. The script `python-setup` handles all of this. First you make it executable, then run it.

```
chmod +x python_setup
source ./python_setup

```
The important packages it installs are listed:
- argparse
- numpy
- matplotlib
- PyYAML
- jupyter
- pathlib
- papermill - used to pass arguments to notebooks/qmd files. Allows for dynamic generation or reports

## Execution

You need to run the experiment to generate its results. To do this choose a config within the `configs` directory and pass its name as an argument to the `run_experiment.sh` script. I have prepared one called `pilot_01`. The code to run it is below
```
./run_experiment.sh pilot_01
```
Don't worry about specifying the directory or the file type suffix, there is code in the script to handle it. Open up the script in whatever text editor you use to see what is happening. 

The results will be deposited in the directory of the same name, which will have automatically been generated. 

## Report Generation

Now you have the results you can generate the report, but don't expect much, I haven't spent much time on it. There is also a script to do generate the report.
```
./generate_report.sh pilot_01
```
The results will be sent to the `pilot_01/report`. 