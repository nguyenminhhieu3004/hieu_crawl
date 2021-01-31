# Các thư viện cần thiết
import os
import requests
import codecs


# Hàm Tạo thư mục và chuyển đến thư mục đó
# Cần truyền vào cho hàm Tên thư mục
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)


# Hàm lưu tất cả các url đã tim được
# Truyền vào một List, set, tuples,... các URL hợp lệ
def luu_file(history):
    stt = 0
    for url_con in history:
        file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
        file.write(requests.get(url_con).text)
        file.close()
        print(url_con)
        stt += 1