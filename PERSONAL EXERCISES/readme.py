f=open("contacts.txt","r")
lines=f.readlines()
lines=[m.strip() for m in lines]
i=0
while i<len(lines):
  k=lines[i]
  k.replace('0',"+256")
  z=k.split()
  x=z[1].title()
  y=z[0].replace("0","+256",1)
  print(f"RECIPEINT: {y}")
  print(f"Hello {x} ,Aiga wishes you amerry chrismas and ahappy new year 2023")
  i+=1

  
