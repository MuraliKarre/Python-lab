phone = input("Phone number: ")
digits_map =  {
   
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
   # "9" : "nine"
}

output = ""
for ch in phone:
    output += digits_map.get(ch, "!") +  " "
print(output)