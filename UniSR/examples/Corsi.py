import UniSR
import config

me = UniSR.User()
me.login(config.username, config.password)
me.getCorsi()
print(me.corsi)
print(me.corso)

for corso in me.corsi:
    me.getFrequenze(corso)
