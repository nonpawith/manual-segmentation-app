import cv2
import heapq
import numpy as np
drawing = False
fill_stack = []           # for multiple undo
def update_window_title(winname, mode, active_class):
    Requires OpenCV >= 4.5.2 for cv2.setWindowTitle to exist.
        cv2.setWindowTitle(winname, new_title)
def mouse_callback(event, x, y, flags, param):
    global mode, drawing, poly_points, anchor_points, livewire_path
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
        elif event == cv2.EVENT_MOUSEMOVE and drawing:
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
        if event == cv2.EVENT_LBUTTONDOWN:
def compute_cost_image(image_gray):
    gx = cv2.Sobel(image_gray, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(image_gray, cv2.CV_32F, 0, 1, ksize=3)
    mag = cv2.magnitude(gx, gy)
    mag_norm = cv2.normalize(mag, None, 0, 1, cv2.NORM_MINMAX)
def dijkstra_path(cost_img, start, end):
    dist = np.full((h, w), np.inf, dtype=np.float32)
    visited = np.zeros((h, w), dtype=bool)
    parent = -1 * np.ones((h, w, 2), dtype=int)
        cur_dist, (cx, cy) = heapq.heappop(pq)
                        heapq.heappush(pq, (nd, (nx, ny)))
def fill_left_side(canvas, points):
    mask = np.zeros(canvas.shape[:2], dtype=np.uint8)
    pts = np.array(points, dtype=np.int32)
    polygon_pts = np.array(polygon_pts, dtype=np.int32)
    cv2.fillPoly(mask, [polygon_pts], 255)
def fill_livewire_polygon(canvas, anchor_points, livewire_path):
    mask = np.zeros(canvas.shape[:2], dtype=np.uint8)
    pts_arr = np.array(poly_pts, dtype=np.int32)
    cv2.fillPoly(mask, [pts_arr], 255)
def apply_matlab_overlap_logic(mask1, mask2, mask3, mask4, mask5):
def label_image_one_session(image_bgr, border=100):
      - 'f' => fill freehand stroke
    global mode, drawing, poly_points, anchor_points, livewire_path
    global active_class, fill_stack, show_instructions
    drawing = False
    fill_stack = []
    big_canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)
    gray_canvas = cv2.cvtColor(big_canvas, cv2.COLOR_BGR2GRAY)
    masks = [np.zeros((h, w), dtype=bool) for _ in range(5)]
    cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow(window_name, 1200, 800)
    cv2.setMouseCallback(window_name, mouse_callback, param)
        "  f => fill freehand stroke",
        "  p => finalize livewire polygon fill",
        "  u => undo last fill",
                cv2.putText(display, line, (10, y_off),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200,200,200), 2, cv2.LINE_AA)
                cv2.line(display, poly_points[i], poly_points[i+1], (0,255,0), 2)
                cv2.circle(display, a, 4, (0,0,255), -1)
                cv2.line(display, livewire_path[i], livewire_path[i+1], (0,255,0), 2)
        display = cv2.addWeighted(overlay, alpha, display, 1 - alpha, 0)
        cv2.putText(display, f"Mode: {mode}, Class: {CLASS_NAMES[active_class]}",
                    (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2, cv2.LINE_AA)
        cv2.imshow(window_name, display)
        key = cv2.waitKey(1) & 0xFF
            if fill_stack:
                last_class, last_fill = fill_stack.pop()
                masks[last_class] &= (~last_fill)
                print(f"Undo fill from class {CLASS_NAMES[last_class]}")
                fill_mask_full = fill_livewire_polygon(big_canvas, anchor_points, livewire_path)
                fill_cropped = fill_mask_full[border:border+h, border:border+w]
                fill_bool = (fill_cropped > 0)
                masks[active_class] |= fill_bool
                fill_stack.append((active_class, fill_bool))
                print("Livewire polygon filled.")
                fill_mask_full = fill_left_side(big_canvas, poly_points)
                fill_cropped = fill_mask_full[border:border+h, border:border+w]
                fill_bool = (fill_cropped > 0)
                masks[active_class] |= fill_bool
                fill_stack.append((active_class, fill_bool))
                print("Freehand fill done.")
    cv2.destroyWindow(window_name)
def get_folder():
    root.withdraw()
def load_progress(progress_file):
def save_progress(progress_file, index):
def main():
        image_bgr = cv2.imread(img_path)
        final_img = np.zeros((h, w, 3), dtype=np.uint8)
        cv2.imshow("Final Segmentation", final_img)
        cv2.waitKey(1000)
        cv2.destroyWindow("Final Segmentation")
        cv2.imwrite(out_path, final_img)