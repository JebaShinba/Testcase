import selenium
from selenium import webdriver
import unittest
from homeobjects.test_login import LoginPage
from configfile.config import get_db, get_users_collection  # Imports from config

class ValidLoginTest(unittest.TestCase):
    valid_users = []

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        # Fetch valid user credentials from MongoDB
        db = get_db()  # Establishes the database connection
        cls_users_collection = get_users_collection()  # Gets the users collection

        # Retrieve only valid users
        cls.valid_users = list(cls_users_collection.find({"is_valid": False}))
        
        print("Valid users fetched:", cls.valid_users)  # Debugging output

        if not cls.valid_users:
            raise Exception("No valid users found in the database!")

    def test_login_with_valid_users(self):
        # Iterate over valid users and perform login
        for index, user_details in enumerate(self.valid_users):
            with self.subTest(user_index=index):
                required_keys = ["username", "password", "baseurl", "expected_error"]
                
                # Ensure all necessary keys are present
                if not all(key in user_details for key in required_keys):
                    print("Skipping login due to missing keys:", user_details)
                    continue  # Skip to the next user if keys are missing

                username = user_details["username"]
                password = user_details["password"]
                base_url = user_details["baseurl"]
                expected_error = user_details["expected_error"]

                # Print the username and password being tested
                print(f"Testing login for Username: '{username}' with Password: '{password}'")

                # Navigate to the base URL
                try:
                    self.driver.get(base_url)
                    print("Navigated to:", base_url)
                except Exception as e:
                    print("Error navigating to base URL:", e)
                    continue  # Skip to the next user if navigation fails

                # Instantiate the LoginPage object
                lg = LoginPage(self.driver)
                lg.setUsername(username)  # Enter the username
                lg.setPassword(password)  # Enter the corresponding password
                lg.clickLogin()
                actual_error = lg.actualError()   
                
                # Assert that the actual error matches the expected error
                self.assertEqual(expected_error, actual_error, f"Failed for Username: '{username}' with Password: '{password}'")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Browser closed.")

if __name__ == '__main__':
    unittest.main()
