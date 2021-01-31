import tim_url
import tai_url

def main():
    url_goc = input('Nhập link khởi đầu: ')
    # tìm các link liên quan với link khởi đầu
    url_tim_duoc = tim_url.tim_url_lien_quan(url_goc, url_goc)

    # thêm tiếp url liên quan
    hang_cho = url_tim_duoc
    history = tim_url.them_va_duyet_hang_cho(hang_cho, url_goc)

    # lưu file lại
    tai_url.tao_thu_muc(input('nhập tên thư mục: '))
    tai_url.luu_file(history)


if __name__ == '__main__':
    main()

