import qrcode


PG_BLUE = (27, 54, 87)
PG_GREEN = (0, 174, 150)

dados = {
    'imagem': "https://img.youtube.com/vi/doT7koXt9vw/maxresdefault.jpg",
    'video': 'https://youtu.be/bMLbf10uC0Y',
    'audio': 'https://open.spotify.com/episode/4qQasqKs6lKFFYRQOWWx3L?si=2af9d92168ee4d50'
}


if __name__ == '__main__':
    cores = [(PG_BLUE, 'white'), ('white', PG_GREEN), (PG_GREEN, PG_BLUE)]
    for i, (chave, valor) in enumerate(dados.items()):
        qr = qrcode.QRCode(None, 
                        qrcode.ERROR_CORRECT_H)
        qr.add_data(valor)
        img = qr.make_image(fill_color=cores[i][0], back_color=cores[i][1])
        img.save(f'img/{chave}.png')