#!/usr/bin/env bash
# 2026-09-11：统一从脚本启动游戏，并把终端输出保存到 logs/。
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
game_dir="$(cd "$script_dir/.." && pwd)"
project_dir="$(cd "$game_dir/.." && pwd)"
log_dir="$game_dir/logs"
mkdir -p "$log_dir"

renpy_sdk="${RENPY_SDK:-}"
if [[ -z "$renpy_sdk" ]]; then
    echo "错误：请先把 RENPY_SDK 设置为 Ren'Py SDK 目录。" | tee "$log_dir/run.log"
    exit 2
fi

runner="$renpy_sdk/lib/py3-windows-x86_64/python.exe"
if [[ ! -f "$runner" ]]; then
    runner="$renpy_sdk/renpy.sh"
fi
if [[ ! -f "$runner" ]]; then
    echo "错误：RENPY_SDK 中未找到 Ren'Py 运行器：$renpy_sdk" | tee "$log_dir/run.log"
    exit 2
fi

if [[ "$runner" == *.exe ]]; then
    "$runner" "$renpy_sdk/renpy.py" "$project_dir" run 2>&1 | tee "$log_dir/run.log"
else
    "$runner" "$project_dir" run 2>&1 | tee "$log_dir/run.log"
fi
