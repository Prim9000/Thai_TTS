# Thai TTS Tacotron [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/Prim9000/619d173e63ec6b6939eb7e814c98fbb9/thaitts_inference.ipynb?hl=en)

Thai TTS Tacotron is the text to speech model in Thai trained by [Tacotron2](https://github.com/NVIDIA/tacotron2).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install thaitts.

```bash
pip install thaitts
```

## Usage

```python
import thaitts
voice = thaitts.synthesis('สวัสดี') # returns the wav file of synthesized speech
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
