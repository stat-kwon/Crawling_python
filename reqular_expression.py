import re

"정규 표현식 연습하기"

# 영어가 아닌 것을 모두 제거
string =  "(Dave)"
print(re.sub("[^a-zA-Z]","",string))

# 숫자 제거후 빈칸 모두 삭제
string = "0h20hf0 hqg94hgueif   abn29hg9ru    gbg0q84h9uegrh     210hr9"
print(re.sub(" ", "", re.sub('[0-9]','', string)))


# 1. 기본적인 패턴 만들기
# 패턴 만들기
pattern = re.compile('D.A')

# 세글자 중 첫글자는 D 마지막 글자는 A에 해당하면 찾기
# 첫번째 만 해당되므로 if pattern == None으로 조건 걸어서 제약을 줄 수 있음
print(pattern.search("D0A"))
print(pattern.search("D0A")[0])
print(pattern.search("D0000A"))
print(pattern.search("DA"))
print(pattern.search("daaA"))
print()
print()

# 정말 dot이 들어간 것을 찾으려면 아래와 같이 패턴을 주면 됨
pattern = re.compile('D\.A')

# 2. 반복 ?, *, +
# 많이 헷갈리는 개념
# ?는 앞 문자가 0번 또는 1번 표시되는 패턴 (없어도 되고 한번 있어도 되는 패턴)
# *는 앞 문자가 0번 또는 그 이상 반복되는 패턴
# +는 앞 문자가 1번 또는 그 이상 반복되는 패턴
# 모두 앞문자가 기준이라는 것을 알아두자

# 앞에 문자 D가 없거나, 여러번 반복되고 마지막이 A 인 문자열
pattern = re.compile('D?A')
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDA"))
print(pattern.search("DDDDDDDA"))
print()
print()

# 앞에 문자 D가 없거나, 여러번 반복되고 마지막이 A 인 문자열
# 정확한 사용 예제는 잘 모르겠음
pattern = re.compile('D*A')
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA"))
print()
print()

# 끝문자가 A로 끝나면서 D를 한번내지 여러개 포함한 문자
# 실질적으로 가장 많이 쓸 것으로 판단됨
pattern = re.compile('D+A')
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA"))
print()
print()

# 3. 또다른 반복 표현
# 또다른 반복 표현: {n}, {m,n}
# {n} : 앞 문자가 n 번 반복되는 패턴
# {m, n} : 앞 문자가 m 번 반복되는 패턴부터 n 번 반복되는 패턴까지
pattern = re.compile('AD{2}A')
print(pattern.search("ADA"))
print(pattern.search("ADDA"))
print(pattern.search("ADDDA"))
print(pattern.search("AADDA"))