import re


def find_names(file):
    with open('test1.txt', encoding='utf8') as f:
        contents = f.read()
        pattern = re.compile(r'[А-Я][а-я]+\s[А-Я][а-я]+\s[А-Я][а-я]+|[А-Я][а-я]+\s[А-Я][.][А-Я][.]')
        result = pattern.findall(contents)
    return result


if __name__ == '__main__':
    print(find_names('test1.txt'))