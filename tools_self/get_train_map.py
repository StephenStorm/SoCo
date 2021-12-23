import os
from glob import glob


root = '/opt/tiger/minist/datasets/imagenet/ILSVRC/Data/CLS-LOC/train'
class_name_file = 'selective_search/complete_class_names.txt'
map_file = '/opt/tiger/minist/datasets/imagenet/train_map.txt'

idx = 0

with open(class_name_file, 'r') as rf:
    class_names = rf.readlines()

class_names = [name.strip() for name in class_names]
print(len(class_names))


class_idx = {}
idx = 0
for name in class_names :
    class_idx[name] = idx
    idx = idx + 1

class_dir = os.listdir(root)
with open(map_file,'w') as wf:
    for name in class_dir:
        if name in class_names:
            local_class_dir = os.path.join(root, name)
            print(local_class_dir+'/*')
            images = glob(local_class_dir+'/*')
            # print(iamges)
            for img in images:
                wf.write(img + '   ' + str(class_idx[name]) + '\n')

        


# with open(class_name_file, 'r') as rf, open(map_file,'w') as wf:
#     for line in rf:
#         wf.write(line.strip() + '    ' + str(idx)+'\n')
#         idx = idx + 1
        