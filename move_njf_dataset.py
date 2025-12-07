#!/usr/bin/env python3
"""
将 ~/lxd_shared/njf_data/toy_arm 下的 view_0~view_11 文件夹中的图片
复制到 data/multipleview/toyarm_single 的 cam_01~cam_12 文件夹中
"""

import os
import shutil
from pathlib import Path
from PIL import Image

# 源路径
source_base = Path.home() / "lxd_shared" / "njf_data" / "toy_arm"

# 目标路径
target_base = Path("data") / "multipleview" / "toyarm_single"

# 创建目标目录
target_base.mkdir(parents=True, exist_ok=True)

# 处理12个view文件夹
for view_idx in range(12):
    view_name = f"view_{view_idx}"
    cam_name = f"cam{view_idx+1:02d}"  # cam_01, cam_02, ..., cam_12
    
    # 源文件夹路径
    source_view_dir = source_base / view_name / "rgb"
    
    # 目标文件夹路径
    target_cam_dir = target_base / cam_name
    target_cam_dir.mkdir(parents=True, exist_ok=True)
    
    # 复制10个图片文件并转换为JPG格式
    for img_idx in range(10):
        source_img_name = f"00000_{img_idx:05d}.png"
        target_img_name = f"frame_{img_idx+1:05d}.jpg"
        
        source_img_path = source_view_dir / source_img_name
        target_img_path = target_cam_dir / target_img_name
        
        if source_img_path.exists():
            # 打开PNG图片并转换为JPG
            img = Image.open(source_img_path)
            # 如果图片有透明通道，转换为RGB模式
            if img.mode in ('RGBA', 'LA', 'P'):
                # 创建白色背景
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = rgb_img
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            # 保存为JPG格式，质量设置为95
            img.save(target_img_path, 'JPEG', quality=95)
            print(f"已转换: {source_img_path} -> {target_img_path}")
        else:
            print(f"警告: 源文件不存在: {source_img_path}")

print("所有文件复制完成！")

