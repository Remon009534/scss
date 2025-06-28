# mysets = ["AMM ", "JAMM ", "LICHU ", "KAMAL "]
# y = list(mysets)
# y[1] = "Arnob"
# mysets = tuple(y)

# print(mysets)
# Students = ["A", "B", "C", "D", "E"]
# print(Students)


user_input = []

counter = 0

while counter <= 5:
    num_input = int(input(f"number {counter}:"))
    if (num_input >=3 and num_input <= 27):
        user_input.append(num_input)
        counter += 1
    
print(user_input)