import UniSR
import config

me = UniSR.User()
me.login(config.username, config.password)
me.bacheca('./uni.db')
