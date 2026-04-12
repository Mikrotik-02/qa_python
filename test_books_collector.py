from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_does_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
    
    import pytest

    @pytest.mark.parametrize('name',['','a'*41])
    def test_add_new_book_not_add_invalid_book(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0
    
    def test_set_book_genre_genre_set_for_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.set_book_genre('Кыца убийца', 'Комедии')
        assert collector.get_book_genre('Кыца убийца') == 'Комедии'
    
    def test_set_book_genre_not_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.set_book_genre('Кыца убийца', 'Триллер')
        assert collector.get_book_genre('Кыца убийца') == ''
    
