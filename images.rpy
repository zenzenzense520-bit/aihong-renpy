## 哀鸿 - 统一视觉资源定义
## 2026-09-11：移除旧建模素材，改用统一生成的章节背景。

transform pos_left:
    xalign 0.18
    yalign 1.0

transform pos_center:
    xalign 0.5
    yalign 1.0

transform pos_right:
    xalign 0.82
    yalign 1.0

## 四张主背景覆盖全篇，避免同一章节内画风跳变。
image bg temple = "images/generated/huazhou_temple.png"
image bg city_north = "images/generated/huazhou_temple.png"
image bg well = "images/generated/huazhou_temple.png"
image bg slaughterhouse = "images/generated/huazhou_temple.png"
image bg alley = "images/generated/huazhou_temple.png"

image bg mountain_pass = "images/generated/famine_road.png"
image bg campfire_cave = "images/generated/famine_road.png"
image bg burning_village = "images/generated/famine_road.png"
image bg taiping_town = "images/generated/famine_road.png"

image bg city_gate = "images/generated/luoyang_city.png"
image bg luoyang_street = "images/generated/luoyang_city.png"
image bg luoyang_inn = "images/generated/luoyang_city.png"
image bg inn_room = "images/generated/luoyang_city.png"
image bg yangzhou_guild = "images/generated/luoyang_city.png"
image bg fu_mansion = "images/generated/luoyang_city.png"
image bg mang_mountain = "images/generated/luoyang_city.png"

image bg yangzhou_canal = "images/generated/yangzhou_canal.png"
image bg jiangyin = "gui/main_menu_v2.png"
image bg nanyang = "images/generated/yangzhou_canal.png"
image bg taoist_temple = "images/generated/huazhou_temple.png"
image bg black = "#000000"

define fade_black = Fade(0.5, 0.3, 0.5, color="#000")
define flash_white = Fade(0.1, 0.1, 0.3, color="#fff")
define flash_red = Fade(0.15, 0.05, 0.3, color="#600")
define slow_fade = Fade(1.0, 0.35, 1.0)
define quick_fade = Fade(0.2, 0.1, 0.2)
define nightmare = Dissolve(0.8)
define memory_flash = Fade(0.15, 0.05, 0.5, color="#fff")

image snow_particle = "#fff8"
image falling_snow = SnowBlossom(
    "snow_particle",
    count=35,
    xspeed=(5, 12),
    yspeed=(18, 35),
    start=10,
    fast=False,
    horizontal=False,
)

image ash_particle = "#8884"
image falling_ash = SnowBlossom(
    "ash_particle",
    count=20,
    border=10,
    xspeed=(3, 8),
    yspeed=(10, 20),
    start=5,
    fast=False,
    horizontal=False,
)
