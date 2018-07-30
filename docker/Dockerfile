FROM continuumio/anaconda
MAINTAINER Ali Sinan Saglam

# Get GCC
#RUN apt-get install -y gcc
RUN apt-get install -y g++
# Get PyEmma
RUN pip install pyemma
# Install WESTPA 
RUN mkdir /home/test/
RUN git clone https://github.com/westpa/westpa.git
RUN mv westpa /home/test/.
# Install workshop tutorial
RUN git clone https://github.com/ASinanSaglam/WESTPA_Workshop_2018_Saglam.git
RUN mv WESTPA_Workshop_2018_Saglam /home/test/westpa/lib/examples
RUN cd /home/test/westpa/lib/examples/WESTPA_Workshop_2018_Saglam
