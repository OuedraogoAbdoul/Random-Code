from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe8e65404d3b9810cc17e144f0b42850a"
# Your Auth Token from twilio.com/console
auth_token  = "e629785e353e94add429ac74bfa6aef6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19XXX076X3", 
    from_="+14153017494",
    body="This is Abdoul Ouedraogo")

print(message.sid)

