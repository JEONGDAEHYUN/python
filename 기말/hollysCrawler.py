from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

#[CODE 1]
def hollys_store(result):
    # 1페이지부터 46페이지까지 반복 (매장 리스트 페이지 순회)
    for page in range(1, 47):
        # 페이지 번호(%d)를 포함하여 할리스커피 매장 리스트 URL 생성
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store' %page
        print(Hollys_url) # 현재 크롤링 중인 URL 출력 (진행 상황 확인용)

        # 생성된 URL에 요청을 보내고 HTML 응답을 받아옴
        html = urllib.request.urlopen(Hollys_url)

        # 받아온 HTML을 BeautifulSoup을 이용해 파싱(분석) 가능한 객체로 변환
        soupHollys = BeautifulSoup(html, 'html.parser')

        # HTML 내에서 실제 매장 정보가 담긴 <tbody> 태그 찾기
        tag_tbody = soupHollys.find('tbody')

        # <tbody> 내의 모든 <tr> 태그(행)를 하나씩 순회하며 정보 추출
        for store in tag_tbody.find_all('tr'):

            # <tr> 태그 내의 요소가 3개 이하라면 유효한 데이터가 아니라고 판단하여 루프 중단
            if len(store) <= 3:
                break

            # 현재 행(tr) 내의 모든 <td> 태그(열)를 찾아 리스트로 저장
            store_td = store.find_all('td')

            # 각 인덱스에 해당하는 정보 추출 (웹사이트 구조에 따라 인덱스 결정됨)
            store_name = store_td[1].string    # 매장명 (2번째 열)
            store_sido = store_td[0].string    # 지역(시/도) (1번째 열)
            store_address = store_td[3].string # 주소 (4번째 열)
            store_phone = store_td[5].string   # 전화번호 (6번째 열)

            # 추출한 정보를 리스트 형태로 묶어서 result 리스트에 추가
            result.append([store_name]+[store_sido]+[store_address]+[store_phone])
    return

def main():
    # 크롤링 결과를 저장할 빈 리스트 초기화
    result = []
    # 작업 시작을 알리는 메시지 출력
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>')

    # 'result' 리스트를 인자로 넘겨주면, 함수 내부에서 이 리스트에 데이터를 채움.
    hollys_store(result)  #[CODE 1] 호출

    # 크롤링이 완료된 result 리스트를 pandas DataFrame으로 변환
    # columns 옵션으로 DataFrame의 열(column) 이름을 지정
    hollys_tbl = pd.DataFrame(result, columns=('store','sido-gu','address','phone'))

    # DataFrame을 CSV 파일로 저장
    # './hollys.csv' : 현재 디렉토리에 'hollys.csv'라는 이름으로 저장
    # encoding='cp949' : 한글이 깨지지 않도록 'cp949' 인코딩 사용 (주로 Windows 환경)
    # mode='w' : 쓰기 모드 (파일이 존재하면 덮어쓰기)
    # index=True : DataFrame의 인덱스(0, 1, 2...)도 파일에 포함 (False로 하면 미포함)
    hollys_tbl.to_csv('./hollys.csv', encoding='cp949', mode='w', index=True)

    # 메모리 관리를 위해 사용했던 result 리스트의 모든 요소를 삭제
    del result[:]

# 이 스크립트 파일이 직접 실행될 때만 main() 함수를 호출하라는 의미
if __name__ =='__main__':
    main()