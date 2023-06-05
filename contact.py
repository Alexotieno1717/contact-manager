import pyperclip


class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = []  # Empty contact list

    def save_contact(self):
        """
        save contact to contact_list
        """
        Contact.contact_list.append(self)

    def __init__(self, first_name, last_name, number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def delete_contact(self):
        """
        delete_contact delete contact from contact_list
        """
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):
        """
        method that takes in a number and returns a contact that matches the number
        """
        for contact in cls.contact_list:
            if contact.number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        """
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending on if the contact exists
        """
        for contact in cls.contact_list:
            if contact.number == number:
                return True
        return False

    @classmethod
    def display_contact(cls):
        """
        method that return contact list
        """
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
