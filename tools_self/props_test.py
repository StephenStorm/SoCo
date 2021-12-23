

with open(ann_file, "r") as f:
    contents = f.readlines()
    images_props = [None] * len(contents)
    for i, line_str in enumerate(contents):
        path_contents = [c for c in line_str.split('\t')]
        im_file_name = path_contents[0]
        basename = os.path.basename(im_file_name).split('.')[0]
        all_props = props_dict[basename]
        converted_props = convert_props(all_props)
        images_props[i] = converted_props  # keep all propos

    del contents