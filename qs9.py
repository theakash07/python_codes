#static program
date = (11, 12, 2014)#tuples cant be split using split() function.
f, s, t = date #data is a tule so data[0],data[1],data[2] value are assigned to respected variable basically we splitted it.
print(f"{f}/{s}/{t}")
print( "The examination will start from : %i / %i / %i"%date)
print(type(date))
