import cv2
import os

# 対応したパスを指定
path = "zaki.jpg"

# 学習済みの顔検出モデル（カスケード分類器）のパス
cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_alt.xml')

# 画像を読み込む
img = cv2.imread(path)
if img is None:
    print("Error: Could not read image file. Please check the path.")
    exit() # 画像が読み込めなかった場合はプログラムを終了する

# 画像をグレースケールに変換
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 学習済みモデルを読み込む
cascade = cv2.CascadeClassifier(cascade_path)
if cascade.empty():
    print("Error: Could not load cascade classifier. Please check the path.")
    exit() # カスケードファイルが読み込めなかった場合はプログラムを終了する

# 顔を検出する
face = cascade.detectMultiScale(img_gray, scaleFactor=1.09, minNeighbors=2, minSize=(35, 35))

print(f"Detected {len(face)} faces.") # 検出した顔の数を表示

for (x, y, w, h) in face:
# 検出した顔の座標を取得し、四角形で囲む
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

# 画像サイズを変更する
# scale_factor = 0.1 # 3倍に拡大
# new_width = int(img.shape[1] * scale_factor)
# new_height = int(img.shape[0] * scale_factor)
# resized_img = cv2.resize(img, (new_width, new_height))

# 結果の画像を表示する
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2

# img = cv2.imread("zaki.jpg")
# cv2.imshow("test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()