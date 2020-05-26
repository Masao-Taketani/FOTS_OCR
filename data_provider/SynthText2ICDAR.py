import scipy.io as sio
import numpy as np
import xml.dom.minidom
import sys
import random
import os

def Mat2Xml(matfile, saveFolder):
    if os.path.exists(saveFolder) is False:
        os.makedirs(saveFolder)
    data = sio.loadmat(matfile)
    xmlFolder = os.path.join(saveFolder, 'anno')

    train_file = open(os.path.join(saveFolder, 'train.txt'), 'w')
    test_file = open(os.path.join(saveFolder, 'test.txt'), 'w')

    for i in range(len(data['txt'][0])):
        contents = []
        for val in data['txt'][0][i]:
            v = [x.split("\n") for x in val.strip().split(" ")]
            contents.extend(sum(v, []))
        print >> sys.stderr, "No.{} data".format(i)
        rec = np.array(data['wordBB'][0][i], dtype=np.int32)
        if len(rec.shape) == 3:
            rec = rec.transpose(2,1,0)
        else:
            rec = rec.transpose(1,0)[np.newaxis, :]

        doc = xml.dom.minidom.Document()
        root = doc.createElement('annotation')
        doc.appendChild(root)
        print("start to process {} object".format(len(rec)))

        for j in range(len(rec)):
            nodeobject = doc.createElement('object')
            nodecontent = doc.createElement('content')
            nodecontent.appendChild(doc.createTextNode(str(contents[j])))

            nodename = doc.createElement('name')
            nodename.appendChild(doc.createTextNode('text'))

            bndbox = {}
            bndbox['x1'] = rec[j][0][0]
            bndbox['y1'] = rec[j][0][1]
            bndbox['x2'] = rec[j][1][0]
            bndbox['y2'] = rec[j][1][1]
            bndbox['x3'] = rec[j][2][0]
            bndbox['y3'] = rec[j][2][1]
            bndbox['x4'] = rec[j][3][0]
            bndbox['y4'] = rec[j][3][1]
            bndbox['xmin'] = min(bndbox['x1'], bndbox['x2'], bndbox['x3'], bndbox['x4'])
            bndbox['xmax'] = max(bndbox['x1'], bndbox['x2'], bndbox['x3'], bndbox['x4'])
            bndbox['ymin'] = min(bndbox['y1'], bndbox['y2'], bndbox['y3'], bndbox['y4'])
            bndbox['ymax'] = max(bndbox['y1'], bndbox['y2'], bndbox['y3'], bndbox['y4'])

            nodebndbox = doc.createElement('bndbox')
            for k in bndbox.keys():
                nodecoord =  doc.createElement(k)
                nodecoord.appendChild(doc.createTextNode(str(bndbox[k])))
                nodebndbox.appendChild(nodecoord)

            nodeobject.appendChild(nodecontent)
            nodeobject.appendChild(nodename)
            nodeobject.appendChild(nodebndbox)
            root.appendChild(nodeobject)

        filename = data['imnames'][0][i][0].replace('.jpg', '.xml')
        fp = open(os.path.join(xmlFolder, filename), 'w')
        doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        fp.close()
        rad = random.uniform(10,20)
        pwd = os.getcwd()
        img_path = os.path.join(pwd, data['imnames'][0][i][0])
        xml_path = os.path.join(pwd, filename)
        file_line = img_path + " " + xml_path + '\n'
        if rad > 18:
            train_file.write(file_line)
        else:
            test_file.write(file_line)

    train_file.close()
    test_file.close()

def Mat2icdar(matfile, saveFolder):
    if os.path.exists(saveFolder) is False:
        os.makedirs(saveFolder)
    data = sio.loadmat(matfile)

    for i in range(len(data['txt'][0])):
        contents = []
        for val in data['txt'][0][i]:
            v = [x.strip().split(" ") for x in val.strip().split("\n")]
            # concatenate all of the list elements
            contents.extend(sum(v, []))
        contents = [el for el in contents if el != '']
        error_msg = "No.{} data".format(i)
        print(error_msg, file=sys.stderr)
        rec = np.array(data['wordBB'][0][i], dtype=np.int32)
        if len(rec.shape) == 3:
            rec = rec.transpose(2,1,0)
        else:
            rec = rec.transpose(1,0)[np.newaxis, :]

        root = []
        print("start to process {} object".format(len(rec)))
        assert len(rec) == len(contents), "filename {}: the length of the objects and the labels differ.".format(data['imnames'][0][i][0])

        for j in range(len(rec)):
            infos = []
            infos.append(str(int(rec[j][0][0])))
            infos.append(str(int(rec[j][0][1])))
            infos.append(str(int(rec[j][1][0])))
            infos.append(str(int(rec[j][1][1])))
            infos.append(str(int(rec[j][2][0])))
            infos.append(str(int(rec[j][2][1])))
            infos.append(str(int(rec[j][3][0])))
            infos.append(str(int(rec[j][3][1])))
            assert len(str(contents[j])) != 0, "filename {}: lebel length is 0".format(data['imnames'][0][i][0])
            infos.append(str(contents[j]))
            root.append(infos)

        filename = data['imnames'][0][i][0].replace('.jpg', '.txt')
        dir_name = os.path.dirname(filename)
        img_dir_path = os.path.join(saveFolder, dir_name)
        if not os.path.exists(img_dir_path):
            print("created dir {}".format(dir_name))
            os.makedirs(img_dir_path, exist_ok=True)
        fp = open(os.path.join(saveFolder, filename), 'w')
        fp.write('\n'.join([','.join([i for i in j]) for j in root]))
        fp.close()

if __name__=='__main__':
    Mat2icdar('data/SynthText/gt.mat', 'data/SynthText')
