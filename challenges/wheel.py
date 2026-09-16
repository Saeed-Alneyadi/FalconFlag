target = [15,55,95,39,71,79,230,30,132,164,46,54,244,244,156,38,172,140,46,172,244,252,46,132,164,148,156,172,22,140,38,214]
def rol8(v): return ((v << 3) | (v >> 5)) & 255
s = input("Flag: ").encode()
print("Correct" if [rol8(x ^ 0xa7) for x in s] == target else "Incorrect")
