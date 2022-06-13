city = input()
comm = float(input())

is_valid = True
comm_p = 0
if city == "Sofia" :
    if comm >= 0 and comm <= 500 :
        comm_p = comm * 0.05
    elif comm > 500 and comm <= 1000 :
        comm_p = comm * 0.07
    elif comm > 1000 and comm <= 10000:
        comm_p = comm * 0.08
    elif comm > 10000:
        comm_p = comm * 0.12
    else:
        is_valid = False
elif city == "Varna":
    if comm >= 0 and comm <= 500 :
        comm_p = comm * 0.045
    elif comm > 500 and comm <= 1000 :
        comm_p = comm * 0.075
    elif comm > 1000 and comm <= 10000:
        comm_p = comm * 0.10
    elif comm > 10000:
        comm_p = comm * 0.13
    else:
        is_valid = False
elif city == "Plovdiv":
    if comm >= 0 and comm <= 500 :
        comm_p = comm * 0.055
    elif comm > 500 and comm <= 1000 :
        comm_p = comm * 0.08
    elif comm > 1000 and comm <= 10000:
        comm_p = comm * 0.12
    elif comm > 10000:
        comm_p = comm * 0.145
    else:
        is_valid= False
else:
    is_valid = False
if is_valid :
    print(f"{comm_p:.2f}")
else :
    print("error")