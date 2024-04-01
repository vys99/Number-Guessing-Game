import random
from prettytable import PrettyTable 


data = {}

def rand_num(stats):
    global hardness
    hardness = stats["hardness"]
    #changed hardness update from here to the level update, since hardness should be only updated if level increases

    k = [random.randint(1,100) for _ in range(0,hardness)]
    print(k)
    a = random.choice(k)
    return a

def result(num,a,stats):
    
    if num == a:
        print("Correct Answer")
        curr_points = stats["points"]
        stats.update({"points":curr_points+5})
        return stats
    else:
        print(f"Ha Ha .. I selected {a}, You lost your life!")
        curr_lives = stats["lives"]
        curr_points = stats["points"]
        stats.update({"lives":curr_lives-1})
        # if curr_points in [0,10,20,30,40,50,60,70,80,90,100]:
        #     stats.update({"points":curr_points})
        # else:
        #     stats.update({"points":curr_points-5})

        return stats
    

    
def levelupdate(num,rn,stats):
        curr_points= stats["points"]
        if curr_points>=10 and curr_points%10==0 and num==rn:
            print("""
                  LEVEL UP...
                  """)
            curr_lives = stats["lives"]
            stats.update({"level":(stats["points"]//10)+1})
            stats.update({"lives":curr_lives+1})
            print(hardness)
            
            stats["hardness"] = hardness+1 if stats["level"]%2!=0 else hardness

def mainfunc(k,x):     
    print("""

            ( LOGIN or REGISTER )
        
    TO LOGIN PRESS 1.
    TO REGISTER PRESS 2.
        

        """)
    
    z = int(input("Enter your option : "))
    if z == 1:
        while k == 'y':
            name = input("Enter your Name : ")
            password = input("Enter your password : ")
            name=name.lower()
            if name in data:
                if data[name]["password"] == password:
                    while x == 'y':
                        print("""
                                1.START GAME
                                2.RULES
                                3.HIGHSCORES
                                
                            """)

                        j = int(input("Enter the option : "))
                        if j==1:
                            stats = {"lives":3,"points":0,"level":1,"hardness":2}
                            table1 = PrettyTable(["Points","Lives","Level"])
                            table1.add_row([stats["points"],stats["lives"],stats["level"]])
                            print(table1)
                            while stats["lives"] > 0:
        
                                table = PrettyTable(["Points","Lives","Level"])
                                
                                rn = rand_num(stats)
                                num = int(input("Enter the number : "))
                                r = result(num,rn,stats)
                                levelupdate(num,rn,stats)
                                # 
                                table.add_row([stats["points"],stats["lives"],stats["level"]])
                                print(table)

                                if stats["points"] > data[name]["highscore"]:
                                    data.update({name:{"password":password,"highscore":stats["points"]}})
                                # print("-----------------------------------------------")
                                print()

                            if stats["lives"]==0:
                                print("GAME OVER.!!")
                            x = input("Do you want to return to Main Menu (y/n)")

                        elif j==2:
                            print("""
                        RULES

                        1.Guess any number from the given set of numbers.
                        2.If the number you guessed is correct you will get 5 points.
                        3.If you get 10 points you will be promoted to level 2 and likewise for each 10 points.
                        4.You will have 3 lives at the beginning of the game and with each wrong guess you will loose 1.
                        5.Also with every level up you will get a bonus life       
                                
                                
                        """)
                            x = input("Do you want to return to Main Menu (y/n)")

                        elif j==3:
                            print("-HIGHSCORE-")
                            print()
                            table2 = PrettyTable(["Name","Highscore"])
                            for i in data:
                                table2.add_row([i,data[i]["highscore"]])
                            
                            print(table2)
                            x = input("Do you want to return to Main Menu (y/n)")
                else:
                    print()
                    print("Check Your Password....")
                    k = input("Do you want to return to Main Menu (y/n)")
            else:
                print()
                print("Player not Found..!!!")
                k = input("Do you want to return to Main Menu (y/n)")

            k = input("Do you want to play again as new player ?(y/n)")
                

    elif z==2:
        print("CREATE PASSWORD")
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        name=name.lower()
        data.update({name:{"password":password,"highscore":0}})
        print("""
              REGISTERED SUCCESSFULLY..
              """)
        mainfunc(k,x)
        
with open("database.txt") as p:
    data = eval(p.read())
x = 'y'
k ='y'
mainfunc(k,x)

file = open("database.txt","w")
file.write(str(data))


