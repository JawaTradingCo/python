import datetime
import sys, getopt
import string

def calculate_age(argv):
    for arg in argv:
        d = arg.split("-",2)

    today = datetime.date.today()
   
 
    born = datetime.date(int(d[0]),int(d[1]),int(d[2]))
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

if __name__ == "__main__":
   age = calculate_age(sys.argv[1:])
   print(age)
