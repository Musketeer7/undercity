def test1(st):
	print("inside test " + st)
	f = open("text.txt", "a")
	print(f)
	f.write("Now the file has more content! " + st)
	f.close()
	print("inside test1 func")

print("inside test")
test1("a")
