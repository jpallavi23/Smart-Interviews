'''
When Valera has got some free time, he goes to the library to read some books. Today he's got t free minutes to read. That's why Valera took n books in the library and for each book he estimated the time he is going to need to read it. Let's number the books by integers from 1 to n. Valera needs ai minutes to read the i-th book.

Valera decided to choose an arbitrary book with number i and read the books one by one, starting from this book. In other words, he will first read book number i, then book number i + 1, then book number i + 2 and so on. He continues the process until he either runs out of the free time or finishes reading the n-th book. Valera reads each book up to the end, that is, he doesn't start reading the book if he doesn't have enough free time to finish reading it.

Print the maximum number of books Valera can read.
Input

The first line contains two integers n and t (1 ≤ n ≤ 105; 1 ≤ t ≤ 109) — the number of books and the number of free minutes Valera's got. The second line contains a sequence of n integers a1, a2, ..., an (1 ≤ ai ≤ 104), where number ai shows the number of minutes that the boy needs to read the i-th book.
Output

Print a single integer — the maximum number of books Valera can read.

Examples
Input
4 5
3 1 2 1

Output
3

Input
3 3
2 2 3

Output
1
'''

no_of_books, total_free_time = map(int, input().split())
book_time = list(map(int, input().split()))
books_read_count = res = 0
for book in range(no_of_books):
    res += book_time[book]
    if res > total_free_time:
        res -= book_time[books_read_count]
        books_read_count += 1
print(no_of_books - books_read_count)