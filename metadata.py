from detectron2.data import DatasetCatalog, MetadataCatalog
from box_detector import get_warehouse_box

classes= ['helmet', 'jacket', 'person', 'shoes', 'no_helmet', 'no_jacket']


def meta_data():
    for d in ["train", "test"]:
        DatasetCatalog.register("/content/drive/My Drive/experiment2/" + d, lambda d=d: get_warehouse_box("/content/drive/MyDrive/NTPC_PPE/csv/PPE_labels.csv", "/content/drive/MyDrive/NTPC_PPE/Jay/"))
        MetadataCatalog.get("/content/drive/My Drive/experiment2/" + d).set(thing_classes=classes)
    ppe_metadata = MetadataCatalog.get("/content/drive/My Drive/experiment2/train")

    return ppe_metadata