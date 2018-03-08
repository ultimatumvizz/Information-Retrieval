from Tkinter import *
#from Tkinter import ttk
import glob
import os
import searchFunction

def inputQuery(event):
    stringSearch = entry.get()
    ##### text = FUNCTION
    res.configure(text = "Results: " + stringSearch )
    searchOuput(stringSearch)


def searchOuput(string):
	found_files = []
	LOCATION = "/home/ultimatum/Downloads"

	for root, dirs, files in os.walk(LOCATION):
		for file in files:
		    if file.endswith(".txt"):
		    	found_files.append((os.path.join(root,file)))

		    	print(os.path.join(root, file))
	root = Tk()
	root.geometry( "640x480" );
	listbox = Listbox(root)

	for a_file in found_files:
	    listbox.insert(END, a_file)
	    string = str(searchFunction.searchResults())
	    listbox.insert(END,string)
	    listbox.insert(END," ")

	listbox.pack(fill=BOTH, expand=YES)

	root.mainloop()

	"""
	for dirname, dirnames, filenames in os.walk(LOCATION):
    for i in glob.glob(dirname+'/'+search+'*'):
        print(i)
        found_files.append(i)
"""


w = Tk()
w.geometry( "640x480" );
Label(w, text="Enter your Search Query:").pack()
entry = Entry(w)
entry.bind("<Return>", inputQuery)
entry.pack()
res = Label(w)
res.pack()

w.mainloop()