class showing_months():
	def reset_date():
		global month
		global year
		from time import time,ctime
		month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'].index(ctime(time()).split()[1].lower())+1
		year=int(ctime(time()).split()[4])
		del time,ctime
	def next_month():
		global month
		global year
		if month==12:
			year+=1
			month=1
		else:
			month+=1
	def previous_month():
		global month
		global year
		if month==1:
			year-=1
			month=12
		else:
			month-=1
	def show_month():
		from calendar import prmonth
		prmonth(year,month)
		del prmonth
	def current_year_month():
		result=[]
		result.append(year)
		result.append(month)
		return result
	def days():
		from calendar import monthrange
		result=monthrange(year,month)[1]
		del monthrange
		return result
class event_handling(): 
	def show_day(year:int,month:int,day:int)->list:
		result=[['22','feed cat','10:45']]
		months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
		mon=months[month-1]
		from Basics import file_handling as f
		data=f.read_csv(f'data/{mon}.csv')
		del f
		final=[]
		for i in data:
			try:
				if int(i[0])==day:
					final.append(i)
			except:
				pass
		return final
	def add_event(year,month,day,event,time)->bool:
		months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
		mon=months[month-1]
		file_name=f'data/{mon}.csv'
		data=[day,event,time]
		from Basics import file_handling as f
		data=f.append_row_csv(file_name,data)
		del f
		return data
	def remove_event(year,month,day,time)->bool:
		months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
		mon=months[month-1]
		file_name=f'data/{mon}.csv'
		from Basics import file_handling as f
		data=f.read_file(file_name)
		del f
		data=data.split('\n')
		events=[]
		for i in data:
			events.append(i.split(','))
		events.pop()
		to_remove=None
		for i in events:
			try:
				i.index(time)
				if i[0]==str(day):
					to_remove=events.index(i)
			except:
				pass
		try:
			events.pop(to_remove)
		except:
			return False
		from Basics import file_handling as f
		f.delete_file(file_name)
		f.create_file(file_name)
		for i in events:
			f.append_row_csv(file_name,i)
		return True

if __name__=='__main__':
	showing_months.reset_date()
	while True:
		showing_months.show_month()
		userin=input('')
		if userin.upper()=='N':
			showing_months.next_month()
		elif userin.upper()=='P':
			showing_months.previous_month()
		elif userin.isnumeric() and int(userin) <= showing_months.days():
			day=int(userin)
			for i in event_handling.show_day(year,month,day):
				print(f'{i[1]}, at {i[2]}')
			userin=input('would you like to [A]dd event,[R]emove event,or e[X]it: ')
			if userin.upper()=='A':
				userin_event=input('what event: ' )
				userin_time=input('at what time: ')
				event_handling.add_event(year,month,day,userin_event,userin_time)
			elif userin.upper()=='R':
				userin_time=input('time: ')
				event_handling.remove_event(year,month,day,userin_time)
			else:
				pass
			