import torch


size = 1024
output_path = 'matrix.pth'


if torch.cuda.is_available():
    device = 'cuda'  # Colab T4 and other NVIDIA GPUs use CUDA.
else:
    device = 'cpu'

a = torch.randn(size, size, device=device)
b = torch.randn(size, size, device=device)
result = a @ b

# Save on the CPU so the file can also be loaded on machines without a GPU.
torch.save(result.cpu(), output_path)
print("done")
