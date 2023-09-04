from twilio.rest import Client

# Twilio account details
twilio_account_sid = 'Your Twilio SID here'
twilio_auth_token = 'Your Twilio Auth Token here'
twilio_source_phone_number = 'Your Twilio phone number here'

# Create a Twilio client object instance
client = Client(twilio_account_sid, twilio_auth_token)

# Send an SMS
message = client.messages.create(
    body="This is my SMS message!",
    from_=twilio_source_phone_number,
    to="Destination phone number here"
)