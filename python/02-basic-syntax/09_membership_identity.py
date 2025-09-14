# 멤버십 : in, not in
print("a" in "apple")  # True
print("b" not in "apple")  # True

# 아이덴티티 : is, is not (동일 객체인지)
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x == y, x is y)  # True True  (값도 같고, 같은 객체)
print(x == z, x is z)  # True False (값은 같지만, 다른 객체)
