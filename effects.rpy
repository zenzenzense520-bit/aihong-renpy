## 哀鸿 - 全局特效和变换系统

# ============================================================
# 屏幕震动效果
# ============================================================

transform slight_shake:
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 2
    linear 0.05 xoffset -2
    linear 0.05 xoffset 0

transform heavy_shake:
    linear 0.05 xoffset 8
    linear 0.05 xoffset -8
    linear 0.05 yoffset 5
    linear 0.05 yoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 yoffset 3
    linear 0.05 yoffset -3
    linear 0.05 xoffset 0
    linear 0.05 yoffset 0

transform heartbeat:
    linear 0.15 xoffset 2 yoffset -1
    linear 0.15 xoffset -1 yoffset 1
    linear 0.3 xoffset 0 yoffset 0
    repeat

# ============================================================
# 图片变换效果
# ============================================================

transform enter_below:
    yoffset 100
    alpha 0.0
    linear 0.4 yoffset 0 alpha 1.0

transform enter_left:
    xoffset -200
    alpha 0.0
    linear 0.5 xoffset 0 alpha 1.0

transform enter_right:
    xoffset 200
    alpha 0.0
    linear 0.5 xoffset 0 alpha 1.0

transform exit_shrink:
    parallel:
        linear 0.4 alpha 0.0
    parallel:
        linear 0.4 zoom 0.8

transform emphasis:
    parallel:
        linear 0.5 zoom 1.05
        linear 0.5 zoom 1.0
        repeat

transform ghost_appear:
    alpha 0.0
    blur 10
    parallel:
        linear 2.0 alpha 0.7
    parallel:
        linear 2.0 blur 3

transform dissolve_away:
    parallel:
        linear 1.5 alpha 0.0
    parallel:
        linear 1.5 blur 8

transform zoom_fade:
    zoom 0.8
    alpha 0.0
    linear 0.6 zoom 1.0 alpha 1.0

# ============================================================
# 文字效果
# ============================================================

transform typewriter:
    alpha 0.0
    linear 0.1 alpha 1.0

transform text_shout:
    linear 0.05 xoffset 2
    linear 0.05 xoffset -2
    linear 0.05 xoffset 1
    linear 0.05 xoffset -1
    linear 0.05 xoffset 0

transform text_fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0

# ============================================================
# 简单暗角覆层
# ============================================================

image dark_vignette = "#0004"
image red_vignette = "#4004"
