# Handles dynamic inputting of digits and selection of pokemon
linkcode = "34858531"
def test_linkcode(linkcode):

    pad1 = (0, 0)
    pad2 = (0, 1)
    pad3 = (0, 2)
    pad4 = (1, 0)
    pad5 = (1, 1)
    pad6 = (1, 2)
    pad7 = (2, 0)
    pad8 = (2, 1)
    pad9 = (2, 2)
    pad0 = (3, 1)
    """
    Always adjust the row first, then the column
    UNLESS the next digit is 0, then just adjust the column first
    """
    cursor_loc = (0, 0)

    for digit in linkcode:
        if digit == "1":
            digit = pad1
        elif digit == "2":
            digit = pad2
        elif digit == "3":
            digit = pad3
        elif digit == "4":
            digit = pad4
        elif digit == "5":
            digit = pad5   
        elif digit == "6":
            digit = pad6
        elif digit == "7":
            digit = pad7
        elif digit == "8":
            digit = pad8
        elif digit == "9":
            digit = pad9
        elif digit == "0":
            digit = pad0
        # update linkcode to remove the working digit
        linkcode = linkcode[1:]

        # how the cursor moves
        result = tuple(a-b for a, b in zip(cursor_loc, digit))

        # set the current cursor location
        cursor_loc = digit
        print(f"Moving cursor to {cursor_loc} with result {result}")


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
