s=" Hello,Rock samson!  "

print(s)
 
print(s.endswith("n!")) #output is true or false

print(s.startswith("  He")) #output is true or false

print(s.count("o"))  #counts the number of 'o'

print(s.capitalize())  #capitalizes first letter of the whole string

print(s.find("home"))  #If given value is absent from the string then return -1

print(s.replace("Rock","Sanju")) #Replaces Rock with Sanju

print(s.upper())         #Capitalizes every character of the string

print(s.lower())         #Lowers every character of the string

print(s.strip())         #The strip() method removes any white spaces before and after the string

print(s.rstrip("!  "))   #The rstrip() removes any trailing characters

print(s.split(","))   #The split() method splits the given string at the specified instance and returns the separated strings as list items

print(s.center(64))   #The center() method aligns the string to the center as per the parameters given by the user

print(s.center(64,"."))  #We can also provide padding character. It will fill the rest of the fill characters provided by the user

print(s.index("Rock"))  #The index() method searches for the first occurrence of the given value and returns the index where it is present

print(s.index("rocky")) #Error

print(s.isalnum())  #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False

print(s.isalpha())  #The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False

print(s.islower())  #The islower() method returns True if all the characters in the string are lower case, else it returns False

print(s.isupper())  #The isupper() method returns True if all the characters in the string are upper case, else it returns False

print(s.isspace())  #The isspace() method returns True only and only if the string contains white spaces, else returns False

print(s.istitle())  #The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False
  
print(s.isprintable()) #The isprintable() method returns True if all the values within the given string are printable, if not, then return False

print(s.swapcase())  #The swapcase() method changes the character casing of the string.

print(s.title())  #Capitalizes the first letter of every word