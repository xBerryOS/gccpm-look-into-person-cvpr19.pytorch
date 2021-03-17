import cv2
from torch.utils.data import Dataset


class SimpleVideoDataset(Dataset):
    def __init__(self):
        super().__init__()
        vidcap = cv2.VideoCapture('data/whole_body.mp4')
        self.images = []
        for _ in range(250):
            success, image = vidcap.read()
            if not success:
                break
            self.images.append(
                image
                # cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            )

    def __len__(self):
        return len(self.images)

    def __getitem__(self, item):
        return {
            'image': self.images[item],
            'file_name': f'{item}.jpg'
        }
