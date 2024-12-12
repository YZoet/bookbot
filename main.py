from count_letters import count_L
with open('books/frankenstein.txt','r') as file:
        Books = file.read();
        words = Books.split()
        Length = (len(words));

        CharCount = Books;
        LowChar = CharCount.lower(); 
        Letters = count_L(LowChar);
        
        char_list = []
        for char, count in Letters.items():
                if char.isalpha():
                        char_dict = {"Letter": char, "count": count}
                        char_list.append(char_dict)
        def sort_on(dict):
                return dict["count"]
        char_list.sort(reverse =True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{Length} words found in the document")
        for dictonary in char_list:
                Symbol = dictonary['Letter']
                number = dictonary['count']
                print(f"The {Symbol} character was found {number} times")
        print("--- End report ---")