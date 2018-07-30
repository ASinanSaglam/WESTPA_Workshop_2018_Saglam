2018 WESTPA Workshop tutorial by Ali Sinan Saglam, uses WESTPA and BioNetGen

This is a mostly self-contained tutorial to run BNG simulations coupled with WESTPA and some example analysis that can be done.

Instructions: 
* There are two options to run this tutorial, you can either build the dependencies yourself or try out building a [docker](https://www.docker.com/) image from the Dockerfile provided in this tutorial, under docker folder. 
  * To build the image in linux just copy the Dockerfile to a folder and do ```docker build -t=westpa_wshop```. 
  * Once the image is built you can start an interactive session with ```docker run -it westpa_wshop```.
  * In the interactive session do ```cd /home/test/westpa``` and run ```./setup.sh```.
  * Once the installation is done do ```cd lib/examples/WESTPA_Workshop_2018_Saglam``` and follow step 5 to run the simulation. 
* If you want to build the dependencies you will need:
  * [Anaconda python distribution](https://www.anaconda.com/download/)
  * [WESTPA](https://github.com/westpa/westpa)
  * [PyEMMA](http://emma-project.org/latest/INSTALL.html)
  * [BioNetGen](https://www.csb.pitt.edu/Faculty/Faeder/?page_id=409). A statically compiled binary is included in this tutorial.
  
I suggest using the following instructions (especially for Linux) for acquiring and installing dependencies: 

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

4. Once the setup is complete, navigate to the examples folder and clone the tutorial:
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
where X is the number of cores you want WESTPA to use. This took about 15 minutes on 4 cores for me on a Xeon @3.5GHz. Some of the analysis will expect 100 iterations, you might have to adjust the notebook if you run less and decide to use your own data. The analysis/pre-prepped_results folder contains all the files you will need for analysis in case something goes wrong with the simulation or if you just want to see the analysis.

Optional note for 2018 workshop attendees: If you are coming to the 2018 WESTPA workshop and interested in systems biology, you will have temporary access to the [H2P cluster](https://crc.pitt.edu/h2p) for the workshop simulations. You can follow almost the same instructions up to this point in the cluster. To run the simulation, just edit env.sh to uncomment the two variable definitions SCRATCH and make sure WEST_PYTHON points directly to the Anaconda python you installed. Once that is done you can simply submit the job with ```sbatch run_H2P.sh``` to run the simulation on a single node with 48 cores. For non-attendees this is also a sample submittion script for single node jobs. Note, to make use of multi-node simulations, you will have to use other work managers. Please visit [the WESTPA wiki](https://github.com/westpa/westpa/wiki/Running-WESTPA-in-a-multi-node-environment) for more information. 

6. Once the simulation is complete, navigate to the analysis folder and run all of the analysis on either the master h5 file you generated (../west.h5) or the pre-calculated one I provide (pre-prepped_results/west.h5)
```
cd analysis
./run_all_analysis.sh ../west.h5
```

7. Finally, you can take a look at the Jupyter notebook that goes with this tutorial by running the following when you are in the analysis folder:
```
jupyter notebook
```
Jupyter comes with Anaconda python so you don't need to install it. Once you have the notebook running on a browser and you are on the file navigator screen, open analysis.ipynb to access the analysis notebook.
