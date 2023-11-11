import time
import random


def initialize_players(num_players):
    players = list(range(1, num_players + 1))
    return players


def determine_moving_players(players):
    num_moving = int(0.8 * len(players))
    moving_players = random.sample(players, num_moving)
    return moving_players


def determine_eliminated_players(players, num_eliminated):
    eliminated_players = random.sample(players, num_eliminated)
    return eliminated_players


def print_game_state(round_num, light, moving, static, eliminated):
    print(f"Round {round_num} - {light} Light")
    print(f"Moved: {', '.join(map(str, moving))}")
    print(f"Static: {', '.join(map(str, static))}")
    if eliminated:
        print(f"Eliminated: {', '.join(map(str, eliminated))}")
    else:
        print("Eliminated: None.")
    print()


def main():
    num_players = 456
    round_duration = 30  # 30 seconds in total
    round_time = 5  # 5 seconds per round

    players = initialize_players(num_players)
    round_num = 1

    while round_num <= round_duration // round_time:
        light = "Green" if round_num % 2 == 1 else "Red"

        if light == "Green":
            moving_players = determine_moving_players(players)
            static_players = [p for p in players if p not in moving_players]
            eliminated_players = None
        else:
            num_eliminated = int(0.05 * len(players))
            eliminated_players = determine_eliminated_players(players, num_eliminated)
            static_players = [p for p in players if p not in eliminated_players]
            moving_players = None

        print_game_state(round_num, light, moving_players, static_players, eliminated_players)

        round_num += 1
        time.sleep(round_time)


if __name__ == "__main":
    main()
