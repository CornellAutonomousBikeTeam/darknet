# open file
# iterate file
# for each file
# make new txt
# in textfile, find dimension
# list class
# take coords and divide dimensions per class
# commit genocide to the eol

# convert match.py single file output to series of txt files that go in the images dir
# train.txt only contains image paths as specified according to AlexeyAB github
import cv2

with open("../trainLong.txt", "r") as file:
    with open("../data/train.txt", "w") as paths:
        for line in file:
            chunks = line.split(" ")
            paths.write(chunks[0]+"\n")

            with open(chunks[0][:-4]+".txt", "w") as image:
                h,w,_ = cv2.imread(chunks[0]).shape

                for i in range(1,len(chunks)):
                    nums = chunks[i].split(",")

                    x_min = int(nums[0])
                    y_min = int(nums[1])
                    x_max = int(nums[2])
                    y_max = int(nums[3])

                    x_center = ((x_min + x_max) / 2) / w
                    y_center = ((y_min + y_max) / 2) / h

                    wd = (x_max-x_min) / w
                    ht = (y_max-y_min) / h
                    # image.write(nums[4] +" " + str(x_center) + " " + str(y_center) + " " + str(wd) + " " + str(ht) + "\n")

                    text = "%s %f %f %f %f\n" % (nums[4].strip(), x_center, y_center, wd, ht) 
                    # object = "%s %f %f %f %f\n" % (nums[4], x_min, y_min, x_max, y_max) 
                    image.write(text)
