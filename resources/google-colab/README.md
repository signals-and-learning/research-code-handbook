# GPU Matrix Multiplication on Google Colab

Start Colab with a T4 GPU:

```sh
colab new --gpu T4 -s matrix
```

Run `matrix.py`:

```sh
colab exec -s matrix -f matrix.py
```

Download the result:

```sh
colab download -s matrix /content/matrix.pth matrix.pth
```

Stop Colab and release the GPU:

```sh
colab stop -s matrix
```

Follow the Google sign-in prompt if asked.

Install the [Colab CLI](https://github.com/googlecolab/google-colab-cli) if needed:

```sh
uv tool install --python 3.12 google-colab-cli
```
