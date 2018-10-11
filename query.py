import pickle
import operator

toLoad = "./invert_index.p"


def query(word, invert_index):
    print("Search result of the word \"" + word + "\"")
    word = word.lower()
    result = []
    if word in invert_index:
        file_list = invert_index[word]
        sorted_by_value = sorted(file_list.items(), key=operator.itemgetter(1), reverse=True)
        for i in sorted_by_value:
            if i[1] > 1:
                result.append(i[0] + " " + str(i[1]) + " matches")
            else:
                result.append(i[0] + " " + str(i[1]) + " match")
    else:
        result.append("Not found.")

    print("\n".join(result))


def main():
    invert_index = pickle.load(open(toLoad, "rb"))
    word = input("Input a word to query. \n")
    query(word, invert_index)


if __name__ == "__main__":
    main()