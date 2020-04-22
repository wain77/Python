from twilio.rest import Client

accountSID = 'AC647e80407ab81d25c6a9d36d0036ab12'
accountAuthToken = 'ff57a1c67c48ba4cd2a1054247ab07bf'

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(accountSID, accountAuthToken)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+12019037158'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+447930271123'

client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
