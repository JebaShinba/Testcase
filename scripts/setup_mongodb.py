import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def setup_mongodb():
    # Retrieve MongoDB URI from environment variable
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")

    try:
        # Connect to MongoDB
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')  # Ping to check connection
        print("MongoDB connected successfully!")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
        exit(1)

    # Set up test data (example)
    db = client.get_database('test_db')  # Use a database for testing
    collection = db.get_collection('test_collection')

    # Example: Insert some test d
    sample_data = [
        {
           
            "username": "",
            "first_name": "admin",
            "last_name": "admin",
            "password": "demo",
            "mode_2fa": "Off",
            "groups": ["Admin"],
            "rights": "Admin",
            "notes": {"info": "this 'notes' field exists only for this default admin user", "p": "donttrustyou"},
            "vec_2fa": None,  # Corrected null to None
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
            "is_valid": False,
            "expected_error": "success",
            
        },
        {
            
            "username": "",
            "first_name": "admin",
            "last_name": "admin",
            "password": "demo",
            "mode_2fa": "Off",
            "groups": ["Admin"],
            "rights": "Admin",
            "notes": {"info": "this 'notes' field exists only for this default admin user", "p": "donttrustyou"},
            "vec_2fa": None,  # Corrected null to None
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
            "is_valid": False,
            "expected_error": "Wrong credentials",
            
        },
        {
            
            "username": "demo",
            "first_name": "admin",
            "last_name": "admin",
            "password": "",
            "mode_2fa": "Off",
            "groups": ["Admin"],
            "rights": "Admin",
            "notes": {"info": "this 'notes' field exists only for this default admin user", "p": "donttrustyou"},
            "vec_2fa": None,  # Corrected null to None
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
            "is_valid": False,
            "expected_error": "Wrong credentials",
            
        },
        {
            
            "username": "demo",
            "first_name": "admin",
            "last_name": "admin",
            "password": "demo",
            "mode_2fa": "Off",
            "groups": ["Admin"],
            "rights": "Admin",
            "notes": {
                "info": "this 'notes' field exists only for this default admin user",
                "p": "donttrustyou"
            },
            "vec_2fa": None,  # Corrected null to None
            "baseurl": "https://demo.filebrowser.org/login?redirect=/files/",
            "is_valid": True,
            "expected_error": "success",
          
        }
    ]
    
    collection.insert_many(sample_data)
    print(f"Test data inserted into {db.name}.{collection.name}")

if __name__ == "__main__":
    setup_mongodb()
