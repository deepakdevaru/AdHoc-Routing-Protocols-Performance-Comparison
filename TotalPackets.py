fname = "Project2Results.csv"

packetReceived = 0

with open(fname) as f:
    content = f.readlines()

for i in content:
	packetInfo = i.split(",")
	#print packetInfo
	
	if packetInfo[2] == "PacketsReceived":
		continue
	
	packetCount = int(packetInfo[2])

	packetReceived += packetCount

print "Total Packets Received: " + str(packetReceived)