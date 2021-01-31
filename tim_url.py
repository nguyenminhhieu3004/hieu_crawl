# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re


# Hàm tìm kiếm các URL liên quan để tải xuống
# Truyền vào URL cần được quét, và URL xuất phát
# Kết quả trả về là tập hợp các URL tìm được
def tim_url_lien_quan(url, url_goc):
    url_tim_duoc = set()
    link = requests.get(url)
    link_soup = BeautifulSoup(link.text, 'html.parser') #dùng để cho ngôn ngữ hiểu
    results = link_soup('a', attrs={'href': True})
    for i in results:
        a = i['href']
        mau1 = '^http[^?#]*$' # biểu thức chính qui
        mau2 = '^/[^?#]*$'
        if re.match(mau1, a): # So sánh mẫu với a, đúng thì add a vào url_tim_duoc
            url_tim_duoc.add(a)
        else:
            if re.match(mau2, a):
                url_lien_quan = url_goc + a
                url_tim_duoc.add(url_lien_quan)
    return url_tim_duoc


# Tăng số lượng URL trong tập hợp lên
# Cần truyền vào một set gồm các phần tử cần được duyệt, và URL xuất phát
# Kết quả trả về tập hợp các URL có số phần tử đạt yêu cầu
def them_va_duyet_hang_cho(hang_cho, url_goc):
    history = hang_cho
    while (len(hang_cho) > 0) and (len(history) < 500):


        # dùng để lọc ra các link cần được duyệt
        # toán tập hợp, để khỏi gặp trường hợp bị trùng link
        url_tim_duoc = tim_url_lien_quan(hang_cho.pop(), url_goc)
        hang_cho = hang_cho | (url_tim_duoc - history)
        history = history | url_tim_duoc
    return history
