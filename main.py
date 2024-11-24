from count_letters import count_L
with open('books/frankenstein.txt','r') as file:
        Books = file.read();
        #print(Books);
        words = Books.split()
        print(len(words));
        CharCount = Books;
        LowChar = CharCount.lower(); 
        Letters = count_L(LowChar);
        print(Letters)