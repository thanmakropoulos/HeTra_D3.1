# Sound detection module

### General module installation

- Clone
```
git clone <repo url>
```
- Create virtual environment
```
python3 -m venv venv
```
- Activate
```
source venv/bin/activate
```
- Install requirements
```
pip install -r requirements.txt
```
- From this [link](https://drive.google.com/drive/folders/1m_gWfx6hXvFnywdSDqwlOqluPRPj1TPN?usp=sharing) copy "model.hdf5" into "model" folder and "labels.npy" into "features" folder

### Run
```
python3 real_time_prediction.py
```
NOTE: increase or decrease the "threshold" variable in "real_time_prediction.py" according to the microphone in use

### Output
- Recorded sounds will be saved in "audio" folder with .wav format
- A JSON file "recognition.json" will be generated in the project root directory


## Tested on
- Python 3.7.3, MacOS Catalina 10.15.6