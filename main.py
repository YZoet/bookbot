with open('books/frankenstein.txt','r') as file:
        Books = file.read();
        print(Books);
count = len(Books);
print(count);