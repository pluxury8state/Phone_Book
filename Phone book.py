from pprint import pprint

def islover(lover_contact):
    if lover_contact == False:
        return 'Нет'
    else:
        return lover_contact


class Phonebook:
    def __init__(self, name):
        self.name_of_phone_name = name
        self.massive_contacts = []

    def __add__(self, other):
        self.massive_contacts.append(other)

    def remove_all(self):                           # вывести все контакты из телефонной книги
        for contacts in self.massive_contacts:
            print(contacts)

    def delete_contact(self, tel_number):   # удаление контакта
        i = 0
        for contact in self.massive_contacts:
            if contact.get_tel() == tel_number:
                del(self.massive_contacts[i])
            i += 1

    def search_by_name_surname(self, name, surname):  # поиск контакта по имени
        for contact in self.massive_contacts:
            if (contact.get_name() == name) and (contact.get_surname() == surname):
                return contact

    def search_lover(self,lover_number):   # поиск контакта с избранным номером
        contacts_with_lover_numbers = []
        for contact in self.massive_contacts:
            if contact.get_lover() == lover_number:
                contacts_with_lover_numbers.append(contact)
        for contacts in contacts_with_lover_numbers:
            print(contacts)



class Contact:

    def __init__(self, name, surname, tel_number, lover_contact=False, **kwargs):
        self.dict_of_info = {}
        self.dict_of_info['Имя'] = name
        self.dict_of_info['Фамилия'] = surname
        self.dict_of_info['Телефон'] = tel_number
        self.dict_of_info['Избранный контакт'] = islover(lover_contact)
        self.dict_of_info['дополнительная информация'] = kwargs

    def get_lover(self):
        return  self.dict_of_info['Избранный контакт']

    def get_tel(self):
        return self.dict_of_info['Телефон']

    def get_name(self):
        return self.dict_of_info['Имя']

    def get_surname(self):
        return self.dict_of_info['Фамилия']

    def __str__(self):
        for keys, values in self.dict_of_info.items():
            print(f'{keys} : {values}')
        return ''


Jhon = Contact('Jhon', 'Andersen', '91230490', '89001238756', email='fwewfwef@gmail.com', pop='fqagrthwthrhqwefwq')
Liz = Contact('Liz', 'Dioptr', '89019433212', '89001238756', email='retwefz@gmaol.com', pop='poqrfrqr')
Lqwdz = Contact('Lqwdz', 'Dioptr', '8901943133', '89674561234', email='rewgwerwefz@gmaol.com', pop='qer')
Faliz = Contact('Faliz', 'Dioptr', '8991233212', email='etwefz@gwrgol.com', pop='qrfqreger')
Aliz = Contact('Aliz', 'Dioptr', '81123481114', email='atwergwgefz@gmaol.com', pop='qqregqer')

first_book = Phonebook('first book')

first_book.__add__(Liz)
first_book.__add__(Jhon)
first_book.__add__(Lqwdz)
first_book.__add__(Faliz)
first_book.__add__(Aliz)


first_book.delete_contact('91230490')

first_book.remove_all()

print(first_book.search_by_name_surname('Faliz', 'Dioptr'))

first_book.search_lover('89001238756')
