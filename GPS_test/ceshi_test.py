import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# 打开摄像头
cap = cv2.VideoCapture(0)

# 手动输入位置信息（中文）
location = "西安航空学院北教学楼"

while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 将 OpenCV 图像转换为 PIL 图像
    pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # 创建字体对象
    font = ImageFont.truetype("msyh.ttc", 24)  # 选择适合中文显示的字体文件（例如微软雅黑）

    # 在 PIL 图像上绘制地址信息
    draw = ImageDraw.Draw(pil_frame)
    draw.text((50, 50), location, font=font, fill=(255, 255, 255))  # 绘制中文字符

    # 将 PIL 图像转换为 OpenCV 图像
    frame_with_text = cv2.cvtColor(np.array(pil_frame), cv2.COLOR_RGB2BGR)

    # 显示图像
    cv2.imshow('Camera', frame_with_text)

    # 检测按键，按下 ESC 键退出循环
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 释放摄像头资源并关闭窗口
# cap.release()
# cv2.destroyAllWindows()
