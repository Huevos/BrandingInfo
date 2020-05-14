# -*- coding: utf-8 -*-

# branding file for sf8008

def getBoxType():
	sf8008type = open("/proc/stb/info/type").read()
	if sf8008type.startswith("11"):
		return "sf8008t"
	elif sf8008type.startswith("12"):
		return "sf8008c"
	else: # sf8008type.startswith("10")
		return "sf8008s"

def getMachineName():
	sf8008type = open("/proc/stb/info/type").read()
	if sf8008type.startswith("11"):
		return "SF8008 4K Twin"
	elif sf8008type.startswith("12"):
		return "SF8008 4K Combo"
	else: # sf8008type.startswith("10")
		return "SF8008 4K Single"

def getBrandOEM():
	return "octagon"

def getDisplayType():
	return "7segment"

def getHaveAVJACK():
	return "True"

def getHaveCI():
	return ""

def getHaveDVI():
	return ""

def getHaveHDMI():
	return "True"

def getHaveHDMIinFHD():
	return ""

def getHaveHDMIinHD():
	return ""

def getHaveMiniTV():
	return ""

def getHaveRCA():
	return ""

def getHaveSCART():
	return ""

def getHaveSCARTYUV():
	return ""

def getHaveTranscoding1():
	return "multitranscoding"

def getHaveWOL():
	return ""

def getHaveWWOL():
	return ""

def getHaveYUV():
	return ""

def getImageArch():
	return "cortexa15hf-neon-vfpv4"

def getImageFileSystem():
	return " octagonemmc"

def getImageFolder():
	return "octagon/sf8008"

def getMachineBrand():
	return "Octagon"

def getMachineBuild():
	return "sf8008"

def getMachineKernelFile():
	return "kernel.bin"

def getMachineMKUBIFS():
	return ""

def getMachineMake():
	return "sf8008"

def getMachineMtdKernel():
	return "mmcblk0p12"

def getMachineMtdRoot():
	return "mmcblk0p16"

def getMachineProcModel():
	return "sf8008"

def getMachineRootFile():
	return "rootfs.tar.bz2"

def getMachineUBINIZE():
	return ""

