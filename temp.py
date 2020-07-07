hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40 :
		x = r*h
		y = (h-40.0) * (r*0.5)
		print(x+y)
else :
	print(h*r)
print("new change in dev branch")
