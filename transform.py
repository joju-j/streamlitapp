import os
from collections import OrderedDict
import torch
from PIL import Image
import torchvision.transforms as transforms

from lib.networks import define_G
from lib.util import tensor2im, save_image
from columns import columns

count=0
# models = {
#     'resnet': {'path': 'models/cyclegan-resnet.pth', 'input_nc': 3, 'output_nc': 3, 'netG': "resnet_9blocks", 'norm': "instance", },
#     'unet': {'path': 'models/cyclegan-unet.pth', 'input_nc': 3, 'output_nc': 3, 'netG': "unet_256", 'norm': "instance", },
#     'pix2pix': {'path': 'models/pix2pix.pth', 'input_nc': 3, 'output_nc': 3, 'netG': "unet_256", 'norm': "batch", },
# }

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


def create_generator(model):
    model_dict = torch.load(model['path'])
    new_dict = OrderedDict()
    for k, v in model_dict.items():
        new_dict[k] = v
    generator_model = define_G(input_nc=model['input_nc'], output_nc=model['output_nc'], netG=model['netG'],
                               norm=model['norm'], ngf=64, use_dropout=False, init_gain=0.02, gpu_ids=[])
    generator_model.load_state_dict(new_dict)

    # Set the model to evaluation mode
    generator_model.eval()

    return generator_model


def sketch2fashion(generator_model, input_image_path, output_image_path,count,types):
    
    
    input_image = Image.open(input_image_path).convert('RGB')
    image_size = input_image.size

    # Preprocess the input image
    input_tensor = transform(input_image).unsqueeze(0)

    # Pass the input image through the generator model
    with torch.no_grad():
        output_tensor = generator_model(input_tensor)

    # Postprocess the output image
    if types=="resnet":
        output_image_resnet = tensor2im(output_tensor)
        print(type(output_image_resnet))
        # output_image = output_image.resize(image_size)
        #Invoke Columns and output
        columns(input_image,output_image_resnet,count,types)
    elif types=="unet":
        output_image_unet = tensor2im(output_tensor)
        print(type(output_image_unet))
        # output_image = output_image.resize(image_size)
        
        #Invoke Columns and output
        columns(input_image,output_image_unet,count,types)
    # elif types=="pix2pix":  
    #     output_image_pix2pix = tensor2im(output_tensor)
    #     print(type(output_image_pix2pix))
    #     # output_image = output_image.resize(image_size)
        
    #     #Invoke Columns and output
    #     columns(input_image,output_image_pix2pix,count,types)



# # set up generators
# resnet = create_generator(models['resnet'])
# print("CycleGAN (Gen: Resnet): Ready", end='\n\n')

# unet = create_generator(models['unet'])
# print("CycleGAN (Gen: U -NET): Ready", end='\n\n')

# pix2pix = create_generator(models['pix2pix'])
# print("Pix 2 Pix (Gen: U NET): Ready", end='\n\n')


# RUNNER

# sketch2fashion(resnet, input_image_path='test.jpg', output_image_path='out_resnet.jpg')
# sketch2fashion(unet, input_image_path='test.jpg', output_image_path='out_unet.jpg')
# sketch2fashion(pix2pix, input_image_path='test.jpg', output_image_path='out_pix2pix.jpg')

# import time

# for file_name in os.listdir('images'):
#     if file_name.endswith(".png"):
#         file_path = 'images/' + file_name
#         sketch2fashion(resnet, input_image_path=file_path, output_image_path='out_resnet.jpg')
#         sketch2fashion(unet, input_image_path=file_path, output_image_path='out_unet.jpg')
#         sketch2fashion(pix2pix, input_image_path=file_path, output_image_path='out_pix2pix.jpg')
#         time.sleep(2)
