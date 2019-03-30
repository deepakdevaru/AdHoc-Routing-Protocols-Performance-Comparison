import sys

#attribute to filename

name= 'IP_Trace.tr'

#open file name to read
with open(name) as f:

    #read each line and store as a list
    linecontents = f.readlines()

#remove white spaces from each list and iterate for all linecontents, create a list of each line withoit spaces
linecontents = [s.strip() for s in linecontents]


#to compute average delay
#initilaise count, sum, maxDelay and dict
count= 0
sum=0
maxDelay = 0
dict = {}


for i in range(0,len(linecontents)):
    linestr=linecontents[i]

    #split each items of a list after a space and append it to new list words
    words=linestr.split(' ')


    #since only packets with payload is requred for calculating the average time and the
    #max time a packet takes to be sent and received

    #checking for packets with only payload : Search for keyword "Payload".
                                            #Payload is at 32
                                            #and number of words should be more than 32

    if(len(words) > 32 and words[32] == "Payload"):

        #packet tracer contains two operation r for receiving (Rx) and t for transmitting(Tx)
        #check if t for 1st transmission

        if words[0] == 't':

            #get node (src) id : nodeid is present at position words[2] -" /NodeList/17/$ns3::Ipv4L3Protocol/Tx(1)"
            #splitting "/NodeList/17/$ns3::Ipv4L3Protocol/Tx(1)" at '/' to get node list

            temp= words[2].split('/')
            origin_nodeID=int(temp[2])  #extract node id , for eg : 17

            #get source ip: source ip is present in ipheader at positon words[23] and destination address at words[25]
            src_ip= words[23]
            temp1= src_ip.split('.')
            originating_nodeID= int(temp1[3])-1

            if origin_nodeID != originating_nodeID:
                continue

            dest_ip = words[25]
            temp1=dest_ip.split('.')
            destined_nodeID=int(temp1[3][:-1])-1

	    
	    id = words[13]



            #only push to disctionary the first time
            if(origin_nodeID,destined_nodeID) not in dict:
                dict[(origin_nodeID,destined_nodeID,id)]= float(words[1])


        #check if 'r'
        elif words[0] == 'r':
            temp = words[2].split('/')
            dest_nodeID =int(temp[2])

            src_ip = words[23]
            temp1 = src_ip.split('.')
            originating_nodeID = int(temp1[3]) - 1



            if destined_nodeID !=dest_nodeID:
                continue
                
                
            dest_ip = words[25]
            temp1 = dest_ip.split('.')
            destined_nodeID = int(temp1[3][:-1]) - 1
            
	    id = words[13]

            #get destination time
            destTime = float(words[1])
            if (originating_nodeID,dest_nodeID,id) in dict:
                originTime= dict[(originating_nodeID,dest_nodeID,id)]

                count +=1
                delay= destTime-originTime
                sum += delay
                maxDelay = max(delay,maxDelay)


#if(count > 0):

print(count)
print("Average delay between transmission and receiving is: " , (sum/count))
print("Max delay between transmission and receiving is: ", (maxDelay))

#else:
    #print("no values found")








