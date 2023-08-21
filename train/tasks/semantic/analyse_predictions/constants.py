
# experiments directory containing predictions,
ROOT_DIR = "/work/akmt/new/lidar-bonnetal/train/tasks/semantic/test_slamantic_predictions"
SEQUENCE = "00" # name of the sequence
LIMIT_LABEL_FILES = 40 # to limit the loading of files, from 0 to this index, EX: [0:1], FIRST LABEL WILL BE LOADED
SAVE_PLOT = False


# Class Info
CLASS_INFO = {0: {'label': 'unlabeled', 'color': [0, 0, 0]},
 1: {'label': 'outlier', 'color': [0, 0, 255]},
 10: {'label': 'car', 'color': [245, 150, 100]},
 11: {'label': 'bicycle', 'color': [245, 230, 100]},
 13: {'label': 'bus', 'color': [250, 80, 100]},
 15: {'label': 'motorcycle', 'color': [150, 60, 30]},
 16: {'label': 'on-rails', 'color': [255, 0, 0]},
 18: {'label': 'truck', 'color': [180, 30, 80]},
 20: {'label': 'other-vehicle', 'color': [255, 0, 0]},
 30: {'label': 'person', 'color': [30, 30, 255]},
 31: {'label': 'bicyclist', 'color': [200, 40, 255]},
 32: {'label': 'motorcyclist', 'color': [90, 30, 150]},
 40: {'label': 'road', 'color': [255, 0, 255]},
 44: {'label': 'parking', 'color': [255, 150, 255]},
 48: {'label': 'sidewalk', 'color': [75, 0, 75]},
 49: {'label': 'other-ground', 'color': [75, 0, 175]},
 50: {'label': 'building', 'color': [0, 200, 255]},
 51: {'label': 'fence', 'color': [50, 120, 255]},
 52: {'label': 'other-structure', 'color': [0, 150, 255]},
 60: {'label': 'lane-marking', 'color': [170, 255, 150]},
 70: {'label': 'vegetation', 'color': [0, 175, 0]},
 71: {'label': 'trunk', 'color': [0, 60, 135]},
 72: {'label': 'terrain', 'color': [80, 240, 150]},
 80: {'label': 'pole', 'color': [150, 240, 255]},
 81: {'label': 'traffic-sign', 'color': [0, 0, 255]},
 99: {'label': 'other-object', 'color': [255, 255, 50]},
 252: {'label': 'moving-car', 'color': [245, 150, 100]},
 253: {'label': 'moving-bicyclist', 'color': [200, 40, 255]},
 254: {'label': 'moving-person', 'color': [30, 30, 255]},
 255: {'label': 'moving-motorcyclist', 'color': [90, 30, 150]},
 256: {'label': 'moving-on-rails', 'color': [255, 0, 0]},
 257: {'label': 'moving-bus', 'color': [250, 80, 100]},
 258: {'label': 'moving-truck', 'color': [180, 30, 80]},
 259: {'label': 'moving-other-vehicle', 'color': [255, 0, 0]}}



# Labels Map
labels_map = {
    0: "unlabeled",
    1: "outlier",
    10: "car",
    11: "bicycle",
    13: "bus",
    15: "motorcycle",
    16: "on-rails",
    18: "truck",
    20: "other-vehicle",
    30: "person",
    31: "bicyclist",
    32: "motorcyclist",
    40: "road",
    44: "parking",
    48: "sidewalk",
    49: "other-ground",
    50: "building",
    51: "fence",
    52: "other-structure",
    60: "lane-marking",
    70: "vegetation",
    71: "trunk",
    72: "terrain",
    80: "pole",
    81: "traffic-sign",
    99: "other-object",
    252: "moving-car",
    253: "moving-bicyclist",
    254: "moving-person",
    255: "moving-motorcyclist",
    256: "moving-on-rails",
    257: "moving-bus",
    258: "moving-truck",
    259: "moving-other-vehicle"
}