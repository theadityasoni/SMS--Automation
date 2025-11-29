from twilio.rest import Client

ACCOUNT_SID="TWILIO_ACCOUNT_SID"
AUTH_TOKEN="TWILIO_AUTH_TOKEN"

TWILIO_NUMBER= "+1234567890"
RECEIVER_NUMBER= "+919XXXXXXXXX"

client = Client(ACCOUNT_SID,AUTH_TOKEN)

message = client.messages.create(
    body="Hello, Aditya This Side",
    from_=TWILIO_NUMBER,
    to=RECEIVER_NUMBER
)
