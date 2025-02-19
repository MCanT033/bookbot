from traceback import print_list


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
    
book_contents = main()

def count(book_contents):
    count_list = book_contents.split()
    print (len(count_list))

count(book_contents)



def char_count(book_contents):
    char_dict = {}
    for i in book_contents:
        if i.lower() in char_dict:
            char_dict[i.lower()] += 1
        else:
            char_dict[i.lower()] = 1
    return char_dict

char_count(book_contents)

char_dict_out = char_count(book_contents)



def dict_to_listed_dict(char_dict):
    dict_list = []
    for char, num in char_dict.items():
        if char.isalpha():
            listed_dict = {"char": char, "num": num}
            dict_list.append(listed_dict)
    #print(dict_list)
    return dict_list

    
sort_in = dict_to_listed_dict(char_dict_out)

def sort_on(sort_in):
    sort_in.sort(reverse=True, key=lambda x:x["num"])
    for item in sort_in:
        char = item["char"]
        num = item["num"]
        print (f"The '{char}' character was found {num} times")
    
sort_on(sort_in)

