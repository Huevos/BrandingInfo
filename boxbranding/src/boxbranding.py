#from machines.boxbranding_common import *
from Plugins.SystemPlugins.BrandingInfo.SupportedFunctions import SUPPORTED_FUNCTIONS
exec("from Plugins.SystemPlugins.BrandingInfo.common import %s" % ','.join(SUPPORTED_FUNCTIONS))
del SUPPORTED_FUNCTIONS
