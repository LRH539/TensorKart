# Installing and Playing tensorkart

Set up a python virtual environment. Currently the project works only with Python 2. Probably use the command `virtualenv2 <env_name>`

```bash
git clone https://github.com/emomicrowave/TensorKart`

mkdir mupen64plus-src && cd "$_"
git clone https://github.com/emomicrowave/gym-mupen64plus
git clone https://github.com/emomicrowave/mupen64plus-input-bot

cd mupen64plus-input-bot

# switch to the multiplayer branch
git branch remotes/origin/multiplayer
git checkout branch multiplayer

make all
sudo make install
```

###Manually install wxPython from 

[link...](https://wxpython.org/Phoenix/snapshot-builds/linux/gtk3/debian-8/)

- check wether you have gtk2 or gtk3
- select a package, which has *cp_27* in its name (Python 2.7)
- use `pip install --pre <link_to_package>` to install wxPython. Both versions 3.0.3 and 4.0.0 work.
- remove *wxPython* from the requirements of the packages. `gym_mupen64plus/setup.py` and 
`TensorKart/requirements.txt`

###Install pip dependencies

- do one of the following:
- tensorflow GPU requires Cuda

```bash
pip install tensorflow
pip install tensorflow-gpu
```

- install dependencies

```bash
cd TensorKart
pip install -r requirements.txt

cd ../gym_mupen64plus
pip install -e .
```

###Other dependencies

The following dependencies cannot be installed with pip. Use your package manager. For archlinux for example

```
sudo pacman -S virtualgl libjpeg6-turbo tk 
```

If you have problems with *libpng*, then try an earlier version of *wxPython*

Here also modify the `gym_mupen4plus/envs/config.yaml` and disable the `USE_XFCV` flag.

### ROM

The Marto Kart 64 is not provided with the project. Aquire it and paste it in `mupen64plus-src/gym-mupen64plus/gym_mupen64plus/ROMs/marioKart.n64`

### Specifications

Training takes a long time. A Lenovo W520 with Quadro 1000M doesn't support tensorflow's required version of CUDA, so we have to use the CPU to train. For example training two samples takes ~10 Minutes. Training with 7 samples takes ~100 Minutes

