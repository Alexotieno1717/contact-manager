import unittest
from contact import Contact
import pyperclip


class TestContact(unittest.TestCase):
    def setUp(self):
        self.new_contact = Contact('Alex', 'Otieno', '0748815593', 'alex@example.co.ke')  # create a contact object

    def test_init(self):
        self.assertEqual(self.new_contact.first_name, 'Alex')
        self.assertEqual(self.new_contact.last_name, 'Otieno')
        self.assertEqual(self.new_contact.number, '0748815593')
        self.assertEqual(self.new_contact.email, 'alex@example.co.ke')

    def test_save_contact(self):
        """
        test_save_contact test case eto test if its save to contact_list
        """
        self.new_contact.save_contact()  # Saving new contact
        self.assertEqual(len(Contact.contact_list), 1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Contact.contact_list = []

    def test_save_multiple_contact(self):
        """
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678", "test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_delete_contact(self):
        """
        test_delete_contact to test if we can remove a contact from our contact list
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678", "test@user.com")
        test_contact.save_contact()

        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    def test_find_contact_by_number(self):
        """
        test to check if we can find a contact by phone number and display information
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223344", "test@user.com")  # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        """
         test to check if we can return a Boolean  if we cannot find the contact
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223344", "test@user.com")  # new contact
        test_contact.save_contact()

        contact_exist = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exist)

    def test_display_all_contacts(self):
        """
         method that returns a list of all contacts saved
        """
        self.assertEqual(Contact.display_contact(), Contact.contact_list)

    def test_copy_email(self):
        """
         Test to confirm that we are copying the email address from a found contact
        """
        self.new_contact.save_contact()
        Contact.copy_email("0712345678")

        self.assertEqual(self.new_contact.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
