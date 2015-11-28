from datetime import datetime
import time


response_1 = raw_input("Start timer now?").lower()
divider = "-" * 80


# starts timer
def start_timer():

	global start_time
	start_time = datetime.now().replace(microsecond = 0)
	
	print divider + "\n"
	print("Timer is starting at %s\n\n" % (time.strftime("%H:%M:%S")))
	raw_input("Press Enter to stop timer.")


""" stops timer, displays timer duration, and exports duration to file labeled 
with the current date in dd_mm_yy format """

def stop_timer():
	
	stop_time = datetime.now().replace(microsecond = 0)
	total_time_duration = str(stop_time - start_time)
	total_time_duration = total_time_duration
	print "\n" + divider + "\n"
	print "HH:MM:SS : " + total_time_duration

	log_name = ((time.strftime("%d_%m_%y")) + ".log")
	update_log = open(log_name , "a")
	update_log.write(total_time_duration + "\n")

	update_log.close()

	

while (response_1 == "yes" or response_1 == "y"):
	start_timer()
	stop_timer()
	response_1 = raw_input("Would you like to run timer again?").lower()

print divider + "\n"

print "Alright, goodbye\n"
	

