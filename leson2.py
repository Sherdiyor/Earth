import re

from transliterate import translit
from num2words import num2words


text_1 = (
    'Ladies and gentlemen, I\'m 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also '
    'told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen. '
)

text_2 = (
    'More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...'
)

print(translit(text_1, 'ru'))
print(" ")
print(translit(text_2, 'ru'))
print(" ")

full_text = text_1 + ' ' + text_2
numbers = re.findall(r'\d+', full_text)

for number in numbers:
    print(f'{number} - {num2words(int(number))}')
