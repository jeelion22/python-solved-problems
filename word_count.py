file_name = input("\nEnter file: ")

fhand = open(file_name, "r")
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigword = None
bigcount = None

for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(f'The word "{bigword}" appears {bigcount} times.\n')
