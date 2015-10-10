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

def explore(folders):
    for folder in folders:
        folder = folder.encode("utf-8")
        if not os.path.isdir(folder):
            os.makedirs(folder)
        print "cd to %s" % folder
        os.chdir(folder)
        me.cd(folder)
        folders_down, files = me.ls()
        explore(folders_down)
        save(files)
        os.chdir("..")
        me.cd("..")

me.getCorsi()
me.cd(me.corso)
explore(me.corsi)
