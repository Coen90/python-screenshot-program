import pyautogui
import time
import os
from PIL import Image

start_time = 5
start_num = 1
end_num = 551
folder_path = "C:/Users/codetree/Desktop/screenshot"
image_prefix = "img"
pdf_name = "test"

# time.sleep(2)
# print(pyautogui.position())


while start_time > 0:
    print(f'{start_time} seconds left, util start')
    time.sleep(1)
    start_time -= 1

while True:
    pyautogui.screenshot(f'{folder_path}/{image_prefix}_{str(start_num).zfill(4)}.png', region=(820, 85, 970, 1255))

    time.sleep(1) # 스크린샷 시간 간격이 필요하다면 추가한다. 1은 초이다.

    # pyautogui.press('right')
    pyautogui.click(2519, 712, duration=0.1)

    start_num += 1
    if(start_num == end_num):
        break

print("이미지 스크린샷 완료..")
print("이미지 스크린샷 완료..")
print("이미지 스크린샷 완료..")
print("이미지 스크린샷 완료..")
print()
print()

print("pdf 변환 시작")

dir_files = os.listdir(folder_path)
file_list = []
img_list = []
for file in dir_files:
    if file.startswith(image_prefix):
        file_list.append(file)
file_list.sort()

now = 1

for file in file_list:
    print(f'{round(now / len(file_list) * 100)} % 진행중 / {now} out of {len(file_list)} {file}')
    im_buf = Image.open(folder_path + "/" + file)
    cvt_rgb = im_buf.convert('RGB')
    img_list.append(cvt_rgb)
    now += 1

img_list[0].save(folder_path + "/" + pdf_name + ".pdf", save_all=True, append_images=img_list[1:])

print("pdf 변환 끝!!")







# 참고 자료

# screenshot
# https://puzizig.com/posts/256/

# image to pdf
# https://inbearblog.blogspot.com/2021/04/image-to-pdf.html