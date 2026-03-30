# Baseline Experiment: Vehicle Detection

This experiment establishes a baseline for vehicle detection using a pre-trained YOLOv8 model.

## Configuration

- **Model:** `yolov8n.pt`
- **Dataset:** A custom subset of a vehicle dataset (e.g., COCO vehicles, or a custom dataset).
- **Epochs:** 10
- **Image Size:** 640x640

## Observations

- The model achieves a reasonable performance out-of-the-box.
- Further improvements can be made by fine-tuning on a larger, more specific dataset.
- The confusion matrix shows some misclassifications between 'car' and 'truck', which is expected.

## Next Steps

- Fine-tune the model on a larger, custom vehicle dataset.
- Experiment with data augmentation techniques.
- Try a larger model (e.g., `yolov8s.pt`) for better accuracy.
