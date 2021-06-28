'''
for {referência} in {sequência}:
    {bloco de código}
    continue
    break
else:
    {bloco de código}
'''

for i in range(0, 10):
    print(i)
    
print('--------')

for i in range(0, 10, 2):
    print(i)

print('--------')

for i in range(10, 0, -2):
    print(i)

print('--------')

for i in [10, 12, 35, 99, 1, 7]:

    if i==99:
        continue

    print(i)

print('--------')

for i in range(0, 10):
    print(i)
    if i==5:
        break
else:
    print('else do for')


