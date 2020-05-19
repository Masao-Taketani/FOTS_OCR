import os
import numpy as np
import glob
from .data_loader import DataLoader
from .data_utils import label_to_array

class ICDARLoader(DataLoader):
	def __init__(self, edition='13', shuffle=False):
		super(ICDARLoader, self).__init__()
		self.edition = edition
		self.shuffle = shuffle # shuffle the polygons

	def load_annotation(self, gt_file):
		text_polys = []
		text_tags = []
		labels = []
		if not os.path.exists(gt_file):
			return np.array(text_polys, dtype=np.float32)
		with open(gt_file, 'r', encoding="utf-8-sig") as f:
			for line in f.readlines():
				try:
					line = line.replace('\xef\xbb\bf', '')
					line = line.replace('\xe2\x80\x8d', '')
					line = line.strip()
					line = line.split(',')
					if self.edition == '17':
						# skip the type of language part
						line.pop(8)
					# Deal with labels containing ","
					if len(line) > 9:
						label = line[8]
						for i in range(len(line) - 9):
							label = label + "," + line[i+9]
					else:
						label = line[-1]
					"""
					eval: evaluate equations written by letters
					(e.g.)
					>>> eval('1 + 2')
					3
					map: it applies a given function to every element of a given
					     array
				    	usage(python3): list(map(func, array))
					"""
					# converting the data type of each element from str to int
					temp_line = list(map(eval, line[:8]))
					x1, y1, x2, y2, x3, y3, x4, y4 = map(float, temp_line)

					text_polys.append([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
					if label == '*' or label == '###' or label == '':
						text_tags.append(True)
						labels.append([-1])
					else:
						labels.append(label_to_array(label))
						text_tags.append(False)
				except Exception as e:
					print(e)
					continue
		text_polys = np.array(text_polys)
		text_tags = np.array(text_tags)
		# data type↓: np.array, np.array, list of lines of letter ids
		return text_polys, text_tags, labels
