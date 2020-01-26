import sys
import os
from PIL import Image, ImageDraw, ImageFilter


def create_thumbnail(base_img_path):
	"""
	���C���֐�
	�O���[�o���ɕϐ����`���Ȃ��悤�ɍ�����֐�
	
	Parameters
	----------
	base_img_path: string
		�T���l�C���摜���������摜�̃p�X
	"""
	
	# ���摜���J��
	base_img = Image.open(base_img_path)
	
	# �摜�̑傫�����擾
	width, height = base_img.size
	
	size = 0		# ���ӂ̒����@�T���l�C���𐳕��`�ɂ��邽�߂Ɏg��
	paste_x = 0		# �\��t����X���W�@�T���l�C���摜�̒��S�Ɍ��摜������悤�ɂ��邽�߂ɂ���
	paste_y = 0		# �\��t����Y���W�@�T���l�C���摜�̒��S�Ɍ��摜������悤�ɂ��邽�߂ɂ���

	# �t�@�C�����Ɗg���q��؂蕪����
	file_name, ext = os.path.splitext(base_img.filename)
	
	
	if width == height:
		# �ӂ̒��������Ƃ��A�t�@�C������ς��ďI���
		base_img.save(base_img.filename + "_thumbnail" + ext, base_img.format)
		return
	elif width > height:
		# ���ӂ𕝂ɐݒ肵�A�����Ԃ��ł���Y�ʒu�𒲐�����
		size = width
		paste_y = int( (width - height) / 2 )	# ����������̂̓s�N�Z���ʒu������������
	else:
		# ���ӂ������ɐݒ肵�A�����Ԃ��ł���X�ʒu�𒲐�����
		size = height
		paste_x = int( (height - width) / 2 )	# ����������̂̓s�N�Z���ʒu������������
	
	# ���ӃT�C�Y�̐����`�摜���쐬
	thumbnail = Image.new(base_img.mode, (size, size), 0xffcccccc)
	
	# ���摜�̓\��t��
	thumbnail.paste(base_img, (paste_x, paste_y))

	# �t�@�C���̕ۑ��@���t�@�C�����̃x�[�X���Ɂu_thumbnail�v������
	thumbnail.save(file_name + "_thumbnail" + ext, base_img.format)

	


def main(argv):
	"""
	���C���֐�
	�O���[�o���ɕϐ����`���Ȃ��悤�ɍ�����֐�
	
	Parameters
	----------
	argv: list
		���̃X�N���v�g�����s�����Ƃ��̈��������̂܂܂��̊֐��Ƃ��ēn��
	"""
	
	
	if len(argv) < 2:
		# ����������������g������\�����ďI������
		print("[usuage] thumb.py image_path")
		return
		
	# �T���l�C���摜�̍쐬
	create_thumbnail(argv[1])
	


if __name__ == '__main__':
	main(sys.argv)