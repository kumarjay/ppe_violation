from detectron2.utils.visualizer import Visualizer

import time
import cv2
import datetime
from config_detectron import configuration
from metadata import meta_data
from db_crud import create

predictor= configuration()
ppe_metadata= meta_data()


def camera(cam, frame_):
    t1 = time.time()
    violated = [2, 1, 4]

    cap = cv2.VideoCapture(f'rtsp://root:root@10.0.87.{cam}/stream1')
    ii = 30
    abc = False

    print(t1)
    print(cam, ' ', frame_)
    while (cap.isOpened()):
        ret, frame = cap.read()

        if time.time() - t1 >= 0.5:

            try:
                dict_ = {1: False,
                         2: False,
                         4: False}
                print(frame.shape)
                # frame= cv2.resize(frame, (800,600))
                output = predictor(frame)
                print('hello...', frame.shape)

                objs = output['instances'].get('pred_classes')

                visualizer = Visualizer(frame[:, :, ::-1], metadata=ppe_metadata, scale=0.5)

                out = visualizer.draw_instance_predictions(output['instances'].to('cpu'))
                # classes_= [value for value in output['instances'].pred_classes if value in a]
                cam_viol = list(set(violated) & set(output['instances'].pred_classes.numpy()))
                # for values in  output['instances'].pred_classes:
                if cam_viol:
                    print(cam_viol)
                    for cam_ in cam_viol:
                        dict_.update({cam_: True})

                    print(dict_)
                    print('camera name is...', f'LM_{cam}')

                    cv2.imwrite(f'C:\\Users\\rstps.ithelpdesk3\\Documents\\PPE_VIOLATION\\LM_{cam}\\abc_0a0{ii}.jpg',
                                out.get_image()[:, :, ::-1])
                    print('Create....')

                    value= create(dict_[2], dict_[1], dict_[4], cam)
                    # cursor = conn.cursor()
                    # cursor.execute(
                    #     "insert into ppe_vio(Date, Time, Helmet, Jacket, Shoes, Camera, Image) values(?,?,?,?,?,?,?)",
                    #     (date.today().strftime('%Y-%m-%d'), datetime.time(datetime.now()).strftime('%H:%M:%S'),
                    #      dict_[2], dict_[1], dict_[4], f'LM_{cam}', f'{cam}_000{ii}.jpg'))
                    # conn.commit()
                    # read(conn)
                    print(value)

                print('out is....', out)

                cv2.imshow(f"{frame_}", out.get_image()[:, :, ::-1])
                # frame3= np.hstack((f'{frame_}',f'{frame_}'))
                t1 = time.time()
                ii += 1

                # cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                print('frame not captured')
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # cv2.destroyAllWindows('{frame_}')
                # cap= cv2.VideoCapture(f'rtsp://root:root@10.0.87.{cam}/stream1')
                break

    cap.release()
    cv2.destroyAllWindows()
