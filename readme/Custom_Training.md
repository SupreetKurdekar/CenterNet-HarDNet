# Changes made for custom training

## Custom dataset class added to datasets - coco_custom.py

Here add class ids of required ids to self._valid_ids

only required class images are extracted from the COCO dataset to make the custom dataset.

## datasets/sample/ctdet.py update

the img_transform function now handles the annotations only for required classes and ignores extra classes in the images.

## datset_factory.py updated to hold COCO_custom class

## exp/ctdet/hardnet68/log

The log file contains the training values for two epochs.
It was taking too long to train on my personal laptop.
Even after reducing the datset to only " truck, cat and dog classes " I was only able to use a batch size of 4

## Running the main script

### COCO datset
download the coco dataset ad specified in the original setup tutorial

### use below command from src folder to run the training.

python main.py ctdet --exp_id coco_h68 --arch hardnet_68 --batch_size 4 --dataset COCO_custom --master_batch 6 --lr 5e-3 --gpus 0 --num_workers 0 --num_epochs 150 --lr_step 100,130


