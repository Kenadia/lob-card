import lob
import config

lob.api_key = config.API_KEY


def verify_params(addressee_name, file_path, message):
    errors = []
    message_length = len(message)
    if message_length < 1 or message_length > 350:
        errors.append("You must supply a message with a max of 350 characters.");
    return errors


def create_card(addressee_name, file_path, message):
    errors = errors_for_params(addressee_name, file_path, message)
    if errors:
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
        return False
    else:
        return True
