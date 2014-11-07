# -- Hdr browser maya commands
# -- written by Michael Kirylo
# -- 2014
# ----------------imports-----------------
import maya.cmds as cmds
import maya.mel as mel


def checkDome():
	lightsInScene = cmds.ls('HDRLightDome_*', tr=True)
	return lightsInScene
def checkRec():
	rectLight = cmds.ls('HDRLightRect_*', tr=True)
	return rectLight
def checkRenderer():
	renderer =	mel.eval('currentRenderer')
	return renderer
def mayaWarning():
	cmds.warning( "Please set the current renderer to Vray." )
def createDomeMaya(suffux,imagePath):
	HDRLight = cmds.shadingNode('VRayLightDomeShape', asLight=True)
	HDRLight = cmds.rename(HDRLight, ('HDRLightDome_' + suffux))
	HDRLightShape = cmds.listRelatives( HDRLight, s=True )
	hdrFileNode = cmds.shadingNode('file', asTexture=True)
	hdrFileNode = cmds.rename(hdrFileNode, ('HDRLightDomeHDR_' + suffux))
	vrayPlacementText = cmds.shadingNode('VRayPlaceEnvTex', asUtility=True)
	vrayPlacementText = cmds.rename(vrayPlacementText, ('HDRLightDomeVrEnvTex_' + suffux))
	cmds.connectAttr( (vrayPlacementText + '.outUV'), (hdrFileNode + '.uvCoord'), force=True)
	cmds.connectAttr( (hdrFileNode + '.outColor'), (HDRLightShape[0] + '.domeTex'), force=True)
	cmds.setAttr ((HDRLightShape[0] + '.domeSpherical') , 1 )
	cmds.setAttr ((HDRLightShape[0] + '.useDomeTex') , 1 )
	cmds.setAttr((hdrFileNode + '.filterType'), 0 )
	cmds.setAttr( (hdrFileNode + '.fileTextureName'), imagePath , type = 'string')
	cmds.setAttr (vrayPlacementText+ '.mappingType', 2)
	return HDRLight
def createRectMaya(suffux,imagePath):
	HDRLight = cmds.shadingNode('VRayLightRectShape', asLight=True)
	HDRLight = cmds.rename(HDRLight, ('HDRLightRect_' + suffux))
	HDRLightShape = cmds.listRelatives( HDRLight, s=True )
	hdrFileNode = cmds.shadingNode('file', asTexture=True)
	hdrFileNode = cmds.rename(hdrFileNode, ('HDRLightRectHDR_' + suffux))
	vrayPlacementText = cmds.shadingNode('place2dTexture', asUtility=True)
	vrayPlacementText = cmds.rename(vrayPlacementText, ('HDRLightRectVrEnvTex_' + suffux))
	cmds.connectAttr( (vrayPlacementText + '.outUV'), (hdrFileNode + '.uvCoord'), force=True)
	cmds.connectAttr( (hdrFileNode + '.outColor'), (HDRLightShape[0] + '.rectTex'), force=True)
	cmds.setAttr ((HDRLightShape[0] + '.useRectTex') , 1 )
	cmds.setAttr((hdrFileNode + '.filterType'), 0 )
	cmds.setAttr( (hdrFileNode + '.fileTextureName'), imagePath , type = 'string')
	cmds.setAttr ((HDRLightShape[0] + '.intensityMult') , 1 )
	return HDRLight
def createEnvMaya(suffux,imagePath):
	hdrFileNode = cmds.shadingNode('file', asTexture=True)
	hdrFileNode = cmds.rename(hdrFileNode, ('HDRLightDomeHDR_' + suffux))
	vrayPlacementText = cmds.shadingNode('VRayPlaceEnvTex', asUtility=True)
	vrayPlacementText = cmds.rename(vrayPlacementText, ('EnvTex_' + suffux))
	cmds.connectAttr( (vrayPlacementText + '.outUV'), (hdrFileNode + '.uvCoord'), force=True)
	cmds.setAttr((hdrFileNode + '.filterType'), 0 )
	cmds.setAttr( (hdrFileNode + '.fileTextureName'), imagePath , type = 'string')
	cmds.setAttr (vrayPlacementText+ '.mappingType', 2)
	cmds.setAttr('vraySettings.cam_overrideEnvtex', 1)
	cmds.connectAttr( (hdrFileNode + '.outColor'), 'vraySettings.cam_envtexGi', force=True)
	cmds.connectAttr( (hdrFileNode + '.outColor'), 'vraySettings.cam_envtexReflect', force=True)
	return HDRLight
# def dockLayout(parent):
# 	dockLayout = cmds.paneLayout(configuration='single', parent=parent)
# 	return dockLayout
# def dockcontrl(dockLayout):
# 	cntrl = cmds.dockControl(allowedArea='all', area='right', floating=True, content=dockLayout, label='Fuse HDRI browser')
# 	return cntrl
# def browserWidget(window,parent):
# 	wind = cmds.control(window, e=True, parent=parent)
# 	return wind