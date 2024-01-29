result = 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
print(result)

spam = ['hello', 'hi', 'howdy', 'heyas']
catresult = 'cat' in spam
howdyresult = 'howdy' not in spam
print(catresult)
print(howdyresult)

spam = ['hello', 'hi', 'howdy', 'heyas']
result1 = 'cat' in spam
result2 = 'howdy' not in spam
result3 = 'cat' not in spam

print(f"Result 1: {result1}, Result 2: {result2}, Result 3: {result3}")

print(f"{result1}, {result2}, {result3}")

print("Result 1: " + str(result1) + ", Result 2: " + str(result2) + ", Result 3: " + str(result3))

print(str(result1) + ", " + str(result2) + ", " + str(result3))