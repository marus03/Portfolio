import os
import requests

def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['png', 'jpg', 'jpeg', 'gif', 'svg']
    for ext in extensions:
        if ext in image_url:
            return ext

def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f'{folder}/{name}.{ext}'
        else:
            image_name: str = f'{name}{ext}'
    else:
        raise Exception('Image could not be located')

    if os.path.isfile(image_name):
        raise Exception('File name already exists')

    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Downloaded "{image_name}" successfully')
    except Exception as e:
        print(f'Error: {e}')

def main():

    input_url: list[str] = ['https://i.pinimg.com/736x/08/62/47/08624776b9f75ce68d418756f0c7e42a.jpg', 'https://i.pinimg.com/564x/ec/b0/de/ecb0de8dbc2bfdd56e79776f57992e33.jpg', 'https://i.pinimg.com/564x/14/1b/83/141b83cad7fe34e20e605ec05f4f4c61.jpg', 'https://i.pinimg.com/564x/7e/1e/17/7e1e176b964265859408eed34281c726.jpg', 'https://i.pinimg.com/564x/85/a2/c8/85a2c8f09581e6d1c2abdddbb5f527cc.jpg']
    # input_name: str = input('What would you like to name it?: ')

    for i in range(len(input_url)):
        download_image(input_url[i], name=f'car_nr{i.__index__()}', folder='images')
        print('Downloading...')
    # download_image(input_url, name=input_name, folder='images')


if __name__ == '__main__':
    main()

