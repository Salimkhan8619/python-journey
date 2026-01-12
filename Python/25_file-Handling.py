# a= "salim is good"

# file=open("salim.txt","w")

# file.write(a)


# file.close()


b = "salim is data Analy."
file=open("robot.txt " , "r")
content=file.read()
print(content)


file.close()

a="salim khan is also good "
file=open("robot.txt","a")
file.write(a)
file.close()