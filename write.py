"""file = open("example.txt", "w")
file.write("Hello World")
file.close()"""
lines = ["Hello\n", "Welcome\n", "Python\n"]

with open("file.txt", "w") as f:
    f.writelines(lines)lines = ["Hello\n", "Welcome\n", "Python\n"]
