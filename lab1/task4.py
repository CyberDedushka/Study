from collections import defaultdict

def group_anagrams(words):
    # Создаем словарь, где ключ - это отсортированное значение слова,
    # а значение - список всех строк с таким же отсортированным значением
    anagram_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)

    # Сортируем значения в словаре и возвращаем списки всех групп
    return [anagram_dict[key] for key in sorted(anagram_dict)]


# Пример использования
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagram_groups = group_anagrams(words)
print(anagram_groups)
