from stupidArtnet import StupidArtnet
import time
import random

# THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
target_ip = '192.168.1.80'		# typically in 2.x or 10.x range
universe = 0 										# see docs
packet_size = 100								# it is not necessary to send whole universe

# CREATING A STUPID ARTNET OBJECT
# SETUP NEEDS A FEW ELEMENTS
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
# ISBROADCAST = DEFAULT FALSE
a = StupidArtnet(target_ip, universe, packet_size, 30, True, False)

# MORE ADVANCED CAN BE SET WITH SETTERS IF NEEDED
# NET         = DEFAULT 0
# SUBNET      = DEFAULT 0

print(a)

packet = bytearray(packet_size)		# create packet for Artnet
#for i in range(packet_size):			# fill packet with sequential values
    #packet[i] = (i % 256)

# ... AND SET IT TO STUPID ARTNET
a.set(packet)						# only on changes

# ALL PACKETS ARE SAVED IN THE CLASS, YOU CAN CHANGE SINGLE VALUES
#a.set_single_value(1, 100)			# set channel 2 to 255 (10secs 50 range) ( 5secs time.sleep(1) )
#a.set_single_value(1, 2)			# set channel 1 to 2 (20secs 100 range) (10secs 50 range)

# ... AND SEND
a.show()


# OR USE STUPIDARTNET FUNCTIONS
#a.flash_all()						# send single packet with all channels at 255

#a.blackout()						# send single packet with all channels at 0
#a.see_buffer()

#time.sleep(1)						# wait a bit, 1 sec

# TO SEND PERSISTENT SIGNAL YOU CAN START THE THREAD
a.start()

# AND MODIFY THE DATA AS YOU GO
for x in range(200):
	for i in range(packet_size):	# Fill buffer with random stuff
		packet[i] = 50
	a.set(packet)
	time.sleep(.1)
 
# SOME DEVICES WOULD HOLD LAST DATA, TURN ALL OFF WHEN DONE

a.blackout()

# ... REMEMBER TO CLOSE THE THREAD ONCE YOU ARE DONE
a.stop()
 
