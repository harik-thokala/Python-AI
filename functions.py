

def checkWeather(temmp):
    temmp = int(input("What is the temperature outside? "))
    if temmp >20:
        return print("It's a hot day")
    elif temmp >10:
        return print("It's a cold day")
    else:
        return print("It's a very cold day")    

checkWeather(temmp=14)
