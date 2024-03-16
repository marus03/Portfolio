import qrcode

class MyQRC:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size = size, border = padding)


    def create_qr(self, file_name: str, fg: str, bg: str):
        user_inp: str = input('Enter: ')

        try:
            self.qr.add_data(user_inp)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f'Successfully created QR {file_name}')

        except Exception as e:
            print(f'Error: {e}')


def main():
    myqr = MyQRC(size=30, padding=3)
    myqr.create_qr('image1.png', fg='black', bg='white')


if __name__ == '__main__':
    main()