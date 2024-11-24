with open('books/frankenstein.txt','r') as file:
        Books = file.read();
        #print(Books);
        words = Books.split()
        print(len(words));
        CharCount = Books;
        LowChar = CharCount.lower(); 
        Letters = count_letters(LowChar)
        
        
def count_letters(s):
        letter_counts = {}
        for char in s:
                if char in letter_counts:
                        letter_counts[char] += 1
                else:
                        letter_counts[char] = 1
        return letter_counts