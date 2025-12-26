import subprocess
import socket
from pathlib import Path
# import chess

word = "hello world"
bstr = "10001001 01010000 01001110 01000111 00001101 00001010 00011010 00001010 00000000 00000000 00000000 00001101 01001001 01001000 01000100 01010010 00000000 00000000 00000000 00000001 00000000 00000000 00000000 00000001 00001000 00000110 00000000 00000000 00000000 00011111 00010101 11000100 10001001 00000000 00000000 00000000 00001101 01001001 01000100 01000001 01010100 01111000 11011010 01100011 01100100 11111000 11001111 01010000 00001111 00000000 00000011 10000110 00000001 10000000 01011010 00110100 01111101 01101011 00000000 00000000 00000000 00000000 01001001 01000101 01001110 01000100 10101110 01000010 01100000 10000010"

BITS = []

for b in bstr:
    if b in ['0', '1']:
        BITS.append(b)

# for char in word:
#     bin = list(format(ord(char), "08b"))
#     BITS += bin


total = len(BITS)
print("total: ", total)
# print("BITS:", ''.join(BITS))
SOCK = "/tmp/binary.sock"

try:
    Path(SOCK).unlink()
except FileNotFoundError:
    pass

server = socket.socket(socket.AF_UNIX)
server.bind(SOCK)

server.listen(1)
 # subprocess.Popen(["/home/linuxer77/Programming Stuff/GO/chessStorj/bot1/lichess-bot-master/venv/bin/python", "/home/linuxer77/Programming Stuff/GO/chessStorj/bot1/lichess-bot-master/lichess-bot.py"], cwd="/home/linuxer77/Programming Stuff/GO/chessStorj/bot1/lichess-bot-master/")
# subprocess.Popen(["/home/linuxer77/Programming Stuff/GO/chessStorj/bot2/lichess-bot-master/venv/bin/python", "/home/linuxer77/Programming Stuff/GO/chessStorj/bot2/lichess-bot-master/lichess-bot.py"], cwd="/home/linuxer77/Programming Stuff/GO/chessStorj/bot2/lichess-bot-master/")
i = 1
print("Server listening")
while BITS:
    conn, _ = server.accept()
    if not BITS:
        conn.close()
        break
    bit = BITS[0] 
    print("Remaining: ", total - i)
    i += 1
    if bit not in ["0", "1"]:
        BITS.pop(0)
        conn.close()
        continue
    
    try:
        conn.send(bit.encode())
        response = conn.recv(1024).decode()
        BITS.pop(0)
    except Exception as e:
        print(f"Error: {e}")
    
    conn.close()

subprocess.run(["pkill", "-f", "lichess-bot.py"])
