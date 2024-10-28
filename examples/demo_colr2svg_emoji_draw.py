import matplotlib.pyplot as plt
from mpl_colr2svg import ColorEmoji

c = "🤐"
# c = '🇰🇷'
c = "😱"
# c = "🤩"
# c = "👽"
# c = "🍵"
# c = '☕'
# c = "😂"
# c = "✋🏾"
# c = "🏎️"


ftname = "seguiemj.ttf"
emoji = ColorEmoji(ftname)

fig, axs = plt.subplots(1, 2, figsize=(10, 5), clear=True, num=1)
ax1 = axs[0]
ax1.set_title("draw in data coordinate")
# ax1.set_aspect(1)

emoji.draw(ax1, c, size=128)

ax2 = axs[1]

emoji.annotate(ax2, c, (0.5, 0.5), fontsize=128)
ax2.set_title("drawing_area with annotate")

plt.show()
