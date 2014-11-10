import lob
import config

lob.api_key = config.API_KEY

def create_card(addressee_name, file_path, message):
    lob.Postcard.create(
        to_address = {
            'name': addressee_name,
            'address_line1': '300 N College St',
            'address_city': 'Northfield',
            'address_state': 'MN',
            'address_zip': '55057',
            'address_country': 'US'
        },
        from_address = {
            'name': 'LobCard',
            'address_line1': '300 N College St',
            'address_city': 'Northfield',
            'address_state': 'MN',
            'address_zip': '55057',
            'address_country': 'US'
        },
        front = open(file_path, 'rb'),
        message = message
    )
