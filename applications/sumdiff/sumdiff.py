"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))

def f(x):
    return x * 4 + 6



def sumdiff(list):
    subtractions = {}
    sub_results = {}
    additions = {}
    add_results = {}
    for num in list:
        for num2 in list:
            sub1result = f(num) - f(num2)
            subtractions[(num, num2)] = sub1result
            if sub1result not in sub_results:
                sub_results[sub1result] = [(num, num2)]
            else:
                sub_results[sub1result].append((num, num2))

            add1result = f(num) + f(num2)
            additions[(num, num2)] = add1result
            if add1result not in add_results:
                add_results[add1result] = [(num, num2)]
            else:
                add_results[add1result].append((num, num2))


    for result in add_results:
        add_pair_array = add_results[result]
        if result in sub_results:
            sub_pair_array = sub_results[result]
        else:
            sub_pair_array = []
        for pair_of_addends in add_pair_array:
            for pair_of_subs in sub_pair_array:
                print(f"f({pair_of_addends[0]}) + f({pair_of_addends[1]}) = f({pair_of_subs[0]}) - f({pair_of_subs[1]})    {f(pair_of_addends[0])} + {f(pair_of_addends[1])} = {f(pair_of_subs[0])} - {f(pair_of_subs[1])}")



print(sumdiff(q))