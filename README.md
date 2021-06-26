# Thai TTS Tacotron [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/Prim9000/619d173e63ec6b6939eb7e814c98fbb9/thaitts_inference.ipynb?hl=en)

Thai TTS Tacotron is the text to speech model in Thai trained by [Tacotron2](https://github.com/NVIDIA/tacotron2).

Model from https://github.com/NVIDIA/tacotron2, the pytorch implementation of [Natural TTS Synthesis By Conditioning Wavenet On Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884) and training with [TSynC2_Nun Dataset](https://aiforthai.in.th/corpus.php).

![image](https://user-images.githubusercontent.com/65888725/123501924-8c190d80-d672-11eb-8a03-3be5e9db5bf9.png)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install thaitts.

```bash
pip install thaitts
```
## Training [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Prim9000/Thai_TTS/blob/main/Train_TTS_Github.ipynb)

Parameters tuning and recheck your training files:

![image](https://user-images.githubusercontent.com/65888725/123502176-7278c580-d674-11eb-9038-bffc2f855f56.png)

1. ```train.py --output_directory=outdir --log_directory=logdir```
2. (OPTIONAL) ```tensorboard --logdir=outdir/logdir```


## Training using pre-trained (warm-start)

Training using a pre-trained model can lead to faster convergence

By default, the dataset dependent text embedding layers are [ignored](https://github.com/Prim9000/tacotron2/blob/master/hparams.py#L22).

```bash 
python train.py --output_directory=outdir --log_directory=logdir -c tacotron2_statedict.pt --warm_start
```

## Usage

```python
import thaitts
voice = thaitts.synthesis('สวัสดี') # returns the wav file of synthesized speech
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References and Related repos
[WaveGlow](https://github.com/NVIDIA/WaveGlow) Faster than real time Flow-based Generative Network for Speech Synthesis

[nv-wavenet](https://github.com/NVIDIA/nv-wavenet/) Faster than real time WaveNet.

[Tacotron 2](https://github.com/NVIDIA/tacotron2), the official repository implementation with Pytorch.

## Medium
Coming Soon
