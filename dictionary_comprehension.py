# dictionary comprehension = create dictionary using an expression 
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
#--------------------------------------------------------------------------------------------
#cities_in_F = {'New York':32,'Bosten':75,'Los Angeles':100,'Chicago':50}

#cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

#print(cities_in_C)
#--------------------------------------------------------------------------------------------
#weather = {'New York':'snowing','Boston':'sunny','Los Angeles':'sunny','Chicago':'cloudy'}
#sunny_weather = {key:value for key,value in weather.items() if value == "sunny"}

#print(sunny_weather)
#--------------------------------------------------------------------------------------------
#cities= {'New York':32,'Bosten':75,'Los Angeles':100,'Chicago':50}
#desc_city = {key: ("WARM") if value >= 40 else "COLD" for key,value in cities.items()}
#print(desc_city)  
#--------------------------------------------------------------------------------------------
def check_temp(temp):
    if temp >= 70:
        return "HOT"
    if temp >=40:
        return "WARM"
    else:
        return "COLD"

cities= {'New York':32,'Bosten':75,'Los Angeles':100,'Chicago':50}
desc_city = {key: check_temp(value) for key,value in cities.items()}
print(desc_city)