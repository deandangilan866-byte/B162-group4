import pprint
from googleapiclient.discovery import build
from google.oauth2 import service_account

KEY_FILE = "credentials/service-account.json"

SCOPE = "https://www.googleapis.com/auth/authorized-buyers-marketplace"

BUYER_NAME = "buyers/123456"

credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE,
    scopes=[SCOPE]
)

marketplace = build("authorizedbuyersmarketplace", "v1", credentials=credentials)


def list_clients():
    request = marketplace.buyers().clients().list(parent=BUYER_NAME)
    try:
        response = request.execute()
        pprint.pprint(response)
    except Exception as e:
        print("Error listing clients:", e)

def get_buyer_accounts():

    return [
        {"clientId": "1001", "displayName": "Dean Dangilan"},
        {"clientId": "1002", "displayName": "Jojo Taguitag"},
        {"clientId": "1003", "displayName": "Judith Patnaan"},
        {"clientId": "1004", "displayName": "Gracelyn Tino"},
        {"clientId": "1005", "displayName": "Bernadeth Huag"},
    ]

def list_client_users(client_id):
    client_name = f"{BUYER_NAME}/clients/{client_id}"
    request = marketplace.buyers().clients().users().list(parent=client_name)
    try:
        response = request.execute()
        pprint.pprint(response)
    except Exception as e:
        print(f"Error listing users for client {client_id}:", e)


if __name__ == "__main__":
    print("=== Listing all clients ===")
    list_clients()

   