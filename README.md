# image-watermark
图片加水印脚本

## 脚本简介

`main.py` 是一个给 **图片添加水印** 的脚本。  

---

## 环境

- python 3.10.14
- pillow 12.1.0

安装依赖：
```bash
pip install pillow==12.1.0
```

需要修改的参数：
```bash
font_path = "msyh.ttc"  # 字体路径
input_path = "input"  # 输入路径
output_path = "output"  # 输出路径
text = "水印文字"  # 水印文字
```

使用方法：
```bash
python main.py
```