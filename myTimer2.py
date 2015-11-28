from datetime import datetime
import time


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

# Adds up log times and prints it out in total minutes

def add_total():
	print divider + "\n"
	log_name = raw_input("Please enter in the name of log file: ")
	add_log = open(log_name, "r")
	time_list = add_log.readlines()
	add_log.close()

	total_minutes = 0
	for i in time_list:
		hours = int(i[0]) * 60
		minutes = int(i[2:4])
		seconds = float(i[5:7]) / 60
		total_minutes += hours + minutes + seconds

	print  ("%.2f minutes total" % total_minutes)
	
# Start of program

# Asks user if timer should start
response_1 = raw_input("Start timer now?").lower()
divider = "-" * 80
while (response_1 == "yes" or response_1 == "y"):
	start_timer()
	stop_timer()
	response_1 = raw_input("Would you like to run timer again?").lower()

# Asks user if they would like a log file totaled
response_2 = raw_input("Would you like to get a sum total of a file?").lower()
while (response_2 == "yes" or response_2 == "y"):
	add_total()
	response_2 = raw_input("Would you like to get a sum total of a file?").lower()

# End of program
print divider + "\n"
print "Alright, goodbye\n"
print divider + "\n"
	

