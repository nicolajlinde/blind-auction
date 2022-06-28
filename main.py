import art

print(art.logo)
print("Welcome to the super secret auction!\n")

bids = []
end_auction = False


def gather_all_bids(auc_name, auc_bid):
    bids.append({"name": auc_name, "bid": auc_bid})


while not end_auction:
    name = input("What's you're name?\n")
    bid = int(input("What will you like to bid?\n$"))

    gather_all_bids(name, bid)

    end = input("Are there anyone else who like to bid? Type 'yes' or 'no'\n").lower()

    if end == "no":
        max_bid = 0
        winner = ""
        for i in bids:
            if i["bid"] > max_bid:
                max_bid = i["bid"]
                winner = i["name"]

        print(f"The highest bid is ${max_bid} and is from {winner}")

        end_auction = True
    elif end == "yes":
        end_auction = False
