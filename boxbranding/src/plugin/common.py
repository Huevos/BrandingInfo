# -*- coding: utf-8 -*-

import os
import re

from SupportedFunctions import IMPORTED_FUNCTIONS
from SupportedMachines import SUPPORTED_MACHINES
from Plugins.Extensions.OpenWebif.controllers.models import owibranding as helper

def sanitize(input): # remove any char that is not valid in a Python token
	return re.sub("[^a-zA-Z0-9_]", "", input)

def tokenise(input): # Makes a valid importable Python token 
	output = sanitize(input)
	if output[:1].isdigit():
		output = "_%s" % output
	return output

#################################################################

# If there is a "#" next to the function name the function will be overwritten

# software specific functions

def getDriverDate():
	return helper.getDriverDate()

def getImageArch(): #
	return ""

def getMachineKernelFile(): #
	return ""

def getMachineMKUBIFS(): #
	return ""

def getMachineMtdKernel(): #
	return ""

def getMachineMtdRoot(): #
	return ""

def getMachineRootFile(): #
	return ""

def getMachineUBINIZE(): #
	return ""

def getImageFileSystem(): #
	return ""
	
##################################################################

# Distro/Build

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

def getOEVersion():
	return helper.getOEVersion()

def getImageVersion():
	return helper.getImageVersion()

def getImageBuild():
	return helper.getImageBuild()

def getImageDevBuild():
	return ""

def getImageType():
	return ""

def getImageFolder(): #
	return ""

def getMachineBuild(): #
	return ""

##################################################################

# These should be the same in all distros, but with non-OE-Alliance distros all bets are off.

def getMachineName(): #
	return helper.getMachineName()

def getMachineProcModel(): #
	return helper.getMachineProcModel()

def getBoxType(): #
	return helper.getBoxType()

##################################################################

# Manufacturer

def getMachineMake(): #
	return ""

def getMachineBrand(): #
	return ""


##################################################################

# Hardware specific functions

def getBrandOEM(): #
	return ""

def getDisplayType(): #
	return ""

def getHaveAVJACK(): #
	return ""

def getHaveCI(): #
	return ""

def getHaveDVI(): #
	return ""

def getHaveHDMI(): #
	return ""

def getHaveHDMIinFHD(): #
	return ""

def getHaveHDMIinHD(): #
	return ""

def getHaveMiniTV(): #
	return ""

def getHaveRCA(): #
	return ""

def getHaveSCART(): #
	return ""

def getHaveSCARTYUV(): #
	return ""

def getHaveTranscoding1(): #
	return ""

def getHaveWOL(): #
	return ""

def getHaveWWOL(): #
	return ""

def getHaveYUV(): #
	return ""

def getHaveTranscoding2(): # Not imported. What is the difference between "Transcoding1" and "Transcoding2"?
	return ""

def getToken():
	eBoxTypeAvailable = False
	try:
		from enigma import getBoxType as eBoxType
		eBoxTypeAvailable = True
	except:
		def eBoxType(): return getBoxType()
	machine = sanitize(eBoxType())
	machine_build = sanitize(getBoxType())
	machine_brand = sanitize(getMachineBrand().replace("@", "a")).lower()
	if machine in SUPPORTED_MACHINES and len(SUPPORTED_MACHINES[machine]) == 1:
		return tokenise(SUPPORTED_MACHINES[machine][0]).lower()
	if machine in SUPPORTED_MACHINES:
		list1 = []
		list2 = []
		list3 = []
		list4 = []
		list5 = []
		i = 0
		for m in SUPPORTED_MACHINES[machine]:
			if machine in m:
				list1.append(i)
			if machine_brand in m:
				list2.append(i)
			if machine in m and machine_brand in m:
				list3.append(i)
			if machine_build in m:
				list4.append(i)
			if machine_build in m and machine_brand in m:
				list5.append(i)
		if list5:
			return tokenise(sorted(list5, key=len)[0]).lower()
		if list3:
			return tokenise(sorted(list3, key=len)[0]).lower()
		if list4:
			return tokenise(sorted(list4, key=len)[0]).lower()
		if list2:
			return tokenise(sorted(list2, key=len)[0]).lower()
		if list1:
			return tokenise(sorted(list1, key=len)[0]).lower()

		return tokenise(SUPPORTED_MACHINES[machine][0]).lower()

	# second attempt
	if eBoxTypeAvailable: # otherwise we are just repeating
		machine = sanitize(getBoxType())
		if machine in SUPPORTED_MACHINES and len(SUPPORTED_MACHINES[machine]) == 1:
			return tokenise(SUPPORTED_MACHINES[machine][0]).lower()
		if machine in SUPPORTED_MACHINES:
			list1 = []
			list2 = []
			list3 = []
			list4 = []
			list5 = []
			i = 0
			for m in SUPPORTED_MACHINES[machine]:
				if machine in m:
					list1.append(i)
				if machine_brand in m:
					list2.append(i)
				if machine in m and machine_brand in m:
					list3.append(i)
				if machine_build in m:
					list4.append(i)
				if machine_build in m and machine_brand in m:
					list5.append(i)
			if list5:
				return tokenise(sorted(list5, key=len)[0]).lower()
			if list3:
				return tokenise(sorted(list3, key=len)[0]).lower()
			if list4:
				return tokenise(sorted(list4, key=len)[0]).lower()
			if list2:
				return tokenise(sorted(list2, key=len)[0]).lower()
			if list1:
				return tokenise(sorted(list1, key=len)[0]).lower()
	
			return tokenise(SUPPORTED_MACHINES[machine][0]).lower()

	# if we got this far we are not in good shape
	return tokenise(machine_build).lower()

token = getToken()
if token:
	print "got token:", token
	exec("from machines.%s import %s" % (token, ','.join(IMPORTED_FUNCTIONS)))
	
	
