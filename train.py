
from sensor.pipeline.training_pipeline import start_training_pipeline

from config import file_path


print(__name__)
if __name__=="__main__":
    try:
        start_training_pipeline()
    except Exception as e:
        print(e)