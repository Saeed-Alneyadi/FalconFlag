target = [28,30,8,22,1,7,215,29,23,20,37,14,220,6,214,201,51,206,60,53,42,47,249,44,36,246,216,237,214,208,202,128]
s = input("Flag: ").encode()
result = [((v + i * 3) & 255) ^ 0x5a for i, v in enumerate(s)]
print("Correct" if result == target else "Incorrect")
