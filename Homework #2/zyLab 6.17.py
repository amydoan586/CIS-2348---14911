#Amy Doan ID:1895125
Password = str(input()) #User input password
Password = Password.replace("i","!") #replace i to !
Password = Password.replace("a","@") #replace a to @
Password = Password.replace("m","M") #replace m to M
Password = Password.replace("B","8") #replace B to 8
Password = Password.replace("o",".") #replace o to .
Password = Password + "q*s" #Adds q*s at the end
print(Password)