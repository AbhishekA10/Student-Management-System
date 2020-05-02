import sqlite3
conn=sqlite3.connect('student.db')
cur=conn.cursor()

def view():
	s='SELECT * from stud ORDER BY rollno ASC'
	print("Roll no","\t Firstname","\t Lastname","\t Department\t","Mobile no","\t Email id")
	for row in cur.execute(s):
		print(row[0],"\t\t",str(row[1]),"\t",str(row[2]),"\t",str(row[3]),"\t",str(row[4]),"\t",str(row[5]))

def insert():
	loop=True
	while(loop):
		print("\nINSERT")
		a=int(input("Enter Roll no:"))
		b=input("Enter Firstname:")
		c=input("Enter Lastname:")
		d=input("Enter Department:")
		e=input("Enter Mobile no:")
		f=input("Enter Email id:")
		cur.execute('INSERT INTO stud(rollno,firstname,lastname,dept,mobileno,emailid) VALUES (?,?,?,?,?,?)',(a,b,c,d,e,f,))
		conn.commit()
		print("Record successfully inserted")
		a=input("Want to insert another record?(Y/N):")
		if a=='Y' or a=='y':
			loop=True
		else:
			loop=False

def search():
	loop=True
	while(loop):
		print("\nSEARCH")
		print("Search using?")
		print("1.Roll no")
		print("2.Firstname")
		print("3.Lastname")
		ch=int(input("Enter choice(1-3):"))
		if ch==1:
			a=input("Enter student's Roll no whose record is to be searched:")
			flag=0
			for s in cur.execute('SELECT * from stud WHERE rollno=?',(a,)):
				if s is not None:
					flag=1
			if flag==0:
				print("Record not found")
			else:
				print("Roll no","\t Firstname","\t Lastname","\t Department\t","Mobile no","\t Email id")
				for s in cur.execute('SELECT * from stud WHERE rollno=?',(a,)):
					print(s[0],"\t\t",str(s[1]),"\t",str(s[2]),"\t",str(s[3]),"\t",str(s[4]),"\t",str(s[5]))
		elif ch==2:
			a=input("Enter student's Firstname whose record is to be searched:")
			flag=0
			for s in cur.execute('SELECT * from stud WHERE firstname=?',(a,)):
				if s is not None:
					flag=1
			if flag==0:
				print("Record not found")
			else:
				print("Roll no","\t Firstname","\t Lastname","\t Department\t","Mobile no","\t Email id")
				for s in cur.execute('SELECT * from stud WHERE firstname=?',(a,)):
					print(s[0],"\t\t",str(s[1]),"\t",str(s[2]),"\t",str(s[3]),"\t",str(s[4]),"\t",str(s[5]))
		else:
			a=input("Enter student's Lastname whose record is to be searched:")
			flag=0
			for s in cur.execute('SELECT * from stud WHERE lastname=?',(a,)):
				if s is not None:
					flag=1
			if flag==0:
				print("Record not found")
			else:	
				print("Roll no","\t Firstname","\t Lastname","\t Department\t","Mobile no","\t Email id")
				for s in cur.execute('SELECT * from stud WHERE lastname=?',(a,)):
					print(s[0],"\t\t",str(s[1]),"\t",str(s[2]),"\t",str(s[3]),"\t",str(s[4]),"\t",str(s[5]))
		conn.commit()
		a=input("Want to search another record?(Y/N):")
		if a=='Y' or a=='y':
			loop=True
		else:
			loop=False

