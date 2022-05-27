import eel
import pathlib
  

MODELS_PATH = rf"{pathlib.Path(__file__).parent}\templates"

eel.init(MODELS_PATH)

@eel.expose
def add(data_1, data_2):  
    print(f"Login: {data_1}")
    print(f"Pass: {data_2}")

# Start the index.html file
eel.start("index.html", cmdline_args=['--viewPort="maximized"'])