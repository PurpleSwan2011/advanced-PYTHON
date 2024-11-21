file = open("Sample.txt3","a")
file.write("My Favourite Subject is Biology")
file.close()

file = open("Sample.txt3","r")
content = file.read()
print("Being a perfect class monitor")
print(content)
file.close()

file = open("Sample.txt3","w")
file.write("A class monitor is a student who assists the teacher in routine duties. They maintain class discipline in the teacher’s absence and lead the class through various activities. They should act as a role model for the rest of the students.")
file.close()
