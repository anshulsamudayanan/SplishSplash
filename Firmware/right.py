from kmk.modules.split import Split

def side_config(split: Split):
    split.split_side = Split.SplitSide.RIGHT
    split.central = False
