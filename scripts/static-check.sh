#!/usr/bin/env bash
# 2026-09-11：在没有 Ren'Py SDK 时检查关键资源、标签和跳转完整性。
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
game_dir="$(cd "$script_dir/.." && pwd)"
log_dir="$game_dir/logs"
mkdir -p "$log_dir"
report="$log_dir/static-check.log"
: > "$report"

required=(
    "gui/main_menu_v2.png"
    "images/generated/huazhou_temple.png"
    "images/generated/famine_road.png"
    "images/generated/luoyang_city.png"
    "images/generated/yangzhou_canal.png"
    "audio/ambient/deep_humidity.ogg"
    "audio/sfx/fire_crackle.ogg"
)

for asset in "${required[@]}"; do
    if [[ ! -s "$game_dir/$asset" ]]; then
        echo "缺失资源：$asset" | tee -a "$report"
        exit 1
    fi
done

duplicate_labels="$(sed -n 's/^label \([A-Za-z0-9_]*\):.*/\1/p' "$game_dir/script.rpy" | sort | uniq -d)"
if [[ -n "$duplicate_labels" ]]; then
    echo "重复标签：$duplicate_labels" | tee -a "$report"
    exit 1
fi

while read -r target; do
    if ! grep -q "^label $target:" "$game_dir/script.rpy"; then
        echo "跳转目标不存在：$target" | tee -a "$report"
        exit 1
    fi
done < <(sed -n 's/^[[:space:]]*jump \([A-Za-z0-9_]*\).*/\1/p' "$game_dir/script.rpy" | sort -u)

if grep -Eq 'show (hong|qing|bai|shen|lan|soldier|old)( |$)' "$game_dir/script.rpy"; then
    echo "仍在调用已移除的旧人物建模。" | tee -a "$report"
    exit 1
fi

echo "静态检查通过：资源、标签、跳转与旧建模引用均正常。" | tee -a "$report"
