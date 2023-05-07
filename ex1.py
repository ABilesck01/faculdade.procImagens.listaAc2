import cv2


def detectar_movimento(video_path, threshold=0.02, num_hist=20):
    cap = cv2.VideoCapture(video_path)

    last_hists = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        last_hists.append(hist)

        if len(last_hists) >= num_hist:
            diff = cv2.compareHist(hist, last_hists[-2], cv2.HISTCMP_CHISQR)

            print(diff)

            if diff > threshold:
                print("Movimento detectado!")
                return

            last_hists.pop(0)

    cap.release()
    print("Nenhum movimento detectado.")


detectar_movimento("videos/cameraEscondida.mp4")
