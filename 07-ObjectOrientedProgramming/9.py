from message import Message, SMS, Email

sms = SMS(123444555, 'Wygrałeś iPhone X. Wejdź na stronę hxxp://totally-not-a-virus.lphone-win-apple.eu.com.ru aby odebrać')

email = Email('ugandanprince@yandex.ru', 'everyone@everywhere.com', 'I give you 1 000 000 USD free!',
              'Helo, I Ugandan prince. I want give yu my money FREE. Send yur card number expiration date name and ccv. Be fast! K THX')

sms.send()
print()
email.send()
