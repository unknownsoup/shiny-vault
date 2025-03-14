# Handles pokemon selection and transfer

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
print_pokemon_range(40, 50, pokemon_db)

    
print(type(pokemon_db))

