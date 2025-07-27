# 🧥 Invisible Cloak using Python (Black Color)

This project creates a magical **invisible cloak effect** using **OpenCV**. When a person wears a **black-colored cloak**, it gets replaced by the background, making it appear as if the person is invisible in that region — just like the cloak in Harry Potter!

---

## 🧠 How it Works

1. **Capture the Background**: A still background is recorded before the person enters the frame.
2. **Color Detection**: The system detects black color in the frame using HSV color space.
3. **Masking & Replacement**: The detected black areas are replaced with the previously captured background.

---

## 🛠️ Tech Stack

- Python
- OpenCV (cv2)
- NumPy

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/invisible-cloak-black.git
cd invisible-cloak-black
pip install opencv-python numpy

