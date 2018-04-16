#!/bin/sh


# This scripts can only be runned from this folder --->/home/patrick/omnetpp-5.2/samples/simulationsPaper

#sudo nohup sh rm_maintence.sh &

U="Cmdenv" # executions enviroment
F="simulations/omnetpp.ini" #simulations .ini location folder

#simulation from the omnetpp.ini to run
C1="WirelessUDP"
C2="WirelessTCP"
C3="WirelessDASH"

N=".:src:/home/patrick/omnetpp-5.2/samples/inet/src/:/home/patrick/omnetpp-5.2/samples/inet/examples:/home/patrick/omnetpp-5.2/samples/inet/tutorials" #imports to run the simulation
L="/home/patrick/omnetpp-5.2/samples/inet/src/INET" #path of the shared libraries
R="'$numHosts>0'" #param of the execution if -r is used

./src/simulationsPaper -m -u $U -f $F -c $C1 -n $N -l $L
./src/simulationsPaper -m -u $U -f $F -c $C2 -n $N -l $L
./src/simulationsPaper -m -u $U -f $F -c $C3 -n $N -l $L


find /home/patrick/omnetpp-5.2/samples/simulationsPaper/simulations/results -iregex ".*\.sca.*" -exec cp {} /home/patrick/omnetpp-5.2/samples/simulationsPaper/sca_source \;

cd simulations/results/

rm -rf Wireless*

cd ..

cd ..