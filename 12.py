import re

CONTACTS = []


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "No user with given name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name and phone"
        except TypeError:
            return "Enter correct command, please"
    return wrapper


@input_error
def parser_command(string):
    # sanitize_string = re.sub(r'[.,()\/+*\]\[\\]', '', string)
    command_list = ['add', 'change', 'phone', 'hello', 'show all', 'good bye',
                    'exit', '.', 'close']
    command = list(filter(lambda i: string.startswith(i), command_list))[0]
    return command


@input_error
def add_contact(string):
    new_contact = string.split(' ')
    while True:
        if len(new_contact) == 0:
            break
        CONTACTS.append({'name': new_contact.pop(0).capitalize(), 'phone':
            new_contact.pop(0)})


@input_error
def change_contact(string):
    new_contact = string.split(' ')
    name = new_contact[0]
    phone = new_contact[1]
    for i in CONTACTS:
        if i['phone'] == phone or i['name'].lower() == name:
            i['name'] = name.capitalize()
            i['phone'] = phone
        else:
            return f"I can not find {name}: {phone}"


@input_error
def find_contact(string):
    find_contacts = []
    for i in CONTACTS:
        if i['phone'] == string:
            find_contacts.append(i['name'])
    if not find_contacts:
        return 'Нет такого контакта, добавьте =)'
    return find_contacts


@input_error
def hello(string):
    return 'How can I help you?'


@input_error
def show_all_cont(string):
    return CONTACTS


@input_error
def bye(string):
    return 'Good bye!'

@input_error
def handler(string_command):
    HANDLER = {
        'add': add_contact,
        'change': change_contact,
        'phone': find_contact,
        'hello': hello,
        'show all': show_all_cont,
        'good bye': bye,
        'exit': bye,
        '.': bye,
        'close': bye
    }
    return HANDLER[string_command]


def main():
    while True:
        command_user = input().lower()
        command = parser_command(command_user)
        print(command)
        if len(command) > 20:
            print("Enter command correct")
            continue
        funkwork = handler(command)
        contact_str = command_user.replace(command, '', 1)
        get_funkwork = funkwork(contact_str.rstrip().lstrip())
        if get_funkwork is not None:
            print(get_funkwork)


if __name__ == '__main__':
    main()
