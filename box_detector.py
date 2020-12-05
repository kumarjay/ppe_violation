from detectron2.structures import BoxMode
import json
import cv2
import numpy as np
import pandas as pd


def get_warehouse_box(csv_file, img_dir):
    # json_file = os.path.join(img_dir, "via_region_data.json")
    df = pd.read_csv(csv_file)
    # df= data
    # print('unique values is.......', df['class'].unique())
    df['filename'] = df['filename'].map(lambda x: img_dir + x)

    classes = ['helmet', 'jacket', 'person', 'shoes', 'no_helmet', 'no_jacket']

    df['class_int'] = df['class'].map(lambda x: classes.index(x))
    # print(df.head())
    # print('file name is........', df['filename'])

    # with open(json_file) as f:
    #     imgs_anns = json.load(f)

    dataset_dicts = []
    for filename in df['filename'].unique().tolist():
        record = {}
        #

        # filename = os.path.join(img_dir, v["filename"])
        try:
            print('reading......', filename)
            height, width = cv2.imread(filename).shape[:2]

            record["file_name"] = filename
            # record["image_id"] = idx
            record["height"] = height
            record["width"] = width

            # annos = v["regions"]
            objs = []
            for index, row in df[df['filename'] == filename].iterrows():
                # assert not anno["region_attributes"]
                # anno = anno["shape_attributes"]
                # px = anno["all_points_x"]
                # py = anno["all_points_y"]
                # poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
                # poly = [p for x in poly for p in x]

                obj = {
                    "bbox": [row['xmin'], row['ymin'], row['xmax'], row['ymax']],
                    "bbox_mode": BoxMode.XYXY_ABS,
                    "category_id": row['class_int'],
                    "iscrowd": 0
                }
                objs.append(obj)
            record["annotations"] = objs
            dataset_dicts.append(record)
        except:
            print('file not able to read......', filename)
    return dataset_dicts