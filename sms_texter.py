# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACfbd526ecea3f7b07b743bc0cb05cfa42"
auth_token = "397fedcc38afa2b27cb6d4251acdcc81"
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="you've won a million dollar",
  from_="+16404008871",
  to="+9779861609593"
)

print(message.sid)
