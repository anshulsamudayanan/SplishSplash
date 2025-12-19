from kmk.modules.split import Split

def side_config(split: Split):
    split.split_side = Split.SplitSide.LEFT
    split.central = True
