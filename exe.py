combos = []


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

# test function


''' def outer(combos):
    count = 0
    combos_pos = []
    for outer in combos:
        for inner in combos:
            temp_list = [outer[0], inner[1]]

            combos_pos.append(temp_list)
            if count >= 1:
                combos_pos.append([outer[0], inner[0]])
        count += 1
    # print(combos)
    for item in combos_pos:
        print(item)
    print(f'count: {count}')
    length = len(combos_pos)
    print(f'items are: {length}') '''


# possibilities
def possible(combos):
    # possibilities = [win, loose, draw]
    counter = 0
    possibilities = ['win', 'loose', 'draw']
    for match in combos:
        for team in match:
            for pos in possibilities:
                # print(f'{match} => {pos}')
                if pos == 'draw':
                    print(f'{match} => {match}::{pos}')
                else:
                    print(f'{match} => {team}::{pos}')
                counter += 1

    print(f'Possibilities: {counter}')


def test():
    take = ""
    coin = []
    while take.lower() != "ok":
        temp = input("enter random staff: ")
        coin.append(temp)
        take = temp
        if take.lower() == "ok":
            break
    print(coin)


inputs()
# outer(combos)
possible(combos)
# test()
