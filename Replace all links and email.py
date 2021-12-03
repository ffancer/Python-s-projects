# Дана строка. Заменить все ссылки и email на ***** (количество звездочек равно длине заменяемого фрагмента).
# Примеры ссылок: www.site.com, http://site.com и т.п. Решить двумя способами: с использованием
# регулярных выражений и без. Сравнить скорости работы.

# Given a string. Replace all links and email with ***** (the number of asterisks is equal to the length
# of the fragment being replaced). Examples of links: www.site.com, http://site.com, etc.
# Solve in two ways: using regular expressions and without. Compare the speed of work.

def replace_links(s):
    return '*' * len(s)


print(replace_links('http://site.com'))
print(replace_links('www.site.com'))
print(replace_links('http://12345678.bra'))
print(replace_links('азбука.ру'))
print(replace_links('www.JOHN_CENA.com'))
