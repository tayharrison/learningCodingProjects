#Create the list of epic programmers'
epic_programmer_list=["Tim Berners-Lee",
                       "Guido van Rossum",
                       "Linus Torvalds",
                       "Larry Page",
                       "Sergey Brin",]
#print to console
print "An epic programmer: " + epic_programmer_list[0]
print "An epic programmer: " + epic_programmer_list[1]
print "An epic programmer: " + epic_programmer_list[2]
print "An epic programmer: " + epic_programmer_list[3]
print "An epic programmer: " + epic_programmer_list[4]

epic_programmer_list[4] = "Sergey Brin"
print epic_programmer_list

#Add myself to the end of the list
epic_programmer_list.append("Me")

#Add this line to show myself in the console
print "An epic programmer: "+ epic_programmer_list[5]

#Looping through each item in epic_programmer_list
for programmer in epic_programmer_list:
    #Print the programmers'name to console
    print "An epic programmer: " + programmer
    
