# score = 78
# if score > 90:
#     print("Grade: A")
# elif score >80:
#     print("Grade: B")
# elif score > 70:
#     print("Grade: C")
# else:
#     print("Grade: E")

# print("Grade: ", score)

# # while
# n = 5
# while n > 0:
#     n -= 1
#     print(n)

for x in[1,2,3,4]:
    if x == 2:
        continue
    if x == 4:
        break
    print(x)

# List
squares = [x ** 2 for x in range(10)]
print(squares)

even_squares = [ x ** 2 for x in range(10) if x  % 2 == 0]
print(even_squares)

# string
text = "Deep learning is amazing"
print(text.lower())
print(text.upper())

print(text.split())
print(text.replace("amazing", "fantastic"))

# F string
model_name = "ResNet18"
accuracy = 0.99
print(f"Model: {model_name}, Accuracy: {accuracy:.2%}")

# Dict
from collections import defaultdict
words_count = defaultdict(int)
for word in "the cat sat on the mat the cat".split():
    words_count[word] +=1
print(dict(words_count))

def add_layer_fixed(layer, layers=None):
    if layers is None:
        layers = []
    layers.append(layer)
    return layers

accuracy = 87
acc = "positive" if accuracy >= 80 else "Negative" 
print(acc)

status = "Converged" if accuracy >= 78 else "Training"
print(status)

