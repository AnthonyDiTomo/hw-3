temperature = 90
#set desired temp
while temperature > 75:
  #statement for all temps above 75  
  print("Temperature is", temperature, "- crank the AC!")
  #stop loop at desired temp
  if temperature == 75:
    break
  #set loop increment  
  temperature -= 3
#statement once desired temp is reached  
print("75. Ahh, that's better.")