def wish(*users, msg='Hello'):
    for u in users:
        print(msg, u)


wish("Jack", "Mark", "Steve", msg="Hi")
wish("Jane", "Ben")
