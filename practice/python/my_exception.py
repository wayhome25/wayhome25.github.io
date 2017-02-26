# 다른파일의 클래스를 불러온다
from my_exception_list import UnexpectedRSPValue

value = input('가위, 바위, 보 중 하나를 선택하세요 >')
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print('입력 값이 올바르지 않습니다.')
