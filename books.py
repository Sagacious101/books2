import os


books = []

def menu(books) -> None:
	os.system("cls")
	print_books(books)
	print("\nЧто будете делать?\n")
	options =["Добавить книгу в библиотеку",
	"Удалить книгу из библиотеки",
	"Найти книгу в библиотеке",
	"Узнать более подробную информацию о книге"]
	option = choose_option(options)
	if option == 1:
		add_book(books)
	elif option == 2:
		print("Какую книгу желаете удалить?")
		option = choose_option(books)
		option -= 1
		delete_book(books, option)
	elif option == 3:
		options =["Найти книги по названию",
		"Найти книги по автору",
		"Найти книги по году"]
		option = choose_option(options)
		if option == 1:
			book_name = input("\nВведите название книги: ")
			book_search(books, "название", book_name)
		elif option == 2:
			book_author = input("\nВведите имя автора: ")
			book_search(books, "автор", book_author)
		elif option == 3:
			book_year = input("\nВведите год написания книги: ")
			book_search(books, "год", book_year)
	elif option == 4:
		num_book = input("\nВведите порядковый номер книги: ")
		if num_book.isdigit():
			num_book = int(num_book)
			if num_book > 0 and num_book <= len(books):
				num_book -= 1
				info_book(books[num_book])
			else:
				print("Ошибка! В библиотеке нет книги под данным порядковым номером.")
				input("Нажмите ENTER чтобы продолжить: ")
				return menu(books)
		else:
			print("Ошибка! Введён не коректный порядковый номер.")
			input("Нажмите ENTER чтобы продолжить: ")
			return menu(books)

def add_book(books: list) -> dict:
	name = input("\nВведите название книги: ")
	if not name:
		print("Ошибка! Не указано название.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	author = input("Введите автора книги: ")
	if not author:
		print("Ошибка! Не указан год.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	year = input("Введите год написания книги: ")
	if not year:
		print("Ошибка! Не указан год.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	if year.isdigit():
		year = str(year)
	else:
		print("Ошибка! Введён не коректный год.")
		input("Нажмите ENTER чтобы продолжить: ")
		return menu(books)
	for num in range(len(books)):
		if books[num]["название"] == name and books[num]["автор"] == author and books[num]["год"] == year:
			print("\nТакая книга уже есть!")
			input("\nНажмите ENTER чтобы продолжить: ")
			return menu(books)
	book = {
	"название": name,
	"автор": author,
	"год": year 
	}
	books.append(book)
	return menu(books)


def choose_option(options: list) -> int:
	for num, option in enumerate(options):
		num += 1
		print(f"{num}.{option}")
	option = input("\nВведите номер варианта и нажмите ENTER: ")
	try:
		option = int(option)
	except ValueError:
		print("\nВвод дожен быть целым не отрицательным числом")
		return choose_option(options)
	else:
		if option <= len(options) and option > 0:
			return option
		else:
			print("Нет такого выбора")
			return choose_option(options)

def book_search(books: list, filter: str, text:str) -> None:
	print("")
	for num, book in enumerate(books):
		if book[filter] == text:
			num += 1
			print(f"{num}.{book['название']}")
	input("\nНажмите ENTER чтобы продолжить: ")
	return menu(books)

def info_book(book: dict) -> None:
	print("\nНазвание книги:", book["название"])
	print("Автор книги:", book["автор"])
	print("Год написания книги:", book["год"])
	input("\nНажмите ENTER чтобы продолжить: ")
	return menu(books)

def delete_book(books: list, num: int) -> None:
	if num >= 0 and num < len(books):
		books.pop(num)
	else:
		print("Нет такой книги")
		input("\nНажмите ENTER чтобы продолжить: ")
		return menu(books)

def print_books(books: list) -> None:
	print("Имеющиеся книги в библиотеке:\n")
	if not books:
		print("Пусто")
	else:
		for num, book in enumerate(books):
			num += 1
			print(f"{num}.{book['название']}")

menu(books)