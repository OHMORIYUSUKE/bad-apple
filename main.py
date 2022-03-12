import cv2
import os

full_path = os.getcwd()

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

print("動画を画像化中...")
save_all_frames('sample2.mp4', 'result_png', 'sample_video_img')

##

path = full_path + "/result_png"

files = os.listdir(path)
files.remove('.gitignore')

##

import numpy as np

print("画像を白黒化中...")

for file_name in files:
  # 入力画像を読み込み
  img = cv2.imread(full_path + "/result_png/" + file_name)

  # グレースケール変換
  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
      
  # しきい値       
  dst = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

      
  # 結果を出力
  cv2.imwrite(full_path + "/result_png2/" + file_name, dst)


##

from PIL import Image
import time

for file_name in files:
  # 画像データの読み込み
  img = Image.open(full_path + "/result_png2/" + file_name)
  ##
  img = img.resize((img.width // 2, img.height // 4))
  # 画像のサイズ(幅[px] x 高さ[px])を取得し、それぞれを変数に代入
  width, height = img.size

  # 0が格納された配列を画像のサイズと同じサイズで用意
  image_array = np.empty((height, width), dtype = int)

  for y in range(height):
      for x in range(width):
          # 順次、ピクセルの色を数値を代入している
          image_array[y][x] = img.getpixel((x, y))
  # 画像データが数値の配列になっていることが確認できる
  # print(image_array)
  for row in range(len(image_array)):
    for col in range(len(image_array[row])):
        if image_array[row][col] == 255:
          print("#", end='')
        else:
          print(" ", end='') 
    print()
  os.system('cls')