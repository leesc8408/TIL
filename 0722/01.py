import requests


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    url = f'https://api.themoviedb.org/3/movie/popular?api_key=a275979c03887da2638b3b3aabee6ccf&language=ko'    # &language=ko : 한글전환
    respon = requests.get(url)
    data = respon.json()    # 응답값 data에 할당
    # print(data.keys())    # 키값 확인
    a = len(data.get('results'))
    return  a


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
