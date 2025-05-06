import os

from .dataset_colmap import ColmapDataset
from .utils import read_colmap_extrinsics_text, read_colmap_intrinsics_text


class ScannetppDataset(ColmapDataset):

    def __init__(
        self,
        path,
        device="cuda",
        split="train",
        downsample_factor=1,
        test_split_interval=8,
        ray_jitter=None,
    ):
        super(ScannetppDataset,
              self).__init__(path, device, split, downsample_factor,
                             test_split_interval, ray_jitter)

    def load_intrinsics_and_extrinsics(self):
        raise NotImplementedError

    def get_images_folder(self):
        return "image_undistorted_fisheye"
