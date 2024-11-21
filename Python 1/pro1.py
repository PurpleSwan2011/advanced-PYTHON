file = open("Sample.txt","a")
file.write("Hello Codingal")
file.close()

file = open("Sample.txt","r")
content = file.read()
print("reading the file content:")
print(content)
file.close()

file = open("Sample.txt","w")
file.write("updated text using write mode !!")
file.close()

file=open("sample.txt2","r")
print("reading the content line by line: \n")

for line in file:
    print(line.strip())
file.close
