# -----------------------------------------------------
# imports
# -----------------------------------------------------
import sys
import os
import maya.cmds as cmds
import maya.mel as mel
# -----------------------------------------------------
# functions
# -----------------------------------------------------
# --get file info
def getFileInfo():
	PathAndName			=		cmds.file(q= True, sn = True)
	PathSplit			=		PathAndName.split( '/' )
	Name				=		PathSplit[-1]
	Path				=		PathSplit
	Path.pop()
	Path="/".join(Path)
	FileDict 			=		{'Name': Name, 'Path':Path,'PathAndName':PathAndName}
	return FileDict
# --load File
def loadAction(fileToOpen):
    if cmds.file(q=True, modified=True):
        msg = "Save changes to %s?"%(cmds.file(q= True, sn = True))
        dialog = cmds.confirmDialog( title='Confirm', message=msg, button=['Save',"Don't Save",'Cancel'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if dialog == 'save':
            cmds.SaveScene()
            cmds.file( fileToOpen, open=True )
        if dialog == "Don't Save":
            cmds.file(new=True, force=True)
            cmds.file( fileToOpen, open=True )
        if dialog == "Cancel":
            pass
# --File name
def getFileName():
	fileName			=		getFileInfo()
	fileName			=		fileName['Name']
	return fileName
# --file name and path
def GetFileNameAndPath():
	fileNamePath		=		getFileInfo()
	fileNamePath		=		fileNamePath['PathAndName']
	return fileNamePath
# -- save file
def save():
	SavedFile			=		cmds.file( s = True )
	return SavedFile
# -- save as
def saveAs(fileName):
	path				=		getFileInfo()
	path				=		path['Path']
	if os.path.exists(path) != True:
		os.makedirs(path)
	cmds.file(rename = fileName)
	cmds.file( s = True )
# -- version up
def vUP():
	fileName			= 		GetFileNameAndPath()
	vName				=		fileName.split( '_' )
	vNum				=		vName[-1]
	vNum				=		''.join(x for x in vNum if x.isdigit())
	vNum				=		int(vNum)+1
	vNum				=		str(vNum).zfill(3)
	newName				=		vName[0] + '_v' + vNum + '.mb'
	saveAs(newName)
# --maya version
def appVersion():
	mayaVersion 		=		cmds.about(version=True)
	return mayaVersion
# -- convert to 
def convertTo(fileToConvertIn):
	dir					=		os.path.dirname(fileToConvertIn)
	if os.path.exists(dir) != True:
		os.makedirs(dir)
	cmds.file(rename = fileToConvertIn)
	cmds.file( s = True )
# -- find units
def getUnits():
	units				=		cmds.currentUnit( query=True, linear=True )
	return units
def getFPS():
	FPS					=		cmds.currentUnit( query=True, time=True )
	return FPS

	
	

	
	

