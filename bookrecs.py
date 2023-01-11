
def sort_books():
    find_books = open("booklist.txt", "r")
    book_list = []

    for book in find_books:
        split_list = book.strip().split(',')
        book_list.append((split_list[0], split_list[1]))
    find_books.close()
    return book_list


def sort_ratings():
    find_ratings = open("ratings.txt", "r")
    names_list = []
    ratings_list = []
    count = 0

    for line in find_ratings:
        count += 1
        if count % 2 != 0:
            names_list.append(line.strip().lower())
        else:
            person_ratings = line.split()
            person_rating_list = []
            for i in person_ratings:
                person_rating_list.append(int(i))
            ratings_list.append(person_rating_list)
    ratings_dictionary = dict(zip(names_list, ratings_list))

    find_ratings.close()
    return ratings_dictionary


def sort_recommendations(readers_name, symbol, rating, books, ratings):
    recommendations_list = []
    for name, number in ratings.items():
        if name == readers_name.lower():
            for i in range(len(number)):
                if symbol == ">":
                    if int(number[i]) > int(rating):
                        recommendations_list.append((books[i], number[i]))
                elif symbol == "<":
                    if int(number[i]) < int(rating):
                        recommendations_list.append((books[i], number[i]))
                elif symbol == "=":
                    if int(number[i]) == int(rating):
                        recommendations_list.append((books[i], number[i]))
    return recommendations_list


def get_input(ratings):
    while True:
        readers_name = input('Enter a reader’s name: ')
        if readers_name == "":
            print("bye!")
            exit()
        elif readers_name.lower() not in ratings:
            print("No such reader " + str(readers_name))
            continue
        else:
            break

    while True:
        symbol = input('Enter a symbol: ')
        if symbol == "":
            print("bye!")
            exit()
        elif symbol not in ('>', '<', '='):
            print("No such symbol")
            continue
        else:
            break

    while True:
        rating = input('Enter a rating: ')
        if rating == "":
            print("bye!")
            exit()
        elif rating not in ('-5', '-3', '0', '1', '3', '5'):
            print("No such rating")
            continue
        else:
            break

    return readers_name, symbol, rating


def print_recommendations(recommendations):
    if recommendations:
        for line in recommendations:
            print(*line, sep=", ", end='\n')
    else:
        print("No books found.")


def main():
    books = sort_books()
    ratings = sort_ratings()
    # input_name, input_symbol, input_rating = get_input(ratings)
    # recommendations = sort_recommendations(input_name, input_symbol, input_rating, books, ratings)
    recommendations = sort_recommendations("Ben", "<", "0", books, ratings)
    print_recommendations(recommendations)


if __name__ == '__main__':
    main()
