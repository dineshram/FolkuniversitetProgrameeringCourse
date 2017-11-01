# create an empty address book dictionary
addressBook = {}
# read entries till an empty string
name = input("Type the Name - leave blank to finish ")
while name != "":
   entry = input("Type the Street, Town, Phone. Leave blank to finish ")
   addressBook[name] = entry
   name = input("Type the Name - leave blank to finish ")
# now ask for one to display
name = input("Which name to display?(blank to finish)")
while name != "":
   print (name, addressBook[name])
   name = input("Which name to display?(blank to finish) ")
