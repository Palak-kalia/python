team={
    "rav":[200,2,1,3],"palak":[150,3,4,2],"rohit":[120,1,2,4],"virat":[100,2,1,4],"shubhman":[160,3,2,1],"dhoni":[145,3,1,4],"rahul":[190,2,3,6]
}
d={}
while True:
    enter_num=int(input())
    if(enter_num==1):
        n=int(input('enter total num of players'))
        for i in range(n):
            name=str(input('enter name'))
            l=[]
            runs=int(input('enter num of runs'))
            l.append(runs)
            fifty=int(input('enter num of fifty'))
            l.append(fifty)
            hundreds=int(input('enter num of hundreds'))
            l.append(hundreds)
            wickets=int(input('enter num of wickets'))
            l.append(wickets)
            d.update({name:l})
            team.update(d)
            print(team)
    elif(enter_num==2):
        print(team.items())
    elif(enter_num==3):
        team.update({'happy':[200,3,4,2]})
        print(team)
    elif(enter_num==4):
        print(team.popitem())
    elif(enter_num==5):
        print(team.get("rav"))
    elif(enter_num==6):
        from collections import Counter
        k=Counter(team)
        high=k.most_common(3)
        print("name : runs")
        for i in high:
            print(i[0]," : ",[1]," ")

        
    
        


    

