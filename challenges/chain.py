target = [145,248,230,41,246,18,181,70,85,32,245,0,148,29,127,64,100,128,26,102,191,11,103,186,56,189,92,52,173,84,19,186]
state = 0x42
result = []
for byte in input("Flag: ").encode():
    state = (byte + state * 3) & 255
    result.append(state ^ 0x9d)
print("Correct" if result == target else "Incorrect")
