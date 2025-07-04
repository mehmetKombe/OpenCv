import cv2
import numpy as np
import mediapipe as mp

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# Ses kontrolü için ayar
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Ses aralığı al (örneğin: -65.25 ile 0.0 dB arası)
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

mpdrawing = mp.solutions.drawing_utils
mpdrawingstyles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mphands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Error")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #eli tespit etmek için mediapipe fonksiyonlarını kullanıdğımız kod aşağıda
        if results.multi_hand_landmarks:
            for lm in results.multi_hand_landmarks:
                mpdrawing.draw_landmarks(
                    image, lm, mp.solutions.hands.HAND_CONNECTIONS,
                    mpdrawingstyles.get_default_hand_landmarks_style(),
                    mpdrawingstyles.get_default_hand_connections_style()
                )

                # El koordinatları
                landmarks = lm.landmark
                h, w, _ = image.shape
                x1, y1 = int(landmarks[4].x * w), int(landmarks[4].y * h)   # Baş parmak ucu
                x2, y2 = int(landmarks[8].x * w), int(landmarks[8].y * h)   # İşaret parmak ucu

                # Mesafe hesaplama yaptık
                distance = np.linalg.norm(np.array([x2, y2]) - np.array([x1, y1]))

                # iki parmak araqsına mavi çizgi ile ne kadar mesafesi olduğunu yazdırırız
                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(image, f"{int(distance)}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                # Sesi ayarla 200px de ses seviyesi 100 20px de ses seviyesi 0
                vol = np.interp(distance, [20, 200], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

        cv2.imshow('Result', image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC ile çık
            break

cap.release()#webcami kapatır
cv2.destroy#opencv pencerelerini kapatır
