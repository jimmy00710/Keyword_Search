import os
import json
from whoosh.lang.morph_en import variations
from tkinter import *

file_list = []
key_list = []



root = Tk()
data = 0

T1 = Text(root, height=2, width=30)
label1 = Label( root, text="Enter Word to Search")
E1 = Entry(root, bd =5)
data_positions = []
def getDate():
	
	# data_positions = []
	data = E1.get()
	for file in os.listdir("/home/swaraj/Desktop/keyword_Search"):
		if file.endswith(".txt"):
			# print(file)
			
			# line_list = []
		
			# print(file)
			fo = open(file,'r')
			line = fo.read()

			if data in line:
				# print('##',keyword)
				lines = line.splitlines()
				# print('###### ', lines)
				# print os.path
				no_of_lines = len(lines)
				for i in range(no_of_lines):
					select_line = lines[i].split()
					if data in select_line:
						data_positions.append([file,i+1,select_line.index(data)+1])
					enum = list(enumerate(select_line,1))
	
	if(len(data_positions) !=0):
		T1 = Text(root, height=2, width=30)
		T1.pack()
		T1.insert(END, "The word was found in the following locations")
		for d in data_positions:
			T2 = Text(root, height=2, width=30)
			T2.pack()
			T2.insert(END,  'File:   ' + str(d[0]))

			T3 = Text(root, height=2, width=30)
			T3.pack()
			T3.insert(END, 'line no:' + str(d[1]))


			T4 = Text(root, height=2, width=30)
			T4.pack()
			T4.insert(END, 'column  ' + str(d[2]))


			# print('file name:', d[0])
			# print('line:     ', d[1])
			# print('column:   ',d[2])
		
	else:
		T = Text(root, height=2, width=30)
		T.pack()
		T.insert(END,  "word not found anywhere")
		
	data = E1.get()
	print (E1.get())
# frame2, text="Forget only frame2", ).pack()

submit = Button(root, text ="Submit", command = getDate)
reset = Button(root, text="Reset", command =T1.update()).pack()
# print(data)
# start.grid_forget()
label1.pack()
E1.pack()

submit.pack(side =BOTTOM)
# reset.pack(side=BOTTOM)
# T.delete('1.0', END)

root.mainloop()