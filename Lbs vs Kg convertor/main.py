print("This is Kilo vs Pound Converter made by Bilal Ahmad Khan, type your weight which you have to convert.")
W = int(input("Weight: "))
U = input("Convert your weight into (L)bs or (K)g ")
if U.upper() == "L":
    converted = W * 0.45
    print(f"You are {converted} kilos")
else:
    converted = W / 0.45
    print(f"You are {converted} pounds")
exit = input("Press any key to end")
