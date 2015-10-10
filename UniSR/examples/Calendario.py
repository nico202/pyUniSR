import UniSR
import config

me = UniSR.User()
me.login(config.username, config.password)
me.calendario()
me.calendario("oggi")
