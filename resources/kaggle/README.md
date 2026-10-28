# GPU Matrix Multiplication on Kaggle

Install the [Kaggle CLI](https://github.com/Kaggle/kaggle-cli) if needed and sign in:

```sh
uv tool install --python 3.12 kaggle
kaggle auth login
```

Run the following commands from this folder (`resources/kaggle`). Replace
`YOUR_USERNAME` in `kernel-metadata.json` and the commands below with your Kaggle
username. The metadata creates a private Python script with GPU enabled.

Upload and run `matrix.py` with a T4 GPU:

```sh
kaggle kernels push -p . --accelerator NvidiaTeslaT4
```

Check the run status:

```sh
kaggle kernels status gpu-matrix-multiplication
```

Repeat the status command until the run is complete. The script saves the result
to `/kaggle/working/matrix.pth`, which Kaggle keeps as an output file.

Download the result to this folder, replacing any previous local `matrix.pth`:

```sh
kaggle kernels output gpu-matrix-multiplication -p . --force --file-pattern 'matrix\.pth$'
```

The batch job ends when the script finishes. To run it again after editing
`matrix.py`, repeat the push command.

See the official [CLI setup](https://github.com/Kaggle/kaggle-cli/blob/main/docs/README.md),
[kernel commands](https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels.md),
and [metadata format](https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels_metadata.md).
