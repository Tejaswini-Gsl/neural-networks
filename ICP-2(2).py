from collections import OrderedDict

with open('input.txt', 'r') as f:
    lines = f.readlines()

word_counts = OrderedDict()
print(word_counts)
for line in lines:
    words = line.strip().split(' ')
    for word in words:
        print(word)
        if word not in word_counts:
            print(word_counts)
            word_counts[word] = 0
        word_counts[word] += 1
print(word_counts)

with open('output.txt','w') as out:  
    for line in lines:
        out.write(line)
      
    out.write('\nWord_Count:\n')
    for word, count in word_counts.items():
        out.write(f'{word}: {count}\n')
        