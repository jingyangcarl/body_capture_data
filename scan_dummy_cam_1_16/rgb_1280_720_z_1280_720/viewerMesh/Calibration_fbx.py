import maya.cmds as cmds

# list all the cameras
cameras = cmds.listCameras(p=True)
print(cameras)

for camera in cameras:
    print(camera)
    print(cmds.xform(cameras[0], q=True, m=True))