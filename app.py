import tkinter as tk
from tkinter import filedialog
    new_title = f"Labeling - Mode: {mode}, Class: {CLASS_NAMES[active_class]}"
    window_name = "Single-Window Labeling"
        "Hotkeys:",
    root = tk.Tk()
    return filedialog.askdirectory(title='Select folder with images')
import os

# -----------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------
mode = "freehand"         # "freehand" or "livewire"
poly_points = []          # freehand stroke points
anchor_points = []        # livewire anchors
livewire_path = []        # the minimal path between consecutive anchors

active_class = 0          # which class is active (0..4)
show_instructions = True  # toggles help text on/off

CLASS_NAMES = ["Septum", "IT", "MT", "Polyp", "Others", "Airway"]
CLASS_COLORS = [
    (14, 201, 255),   # class0: septum
    (36, 28, 237),    # class1: IT
    (77, 250, 117),   # class2: MT
    (232, 162, 0),    # class3: polyp
    (195, 195, 195),  # class4: others
    (190, 136, 239)   # class5: airway (auto leftover)
]

# -----------------------------------------------------------------------------
# HELPER: Update Window Title
# -----------------------------------------------------------------------------
    """
    Updates the OpenCV window title to show the current mode and class.
    """
    try:
    except:
        # If older OpenCV doesn't support setWindowTitle, just ignore
        pass

# -----------------------------------------------------------------------------
# MOUSE CALLBACK
# -----------------------------------------------------------------------------

    if mode == "freehand":
        # Freehand strokes
            poly_points.append((x, y))
            poly_points.append((x, y))
            poly_points.append((x, y))

    elif mode == "livewire":
        # Left-click => place anchor
            if len(anchor_points) == 0:
                anchor_points.append((x, y))
            else:
                last_anchor = anchor_points[-1]
                path_xy = dijkstra_path(param["cost_img"], last_anchor, (x, y))
                if len(path_xy) > 1:
                    path_xy = path_xy[1:]
                anchor_points.append((x, y))
                livewire_path.extend(path_xy)

# -----------------------------------------------------------------------------
# LIVEWIRE + FREEHAND UTILS
# -----------------------------------------------------------------------------
    cost_img = 1.0 - mag_norm  # edges => near 0 cost
    return cost_img

    h, w = cost_img.shape
    sx, sy = start
    ex, ey = end

    dist[sy, sx] = 0.0

    pq = [(0.0, (sx, sy))]
    neighbors = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]

    while pq:
        if visited[cy, cx]:
            continue
        visited[cy, cx] = True
        if (cx, cy) == (ex, ey):
            break

        for dx, dy in neighbors:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny, nx]:
                    cost_here = cost_img[ny, nx]
                    nd = cur_dist + cost_here
                    if nd < dist[ny, nx]:
                        dist[ny, nx] = nd
                        parent[ny, nx] = [cx, cy]

    # Reconstruct path
    path = []
    cx, cy = ex, ey
    while (cx != -1 and cy != -1):
        path.append((cx, cy))
        px, py = parent[cy, cx]
        if px == -1 and py == -1:
            break
        cx, cy = px, py
    path.reverse()
    return path

    """
    For freehand: build polygon "above" the stroke.
    """
    if len(points) < 2:
        return mask
    first_pt = pts[0]
    last_pt  = pts[-1]

    big_offset = 2000
    polygon_pts = pts.tolist()
    polygon_pts.append([last_pt[0], last_pt[1] - big_offset])
    polygon_pts.append([first_pt[0], first_pt[1] - big_offset])
    polygon_pts.append([first_pt[0], first_pt[1]])

    return mask

    """
    Combine anchors + path => polygon
    """
    if len(anchor_points) < 2:
        return mask

    poly_pts = anchor_points[:1] + livewire_path
    if len(poly_pts) < 3:
        return mask

    return mask

# -----------------------------------------------------------------------------
# MATLAB Overlap Logic
# -----------------------------------------------------------------------------
    BW6 = (mask5 & mask1) | (mask5 & mask2) | (mask5 & mask3) | (mask5 & mask4)
    BW7 = (mask3 & mask1) | (mask3 & mask2)
    BW8 = (mask4 & mask1) | (mask4 & mask2)
    BW9 = (mask2 & mask1)

    mask5_clean = mask5 & ~BW6
    mask4_clean = mask4 & ~BW8
    mask3_clean = mask3 & ~BW7
    mask2_clean = mask2
    mask1_clean = mask1 & ~BW9
    return mask1_clean, mask2_clean, mask3_clean, mask4_clean, mask5_clean

