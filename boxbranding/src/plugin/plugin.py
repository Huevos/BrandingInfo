from enigma import getDesktop

from Plugins.Plugin import PluginDescriptor

from Components.ActionMap import ActionMap
from Components.ScrollLabel import ScrollLabel
from Components.Sources.StaticText import StaticText

from Screens.Screen import Screen

from boxbranding import *
#from common import *
from SupportedFunctions import SUPPORTED_FUNCTIONS

import os
imagesPath = "%s/images" % os.path.dirname(os.path.realpath(__file__))

class InfoScreen(Screen):
	skinTemplate = """
		<screen name="BrandingInfo" position="center,center" size="%d,%d">
			<widget name="text" position="%d,%d" size="%d,%d" zPosition="10" font="Regular;%d" transparent="1"  scrollbarMode="showOnDemand"/>
			<ePixmap pixmap="imagesPath/key_red.png" position="%d,e-%d" size="%d,%d" alphatest="on" scale="1" />
			<widget render="Label" source="key_red" position="%d,e-%d" zPosition="1" size="%d,%d" font="Regular;%d" halign="center" valign="center" backgroundColor="#9f1313" transparent="1"/>
		</screen>""".replace("imagesPath", imagesPath)
	scaleData = [
		1000, 650,
		10 ,10, 980, 580, 22,
		10, 50, 140, 40,
		10, 50, 140, 40, 20,
	]
	# The skin template is designed for a HD screen so the scaling factor is 720.
	# double negative to round up not round down
	skin = skinTemplate % tuple([-(x*getDesktop(0).size().height()/(-720)) for x in scaleData])

	def __init__(self, session):
		self.session = session
		Screen.__init__(self, session)
		Screen.setTitle(self, _("Branding info"))

		self.skinName = ["Branding_info"]

		self["text"] = ScrollLabel("")

		self["actions"] = ActionMap(["SetupActions", "ColorActions", "DirectionActions", "MenuActions"],
		{
			"red": self.close,
			"cancel": self.close,
			"menu": self.close,
			"up": self["text"].pageUp,
			"down": self["text"].pageDown,		
			"left": self["text"].pageUp,
			"right": self["text"].pageDown,
			
		}, -2)

		self["key_red"] = StaticText(_("Close"))

		#content = ["%s=%s\n" % (m, eval("%s()" % m)) for m in sorted(SUPPORTED_FUNCTIONS)]
		exec("FUNCTIONS_DICT = {%s}" % ''.join(["'%s': %s()," % (m, m) for m in SUPPORTED_FUNCTIONS]))
		content = ["%s = '%s'\n" % (m, FUNCTIONS_DICT[m]) for m in sorted(FUNCTIONS_DICT.keys()) ]

		self["text"].setText(''.join(content))


def Main(session, **kwargs):
	session.open(InfoScreen)

def fromMenu(menuid):
	if menuid == "information":
		return [(_("Branding"), Main, "branding info", None)]
	return []

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Branding info"), description=_("branding info"), where=PluginDescriptor.WHERE_MENU, needsRestart=True, fnc=fromMenu)
