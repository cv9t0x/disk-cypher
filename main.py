import cv2 as cv
import numpy as np

SIZE_MAP = (600, 600, 3)
CENTER = (SIZE_MAP[0] // 2, SIZE_MAP[1] // 2)
RADIUS = SIZE_MAP[0] // 2
DELTA = 360 // 45


def get_colors():
    return [
        (255, 0, 0),     # Red
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
        (255, 255, 0),   # Yellow
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Cyan
        (128, 128, 128)  # Gray
    ]


def get_alphabet():
    colors = get_colors()
    q_colors = len(colors)

    alphabet = {
        chr(i): (
            (colors[q_colors - i // q_colors - 1]),
            (colors[i % q_colors])
        ) for i in range(65, 91)
    }
    alphabet[" "] = ((255, 255, 255), (255, 255, 255))

    return alphabet


def draw_code(image_map, message, symbol_colors):
    angle = 0
    angle_message = 2 * DELTA * len(message)

    while angle < 360:
        current_color = symbol_colors.get(
            message[angle % angle_message // (2 * DELTA)], (0, 0, 0))[0]
        image_map = cv.ellipse(
            image_map, CENTER, (RADIUS, RADIUS), 0, angle, angle + DELTA, current_color, -1)
        angle += DELTA

        current_color = symbol_colors.get(
            message[(angle - 8) % angle_message // (2 * DELTA)], (0, 0, 0))[1]
        image_map = cv.ellipse(
            image_map, CENTER, (RADIUS, RADIUS), 0, angle, angle + DELTA, current_color, -1)
        angle += DELTA

    return image_map


def create_image_map():
    image_map = np.zeros(shape=SIZE_MAP, dtype='uint8')
    image_map = cv.rectangle(
        image_map, (0, 0), (SIZE_MAP[0], SIZE_MAP[1]), (220, 200, 200), -1)
    image_map = cv.circle(image_map, CENTER, RADIUS, (255, 255, 255), -1)
    return image_map


def save_and_display_image(image_map):
    cv.imwrite("cypher.png", image_map)

    cv.namedWindow("Image")
    cv.imshow("Image", image_map)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    message = "Hello World"
    symbol_colors = get_alphabet()

    print("Symbol Colors:", symbol_colors)

    image_map = create_image_map()
    image_map = draw_code(image_map, message.upper(), symbol_colors)

    save_and_display_image(image_map)


if __name__ == "__main__":
    main()
