FROM continuumio/anaconda

WORKDIR /home/test
# Get GCC
RUN apt-get install -y g++
# Get PyEmma
RUN pip install pyemma
# Install WESTPA 
RUN git clone https://github.com/westpa/westpa.git
# Install workshop tutorial
RUN git clone https://github.com/ASinanSaglam/WESTPA_Workshop_2018_Saglam.git
RUN mv WESTPA_Workshop_2018_Saglam /home/test/westpa/lib/examples
EXPOSE 8888

WORKDIR /home/test/westpa
RUN /home/test/westpa/setup.sh
WORKDIR /home/test/westpa/lib/examples/WESTPA_Workshop_2018_Saglam
