months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
x=0
for i in months:
	try:
		open(f'./data/{i}.csv','x')
	except:
		x=1
	if x==1:	
		raise FileExistsError('the month csv files already exist')