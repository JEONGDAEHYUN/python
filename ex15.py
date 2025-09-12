english_dict = {}

english=["one", "two", "three", "four", "five","six", "seven", "eight", "nine", "ten"]
kor=["하나", "둘", "셋", "넷", "다섯","여섯", "일곱", "여덟", "아홉", "열"]
i=0;

while i<=10:
    english_dict[english[i]]=kor[i]
    i += 1

print(english_dict)