import json

class Card():
    
    def __init__(self, card):
        self.card = card

    def get_dico(self):
        """ Return a dictionnary of the card"""
        return self.card

    def get_name(self):
        """ Return the french name of the card"""
        return self.card['name']
    
    def get_name_en(self):
        """ Return the english name of the card"""
        return self.card['name_en']

    def get_id(self):
        """ Return the id of the card"""
        return self.card['id']

    def get_key(self):
        """ Return the key (name of the card without uppercase and space and accent) of the card """
        return self.card['key']

    def get_elixir(self):
        """ Return the elixir of the card"""
        return self.card['elixir']

    def get_rarity(self):
        """ Return the rarity of the card"""
        return self.card['rarity']

    def get_type(self):
        """ Return the type of the card"""
        return self.card['type']

    def get_arena_unlock(self):
        """ Return the unlock arena of the card"""
        return self.card['arena_unlock']

    def get_damage(self):
        """ Return the damage of the card"""
        return self.card['damage']

    def get_damage_per_second(self):
        """ Return the damage per second of the card"""
        return self.card['damage_per_sec']

    def get_hitpoints(self):
        """ Return the health point of the card"""
        return self.card['hitpoints']

    def get_hit_speed(self):
        """ Return the hit speed of the card"""
        return self.card['hit_speed']

    def get_targets(self):
        """ Return the target of the card"""
        return self.card['targets']

    def get_speed(self):
        """ Return the speed of the card"""
        return self.card['speed']

    def get_range(self):
        """ Return the range of the card"""
        return self.card['range']

    def get_count(self):
        """ Return the number of the card"""
        return self.card['count']

    def get_attack_type(self):
        """ Return the attack type of the card"""
        return self.card['attack_type']

    def get_radius(self):
        """ Return the radius of the card"""
        return self.card['radius']

    def get_duration(self):
        """ Return the duration of the card"""
        return self.card['duration']

    def get_slowdown_ennemies(self):
        """ Return the slowdown_ennemies value of the card"""
        return self.card['slowdown_ennemies']

    def get_crown_tower_damage(self):
        """ Return the crown tower damage of the card"""
        return self.card['crown_tower_damage']

    def get_stun_duration(self):
        """ Return the stun duration of the card"""
        return self.card['stun_duration']

    def has_evolution(self):
        """ Return if the card has a evolution"""
        return self.card['has_evolution']

    def has_hero(self):
        """ Return if the card has a hero"""
        return self.card['has_hero']
    
    def get_release_year(self):
        """ Return the release year of the card"""
        return self.card['release_year']
    
    def get_icon_url(self):
        """ Return the url icon of the card"""
        return self.card['icon_url']
    
    def get_description(self):
        """ Return the description of the card"""
        return self.card['description']

    def get_icon_path(self):
        """ Return the icon path of the card"""
        return self.card['icon_path']

    def get_emojis(self):
        """ Return a list of emojis of the card"""
        return self.card['emojis']

    def get_portee_or_radius(self):
        """ Return the range or radius based on card type.
            For spells : returns radius
            For troops and buildings: returns range
        """
        if self.get_type() == "Sort":
            return self.get_radius()
        else:  # Troupe or Bâtiment
            return self.get_range()
class Cards():

    def __init__(self):
        with open("cards_cr.json", "r", encoding='utf-8') as f:
            item = json.load(f)

        self.item = item
        self.meta = item['meta']
        self.cards = item['cards']

    # META
    def get_number_of_cards(self):
        """ Return the number of card"""
        return len(self.cards)

    def get_attributes_list(self):
        """ Return possible attributes """
        return self.meta['attributes']

    def get_rarity_values(self):
        """ Return possible rarity values"""
        return self.meta['rarity_values']
    
    def get_type_values(self):
        """ Return possible type values"""
        return self.meta['type_values']

    def get_targets_values(self):
        """ Return possible targets values"""
        return self.meta['targets_values']
    
    def get_speed_values(self):
        """ Return possible speed values"""
        return self.meta['speed_values']

    def get_attack_type_values(self):
        """ Return possible attack type values"""
        return self.meta['attack_type_values']


    # CARDS
   
    def get_card_by_id(self, id: int):
        """
        Claim card by an id
        
        Param:
        id (int): Card's id
        
        Return:
        (Class) Class of the card
        """
        nb_card = self.get_number_of_cards()
        if id > nb_card or id < 0:
            raise Exception("Id not found")

        return Card(self.cards[id])
    
    def get_card_by_name(self, name: str):
        """
        Claim card by his name
        
        Param:
        name (string): Card's name in lowercase without space and accent
        
        Return:
        (Class) Class of the card
        """
        nb_card = self.get_number_of_cards()
        for i in range(nb_card):
            if self.cards[i]['name'] == name:
                return Card(self.cards[i])
        return None
    
    def get_card_by_key(self, key: str):
        """
        Claim card by his key
        
        Param:
        key (string): Card's name in lowercase without space and accent
        
        Return:
        (Class) Class of the card
        """
        nb_card = self.get_number_of_cards()
        for i in range(nb_card):
            if self.cards[i]['key'] == key:
                return Card(self.cards[i])
        return None
    
    def get_all_card_name_with_image_path(self):
        """
        Claim all card's name sorted in A to Z with this image relative path
                
        Return:
        (List) List of dictionnary with all the card's name with his image path
        """
        cards_name_image_list = []
        nbre_card = self.get_number_of_cards()
        for i in range(0, nbre_card):
            cards_name_image_list.append({"name": self.get_card_by_id(i).get_name(), "path":self.get_card_by_id(i).get_icon_path()})
        return cards_name_image_list

cards = Cards()
