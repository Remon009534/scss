# 1.
# weekday = 0
# vacation = 0

# def sleep_in(weekday, vacation):
#     if not  weekday or vacation:
#         return True
#     else:
#         return False
# x = sleep_in(weekday, vacation)
# print(x)

# 2.
# def monkey_trouble(a, b):
#     if a == "smile":
#         return True
#     elif b == "smile":
#         return True
#     else:
#         return False

# print(monkey_trouble("sad", "smile"))

# values_1 = input("Enter your number:")
# values_2 = input("Enter your number:")

# 3.
# def sum_double(values_1, values_2):
#     return values_1 + values_2
# def sum_double_2(values_1, values_2):
#     return values_1 * values_2

# print(sum_double(1, 2))
# print(sum_double(3, 2))
# print(sum_double_2(2, 2))


# 6.
# def makes10(a, b):
#     if a or b == "10":
#         return True
#     elif a + b == "10":
#         return True
#     elif a == "10":
#         return True
#     elif b == '10':
#         return True
#     else:
#         return False
# print(makes10(9, 9))

 # 7.
# def near_hundred(n):
#     if (89 < n < 111) or (189 < n < 211):
#         return True
#     else:
#         return False
# print(near_hundred(93))
# print(near_hundred(89))
# print(near_hundred(90))

# 9.
# def not_string(n):
#     if n == "Not":
#         return n
#     else:
#         return " not " + n
# print(not_string('candy'))
# print(not_string('x'))
# print(not_string('not bad'))

# 8.
# def pos_neg(a, b):
#     if a < 0 or b < 0:
#         return True
#     else:
#         return False
# print(pos_neg(-4, -5))

# def near_hundred(n):
#         if 90 <= n <= 110:
#                 return True
#         elif 190 <= n <= 210:
#                 return True
#         else:
#                 return False
# print(near_hundred(193))

# 12.
# def front3(str_):
#         if str_:
#                 return str_[:3] + str_[:3] + str_[:3]
# print(front3("java"))

# 10.
# def missing_char(str, n):
#     return str[:n] + str[n+1]
# print(missing_char('kitten', 1))

# y = input("Enter a word:")
# def front3(y):
#     if len(y) < 3:
#         return y
#     front = y[0:3]
#     return front * 3
# print(front3(y))
y = input("Enter a word:")

def front_back(y):
    return y[:-1] + y[1:-1] + y[0]
print(front_back(y))






   

    











    
    

