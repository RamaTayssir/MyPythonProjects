#setup
Library = []

# Adding Individual BooksI
books = input("Enter the name of a book you own: ")
Library.append(books)

another_books = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if another_books:
 Library.append(another_books)
else:
 Library == books
print(f"your Library: {Library}")

# Managing the Wishlist
wishList=[]
wList = input("Enter the name of a book you wish to have in the future: ")
wishList.append(wList)

another_wList = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if another_wList:
 wishList.append(another_wList)
else:
 wishList== wList

print(f"Your wishlist: {wishList}")

# Merging Wishlist into Library
acquired_book = input("Enter the name of a book from your wishlist that you're acquired (or press 'Enter' to skip): ")

if acquired_book in wishList:
 wishList.remove(acquired_book)
 Library.append(acquired_book)
else:
 print("Sorry, you don't have this book in your wishlist! ")

print(f"Update library: {Library}")
print(f"Update wishlist: {wishList}")

# Donating Books
donate_book = input("Enter the name of abook from your library your wish to donate (or press 'Enter' to skip): ")
if donate_book in Library:
 Library.remove(donate_book)
else:
 print("Sorry, you don't have this book in your Library!")
 
print(f"Final library after Donations: {Library}")