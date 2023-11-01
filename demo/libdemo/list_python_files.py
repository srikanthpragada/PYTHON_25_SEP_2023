import os

result = os.walk(r"d:\classroom\sep25\demo")  # demo folder
total_count = 0
for (dirname, dirs, files) in result:
    print("Directory : ", dirname)
    print("=" * 80)
    count = 0
    for filename in files:
        if filename.endswith(".py"):
            print(filename)
            count += 1

    if count > 0:
        print('Count = ', count)
        total_count += count

print("Total count  = ", total_count)
