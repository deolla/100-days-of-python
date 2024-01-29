target = int(input())
cunt = 0

for i in range(1, target + 1):
    if i % 2 == 0:
        cunt += i
        # print(i)
print(cunt)

# or

target = int(input())
cunt = 0

for i in range(2, target + 1, 2):
    cunt += i
    # print(i)
print(cunt)