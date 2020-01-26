import sys
import os
from PIL import Image, ImageDraw, ImageFilter


def create_thumbnail(base_img_path):
	"""
	メイン関数
	グローバルに変数を定義しないように作った関数
	
	Parameters
	----------
	base_img_path: string
		サムネイル画像化したい画像のパス
	"""
	
	# 元画像を開く
	base_img = Image.open(base_img_path)
	
	# 画像の大きさを取得
	width, height = base_img.size
	
	size = 0		# 長辺の長さ　サムネイルを正方形にするために使う
	paste_x = 0		# 貼り付け先X座標　サムネイル画像の中心に元画像が来るようにするためにつかう
	paste_y = 0		# 貼り付け先Y座標　サムネイル画像の中心に元画像が来るようにするためにつかう

	# ファイル名と拡張子を切り分ける
	file_name, ext = os.path.splitext(base_img.filename)
	
	
	if width == height:
		# 辺の長さ同じとき、ファイル名を変えて終わり
		base_img.save(base_img.filename + "_thumbnail" + ext, base_img.format)
		return
	elif width > height:
		# 長辺を幅に設定し、すき間ができるY位置を調整する
		size = width
		paste_y = int( (width - height) / 2 )	# 整数化するのはピクセル位置が整数だから
	else:
		# 長辺を高さに設定し、すき間ができるX位置を調整する
		size = height
		paste_x = int( (height - width) / 2 )	# 整数化するのはピクセル位置が整数だから
	
	# 長辺サイズの正方形画像を作成
	thumbnail = Image.new(base_img.mode, (size, size), 0xffcccccc)
	
	# 元画像の貼り付け
	thumbnail.paste(base_img, (paste_x, paste_y))

	# ファイルの保存　元ファイル名のベース名に「_thumbnail」をつける
	thumbnail.save(file_name + "_thumbnail" + ext, base_img.format)

	


def main(argv):
	"""
	メイン関数
	グローバルに変数を定義しないように作った関数
	
	Parameters
	----------
	argv: list
		このスクリプトを実行したときの引数をそのままこの関数として渡す
	"""
	
	
	if len(argv) < 2:
		# 引数が無かったら使い方を表示して終了する
		print("[usuage] thumb.py image_path")
		return
		
	# サムネイル画像の作成
	create_thumbnail(argv[1])
	


if __name__ == '__main__':
	main(sys.argv)