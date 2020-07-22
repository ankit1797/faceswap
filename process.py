import imageio
from datetime import datetime
print(datetime)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")
from demo import make_animation
from demo import load_checkpoints
from skimage import img_as_ubyte
# import asyncio


def get(source_image, driving_video):
    source_image = imageio.imread(source_image)
    driving_video = imageio.mimread(driving_video)


    #Resize image and video to 256x256

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    generator, kp_detector = load_checkpoints(config_path='./first-order-motion-model/config/vox-256.yaml', 
                                checkpoint_path='./vox-cpk.pth.tar')

    
    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

    #save resulting video
    imageio.mimsave('./files/generated.mp4', [img_as_ubyte(frame) for frame in predictions])
    #video can be downloaded from /content folder
    return True