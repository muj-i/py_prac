qs1 = ["What is the capital of Bangladesh?", ["Dhaka", "Katmandu", "Hongkong", "Seoul"]]
qs2 = ["What is the national fish of Bangladesh?", ["Rui", "Hilsha", "Puti", "Vetki"]]

quess = [qs1, qs2]

for Ques in quess:
    print(Ques[0])
    print("Options:", Ques[1])
    ans = input("Type Ans: ")
    if Ques == qs1:
        if ans == "Dhaka":
            print("Won 25 mil")
        else:
            print("Loss 25 mil")
    elif Ques == qs2:
        if ans == "Hilsha":
            print("Won 1 bil")
        else:
            print("Loss 1 bil")
