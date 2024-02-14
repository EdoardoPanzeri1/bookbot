def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        
        counting_dict = count_letters(file_contents)
        sorting_list = chars_dict_to_sorted_list(counting_dict)
        
        print(f"--- Begin report of books/frankestein.txt ---")
        print(f"{num_words} words found in the document")
        print()
        for i in sorting_list:
            print(f"The  {i["char"]} character was found {i["num"]} times")
        
        print("--- End report ---")
        
        
    
def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_letters(file_contents):
    count_dic = {}
    for i in file_contents:
        lowered = i.lower()
        if i.isalpha() is True:  
            if lowered in count_dic:
                count_dic[lowered] += 1
            else:
                count_dic[lowered] = 1
            
    return count_dic

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




main()