# -----------------------------------------------------------------------------
# SINGLE-WINDOW LABELING (returns (masks, finished_labeling, stop_now))
# -----------------------------------------------------------------------------
    """
    Single-window approach:
      - '1..5' => select class (0..4)
      - 'l' => toggle livewire mode
      - 'p' => finalize livewire polygon
      - 'u' => undo
      - 'c' => clear stroke/anchors
      - 'd' => done labeling => finalize + save
      - 'q' => quit entire program
      - 'h' => hide/show instructions
      - ESC => skip labeling
    """

    mode = "freehand"
    poly_points.clear()
    anchor_points.clear()
    livewire_path.clear()

    active_class = 0
    finished_labeling = False
    stop_now = False

    h, w = image_bgr.shape[:2]
    canvas_h = h + 2*border
    canvas_w = w + 2*border

    big_canvas[border:border+h, border:border+w] = image_bgr

    cost_img = compute_cost_image(gray_canvas)

    # 5 boolean masks for classes 0..4

    param = {"cost_img": cost_img}

    # At the start, set window title
    update_window_title(window_name, mode, active_class)

    instructions = [
        "  1..5 => select class (0..4)",
        "  l => toggle livewire mode",
        "  c => clear stroke/anchors",
        "  d => done labeling (save + finalize)",
        "  q => quit entire program",
        "  h => hide/show this help text",
        "  ESC => skip labeling this image"
    ]

    while True:
        display = big_canvas.copy()

        if show_instructions:
            y_off = 20
            for line in instructions:
                y_off += 25

        # Draw freehand stroke or livewire anchors
        if mode == "freehand":
            for i in range(len(poly_points) - 1):
        else:  # livewire
            for a in anchor_points:
            for i in range(len(livewire_path) - 1):

        # Overlay labeled masks
        overlay = display.copy()
        for cidx in range(5):
            color = CLASS_COLORS[cidx]
            region = masks[cidx]
            overlay[border:border+h, border:border+w][region] = color

        alpha = 0.4

        # Show mode + class near the bottom


        if key == 27:  
            print("Skipping labeling this image.")
            break

        elif key == ord('q'):
            stop_now = True
            print("User pressed 'q' => quit entire program.")
            break

        elif key == ord('d'):
            finished_labeling = True
            break

        elif key == ord('h'):
            show_instructions = not show_instructions
            print(f"show_instructions => {show_instructions}")

        elif key in [ord('1'), ord('2'), ord('3'), ord('4'), ord('5')]:
            cidx = key - ord('1')
            if 0 <= cidx < 5:
                active_class = cidx
                print(f"Active class => {CLASS_NAMES[active_class]}")
                update_window_title(window_name, mode, active_class)

        elif key == ord('u'):
            else:
                print("Nothing to undo.")

        elif key == ord('c'):
            poly_points.clear()
            anchor_points.clear()
            livewire_path.clear()
            print("Cleared current stroke/anchors.")

        elif key == ord('l'):
            if mode == "freehand":
                mode = "livewire"
                print("Switched to livewire mode. Press 'p' to finalize polygon.")
            else:
                mode = "freehand"
                print("Switched to freehand mode.")
            update_window_title(window_name, mode, active_class)

        elif key == ord('p'):
            if mode == "livewire" and len(anchor_points) >= 2:
                anchor_points.clear()
                livewire_path.clear()
            else:
                print("Not in livewire mode or not enough anchors to finalize.")

        elif key == ord('f'):
            if mode == "freehand" and len(poly_points) > 1:
                poly_points.clear()
            else:
                print("Either not in freehand mode or not enough points.")

    return masks, finished_labeling, stop_now

# -----------------------------------------------------------------------------
# FOLDER + PROGRESS
# -----------------------------------------------------------------------------

    if os.path.exists(progress_file):
        try:
            with open(progress_file, 'r') as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

    with open(progress_file, 'w') as f:
        f.write(str(index))

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
    folder_path = get_folder()
    if not folder_path:
        print("No folder selected. Exiting.")
        return

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]
    image_files.sort()

    progress_file = os.path.join(folder_path, 'segmentation_progress.txt')
    start_index = load_progress(progress_file)
    print(f"Starting from image index = {start_index}")

    for i in range(start_index, len(image_files)):
        img_name = image_files[i]
        img_path = os.path.join(folder_path, img_name)
        print(f"\nProcessing image {i+1}/{len(image_files)}: {img_name}")

        if image_bgr is None:
            print("Cannot read, skipping.")
            continue

        masks_0to4, finished, stop_now = label_image_one_session(image_bgr, border=100)

        if stop_now:
            print("Stopping entire labeling process now (user pressed 'q').")
            break

        if not finished:
            print("Skipping save for this image (user pressed ESC).")
            continue

        # If finished => Overlap logic + save
        mask1, mask2, mask3, mask4, mask5 = masks_0to4
        m1c, m2c, m3c, m4c, m5c = apply_matlab_overlap_logic(mask1, mask2, mask3, mask4, mask5)
        mask_airway = ~ (m1c | m2c | m3c | m4c | m5c)

        h, w = image_bgr.shape[:2]
        final_img[m1c] = CLASS_COLORS[0]
        final_img[m2c] = CLASS_COLORS[1]
        final_img[m3c] = CLASS_COLORS[2]
        final_img[m4c] = CLASS_COLORS[3]
        final_img[m5c] = CLASS_COLORS[4]
        final_img[mask_airway] = CLASS_COLORS[5]


        base, _ = os.path.splitext(img_name)
        out_path = os.path.join(folder_path, base + ".png")
        print(f"Saved: {out_path}")

        save_progress(progress_file, i+1)

    print("All done!")

if __name__ == "__main__":
    main()



if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)  # Replace with your actual class name
    root.mainloop()
