import argparse

def calculate_leaf_and_page(card_number):
    cards_per_leaf = 18
    cards_per_page = 9

    leaf_number = (card_number - 1) // cards_per_leaf + 1
    position_in_leaf = (card_number - 1) % cards_per_leaf + 1

    if position_in_leaf <= cards_per_page:
        page_number = 1  # Front page
    else:
        page_number = 2  # Back page

    return leaf_number, page_number

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the leaf and page for a given card number.")
    parser.add_argument("--card-number", type=int, required=True, help="The card number to find the leaf and page for.")
    args = parser.parse_args()

    leaf, page = calculate_leaf_and_page(args.card_number)
    print(f"Card number {args.card_number} should be placed in leaf {leaf}, page {page}.")