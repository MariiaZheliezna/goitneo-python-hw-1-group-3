message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
offset = offset % 26
encoded_message = ""
for ch in message:
    if (ord(ch) <= ord("z") and ord(ch) >= ord("a")):  # проверка на то, что это символы a-z A-Z
        pos = ord(ch) - ord("a")
        pos = pos + offset - 26*((pos+offset)//26)
        encoded_message = encoded_message + chr(pos + ord("a"))
    elif (ord(ch) <= ord("Z") and ord(ch) >= ord("A")):
        pos = ord(ch) - ord("A")
        pos = pos + offset - 26*((pos+offset)//26)
        encoded_message = encoded_message + chr(pos + ord("A"))        
    else:
        encoded_message = encoded_message + ch 
print(encoded_message)

       
    
    


