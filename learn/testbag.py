
from arraybag import ArrayBag
from arraysortedbag import ArraySortedBag
from linkbag import LinkBag

def test(bagType):
	lyst=[2013,61,1973,999,456,78,932,399,21,146,2000,1983]
	print("The items of lyst is: \033[1;34;40m%s\033[0m" % lyst)
	b1=bagType(lyst)
	print("len(b1): Expect // \033[1;34;40m12\033[0m // \033[1;34;40m%d\033[0m" %len(b1))
	print("mem alloced for b1: Expect // \033[1;34;40m20\033[0m // \033[1;34;40m%d\033[0m" % b1.mem())
	print("Expect the b1 bag's string: \033[1;34;40m%s\033[0m" % b1)
	print("--------------------------------")
	print("remove first 7 items in b1:")
	for i in range(7):
		b1.remove(b1._items[0])
	print("Expect the bag's string:",b1)
	print("len(b1): Expect // 5 //",len(b1))
	print("mem alloced for b1: Expect // 10 //",b1.mem())
	print("--------------------------------")
	print("21 in b1: Expect // True //",21 in b1)
	print("2012 in b1: Expect // False //",2012 in b1)
	print("Expect the items by tab:")
	for item in b1:
		print(item,end="\t")
	print()
	b1.clear()
	print("b1.clear(): Expect // {} //",b1)
	b1.add(25)
	b1.remove(25)
	print("b1.add(25), b1.remove(25): Expect // {} //",b1)
	b1=bagType(lyst)
	b2=bagType(b1)
	print("b1=bagType(lyst), b2=bagType(b1), b1==b2: Expect // True //",b1==b2)
	print("b1 is b2: Expect // False //",b1 is b2)
	for item in lyst:
		b1.remove(item)
	print("b1.remove the items in lyst: Expect // {} //",b1)
	print("b2.remove(99): Expect crash with KeyError:")
	b2.remove(99)

if None:
	print("yeah")
b3=ArrayBag()
b3.add(3)
b3.add(5)
b3Iter=iter(b3)
print(b3Iter)
b3b=next(b3Iter)
b3b=next(b3Iter)
print(b3Iter)
print(b3b)

#test(LinkBag)
test(ArrayBag)
#test(ArraySortedBag)
	
