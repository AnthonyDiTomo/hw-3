disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]
#Declare loop range
for name in range(len(disney_characters)):
  #statement if "u" found
  if "u" in disney_characters[name]:
    print(disney_characters[name], "U are so Uniquely U!")
  #statement if "i" found
  elif "i" in disney_characters[name]:
    print(disney_characters[name], "I bet you're Impressively Intelligent!")
  #statement if "o" found  
  elif "o" in disney_characters[name]:
    print(disney_characters[name], "O My! How Original!")
  #if neither "u","i", nor "o" is found
  else:
    print(disney_characters[name], "Ehh, a's and e's are so ordinary.")