## How It Works

This project stores an image inside chess games by encoding its binary data into chessboard square colors.

### Step-by-step explanation

1. **Convert image to binary**  
   The image is turned into a long string of 0s and 1s (binary data).

2. **Map bits to square colors**  
   - `0` → white square  
   - `1` → black square

3. **Generate moves with Lichess bots**  
   Two bots play against each other on Lichess.  
   For each bit in the binary string:  
   - If the bit is `0` → move a piece to a **white** square (e.g. e4, d5, etc.)  
   - If the bit is `1` → move a piece to a **black** square  

   The bots keep making legal random moves to squares of the required color.

4. **Handle game endings**  
   If a game ends (checkmate, draw, etc.) before all bits are encoded, the bot automatically starts a new game and continues encoding.

5. **Decode the image**  
   After all bits are stored:  
   - Collect all the PGN files  
   - Extract the sequence of target square colors  
   - Convert back to binary (white = 0, black = 1)  
   - Rebuild the original image

### Purpose

Absolutely none.  
Just a fun, completely pointless steganography experiment using chess.
