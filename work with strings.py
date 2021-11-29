# Дано предложение. Заменить группы пробелов одиночными, крайние пробелы удалить.
# Все слова перевести в нижний регистр, первые буквы сделать заглавными.
# A sentence is given. Replace groups of spaces with single ones, remove trailing spaces.
# Convert all words to lower case, capitalize the first letters.

def work_with_sentence(s):
    s = s.split()
    return' '.join(s).lower().title()


print(work_with_sentence('   BOB  wAnNa     be   a  doctor   '))
print(work_with_sentence('1    2   3  4  5         6'))
print(work_with_sentence('  margo     has     22     eggs             '))