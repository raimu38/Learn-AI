import torch

print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU count:", torch.cuda.device_count())
    print("Current device name:", torch.cuda.get_device_name(0))
