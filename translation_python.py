from translate import Translator
translator= Translator(to_lang="German")
translation = translator.translate("At first glance the refresh token may look pointless, but in fact it is necessary to make sure the user still have the correct permissions. If your access token have a long expire time, it may take longer to update the information associated with the token. That’s because the authentication check is done by cryptographic means, instead of querying the database and verifying the data. So some information is sort of cached.")
print(translation)



translator= Translator(from_lang="german",to_lang="spanish")
translation = translator.translate("Guten Morgen")
print(translation)