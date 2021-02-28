import math
import numpy
import random


list_of_ind_x = []
list_of_ind_y = []


def function(x,y):
    return math.cos(x) - math.sin(y) + math.cos(x ** 2)

def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

def dec_to_bin(n, len_bin):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2

    while len(s) != len_bin:
        s = "0" + s
    return s

def bin_to_dec(digit):
    dec = 0
    for i in range(0, len(digit)):
        dec += int(digit[i]) * (2 ** (len(digit) - i - 1))
    return dec

def method_blanket(num_of_ind, x_a, x_b, y_a, y_b):
    global list_of_ind_x, list_of_ind_y

    len_x = x_b - x_a
    len_y = y_b - y_a
    sw = True
    i = 1
    list_ratio = []
    list_coef_x = []
    list_coef_y = []
    divider = 0
    while sw:
        temp_1 = num_of_ind / i
        # print(f"temp_1 : {temp_1}")
        if temp_1 % 1 == 0:
            # print(f"i: {i}")
            if len_y >= len_x:
                coef_y = len_y / (temp_1 + 1)
                coef_x = len_x / (i + 1)
            else:
                coef_y = len_y / (i + 1)
                coef_x = len_x / (temp_1 + 1)
            # print(f"coef_x: {coef_x}")
            # print(f"coef_y: {coef_y}")
            ratio = abs(coef_y - coef_x)
            # print(f"ratio: {ratio}")
            list_ratio.append(ratio)
            list_coef_x.append(coef_x)
            list_coef_y.append(coef_y)
            if i != 1:
                if (list_ratio[len(list_ratio) - 1] >= list_ratio[len(list_ratio) - 2]):
                    sw = False
                else:
                    divider = i
                    # print(f"divider: {divider}")
            else:
                divider = i
                # print(f"divider: {divider}")
        i = i + 1

    for i in range(divider):
        for j in range(int(num_of_ind / divider)):
            if len_y >= len_x:
                list_of_ind_y.append(y_a + ((j + 1) * list_coef_y[len(list_coef_y) - 2]))
                list_of_ind_x.append(x_a + ((i + 1) * list_coef_x[len(list_coef_x) - 2]))
            else:
                list_of_ind_y.append(y_a + ((i + 1) * list_coef_y[len(list_coef_y) - 2]))
                list_of_ind_x.append(x_a + ((j + 1) * list_coef_x[len(list_coef_x) - 2]))
#input data
# function
funk = "x^2-y^2"

# граници для "х"
x_a = 1
x_b = 5

# граници для "y"
y_a = 1
y_b = 3

# epsilon
epsilon = 0.1
q_eps = get_count(epsilon)

# number of iterations
k = 10

# number of individums
num_of_ind = 6

P_c = 0.9
P_m = 0.05
#------------------------------------
list_of_f = []
list_of_X_x = []
list_of_X_y = []
list_F_mean = []

#initialization----------------------

L_x = math.ceil(math.log2((x_b - x_a) * (10 ** q_eps) + 1))
L_y = math.ceil(math.log2((y_b - y_a) * (10 ** q_eps) + 1))

h_x = (x_b - x_a)/((2 ** L_x) - 1)
h_y = (y_b - y_a)/((2 ** L_y) - 1)

print(f"L_x: {L_x}")
print(f"L_y: {L_y}")
print(f"h_x: {h_x}")
print(f"h_y: {h_y}")

#тут должна быть функция для рапределения точек
method_blanket(num_of_ind, x_a, x_b, y_a, y_b)
print(f"list_of_ind_x: {list_of_ind_x}")
print(f"list_of_ind_y: {list_of_ind_y}")

for i in range(num_of_ind):
    list_of_f.append(function(list_of_ind_x[i], list_of_ind_y[i]))
print(f"list_of_f: {list_of_f}")

# 2 calculating the fitness of the entire population
print("")
print("---------------------------------------------------")
print("2 calculating the fitness of the entire population")
print("")


F_mean_1 = numpy.mean(list_of_f)
print(f"F_mean_1: {F_mean_1}")

for i in range(num_of_ind):
    list_of_X_x.append(dec_to_bin(math.ceil((list_of_ind_x[i] - x_a) / h_x), L_x))
    list_of_X_y.append(dec_to_bin(math.ceil((list_of_ind_y[i] - y_a) / h_y), L_y))

