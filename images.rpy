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

## 2026-09-18：原图为 1672×941，按游戏 1920×1080 等比铺满，避免留黑边。
image bg temple = Transform("images/generated/huazhou_temple.png", xysize=(1920, 1080), fit="cover")
image bg city_north = Transform("images/generated/huazhou_temple.png", xysize=(1920, 1080), fit="cover")
image bg well = Transform("images/generated/huazhou_temple.png", xysize=(1920, 1080), fit="cover")
image bg slaughterhouse = Transform("images/generated/huazhou_temple.png", xysize=(1920, 1080), fit="cover")
image bg alley = Transform("images/generated/huazhou_temple.png", xysize=(1920, 1080), fit="cover")

image bg mountain_pass = Transform("images/generated/famine_road.png", xysize=(1920, 1080), fit="cover")
image bg campfire_cave = Transform("images/generated/famine_road.png", xysize=(1920, 1080), fit="cover")
image bg burning_village = Transform("images/generated/famine_road.png", xysize=(1920, 1080), fit="cover")
image bg taiping_town = Transform("images/generated/famine_road.png", xysize=(1920, 1080), fit="cover")

image bg city_gate = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")
image bg luoyang_street = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")
image bg luoyang_inn = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")
image bg inn_room = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")
image bg yangzhou_guild = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")
image bg fu_mansion = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")
image bg mang_mountain = Transform("images/generated/luoyang_city.png", xysize=(1920, 1080), fit="cover")

image bg yangzhou_canal = Transform("images/generated/yangzhou_canal.png", xysize=(1920, 1080), fit="cover")
image bg jiangyin = Transform("gui/main_menu_v2.png", xysize=(1920, 1080), fit="cover")
image bg nanyang = Transform("images/generated/yangzhou_canal.png", xysize=(1920, 1080), fit="cover")
image bg taoist_temple = Transform("images/generated/huazhou_temple.png", xysize=(1920, 1080), fit="cover")
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
