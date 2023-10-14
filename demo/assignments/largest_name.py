
def largest(*names):
    lname = ""
    for n in names:
        if n > lname:
            lname = n

    return lname


print( largest("Joseph", "Bill", "Kevin"))


