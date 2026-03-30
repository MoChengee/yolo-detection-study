# YOLO Detection Study

This project documents my journey of learning and experimenting with YOLO object detection, starting from basic training to more advanced fine-tuning.

## Project Structure

```
yolo-detection-study
 ├── scripts/         # Training and inference scripts
 ├── experiments/     # Markdown files documenting experiments
 ├── results/         # Output images, plots, and logs from experiments
 ├── configs/         # Dataset and model configuration files
 ├── requirements.txt # Project dependencies
 └── README.md
```

## Experiments

### [Baseline: Vehicle Detection](experiments/baseline.md)

I started with a baseline experiment to train a `yolov8n` model on a small vehicle dataset. This helped me understand the end-to-end training and evaluation process.

**Key Results:**

- **Results Plot:** Shows training metrics like loss and mAP.
  ![Results Plot](results/vehicles_baseline/results.png)

- **Confusion Matrix:** Visualizes classification performance.
  ![Confusion Matrix](results/vehicles_baseline/confusion_matrix.png)

*Note: The images above are placeholders. You should replace them with your actual experiment outputs.*

## How to Run

1.  **Setup Environment:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Training:**
    Modify the script `scripts/train.py` to point to your dataset configuration.
    ```bash
    python scripts/train.py
    ```
