import glob
import os
from time import sleep

list_of_files = glob.glob(
    f"{os.getcwd()}/coda_inventories/*"
)  # * means all if need specific format then *.csv

latest_file = max(list_of_files, key=os.path.getctime)


def coda_inv_review():
    print("Let's review your CoDa patterns.")
    sleep(0.1)
    print("'r' to review your latest inventory.")
    sleep(0.1)
    print("'c' to see comparisons across multiple inventories.")
    response = input()
    if response == "r":
        # pull up latest inventory, give initial stats
        def count_lines(path):
            count = 0
            with open(path, "r") as f:
                for line in f:
                    # print(line)
                    count += 1
                return count

        def print_lines(path):
            with open(path, "r") as f:
                for line in f:
                    print(line)

        count_5s = count_lines(f"{latest_file}/5s.txt")
        count_4s = count_lines(f"{latest_file}/4s.txt")
        count_3s = count_lines(f"{latest_file}/3s.txt")
        count_2s = count_lines(f"{latest_file}/2s.txt")
        count_1s = count_lines(f"{latest_file}/1s.txt")
        print("In your last inventory you recorded:")
        sleep(0.1)
        print(f"{count_5s} patterns with a 5 rating.")
        sleep(0.1)
        print(f"{count_4s} patterns with a 4 rating.")
        sleep(0.1)
        print(f"{count_3s} patterns with a 3 rating.")
        sleep(0.1)
        print(f"{count_2s} patterns with a 2 rating.")
        sleep(0.1)
        print(f"{count_1s} patterns with a 1 rating.")
        sleep(0.1)
        while True:
            print("If you would like to see the list of patterns at a specific rating,")
            sleep(0.1)
            print("relpy with the rating number '1-5'.")
            sleep(0.1)
            print("Otherwise, hit enter to continue.")
            response = input()
            if response == "5":
                print_lines(f"{latest_file}/5s.txt")
            elif response == "4":
                print_lines(f"{latest_file}/4s.txt")
            elif response == "3":
                print_lines(f"{latest_file}/3s.txt")
            elif response == "2":
                print_lines(f"{latest_file}/2s.txt")
            elif response == "1":
                print_lines(f"{latest_file}/1s.txt")
            else:
                break

    elif response == "c":
        print(
            f"You've taken {len(list_of_files)} total CoDa inventories since 6/6/2020."
        )
    else:
        print("Please respond with either 'r' or 'c'.")


# Offer a report of most recent inventory by totals of each rating, and broken down by catigory
# Be able to pull up response lists based on rating or catigory
# Offer a list of what ranked higher since last inventory
# Offer a list of what ranked lower since last inventory
# Show all time averages, highest to lowest.
# Show all time catigory averages, highest to lowest.
