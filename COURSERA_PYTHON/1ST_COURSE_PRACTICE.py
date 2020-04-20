total=0
n=0
while True:
    user_data = input("enter a number:")
    if user_data =="done":
        break
    try:
            num=float(user_data)
    except:
        print("enter a valid number")
        continue
    total+=num
    n+=1
    print("total:",total)
    print("n=",n)
average=total/n
print("total:",total)
print("count:",n)
print("average:",average)