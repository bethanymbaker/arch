import os

# script = 'this is my script'
# print(f"{script}")

# print(os.environ['HOME'])
# print(os.environ)

for a in os.environ:
    print('Var: ', a, 'Value: ', os.getenv(a))
print("all done")



print("Hi I love you Alex")