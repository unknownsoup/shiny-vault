# Handles dynamic inputting of digits and selection of pokemon
linkcode = "3047"

# function to navigate the cursor
def navigate(row, col):
            if row < 0:
                for i in range(abs(row)):
                    print("Moving DOWN")
            elif row > 0:
                for i in range(row):
                    print("Moving UP")

            if col < 0:
                for i in range(abs(col)):
                    print("Moving RIGHT")
            elif col > 0:
                for i in range(col):
                    print("Moving LEFT")


def test_linkcode(linkcode):

    pad_positions = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "0": (3, 1)
    }
    """
    Always adjust the row first, then the column
    UNLESS the next digit is 0, then just adjust the column first
    """
    cursor_loc = (0, 0)
    for digit in linkcode:
        # get the target digit's position
        target_digit = pad_positions[digit]
        # update linkcode to remove the working digit
        linkcode = linkcode[1:]

        # Special case for digit 0
        #     Move the cursor to the column first, then the row
        if digit == "0":
            col = cursor_loc[1] - target_digit[1]
            navigate(0, col)
            row = cursor_loc[0] - target_digit[0]
            navigate(row, 0)
        else:
            # finding exacltly how many rows and columns to move
            row, col = tuple(a-b for a, b in zip(cursor_loc, target_digit))

            # navigate the cursor
            navigate(row, col)

        # set the current cursor location
        cursor_loc = target_digit
        
        print(f"Moving to {cursor_loc}")
    


test_linkcode(linkcode)


# Creating the simulated database that's an exact copy of the Trading Switch's Boxes
pokemon_db = {}
for box in range(1, 33):  # 32 boxes
    for row in range(1, 6):  # 5 rows per box
        for col in range(1, 7):  # 6 columns per row
            id_num = ((box - 1) * 30) + ((row - 1) * 6) + col
            pokemon_db[id_num] = {
                "box": box,
                "row": row,
                "col": col,
                "present": True,  # True means Pokémon is still there
            }

# when a pokemon is traded run
# pokemon_db[id]["present" = False]
start_id = 0
end_in = 0

def print_pokemon_range(start_id, end_id, db):
    for id_num in range(start_id, end_id + 1):
        poke = db.get(id_num, None)
        if poke:
            status = "Available" if poke["present"] else "Traded"
            print(f"ID {id_num}: Box {poke['box']}, Row {poke['row']}, Col {poke['col']} - {status}")

# Example: Print Pokémon IDs 40 to 50
#print_pokemon_range(40, 50, pokemon_db)

#print(type(pokemon_db))
