# goes in /usr/lib/enigma2/python

import os

def getFeedsUrl():
	try:
		content = open("/etc/opkg/all-feed.conf", 'r').readline().strip()
		return content[content.find('http'):-4]
	except:
		return ""

def getImageDistro():
	try:
		return open("/etc/opkg/all-feed.conf", 'r').readline().strip().lower().split()[1].replace("-all", "")
	except:
		return ""

def getMachineName():
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		return owibranding.getMachineName()
	return getMachineMake()

def getMachineProcModel():
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		return owibranding.getMachineProcModel()
	return getMachineMake()

def getBoxType():
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		bt = owibranding.getBoxType()
		if bt.startswith("sf8008"):
			sf8008type = open("/proc/stb/info/type").read()
			if sf8008type == "10":
				return "sf8008s"
			if sf8008type == "11":
				return "sf8008t"
		return bt
	return getMachineMake()

def getOEVersion():
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		return owibranding.getOEVersion()
	return ""

def getImageVersion():
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		return owibranding.getImageVersion()
	return ""

def getImageBuild():
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		return owibranding.getImageBuild()
	return ""

def getImageDevBuild():
	return ""

def getImageType():
	return ""

def getDriverDate():
	import re
	if os.path.isfile("/usr/lib/enigma2/python/Plugins/Extensions/OpenWebif/controllers/models/owibranding.pyo"):
		from Plugins.Extensions.OpenWebif.controllers.models import owibranding
		search = re.search('([0-9]{8})', owibranding.getDriverDate())
		return search.group(1)
	return ""

def getHaveTranscoding2():
	return ""
