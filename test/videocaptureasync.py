import time
import unittest

import cv2

from smbh.py.video.capture import VideoCaptureAsync


class VideoCaptureTest(unittest.TestCase):
    def setUp(self):
        pass

    def _run(self, n_frames=500, width=1280, height=720, async=False):
        if async:
            cap = VideoCaptureAsync(0)
        else:
            cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        if async:
            cap.start()
        t0 = time.time()
        i = 0
        while i < n_frames:
            _, frame = cap.read()
            cv2.imshow('Frame', frame)
            cv2.waitKey(1) & 0xFF
            i += 1
        print('[i] Frames per second: {:.2f}, async={}'.format(n_frames / (time.time() - t0), async))
        if async:
            cap.stop()
        cv2.destroyAllWindows()

    def test_video_capture(self):
        n_frames = 500
        self._run(n_frames, 1280, 720, False)

    def test_video_capture_async(self):
        n_frames = 500
        self._run(n_frames, 1280, 720, True)


if __name__ == '__main__':
    unittest.main()
