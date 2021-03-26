import re


def find_names(file):
    with open('test1.txt', encoding='utf8') as f:
        contents = f.read()
        pattern = re.compile(r'[А-Я]{1}[а-я]+\s[А-Я]{1}[а-я]+\s[А-Я]{1}[а-я]+|[А-Я]{1}[а-я]+\s[А-Я]{1}[.][А-Я]{1}[.]')
        result = pattern.findall(contents)
    return result


if __name__ == '__main__':
    print(find_names('test1.txt'))