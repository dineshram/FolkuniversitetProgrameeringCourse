# create an empty address book dictionary
addressBook = {}

# read entries till an empty string
print 
name = raw_input("Type the Name - leave blank to finish")
while name != "":
   entry = raw_input("Type the Street, Town, Phone. Leave blank to finish")
   addressBook[name] = entry
   name = raw_input("Type the Name - leave blank to finish")

# now ask for one to display
name = raw_input("Which name to display?(blank to finish)")
while name != "":
   print name, addressBook[name]
   name = raw_input("Which name to display?(blank to finish)")
