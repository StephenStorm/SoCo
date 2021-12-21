import os

imagenet_root = 'imagenet_root'
proposal_root = 'imagenet_root_proposals_mp'
split = 'train'

class_name_file = 'selective_search/complete_class_names.txt'

image_dir = os.path.join(imagenet_root, split)
proposal_dir = os.path.join(proposal_root, split)

class_names = sorted(os.listdir(image_dir))

proposal_names = sorted(os.listdir(proposal_dir))

done_class_names = [name+'\n' for name in class_names if name in proposal_names and len(os.listdir(os.path.join(image_dir, name))) == len(os.listdir(os.path.join(proposal_dir, name)))]

# print(done_class_names)
with open(class_name_file, 'w') as wf:
    wf.writelines(done_class_names)
print(len(done_class_names))