def modify():
	loop=True
	while(loop):
		print("\nMODIFY")
		a=input("Enter student's Firstname whose record is to be modified:")
		b=input("Enter student's Lastname whose record is to be modified:")
		f=0
		for s in cur.execute('SELECT * from stud WHERE firstname=? AND lastname=?',(a,b,)):
			if s is not None:
				f=1
				print("What to modify?")
				print("1.Roll no")
				print("2.Firstname")
				print("3.Lastname")
				print("4.Department")
				print("5.Mobile no")
				print("6.Email id")
				ch=int(input("Enter choice(1-6):"))		
				if ch==1:
					c=int(input("Enter new Roll no:"))
					flag=0
					for s in cur.execute('SELECT rollno from stud WHERE firstname=? AND lastname=?',(a,b,)):
						if s is not None:
							cur.execute('UPDATE stud SET rollno=? WHERE firstname=? AND lastname=?',(c,a,b,))
							flag=1
							print("Record successfully modified") 
					if flag==0:
						print("Record not found")
				elif ch==2:
					c=input("Enter new Firstname:")
					flag=0
					for s in cur.execute('SELECT firstname from stud WHERE firstname=? AND lastname=?',(a,b,)):
						if s is not None:
							cur.execute('UPDATE stud SET firstname=? WHERE firstname=? AND lastname=?',(c,a,b,))
							flag=1
							print("Record successfully modified") 
					if flag==0:
						print("Record not found")
				elif ch==3:
					c=input("Enter new Lastname:")
					flag=0
					for s in cur.execute('SELECT lastname from stud WHERE firstname=? AND lastname=?',(a,b,)):
						if s is not None:
							cur.execute('UPDATE stud SET lastname=? WHERE firstname=? AND lastname=?',(c,a,b,))
							flag=1
							print("Record successfully modified") 
					if flag==0:
						print("Record not found")
				elif ch==4:
					c=input("Enter new Department:")
					flag=0
					for s in cur.execute('SELECT dept from stud WHERE firstname=? AND lastname=?',(a,b,)):
						if s is not None:
							cur.execute('UPDATE stud SET dept=? WHERE firstname=? AND lastname=?',(c,a,b,))
							flag=1
							print("Record successfully modified") 
					if flag==0:
						print("Record not found")
				elif ch==5:
					c=input("Enter new Mobile no:")
					flag=0
					for s in cur.execute('SELECT mobileno from stud WHERE firstname=? AND lastname=?',(a,b,)):
						if s is not None:
							cur.execute('UPDATE stud SET mobileno=? WHERE firstname=? AND lastname=?',(c,a,b,))
							flag=1
							print("Record successfully modified") 
					if flag==0:
						print("Record not found")
				else:
					c=input("Enter new Email id:")
					flag=0
					for s in cur.execute('SELECT emailid from stud WHERE firstname=? AND lastname=?',(a,b,)):
						if s is not None:
							cur.execute('UPDATE stud SET emailid=? WHERE firstname=? AND lastname=?',(c,a,b,))
							flag=1
							print("Record successfully modified") 
					if flag==0:
						print("Record not found")
		if f==0:
			print("Record not found")
		conn.commit()
		a=input("Want to modify another record?(Y/N):")
		if a=='Y' or a=='y':
			loop=True
		else:
			loop=False

def delete():
	loop=True
	while(loop):
		print("\nDELETE")
		print("Delete using?")
		print("1.Roll no")
		print("2.Name")
		ch=int(input("Enter choice(1-2):"))
		if ch==1:
			a=input("Enter student's Roll no whose record is to be deleted:")
			flag=0
			for s in cur.execute('SELECT * from stud WHERE rollno=?',(a,)):
				if s is not None:
					cur.execute('DELETE from stud WHERE rollno=?',(a,))
					flag=1
					print("Record successfully deleted") 
			if flag==0:
				print("Record not found")
		else:
			a=input("Enter student's Firstname whose record is to be deleted:")
			b=input("Enter student's Lastname whose record is to be deleted:")
			flag=0
			for s in cur.execute('SELECT * from stud WHERE firstname=? AND lastname=?',(a,b,)):
				if s is not None:
					cur.execute('DELETE from stud WHERE firstname=? AND lastname=?',(a,b,))
					flag=1	
					print("Record successfully deleted") 		
			if flag==0:
				print("Record not found")
		conn.commit()
		a=input("Want to delete another record?(Y/N):")
		if a=='Y' or a=='y':
			loop=True
		else:
			loop=False

loop=True
while(loop):
	print("Student Management System")
	print("1.View")
	print("2.Insert")
	print("3.Search")
	print("4.Modify")
	print("5.Delete")
	print("6.Exit")
	choice=int(input("Enter choice(1-6):"))
	if choice==1:
		view()
	elif choice==2:
		insert()
	elif choice==3:
		search()
	elif choice==4:
		modify()
	elif choice==5:
		delete()
	else:
		break
	a=input("Want to perform other operations?(Y/N):")
	if a=='Y' or a=='y':
		print("\n")
		loop=True
	else:
		loop=False