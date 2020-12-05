import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as exe:
    cam = [8, 7]
    frame = ['frame 8', 'frame 7']
    exe.map(camera, cam, frame)
