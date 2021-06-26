# Thai TTS Tacotron [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/Prim9000/619d173e63ec6b6939eb7e814c98fbb9/thaitts_inference.ipynb?hl=en) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Thai TTS Tacotron is the text to speech model in Thai trained by [Tacotron2](https://github.com/NVIDIA/tacotron2).

Model from https://github.com/NVIDIA/tacotron2, the pytorch implementation of [Natural TTS Synthesis By Conditioning Wavenet On Mel Spectrogram Predictions](https://arxiv.org/abs/1712.05884) and training with [TSynC2_Nun Dataset](https://aiforthai.in.th/corpus.php).

![image](https://user-images.githubusercontent.com/65888725/123501924-8c190d80-d672-11eb-8a03-3be5e9db5bf9.png)


## Installation
Use the git clone to clone the tacotron project.

```bash
%tensorflow_version 1.x
import os
from os.path import exists, join, basename, splitext
git_repo_url = 'https://github.com/Prim9000/tacotron2.git'
project_name = splitext(basename(git_repo_url))[0]
if not exists(project_name):
  # clone and install
  !git clone -q --recursive {git_repo_url}
  !cd {project_name}/waveglow && git checkout 9168aea
  !pip install -q librosa unidecode
  
import sys
sys.path.append(join(project_name, 'waveglow/'))
sys.path.append(project_name)
import time
import matplotlib
import matplotlib.pylab as plt
plt.rcParams["axes.grid"] = False
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

## Synthesizing Text

```python
checkpoint_path = "checkpoint_path/checkpoint" # your model's checkpoint path
model = load_model(hparams)
model.load_state_dict(torch.load(checkpoint_path)['state_dict'])
_ = model.cuda().eval().half()

text = "สวัสดี ยินดีต้อนรับ สู่ ระบบ สังเคราะห์ เสียง" #change input text here

sequence = np.array(text_to_sequence(text, ['english_cleaners']))[None, :]
sequence = torch.autograd.Variable(
    torch.from_numpy(sequence)).cuda().long()
    
mel_outputs, mel_outputs_postnet, _, alignments = model.inference(sequence)
plot_data((mel_outputs.float().data.cpu().numpy()[0],
           mel_outputs_postnet.float().data.cpu().numpy()[0],
           alignments.float().data.cpu().numpy()[0].T))
           
with torch.no_grad():
    audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
ipd.Audio(audio[0].data.cpu().numpy(), rate=hparams.sampling_rate)
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