for i in range(k):
    print(f"---------------Iteration {i + 1} -----------------")
    list_percent_fitnes_f = []
    list_random_value = []
    list_descendant_X_x = []
    list_descendant_X_y = []
    list_dec_X_x = []
    list_dec_X_y = []
    list_of_fitnes_f = []

    print(f"list_of_X_x: {list_of_X_x}")
    print(f"list_of_X_y: {list_of_X_y}")

    f_min = min(list_of_f)
    print(f"f_min: {f_min}")
    if f_min < 0:
        for i in range(num_of_ind):
            list_of_fitnes_f.append(list_of_f[i] + 2 * abs(f_min))
    else:
        for i in range(num_of_ind):
            list_of_fitnes_f.append(list_of_f[i])

    F_mean_2 = numpy.mean(list_of_fitnes_f)
    Sum_fitnes_f = sum(list_of_fitnes_f)

    for i in range(num_of_ind):
        list_percent_fitnes_f.append(list_of_fitnes_f[i] / Sum_fitnes_f * 100)
    print(f"list_of_fitnes_f: { list_of_fitnes_f}")
    print(f"F_mean_2: {F_mean_2}")

    temp = 0
    for i in range(num_of_ind):
        temp += list_percent_fitnes_f[i]
        list_percent_fitnes_f[i] = temp

    print(f"list_percent_fitnes_f: { list_percent_fitnes_f}")
    temp = 0
    for i in range(num_of_ind):
        rand = random.random() * 100
        for j in range(num_of_ind):
            if (rand < list_percent_fitnes_f[0] and j == 0 ):
                list_random_value.append(0)
            elif ( rand < list_percent_fitnes_f[j] and rand >= list_percent_fitnes_f[j - 1] ):
                list_random_value.append(j)

    print(f"list_random_value: { list_random_value }")

    locus = random.randint(1, L_y-1)
    print(f"locus: {locus}")

    num_of_ind_2 = num_of_ind / 2

    print(f"list_of_X_x: {list_of_X_x}")
    print(f"list_of_X_y: {list_of_X_y}")

    #crossbreeding
    if (random.random() < P_c):
        # FOR list_descendant_X_x
        for i in range(1, int(num_of_ind_2) + 1):
            temp_str_x1 = list(list_of_X_x[list_random_value[2 * i - 2]])
            temp_str_x2 = list(list_of_X_x[list_random_value[2 * i - 1]])

            for j in range(locus, L_x):
                temp_elem = temp_str_x1[j]
                temp_str_x1[j] = temp_str_x2[j]
                temp_str_x2[j] = temp_elem

            list_descendant_X_x.append("".join(temp_str_x1))
            list_descendant_X_x.append("".join(temp_str_x2))

        # FOR list_descendant_X_y
        for i in range(1, int(num_of_ind_2) + 1):
            temp_str_x1 = list(list_of_X_y[list_random_value[2 * i - 2]])
            temp_str_x2 = list(list_of_X_y[list_random_value[2 * i - 1]])

            for j in range(locus, L_y):
                temp_elem = temp_str_x1[j]
                temp_str_x1[j] = temp_str_x2[j]
                temp_str_x2[j] = temp_elem


            list_descendant_X_y.append("".join(temp_str_x1))
            list_descendant_X_y.append("".join(temp_str_x2))

    else:
        for i in range(num_of_ind):
            list_descendant_X_x.append(list_of_X_x[i])
            list_descendant_X_y.append(list_of_X_y[i])

    #print(f"list_descendant_X_y: {list_descendant_X_x}")
    #mutation
    for i in range(num_of_ind):
        if (random.random() < P_m):
            # FOR list_descendant_X_x
            temp_str_x1 = list(list_descendant_X_x[i])
            temp_rand_elem = random.randint(0, L_x-1)

            if(temp_str_x1[temp_rand_elem] == "0"):
                temp_str_x1[temp_rand_elem] = "1"

            else:
                temp_str_x1[temp_rand_elem] = "0"

            list_descendant_X_x[i] = "".join(temp_str_x1)

            # FOR list_descendant_X_y
            temp_str_x2 = list(list_descendant_X_y[i])
            temp_rand_elem = random.randint(0, L_y - 1)

            if (temp_str_x2[temp_rand_elem] == "0"):
                temp_str_x2[temp_rand_elem] = "1"

            else:
                temp_str_x2[temp_rand_elem] = "0"

            list_descendant_X_y[i] = "".join(temp_str_x2)


    print(f"list_descendant_X_x: {list_descendant_X_x}")
    print(f"list_descendant_X_y: {list_descendant_X_y}")

    for i in range(num_of_ind):
        list_dec_X_x.append(bin_to_dec(list_descendant_X_x[i]))
        list_dec_X_y.append(bin_to_dec(list_descendant_X_y[i]))

    # print(f"list_dec_X_x: {list_dec_X_x}")
    # print(f"list_dec_X_y: {list_dec_X_y}")

    list_end_func = []

    for i in range(num_of_ind):
        x = x_a + h_x * list_dec_X_x[i]
        y = y_a + h_y * list_dec_X_y[i]
        list_end_func.append(function(x, y))

    F_mean_end = numpy.mean(list_end_func)
    print(f"F_mean_end: {F_mean_end}")
    print(f"list_end_f: {list_end_func}")
    print(f"Max f_ind in iteration {list_end_func.index(max(list_end_func)) + 1}: {max(list_end_func)}")
    list_F_mean.append(F_mean_end)
    F_mean_1 = F_mean_end
    list_of_f = list_end_func
    list_of_X_x = list_descendant_X_x
    list_of_X_y = list_descendant_X_y
    print(" ")

max_elem = max(list_F_mean)
print(f"Max F_mean in iteration {list_F_mean.index(max_elem) + 1}: {max_elem}")