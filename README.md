2018 WESTPA Workshop tutorial by Ali Sinan Saglam, uses WESTPA and BioNetGen

This is a mostly self-contained tutorial to run BNG simulations coupled with WESTPA and some example analysis that can be done.

Instructions: 
* For this tutorial you will need:
  * [Anaconda python distribution](https://www.anaconda.com/download/)
  * [WESTPA](https://github.com/westpa/westpa)
  * [PyEMMA](http://emma-project.org/latest/INSTALL.html)
  * [BioNetGen](https://www.csb.pitt.edu/Faculty/Faeder/?page_id=409). A statically compiled binary is included in this tutorial.
* Once you have the requirements installed, clone this repo under westpa/lib/examples folder
* If you have WESTPA installed correctly (e.g. ran setup.sh) the example should run after ./init.sh and ./run.sh
  * You should specify the number of cores you want the example to use with ./run.sh --n-workers X, where X is the number of cores you want used. 
* Once the simulation is done you can go to the analysis folder and run all analysis for this tutorial with ./run_all_analysis.sh
* Additionally you can go to do the analysis folder and start a jupyter notebook in that folder for the analysis tutorial as well.
