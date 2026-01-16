from PIL import Image, ImageDraw, ImageFont
import math

def add_full_watermark(
    image_path,
    output_path,
    text,
    font_path,
    opacity=80
):
    base = Image.open(image_path).convert("RGBA")
    width, height = base.size

    # 自动字号（按图片尺寸）
    font_size = int(min(width, height) / 10)
    font = ImageFont.truetype(font_path, font_size)

    # 创建透明水印层（扩大，防止旋转后露白）
    watermark = Image.new("RGBA", (width * 2, height * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)

    # 计算文字尺寸
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # 间距
    x_step = text_w + 200
    y_step = text_h + 200

    # 平铺绘制
    for x in range(0, watermark.size[0], x_step):
        for y in range(0, watermark.size[1], y_step):
            draw.text(
                (x, y),
                text,
                font=font,
                fill=(255, 255, 255, opacity)
            )

    # 旋转水印层
    watermark = watermark.rotate(45, expand=True)

    # 裁剪到原图大小
    cx = (watermark.size[0] - width) // 2
    cy = (watermark.size[1] - height) // 2
    watermark = watermark.crop((cx, cy, cx + width, cy + height))

    # 合成
    result = Image.alpha_composite(base, watermark)
    result.convert("RGB").save(output_path)


# 需要手动修改一些参数来运行此脚本
if __name__ == "__main__":
    add_full_watermark(
        image_path="yuwei-touxiang.jpg",
        output_path="yuwei-touxiang-watermark.jpg",
        font_path="/mnt/c/Windows/Fonts/msyh.ttc",
        text="水印内容"
    )
