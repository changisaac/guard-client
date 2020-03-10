# Code Notes

##Note on how frames are referenced in the db:

Each detection ran frame represents the collection 
of non-detection ran frames before and after the frame
up till the previous and next detection ran frame

ex: detection ran frames = 0.png, 100.png then the detections
    for 0.png in the db will reference the frames from 0 to 100

ex: detection ran frames = 0.png , 100.png, 200.png then the detections
    for 100.png in the db will reference the frames from 0 to 200

#Setup Notes

##To load new bag files into the db:

- Pull git repo `guard-client`
- download pre-trained weights for yolov3 and place into `object_detection/nn_data` directory
    - link for downloads in README in diriectory
- If collected separate gpx file make sure gpx file is in gps directory
and that the `gps_processor.py` is ran on it to reformat the gps data into a json
- Place bag file of images in directory specified by `img_bag_file` in `main()` of `frrame_processor.py`
- Delete everything in directory images are written to specified in `img_out_dir` in `main()` of `frame_processor.py` so no duplicate image files
- Specify ros topic of image in rosbag under `img_topic` in `main()` of `frame_processor.py`
- Drop `guard-db-test` in mongodb if re-running an old rosbag to avoid duplicate documents
- Make sure `guard_constants.py` has correct vlaues for mongodb host and download directory 'DOWNLOAD_DIR'
- Make sure separate script is ran to insert all images into correct places in s3
    - Location in s3 of raw imagse: `images/<collector_id>/<collection_seq>`
    - Though this is not needed for loading image data to db this is the pattern referenced in the db
    - Without the images loaded to the correct place, downloading queries will not work
- Run `python frame_processor.py`
- The directory specified in th `main()` of `frame_processor.py` for `img_out_dir` will start filling up with images
- After it finishes extracting all images, the script will start running object detecion and put them in a dirctory called `object_detecions` under the specified `img_out_dir` in `framr_processo.py` 
- Along the way intermediary data with image meta data and detection data is also output to json
- After object detection, script will parse all json files and place into dbs accordingly
- Once this is complete GuardClient can be used

