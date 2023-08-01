class PoliceCase():
  def __init__(self,victim,suspect,station,district):
    self.victim=victim
    self.suspect=suspect
    self.station=station
    self.district=district
  def __str__(self):
    all=f"Victim:{self.victim},Sustpect:{self.suspect},Police Station:{self.station},Residence:{self.district}"
  def __eq__(self):
    if(self.victim==other.victim):
      
case1 = PoliceCase("jose","akello","CPP1","Wakiso")
case2 = PoliceCase("mary","kakaire","CPP2","Koboko")
case3 = PoliceCase("jose","john","CPP1","Wakiso")

print(case1)
print(case2)
print(case3)

cases=(case1,case2,case3)
incharge=("Mwonge","Juma","Kennedy")

for(x,y in zip(incharge,cases))
print(f"{x} worked on cases with the {y}")





  