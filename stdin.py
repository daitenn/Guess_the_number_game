import random
import sys

x = random.randint(2, 10)
print(x)

sys.stdout.buffer.write(b"What do you choice(min)?\n")
sys.stdout.flush()
n = sys.stdin.buffer.readline()
print("n :" + str(n.decode()))

sys.stdout.buffer.write(b"What do you choice(max)?\n")
sys.stdout.flush()
m = sys.stdin.buffer.readline()
print("m :" + str(m.decode()))

for i in range(0, 5):
    print("Decide on the minimum and maximum numbers of your choice.(up to 5 times)\n")
    sys.stdout.buffer.write(b"What do you choice?\n")
    sys.stdout.flush()
    res = sys.stdin.buffer.readline()
    print("decide: " + str(res.decode()))

    computer = random.randint(int(n), int(m))

    if (int(res.decode()) == int(computer)):
        print("computer: " + str(computer))
        print("Your number: " + str(res.decode()))
        print("Great!!!")
        break
    else:
        print("computer: " + str(computer))
        print("Your number: " + str(res.decode()))
        if (i == 5):
            print("残念！！一からやり直し！！")
            break
        print("Please try again!")
