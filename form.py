#name = 6

#if name <= 3:
#    print("Looks too short")
#elif name >= 50:
#    print("Looks too long")
#else:
#    print("looks good")

name = "Jwegfheofjwohfwpjerfhwefhewoihfpewnf;wdioewfholewnf"

if len(name) < 3:
    print("User name must be atleast above 3 characters")
elif len(name) >= 50:
    print("User name not exceed 50 Characters")
else:
    print("User name is PERFECT")
