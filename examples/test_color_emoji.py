# import numpy as np
import pandas as pd
# from colr_to_svg import Colr2SVG
# from matplotlib.offsetbox import AnnotationBbox
import matplotlib.pyplot as plt

# %% prepare data

emoji_popularity = [["😂", 223.94],
                    ["🤣", 170.29],
                    ["❤️", 95.02],
                    ["🙏", 116.92],
                    ["😭", 95.02],
                    ["😍", 77.3],
                    ["✨", 76.34],
                    ["🔥", 71.52],
                    ["😊", 70.15],
                    ["🥰", 67.35],
                    ]

df = pd.DataFrame(emoji_popularity, columns=["Emoji", "Popularity"])


# %% use seabon to make barplot.

import seaborn as sns
sns.set_color_codes("muted")
sns.set(font_scale = 1.5)

fig, ax = plt.subplots(1, 1, figsize=(7, 4), clear=True, num=2, layout="constrained")

sns.barplot(x="Emoji", y="Popularity", data=df,
            label="Emoji Popularity", color="b")

# %% replace emoji with a ColorEmoji

from mpl_colr2svg import ColorEmoji

ftname = "seguiemj.ttf"
emoji = ColorEmoji(ftname)

fontsize = 25
for l in ax.get_xticklabels():
    c = l.get_text()
    xy = l.get_position()

    l.set_visible(False)

    emoji.annotate(ax, c, xy, xycoords=("data", "axes fraction"),
                   box_alignment=(0.5, 1), fontsize=fontsize,
                   annotation_clip=True)

ax.xaxis.labelpad = fontsize * 1.7

plt.show()
