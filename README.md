# Manual Segmentation App

A tkinter-based GUI application for manual segmentation of anterior nasal endoscopy images into multiple anatomical classes. Designed for research use and supports both **freehand** and **livewire (intelligent scissors)** segmentation modes.

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
git clone https://github.com/nonpawith/manual-segmentation-app.git
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

## 🪜 Step-by-Step Usage

1. **Launch the App**
   - Run `python app.py` to open the tkinter interface.

2. **Load an Image**
   - Use the file dialog to select an image (e.g., an endoscopic frame in `.jpg` or `.png` format).

3. **Choose a Segmentation Mode**
   - Click to toggle between:
     - **Freehand**: Draw directly over the image with mouse drag.
     - **Livewire**: Place anchor points and let the app compute the optimal path along edges.

4. **Select a Class**
   - Choose one of the six segmentation classes:
     - Septum
     - Inferior Turbinate (IT)
     - Middle Turbinate (MT)
     - Polyp
     - Others
     - Airway (auto leftover class)

5. **Start Annotating**
   - In **Freehand** mode: click and drag to draw the contour.
   - In **Livewire** mode: click to place anchors. The algorithm will trace a path between points based on edge strength.

6. **Undo / Redraw**
   - Press the **Undo** button to remove the last stroke or segment.

7. **Save or Export**
   - (Optional) Save the final mask or annotation results (depending on implementation).

> ⚠️ Note: Class overlays are color-coded for clarity, and multiple regions can be drawn per class.

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

## 📄 Additional note

This project is intended for academic and research use.

I am always open to code review. Please put in a push request if you spot any errors or see more efficient ways of presenting the code.

If you have further questions, please do not hesitate to contact me at nonpawith.phoommanee@ucl.ac.uk.

---

## 🤝 Acknowledgments


If you use this tool in your research or publication, please cite the repository as:

> Nonpawith Phoommanee. *Manual Segmentation App*. GitHub repository, https://github.com/nonpawith/manual-segmentation-app, 2025.

BibTeX:
```bibtex
@misc{NonpawithSegmentationApp,
  author = {Nonpawith Phoommanee},
  title = {Manual Segmentation App},
  year = {2025},
  howpublished = {\url{https://github.com/nonpawith/manual-segmentation-app}},
  note = {Accessed: YYYY-MM-DD}
}
