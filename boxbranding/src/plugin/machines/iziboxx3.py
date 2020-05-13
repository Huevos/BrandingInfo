# -*- coding: utf-8 -*-

# branding file for iziboxx3

def getBrandOEM():
	return "dinobot"

def getDisplayType():
	return "7segment"

def getHaveAVJACK():
	return "False"

def getHaveCI():
	return "False"

def getHaveDVI():
	return "False"

def getHaveHDMI():
	return "True"

def getHaveHDMIinFHD():
	return "False"

def getHaveHDMIinHD():
	return "False"

def getHaveMiniTV():
	return "False"

def getHaveRCA():
	return "True"

def getHaveSCART():
	return "False"

def getHaveSCARTYUV():
	return "False"

def getHaveTranscoding1():
	return "multitranscoding"

def getHaveWOL():
	return "False"

def getHaveWWOL():
	return "False"

def getHaveYUV():
	return "False"

def getImageArch():
	return "cortexa15hf-neon-vfpv4"

def getImageFileSystem():
	return " ubi"

def getImageFolder():
	return "izibox/x3"

def getMachineBrand():
	return "IZIBOX"

def getMachineBuild():
	return "iziboxx3"

def getMachineKernelFile():
	return "uImage"

def getMachineMKUBIFS():
	return "-F -m 2048 -e 126976 -c 3840"

def getMachineMake():
	return "iziboxx3"

def getMachineMtdKernel():
	return "mtd10"

def getMachineMtdRoot():
	return "mtd11"

def getMachineRootFile():
	return "rootfs.bin"

def getMachineUBINIZE():
	return "-m 2048 -p 128KiB"
