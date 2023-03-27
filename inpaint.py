import cv2

def inpaint(frame, center_x, center_y, radius):
    """
    Inpaints a circular region centered at (center_x, center_y) with radius 'radius'
    in the given frame using OpenCV's inpainting function.

    Args:
    - frame: A numpy array representing the input frame.
    - center_x: The x-coordinate of the center of the circular region.
    - center_y: The y-coordinate of the center of the circular region.
    - radius: The radius of the circular region.

    Returns:
    - A numpy array representing the inpainted frame.
    """

    mask = create_mask(frame, center_x, center_y, radius)
    return cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)

def create_mask(frame, center_x, center_y, radius):
    """
    Creates a binary mask with a circular region centered at (center_x, center_y)
    with radius 'radius', and zeros elsewhere.

    Args:
    - frame: A numpy array representing the input frame.
    - center_x: The x-coordinate of the center of the circular region.
    - center_y: The y-coordinate of the center of the circular region.
    - radius: The radius of the circular region.

    Returns:
    - A numpy array representing the binary mask.
    """

    mask = cv2.circle(frame.copy(), (center_x, center_y), radius, (255, 255, 255), -1)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
    return mask
