import json

def add_icons():
    assets_path = 'assets.json'
    cards_path = 'cards_cr1.json'
    output_path = 'cards_cr_updated.json'

    with open(assets_path, 'r', encoding='utf-8') as f:
        assets_data = json.load(f)

    with open(cards_path, 'r', encoding='utf-8') as f:
        cards_data = json.load(f)

    assets_map = {}
    for item in assets_data.get('items', []):
        name = item.get('name')
        icon_url = item.get('iconUrls', {}).get('medium')
        if name and icon_url:
            assets_map[name] = icon_url

    updated_count = 0
    not_found = []

    for card in cards_data.get('cards', []):
        name_en = card.get('name_en')
        
        if name_en in assets_map:
            card['icon'] = assets_map[name_en]
            updated_count += 1
        else:
            not_found.append(name_en)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cards_data, f, indent=2, ensure_ascii=False)
    print(f"Fichier {output_path} sauvegardé")

    if not_found:
        print(f"\n{len(not_found)} cartes non trouvées:")
        for name in not_found:
            print(f"\t{name}")

add_icons()
