from PIL import Image, ImageDraw

def main():
    image = Image.open("matrix.jpg")
    print(image.size)
    print(image.format)
    print(image.mode)

    width = image.size[0] // 2
    heigth = image.size[1] // 2

    new_size = (width, heigth)

    new_image = image.resize(new_size)
    draw = ImageDraw.Draw(new_image)
    draw.text(
        xy=(10, 10),
        text="Hola Python",
        fill=(255, 255, 255)
    )
    new_image.save('matrix_resized.jpg', 'JPEG', quality=90)


if __name__ == "__main__":
    main()