import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

WIDTH = 16
HEIGHT = 9
N_STARS = 1200
FPS = 30
DURATION_SEC = 30 
OUTFILE = f"stars_loop_{DURATION_SEC}s.mp4"

frames = int(DURATION_SEC * FPS)
interval_ms = int(1000 / FPS)

fig, ax = plt.subplots(figsize=(16,9), facecolor='black')
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_facecolor('black')
ax.axis('off')

np.random.seed(42)

star_x = np.random.uniform(0, WIDTH, N_STARS)
star_y = np.random.uniform(0, HEIGHT, N_STARS)
per_frame_shift = -WIDTH / frames
star_vx = np.full(N_STARS, per_frame_shift)

stars = ax.scatter(star_x, star_y, c='white', s=1.5, alpha=0.9)

def init():
    global star_x, star_y, star_vx
    np.random.seed(42)
    star_x = np.random.uniform(0, WIDTH, N_STARS)
    star_y = np.random.uniform(0, HEIGHT, N_STARS)
    star_vx = np.full(N_STARS, per_frame_shift)
    stars.set_offsets(np.c_[star_x, star_y])
    return stars,

def anim(f):
    global star_x, star_y, star_vx
    star_x = (star_x + star_vx) % WIDTH
    stars.set_offsets(np.c_[star_x, star_y])
    return stars,

ani = animation.FuncAnimation(fig, anim, frames=frames, init_func=init,
                              interval=interval_ms, blit=True)

ani.save(OUTFILE, fps=FPS, writer='ffmpeg', dpi=120)
print(f"Saved {OUTFILE} ({DURATION_SEC}s loop, {frames} frames @ {FPS} fps)")