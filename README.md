How It Works
Take an image and convert it to binary—a long string of 0s and 1s. Map these bits to the chessboard's colors: white squares represent 0, black squares represent 1.
Set up two bots on Lichess to play against each other. For each bit, the bot makes a move to a square matching the bit's value (e.g., to a white square for 0, like e4). The game continues until all bits are encoded. If it ends early, the bot starts a new game automatically.
Once complete, collect the PGN files from the games, decode them back to binary, and reconstruct the original image.
