from datetime import datetime
import time

answer = raw_input("Start timer now?").lower()


if (answer == "yes" or answer == "y"):

	start_time = datetime.now()
	divider = "-" * 80
	print divider + "\n"
	print("Timer is starting at %s\n\n" % (time.strftime("%H:%M:%S")))
	raw_input("Press Enter to stop timer.")

	stop_time = datetime.now()
	total_time_duration = stop_time - start_time
	print "\n" + divider + "\n"
	print total_time_duration


	


else:
	print "Alright, goodbye"
	print answer

