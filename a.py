from roboflow import Roboflow

rf = Roboflow(api_key="pWZLdpgG8WdyM76kb4Q3")
project = rf.workspace("imageinpainting-vnx6b").project("vto-inpainting")
version = project.version(1)
dataset = version.download("yolov8")

print("Dataset downloaded to:", dataset.location)
