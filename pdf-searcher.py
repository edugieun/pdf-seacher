from ast import keyword
from fileinput import filelineno, filename
from hashlib import new
from pydoc import pathdirs
from turtle import filling
import PyPDF2
import os
from IPython import embed
# 문자열 모든 단어 검색하려면 필요
import re
import os






def search_keyword(files, keyword):
    path_dir = 'C:/Users/gieun/Desktop/pdf-seacher/sample'
    how_many_word_you_want = 50
    # 파일 리스트 넣을 곳
    new_file_list = []
    for file in files:
        # PDF를 읽기 위해 변환
        pdf_file = open(path_dir + '/' + file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file, strict=False)

        # 페이지 개수 numPages
        num_of_pages = pdf_reader.numPages

        # 파일 내 검색 및 키워드 주변 출력
        for i in list(range(num_of_pages)):
            content = pdf_reader.getPage(i).extractText()
            keyword_index = [j.start() for j in re.finditer(keyword, content.lower())]

            for k in keyword_index:
                if k < how_many_word_you_want:
                    print(content[k:k + how_many_word_you_want])
                elif (k + how_many_word_you_want) >= len(content):
                    print(content[k - how_many_word_you_want:k])
                else:
                    print(content[k - how_many_word_you_want:k + how_many_word_you_want])
                print()
        # 검색된 키워드가 존재한다면 추가 검색을 위해 새로운 리스트에 넣어줌
        if keyword_index:
            new_file_list.append(file)
    # 재검색
    print("재검색이 필요 없으시면 엔터를 눌러주세요\n new keyword : ", end='')
    new_keyword = input()
    if new_keyword == "":
        return
    search_keyword(new_file_list, new_keyword)
    return


# def __main__():
file_list = os.listdir(path_dir)
print("검색하실 키워드를 입력해 주세요!!\nkeyword : ", end='')
user_keyword = input()
search_keyword(file_list, user_keyword)

# pdf1 : 문장1, 문장2, 문장3
# pdf2 : 문장1, 문장2, 문장3

# 221102 키워드 검색 및 주변 문장 검색까지 완료
# 221105 키워드1 검색한 논문 내에서 키워드2 재검색

# 필요 버튼
# 1. 검색
# 2. 재검색
# 3. 폴더 선택 버튼