from tabulate import tabulate
def totals(mylist):
    votes_cast = 0
    for x in mylist:
        votes_cast = votes_cast + x
    return votes_cast


def percentvote(myvotes, votes_cast):
    percent = (myvotes / votes_cast) * 100
    return percent


no_of_poll_stations = int(input("Enter number of polling stations: \n"))
candidate1 = input("Enter the name of the candidate1:\n")
candidate2 = input("Enter the name of the candidate2:\n ")
poll_stations = []
candidate1_votes = []
candidate2_votes = []
poll_stations_total = []
row=["stations"]
row.extend(poll_stations)
row1=[candidate1]
row1.extend(candidate1_votes)
row2=[candidate2]
row2.extend(candidate2_votes)
row3=["total"]
row3.extend(poll_stations)



i = 1
while i <= no_of_poll_stations:
    poll_station = input(f"Enter the polling station{i} name/code: ")
    poll_stations.append(poll_station)
    votes1 = input(f"Enter the votes for candidate1 at {poll_station}: ")
    candidate1_votes.append(votes1)
    votes2 = input(f"Enter the votes for candidate2 at {poll_station}: ")
    candidate2_votes.append(votes2)
    votes_cast = input(f"Enter the total votes cast at {poll_station}: ")
    poll_stations_total.append(votes_cast)
    i = i + 1

if bool(poll_stations_total) and bool(votes1) and bool(votes2) and bool(votes_cast):

    try:
        no_of_poll_stations = int(no_of_poll_stations)
        votes1 = int(votes1)
        votes2 = int(votes2)
        votes_cast = int(votes_cast)
    except:
        print("Please enter the correct numerical values to proceed")
    result=[row,row1,row2,row3]
    #print(poll_stations)
    #total1=sum(candidate1_votes)
    #total2=sum(candidate2_votes)
    #poll_stations_total.sum()
    #print(candidate1_votes, end="")
    #print(candidate1)
    #print(candidate2_votes, end="")
    #print(candidate2)
    #print(poll_stations_total)
    print(tabulate(result))

else:
    print("Please fill in all dat is mandatory")
