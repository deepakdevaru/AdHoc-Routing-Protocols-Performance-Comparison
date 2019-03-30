# AdHoc-Routing-Protocols-Performance-Comparison
Wireless and Mobile Networking Course Project 

The code is used to run the simulation and provide 4 different types of outputs:
1) A .routes file containing routing tables of each nodes,
2) A .tr file containing all transmissions and receptions on the network, 
3) A .csv file containing a summary of successful transmitted packets

We want to be able to see how many packet are successfully received.
This information was obtained from the .csv file. We wrote a Python code that parses the .csv file to calculate the total number of packets received during the simulationa and we named it parser.py.

We used IPTracer.tr file to and parsed it for different protocols (AODV,DSDV,DSR) using python scripts (delay.py) and calculated the max delay and average for each type of protocols

We then performed performance analysis on the nodes on:
  1. Effect of mobility on nodes with pause time as 1 sec
  2. Effect on performance (Average Delay, Max Delay and Total packet received)  when number of nodes are increased and mobility introduced.
  
Performace is evaluated and compared

Excecution Environment :
C++
Ununtu 14
ns3.25
python 3
