from Cards import Cards

import requests

cards = Cards()

def DownloadFile(url, local_filename):
    r = requests.get(url)
    f = open(f'./assets/clash_royale_cards/{local_filename}.png', 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:
            f.write(chunk)
    f.close()
    return

nbre_card = cards.get_number_of_cards()


for i in range(nbre_card):
    card = cards.get_card_by_id(i)
    card_name = card.get_key()
    card_url_image = card.get_icon_url()
    DownloadFile(card_url_image, card_name)