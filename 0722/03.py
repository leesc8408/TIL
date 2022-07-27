import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.  
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=a275979c03887da2638b3b3aabee6ccf&language=ko'    
    respon = requests.get(url)
    data = respon.json()    
    avg5 = [] 
    n = []
    
    for i in (data.get('results')): 
      n.append(i.get('vote_average')) # 평점을 리스트(n)에 모음
    n_list = sorted(n) # 평점들을 순차 정렬 
    n_list.reverse()  # 리버스 
    # print(n_list)
    for i in (data.get('results')):         # 다시 반복문 돌면서
      if i.get('vote_average') >= n_list[4]:    # 평점을 리스트 n_list[4]값과 비교하여 리스트 추가
        avg5.append(i)
    return  avg5


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
