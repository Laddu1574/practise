f = open("New Text Document.txt","r")
print(f.read()) #read all the content as it is
# print(f.readline()) #read only line by line
# print(f.readlines()) #read the content as list

# f = open("New Text Document.txt","w")
# f.write("I am laddu") #it will overwrite the old data to new

# f = open("New Text Document.txt","a")
# f.write("\nI am NSN employee") #it will add the data to existing content

# import os
# os.remove("New Text Document.txt") #python doesn't have remove method, so we import os and remove the data