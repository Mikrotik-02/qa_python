from main import BooksCollector
import pytest
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

    @pytest.mark.parametrize('genre, expected_count', [('Комедии', 2), ('Ужасы', 1),])
    def test_get_books_with_specific_genre_returns_correct_count(self, genre, expected_count):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Кыца убийца', 'Комедии')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert len(collector.get_books_with_specific_genre(genre)) == expected_count
    
    def test_get_books_for_children_returns_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Кыца убийца', 'Комедии')
        collector.set_book_genre( 'Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_for_children() == ['Кыца убийца']

    def test_add_book_in_favorites_add_two_favorite_books(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Кыца убийца')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        result = collector.get_list_of_favorites_books()

        assert len(result) == 2
        assert 'Кыца убийца' in result
        assert 'Гордость и предубеждение и зомби' in result

    def test_add_book_in_favorites_not_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.add_new_book('Кыца убийца')
        collector.add_book_in_favorites('Кыца убийца')
        assert len(collector.get_list_of_favorites_books()) == 1
    
    def test_add_book_in_favorites_not_add_book_not_in_book_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Кыца убийца')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.add_book_in_favorites('Кыца убийца')
        collector.delete_book_from_favorites('Кыца убийца')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_delete_invalid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кыца убийца')
        collector.add_book_in_favorites('Кыца убийца')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Кыца убийца']