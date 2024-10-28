from mpl_colr2svg.color_emoji_blackrenderer import ColorEmojiBlackrenderer

fontPath = "seguiemj.ttf"
textString = "L❤️VE"

emoji = ColorEmojiBlackrenderer(fontPath)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1, clear=True, num=1)

emoji.annotate(ax, textString, (0.5, 0.5), fontsize=128)
# ax.set_aspect(1)

plt.show()
