import datetime
import sys, getopt
import re

# usage: age.py yyyy-mm-dd
# example: age.py 1972-05-07

def calculate_age(age):
	d = age.split("-",2)
	if re.findall(r"\b([0-9]{4})(-)([0-9]{2})(-)([0-9]{2})\b",age):
		today = datetime.date.today()
		born = datetime.date(int(d[0]),int(d[1]),int(d[2]))
		age =  today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		print str(age) + " years old"
	else:
		print "Improper format"
		return
		
if __name__ == "__main__":
	age = raw_input("Enter a date [yyyy-mm-dd]: ")
	age = calculate_age(age)
	
