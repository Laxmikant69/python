def Tower_of_Hanoi(disk,src,dest,axiliary):
    if disk==1:
        print("Transfer disk 1 from source",src,"to destination",dest)
        return
    Tower_of_Hanoi(disk-1,src,axiliary,dest)
    print("Transfer disk",disk,"from source",src,"to destination",dest)
    Tower_of_Hanoi(disk-1,axiliary,dest,src)

disk=int(input("for how many rings you want to search."))
Tower_of_Hanoi(disk,'A','B','C')
