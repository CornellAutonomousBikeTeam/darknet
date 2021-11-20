with open("../rawtrain.txt", "r") as data:
    selected = open("../selectedtrain.txt", "w")

    objectIDs = {
    1:'person',
    2:'bicycle',
    3:'car',
    4:'motorcycle',
    6:'bus',
    8:'truck',
    10:'traffic light',
    11:'fire hydrant',
    13:'stop sign',  
    14:'parking meter',
    15:'bench',
    17:'cat',
    18:'dog', 
    64:'potted plant'
}

    for line in data:
        # keep track of whether we've added the file path to the beginning of the line
        path = False

        # chunks within line
        chunks = line.split(" ")
        for i in range(1, len(chunks)):

            # numbers to describe each object
            nums = chunks[i].split(",")

            # if the object is the right category
            if int(nums[4]) in objectIDs.keys():
                if not path: # if path isn't on line yet
                    selected.write(chunks[0])
                    path = True
                
                # copy over chunk
                selected.write(" " + chunks[i].strip())

        if path: # if we've written anything on this line
            selected.write('\n')
                



