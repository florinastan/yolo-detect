import cv2


def show_image(image, window_name='Image'):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def real_time_object_detection(yolo, video_path='video.mp4', output_path='output_video.avi'):
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if ret == False:
            print('Unable to read video')
            break

        try:
            pred_image = yolo.predictions(frame)
            out.write(pred_image)  # Write the frame to the output video
        except:
            pass

        cv2.imshow('YOLO', pred_image)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    out.release()
