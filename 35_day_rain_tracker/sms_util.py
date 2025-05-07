# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+17179317258",
    to="+4917664041684",
)

print(message.body)