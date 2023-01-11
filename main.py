

find_books = open("booklist.txt", "r")
book_list = []


for book in find_books:
    split_list = book.strip().split(',')
    book_list.append((splitList[0],splitList[1]))


book_rate = open("bookrecs.py", "r")
names = []
num_list = []
count = 0
for line in book_rate:
    if count % 2 != 0:
        names.append(line.strip().lower())
    else:
        personal_ratings = line.split()
        personal_ratings_list = []
        for i in personal_ratings:
            personal_ratings_list.append(int(i))
            num_list.append(personal_ratings_list)
ratings_dictionary = dict(zip(names, (num_list)))

def input():
    name = input("Enter Your Name!")
    name = name.split()
    name_list = []
    if len(name) == 1:
        for i in name:
            name_input.append(i)
        return name_input
    elif len(name) == 3:
        for i in name:
            name_input.append(i)
        return name_input
    elif len(name_input) == 5:
        for i in name:
            name_input.append(i)
        return name_input
    elif len(name_input) == 

    







