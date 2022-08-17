import itertools
# from colorama import *

combos = []
# possible_solutions = []
pos = []


def raw():

    outcomes = ('win', 'loose', 'draw')
    teams = int(input("Enter no of teams: "))
    team_outcomes = [outcomes] * teams
    iterator = itertools.product(*team_outcomes)
    # iterator = itertools.combinations(*team_outcomes)
    possible_solutions = list(iterator)
    length = len(possible_solutions)
    print(f"possibilities: {length} => {possible_solutions}")
    # print(8 ^ 3)
    # print(f"This is color!")


def inputs():
    # variables for teams and storing break keyword resp.

    user1 = ""
    user2 = ""
    # check if 'ok' keyword is typed to stops
    while user1 != 'ok' or user2 != 'ok':
        # for ensuring there are a pair of two teams
        count = 0
        # get first team
        if count != 2:
            user1 = input("Type a team(type 'ok' to finish): ")
            count += 1

            # check if 'ok' keyword is typed to stop
            if user1 == "ok" or user2 == "ok":
                break

            # get 2nd team after first team
            if count == 1:
                user2 = input(f"{user1} Vs (type 'ok' to finish): ")
                count += 1

            # show progress so far
            combos.append([user1, user2])
            print(combos)

            # check if 'ok' keyword is typed to stop
            if user1 == "ok" or user2 == "ok":
                break

        # check if 'ok' keyword is typed to stop
        if user1 == "ok" or user2 == "ok":
            break

        # generate teams
        # combos.append([user1, user2])
    # print(combos)
    return combos


def iterator(combos, pos):
    c_length = len(combos)
    outcomes = ('win', 'los', 'draw')
    teams = c_length
    team_outcomes = [outcomes] * teams
    iterator = itertools.product(*team_outcomes)
    possible_solutions = list(iterator)
    length = len(possible_solutions)
    pos.append(possible_solutions)
    # pos = iterator
    print(f"possibilities: {length} => {possible_solutions}")
    return possible_solutions
    return pos


def show(combos, pos):
    # loop through combos
    list4 = set()
    for teams in combos:
        for poss_outer in pos:
            for poss_inner in poss_outer:
                for a in poss_inner:

                    list4. add('\n'+str(teams[0]) + " => " + str(a)+'\n')

                ''' for i in range(0, len(poss_outer)):
                    list4. append(str(teams[0])+str(poss_inner[i])) '''

    print(*list4)
    print(len(list4))
    print(f"possibilities:=> {pos}")


def test():
    pass


# functions
# raw()
inputs()
iterator(combos, pos)
show(combos, pos)
