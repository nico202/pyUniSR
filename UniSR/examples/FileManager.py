import UniSR
import config
import os
import os.path

me = UniSR.User()
me.login(config.username, config.password)
folders, files = me.datiDocenti()

def save(files):
    for file in files:
        file = file.encode('utf-8')
        if not os.path.isfile(file):
            me.saveFile(file, me.getFile(file))

def explore(folders, level = 0):
    for folder in folders:
        folder = folder.encode("utf-8")
        if not os.path.isdir(folder):
            os.makedirs(folder)
        level += 1
        print("|"*( 1 if (level - 1) else 0)+"----"*(level-1)+"%s" % folder)
        os.chdir(folder)
        me.cd(folder)
        folders_down, files = me.ls()
        explore(folders_down, level) #recursive yay
        save(files)
        level -= 1
        os.chdir("..")
        me.cd("..")

me.getCorsi()
#me.cd(me.corso) ##<- not working, should be set manually for now
me.ls()
me.cd("CdL magistrale in Psicologia")
me.ls()
explore(me.corsi)
