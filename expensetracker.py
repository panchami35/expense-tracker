expenses=[]
print("WELCOME✨")
while True:

    print("===MENU===")
    print("1.ADD EXPENSE")
    print("2.VIEW EXPENSE")
    print("3.TOTAL EXPENSE")
    print("4.Remove all expenses")
    print("5.EXIT")

    choice=int(input("enter your choice:"))

    if choice==1:
        date=input("enter the date:")
        category=input("enter the category:")
        description=input("give more detail:")
        amount=float(input("enter the amount:"))

        expense={"date":date,"category":category,"description":description,"amount":amount}
        expenses.append(expense)
        print("EXPENSES ADDED SUCCESFULLY")
            
    elif choice==2:
        if(len(expenses)==0):
            print("no expenses added!")
        else:
            print("your expenses are:")
            count=1
            for m in expenses:
                print(f"expenseNO{count}::{m["date"]},{m["category"]},{m["description"]},{m["amount"]}")
                count+=1
    elif choice==3:
        total=0
        for m in expenses:
            total=total+m["amount"]
        print("\n total_expense:",total)
    elif choice==4:
       expenses.remove(expense) 
       print("enpenses removed succesfully")
    elif choice==5:

        print("thank you!!")
        break
    else:
        print("invalid choice")

    



