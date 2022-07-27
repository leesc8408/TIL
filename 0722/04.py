import requests
from pprint import pprint


def recommendation(title):
    pass 
    # 여기에 코드를 작성합니다.  
    url = f'https://api.themoviedb.org/3'   # 입력할 url을 메인과
    path = f'/search/movie'                  # 사용하고자 하는 항목의 url로 분리
    params = {
        'api_key' : 'a275979c03887da2638b3b3aabee6ccf',     # api_key와
        'language' : 'ko',                                  # 언어설정
        'query' : title                                     # 검색 할 입력값(query)과 함수의 변수(title)
    }

    respon1 = requests.get(url + path, params = params).json()   # 위의 사항들로 응답값을 받아 json으로 전환
    # print(respon1, type(respon))
    
    chu_list = []
    id_list = []
    if respon1['results']:                      # 도저히 마지막 예시에서 에러나서 다른 분 코드 봤습니다.
        for i in respon1.get('results'):        # if문으로 응답값 중 'results'의 유무로 실행 여부를 판단 else면 None
            id_list.append(i.get('id'))
        # print(id_list)
        movie_id = id_list[0]

        url = f'https://api.themoviedb.org/3'           # 메인 url
        path = f'/movie/{movie_id}/recommendations'  # 추천 영화 조회 url 
        params = {
            'api_key' : 'a275979c03887da2638b3b3aabee6ccf',     # api_key와
            'language' : 'ko',                                  # 언어설정
            'movie_id' : movie_id                               # 검색할 영화 id
        }
        respon2 = requests.get(url + path, params = params).json()
        # print(respon2, type(respon2))
        for i in respon2.get('results'):
            chu_list.append(i.get('title'))
        return chu_list
    else:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
