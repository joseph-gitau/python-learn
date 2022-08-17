import itertools


def raw():

    outcomes = ('win', 'los', 'draw')
    teams = int(input("Enter no of teams: "))
    team_outcomes = [outcomes] * teams
    iterator = itertools.product(*team_outcomes)
    # iterator = itertools.combinations(*team_outcomes)
    possible_solutions = list(iterator)
    length = len(possible_solutions)
    print(f"possibilities: {length} => {possible_solutions}")
    # print(8 ^ 3)
    # print(f"This is color!")
    # print(team_outcomes)


def nums():
    arr = ('eess', 'rrr'), ('dede', 'eefefef')
    pos = ('win', 'win'), ('win', 'los')
    list = dict(zip(arr, pos))
    print(list)


def run():
    list1 = ["a", "b", "c"]
    list2 = ["d", "e", "f"]
    list3 = [1, 2, 3]
    list4 = []
    for i in range(0, len(list1)):
        list4. append(list1[i]+list2[i]+str(list3[i]))

    print(*list4)


# run()
nums()
raw()
