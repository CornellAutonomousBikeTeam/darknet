# match categories to line numbers
with open("../selectedtrain.txt", "r") as data:
    selected = open("../trainLong.txt", "w")

    objectIDs = {
        1:0,
        2:1,
        3:2,
        4:3,
        6:4,
        8:5,
        10:6,
        11:7,
        13:8,  
        14:9,
        15:10,
        17:11,
        18:12,
        64:13
    }

    for line in data:
        # keep track of whether we've added the file path to the beginning of the line
        path = False

        # chunks within line
        chunks = line.split(" ")
        for i in range(1, len(chunks)):

            # numbers to describe each object
            nums = chunks[i].split(",")

            # convert category number
            # print("before " + nums[4])
            nums[4] = str(objectIDs.get(int(nums[4])))
            # print("after " + nums[4])

            if not path: # if path isn't on line yet
                selected.write(chunks[0])
                path = True
            
            newChunk = nums[0] + "," + nums[1] + ',' + nums[2] + "," + nums[3] + "," + nums[4]
            # copy over chunk
            selected.write(" " + newChunk.strip())
        selected.write('\n')
