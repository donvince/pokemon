import argparse

def calculate_leaf_page_and_sleeve(card_number):
    cards_per_leaf = 18
    cards_per_page = 9

    leaf_number = (card_number - 1) // cards_per_leaf + 1
    position_in_leaf = (card_number - 1) % cards_per_leaf + 1

    if position_in_leaf <= cards_per_page:
        page_text = "Front page"
        sleeve_position = position_in_leaf
    else:
        page_text = "Back page"
        sleeve_position = position_in_leaf - cards_per_page

    return leaf_number, page_text, sleeve_position

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the leaf, page, and sleeve position for a given card number.")
    parser.add_argument("--card-number", type=int, required=True, help="The card number to find the leaf, page, and sleeve position for.")
    args = parser.parse_args()

    leaf, page, sleeve = calculate_leaf_page_and_sleeve(args.card_number)
    print(f"Card number {args.card_number} should be placed in leaf {leaf}, {page}, sleeve position {sleeve}.")