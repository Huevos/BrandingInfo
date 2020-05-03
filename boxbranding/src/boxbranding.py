from machines.boxbranding_common import *
exec("from machines.%s import *" % open("machinebuild","r").read())
