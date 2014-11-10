import lob
import config

lob.api_key = config.API_KEY


def errors_for_params(addressee_name, file_path, message):
    errors = []
    message_length = len(message)
    if message_length < 1 or message_length > 350:
        errors.append("You must supply a message with a max of 350 characters.");
    return errors


def create_card(addressee_name, file_path, message):
    errors = errors_for_params(addressee_name, file_path, message)
    if errors:
        # Todo: Throw a custom error
        return False
    return lob.Postcard.create(
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
        message = message,
        full_bleed = 1,
    )


def main():
    print 'Name of recipient:',
    name = raw_input().strip()
    print 'Local path to image to use for postcard front (must be 6.25in x 4.25in):',
    filename = raw_input().strip()
    print 'Message:',
    message = raw_input().strip()
    try:
        if create_card(name, filename, message):
            print 'Success! Your postcard has been sent.'
        else:
            print 'Error: Invalid parameters'
    except IOError:
        print 'Error: The specified image was not found.'
    except InvalidRequestError:
        print 'Error: Invalid request.'


if __name__ == '__main__':
    main()
