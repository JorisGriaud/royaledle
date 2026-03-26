import json

def process_cards():
    with open('cards_cr.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update meta attributes
    if 'meta' in data and 'attributes' in data['meta']:
        if 'icon_path' not in data['meta']['attributes']:
            data['meta']['attributes'].append('icon_path')

    # Update cards
    for card in data.get('cards', []):
        key = card.get('key')
        card['icon_path'] = f"assets/clash_royale_cards/{key}.png"

    with open('cards_cr.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    process_cards()
