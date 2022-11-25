import os

VIDEOPATH = os.path.join(os.getcwd(), 'videos', 'my_video-1.mkv')
MODELPATH = os.path.join(os.getcwd(),'utils/models','faster_rcnn_inception_v2_coco_2018_01_28','frozen_inference_graph.pb')
COCO_NAMEPATH = os.path.join(os.getcwd(), 'utils/labels', 'coco.names')

THREAD = False

BLACK = (0,0,0)
WHITE = (255,255,255)