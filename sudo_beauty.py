import os

# print(os.environ['HOME'])
# print(os.environ)

for a in os.environ:
    print(f"Var: {a}; Value: {os.getenv(a)}")

