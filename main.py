import cv2
import pytesseract

video_path = 'your-videos-actual-path.mp4'  # Replace with the actual path to your video file

def extract_frames(video_path, interval=30):
    """
    Extracts frames from a video file.
    
    :param video_path: Path to the video file.
    :param interval: Interval in seconds to capture frames.
    :return: A list of image frames.
    """
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

        # Capture a frame at the specified interval
        if current_frame % (fps * interval) == 0:
            frames.append(frame)

    cap.release()
    return frames

def extract_text_from_frame(frame):
    """
    Extracts text from a single image frame using Tesseract OCR.
    
    :param frame: The image frame from which to extract text.
    :return: Extracted text as a string.
    """
    # Convert frame to grayscale for better OCR accuracy
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Further image preprocessing can be added here if needed

    # Extract text using Tesseract OCR
    return pytesseract.image_to_string(gray)

def main():
    frames = extract_frames(video_path, interval=30)  # Extract frames every 30 seconds
    with open('OCR-OUTPUT.txt', 'w') as file:
        for i, frame in enumerate(frames):
            text = extract_text_from_frame(frame)
            file.write(f"Text from frame {i}:\n{text}\n\n")

if __name__ == "__main__":
    main()
