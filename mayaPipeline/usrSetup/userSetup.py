import sys
import maya.cmds as cmds
import maya.mel as mel

# -- directories
pythonPath = "S:\outfit\shared\mayaPipeline\scripts\python"
PipelinePath = "S:\outfit\shared\pythonPipeline"
sys.path.append( pythonPath  )
sys.path.append( PipelinePath  )
cmds.evalDeferred("from mayaSceneTool import *")
cmds.evalDeferred("run()")