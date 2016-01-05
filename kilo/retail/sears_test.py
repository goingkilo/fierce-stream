import sears

print 100*'--'
a = sears.get('laptop')

for i in a:
	for j in i.keys():
		print j,':',i[j]
	print ' '


print 100*'--'
b = sears.get_cells(a)
for i in b:
	print i


print 100*'--'
c  = sears.make_rows(b)

for i in c:
	print i

print 100*'==='
