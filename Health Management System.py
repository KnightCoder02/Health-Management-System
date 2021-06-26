# Health Management System
# 3 clients - Harry, Rohan and Hammad

# def getdate():
#     import datetime
#     return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

print("Health Management System")
client_list = {1 : "Harry", 2 : "Rohan", 3 : "Hammad"}
log_list = {1 : "Exercise", 2 : "Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name: ")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())
    print("Selected Client:", client_list[client_name], "\n", end="")
    print("Press 1 for log")
    print("Press 2 for retrive")
    op = int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to log", value, "\n", end="")
        log_name = int(input())
        print("Selected Job:", log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = 'y'
        while(k is not "n"):
            print("Enter", log_list[log_name], "\n", end="")
            mytext = input()
            f.write("[" + str(getdate()) + "]:" + mytext + "\n")
            k = input("ADD MORE? Y/N:")
            continue
        f.close()
        
    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrive", value, "\n", end="")
        log_name = int(input())
        print(client_list[client_name] + "-", log_list[log_name], "Report: ", "\n", end="")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    
    else:
        print("Invalid Input!!!")

except Exception as e:
    print("Wrong Input!!!")