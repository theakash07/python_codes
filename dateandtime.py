#python program to find version of python uing sys module of python
import datetime
print("Current date and time :")

time=datetime.now()
#strftime function is used to format the date and time it comes along with datetime moudlue only used to fomrat date and time
print(time.strftime("%Y-%M-%D  %H-%M-%S"))
