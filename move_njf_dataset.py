#!/usr/bin/env python3
"""
将 ~/lxd_shared/njf_data/toy_arm 下的 view_0~view_11 文件夹中的图片
复制到 data/multipleview/toyarm_single 的 cam_01~cam_12 文件夹中
"""

import os
import shutil
from pathlib import Path

# 源路径
source_base = Path.home() / "lxd_shared" / "njf_data" / "toy_arm"

# 目标路径
target_base = Path("data") / "multipleview" / "toyarm_single"

# 创建目标目录
target_base.mkdir(parents=True, exist_ok=True)

# 处理12个view文件夹
for view_idx in range(12):
    view_name = f"view_{view_idx}"
    cam_name = f"cam_{view_idx+1:02d}"  # cam_01, cam_02, ..., cam_12
    
    # 源文件夹路径
    source_view_dir = source_base / view_name / "rgb"
    
    # 目标文件夹路径
    target_cam_dir = target_base / cam_name
    target_cam_dir.mkdir(parents=True, exist_ok=True)
    
    # 复制10个图片文件
    for img_idx in range(10):
        source_img_name = f"00000_{img_idx:05d}.png"
        target_img_name = f"frame_{img_idx+1:05d}.png"
        
        source_img_path = source_view_dir / source_img_name
        target_img_path = target_cam_dir / target_img_name
        
        if source_img_path.exists():
            shutil.copy2(source_img_path, target_img_path)
            print(f"已复制: {source_img_path} -> {target_img_path}")
        else:
            print(f"警告: 源文件不存在: {source_img_path}")

print("所有文件复制完成！")

