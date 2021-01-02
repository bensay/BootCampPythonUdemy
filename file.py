
# Write
file = open("test.txt", 'w')
file.write('pink')
file.close()
# Create from a list
file = open("test.txt", 'w')
x = ['red', 'blue', 'green', 'black', 'white']
for item in x:
    file.write(item + '\n')
file.close()
# Append to the text
file = open("test.txt", 'a')
file.write("pink\n")
file.write("brown\n")
file.close()
# Write and Read
file = open("test.txt", 'a+')
file.write("Yellow\n")
file.write("Violet")
z = file.read()
print(z)
file.close()