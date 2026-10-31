class file_handling():
	def create_file(file_name:str)-> bool:
		try:
			with open(file_name,'x'):
				pass
			return True
		except:
			return False
	def read_file(file_name:str)->str:
		try:
			with open(file_name,'r') as f:
				contents=f.read()
			return contents
		except:
			return False
	def append_file(file_name:str,text: str)->bool:
		try:
			with open(file_name,'a') as f:
				f.write(text)
			return True
		except:
			return False
	def write_file(file_name:str,text: str)->bool:
		try:
			with open(file_name,'w') as f:
				f.write(text)
			return True
		except:
			return False
	def delete_file(file_name:str)->bool:
		from os import remove
		try:
			remove(file_name)
			return True
		except:
			return False
	def read_csv(file_name:str)->list:
		data=file_handling.read_file(file_name)
		data=data.split('\n')
		data.pop(len(data)-1)
		result=[]
		for i in data:
			result.append(i.split(','))
		return result
	def append_row_csv(file_name:str,text:list)->bool:
		try:
			data=file_handling.read_csv(file_name)
			row=len(data)+1
			for i in text:
				file_handling.append_file(file_name,f'{i},')
			file_handling.append_file(file_name,f'\n')
			return True
		except:
			False
if __name__=='__main__':
	mode=1
	if mode==0:
		file_name='results.txt'
		print(file_handling.read_file(file_name))
		file_handling.append_file(file_name,'hello')
		print(file_handling.read_file(file_name))
		file_handling.write_file(file_name,'override ')
		print(file_handling.read_file(file_name))
	if mode == 1:
		file_name='data/oct.csv'
		file_handling.append_row_csv(file_name,['thing','thing 2','thing 3','thing 4'])