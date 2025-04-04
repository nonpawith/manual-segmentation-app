# Manual Segmentation App

A tkinter-based GUI application for manual segmentation of endoscopy images into multiple anatomical classes. Designed for research use and supports both **freehand** and **livewire (intelligent scissors)** segmentation modes.

---

## 🖼️ Features

- Two annotation modes: Freehand and Livewire
- Supports six segmentation classes:
  - Septum
  - Inferior Turbinate (IT)
  - Middle Turbinate (MT)
  - Polyp
  - Others
  - Airway (auto leftover)
- Undo functionality
- Overlay display of segmentation masks
- Class-specific colors for easy annotation

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/manual-segmentation-app.git
cd manual-segmentation-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: `tkinter` is typically included with Python installations. If it's missing, install the `tk` package or use a standard Python distribution (e.g., Anaconda).

---

## 🏃‍♂️ Run the App

```bash
python app.py
```

---

## 📁 Project Structure

```
manual-segmentation-app/
├── app.py                  # GUI interface using tkinter
├── segmentation_core.py    # Image processing and segmentation logic
├── requirements.txt        # Python dependencies
└── README.md               # You're reading it :)
```

---

## 📸 Screenshots (Optional)

You can add GUI screenshots or usage GIFs here for better clarity.

---

## 📄 License

This project is intended for academic and research use. Include your license terms here (e.g., MIT, GPL, or custom).

---

## 🤝 Acknowledgments

If used in a publication or research, please cite or acknowledge the original authors.
