# 进行人脸录入 / face register
# 录入多张人脸 / support multi-faces

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Dlib_face_recognition_from_camera
# Mail:     coneypo@foxmail.com

# Created at 2018-05-11
# Updated at 2018-10-29

import dlib         # 人脸处理的库 Dlib
import numpy as np  # 数据处理的库 Numpy
import cv2          # 图像处理的库 OpenCv

import os           # 读写文件
import shutil       # 读写文件

# Dlib 正向人脸检测器
detector = dlib.get_frontal_face_detector()

# Dlib 68 点特征预测器
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# OpenCv 调用摄像头
cap = cv2.VideoCapture(0)

# 设置视频参数
# cap.set(3, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
size = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
_,frame = cap.read()
print(size) # 正确结果（1024,1280）
print(frame.shape)# 正确结果（1024,1280, 3）

# 人脸截图的计数器
cnt_ss = 0

# 存储人脸的文件夹
current_face_dir = 0

# 保存的路径
path_make_dir = "/Users/shucan/Documents/ai_study/face_recognition/data/data_faces_from_camera/"
path_csv = "/Users/shucan/Documents/ai_study/face_recognition/data/data_csvs_from_camera/"


# (optional) 删除之前存的人脸数据文件夹
def pre_clear():
    folders_rd = os.listdir(path_make_dir)
    for i in range(len(folders_rd)):
        shutil.rmtree(path_make_dir+folders_rd[i])

    csv_rd = os.listdir(path_csv)
    for i in range(len(csv_rd)):
        os.remove(path_csv+csv_rd[i])


# 每次程序录入之前，删掉之前存的人脸数据
pre_clear()


# 人脸种类数目的计数器
person_cnt = 0

while cap.isOpened():
    print("打印人脸截图的计数器", cnt_ss)
    # 480 height * 640 width
    # cap.read()按帧读取视频，每次读取一帧数据进行数据操作
    flag, img_rd = cap.read()
    # 这里读取出来的是720 1280，所以调取出来的摄像机的大小其实就是720 1280
    print("输出一下numpy.ndarray大小", img_rd.size)
    # 输出的其实是一个三维数组
    print("输出一下numpy.ndarray的维度shape", img_rd.shape)
    # print(type(img_rd))
    # print(img_rd)
    kk = cv2.waitKey(1)

    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)

    print("RGB颜色空间转换成灰度", img_gray)
    print("灰度图的shape", img_gray.shape)

    # 人脸数 faces
    faces = detector(img_gray, 0)

    # 待会要写的字体
    font = cv2.FONT_HERSHEY_COMPLEX

    # 按下 'n' 新建存储人脸的文件夹
    if kk == ord('n'):
        person_cnt += 1
        current_face_dir = path_make_dir + "person_" + str(person_cnt)
        print('\n')
        for dirs in (os.listdir(path_make_dir)):
            if current_face_dir == path_make_dir + dirs:
                shutil.rmtree(current_face_dir)
                print("删除旧的文件夹:", current_face_dir)
        os.makedirs(current_face_dir)
        print("新建的人脸文件夹: ", current_face_dir)

        # 将人脸计数器清零
        cnt_ss = 0

    # 其实底层每触发一次检测到人脸的的机制这里就会调用一次，底层一直在人脸检测到机制
    if len(faces) != 0:
        # 检测到人脸

        # 矩形框
        for k, d in enumerate(faces):
            # print("输出K值", k)
            # print("输出d值", d)
            print("输出d.left", d.left())
            print("输出d.top", d.top())
            print("输出d.right", d.right())
            print("输出d.bottom", d.bottom())

            # 计算矩形大小
            # (x,y), (宽度width, 高度height)
            pos_start = tuple([d.left(), d.top()])
            print(pos_start)
            pos_end = tuple([d.right(), d.bottom()])
            print(pos_end)

        # 计算矩形框大小
            height = (d.bottom() - d.top())
            width = (d.right() - d.left())

            hh = int(height/2)
            ww = int(width/2)

            # 设置颜色 / The color of rectangle of faces detected
            color_rectangle = (255, 255, 255)
            if (d.right()) + ww > 1280 or (d.bottom() + hh >720) or (d.left() - ww < 0) or ( d.top() -hh < 0):
                cv2.putText(img_rd, "OUT OF RANGE", (20, 300), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                color_rectangle = (0, 0, 255)
            else:
                color_rectangle = (255, 255, 255)

            cv2.rectangle(img_rd,
                          #对角线坐标构建矩形边框
                          tuple([d.left() , d.top() ]),
                          tuple([d.right() , d.bottom() ]),
                          color_rectangle, 4)

            # 根据人脸大小生成空的图像
            im_blank = np.zeros((int(height*2), width*2, 3), np.uint8)

            # 按下 's' 保存摄像头中的人脸到本地
            if kk == ord('s'):
                cnt_ss += 1
                for ii in range(height * 2):    # 循环742次
                    for jj in range(width * 2):   # 循环744次
                        # hh=371/2 = 185 ww = 372/2 = 186
                        # print(ii)
                        # print(jj)
                        # print(d.top()-hh + ii)
                        # print(d.left()-ww+ jj)
                        im_blank[ii][jj] = img_rd[d.top() - hh + ii][d.left() - ww + jj]
                cv2.imwrite(str(current_face_dir) + "/img_face_" + str(cnt_ss) + ".jpg", im_blank)
                print("写入本地：", str(current_face_dir) + "/img_face_" + str(cnt_ss) + ".jpg")

        # 显示人脸数
    cv2.putText(img_rd, "Faces: " + str(len(faces)), (20, 100), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

    # 添加说明
    cv2.putText(img_rd, "Face Register", (20, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img_rd, "N: New face folder", (20, 350), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img_rd, "S: Save face", (20, 400), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img_rd, "Q: Quit", (20, 450), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)

    # 按下 'q' 键退出
    if kk == ord('q'):
        break

    # 窗口显示
    # cv2.namedWindow("camera3", 0) # 如果需要摄像头窗口大小可调
    cv2.imshow("camera", img_rd)

# 释放摄像头
cap.release()

# 删除建立的窗口,关闭所有的图像窗口
cv2.destroyAllWindows()


#cv2.waitKey(1)，waitKey（）方法本身表示等待键盘输入，

#参数是1，表示延时1ms切换到下一帧图像，对于视频而言；

#参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停,；

#参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