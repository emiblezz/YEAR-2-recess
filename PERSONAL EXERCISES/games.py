from tabulate import tabulate


number_of_teams = int(input("ENTER NUMBER OF TEAMS PARTICIPATING: "))
name=["TEAM :"]
win=["WON :"]
lose=["LOST :"]
draw=["DREW :"]
total=["TOTAL :"]
i=1
while i<= number_of_teams:
    naming=input(f"Enter name of the Team {i} : ")
    name.append(naming)
    winning= int(input(f"Enter number of wins for  the Team {i} : "))
    win.append(winning)
    losing = int(input(f"Enter number of loses for  the Team {i} : "))
    lose.append(losing)
    drawing = int(input(f"Enter number of wins for  the Team {i} : "))
    draw.append(drawing)
    win_points=winning*3
    draw_points=drawing*1
    lose_points=losing*0
    total_points=win_points+draw_points+lose_points
    total.append(total_points)
    i=i+1

#print(name)
#print(win)
#print(lose)
#print(draw)
result=[name,win,lose,draw,total]
print(tabulate(result))