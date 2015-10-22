import UniSR
import config

me = UniSR.User()
me.login(config.username, config.password)
me.prenotazioni()
