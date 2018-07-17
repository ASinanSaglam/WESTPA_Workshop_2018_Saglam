2018 WESTPA Workshop tutorial by Ali Sinan Saglam, uses WESTPA and BioNetGen

This is a mostly self-contained tutorial to run BNG simulations coupled with WESTPA and some example analysis that can be done.

Instructions: 
* For this tutorial you will need:
  * [Anaconda python distribution](https://www.anaconda.com/download/)
  * [WESTPA](https://github.com/westpa/westpa)
  * [PyEMMA](http://emma-project.org/latest/INSTALL.html)
  * [BioNetGen](https://www.csb.pitt.edu/Faculty/Faeder/?page_id=409). A statically compiled binary is included in this tutorial.
  
I suggest using the following instructions for acquiring and installing dependencies: 

1. Install Anaconda python using (link is for linux, 64bit version):
```
wget https://repo.anaconda.com/archive/Anaconda2-5.2.0-Linux-x86_64.sh
chmod u+x Anaconda2-5.2.0-Linux-x86_64.sh
./Anaconda2-5.2.0-Linux-x86_64.sh
```
The last command will ask you where you want Anaconda python installed it will also ask if you want to make it the default python (I suggest doing so if you don't use another python). 

2. You then want to use "pip" command that comes with Anaconda python (specifically the one you just installed) to install PyEmma with:
```
pip install pyemma
```
If you are not sure if you are using the right pip you can try doing
```
which pip
```
to see if it points to the anaconda python 2.7 you installed.

3. Once both are installed, you want to clone and install WESTPA:
```
git clone https://github.com/westpa/westpa.git
cd westpa
./setup.sh
```
Before running setup.sh, I suggest checking to make sure you have the right python with
```
which python
```
and make sure it points to the anaconda python 2.7 you installed.

4. Once the setup completes, navigate to the examples folder and clone the tutorial:
```
cd lib/examples
git clone https://github.com/ASinanSaglam/WESTPA_Workshop_2018_Saglam.git
cd WESTPA_Workshop_2018_Saglam
```

5. Now the simulation is ready! By default the number of iterations is set to 100 which can be changed by editing "west.cfg" file. You can run the simulation with:
```
./init.sh
./run.sh --n-workers X
```
where X is the number of cores you want used. This took about 10-15 minutes on 4 cores for me. Some of the analysis will expect 100 iterations. The analysis/pre-prepped_results folder contains all the files you will need for analysis in case something goes wrong with the simulation or if you just want to see the analysis.

6. Once the simulation is complete, navigate to the analysis folder and run all of the analysis on either the master h5 file you generated (../west.h5) or the pre-calculated one I provide (pre-prepped_results/west.h5)
```
cd analysis
./run_all_analysis.sh ../west.h5
```
This should all run without issues if you have 100 iterations or pointed to the h5 file I provided. 

7. Finally, you can take a look at the Jupyter notebook that goes with this tutorial by running the following:
```
jupyter notebook
```
Jupyter comes with Anaconda python and this should just run. Once you open up the file navigator, just open analysis.ipynb. 
