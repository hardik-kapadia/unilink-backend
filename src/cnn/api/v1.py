from fastapi import APIRouter, Depends, File, Form, UploadFile
from src.cnn.sentiment import SentimentAnalyser
from src.cnn.utils import CCNNWrapper
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pprint import pprint
from tensorflow import keras
import cv2
import numpy as np

ccnn_router = APIRouter(prefix="/cnn")
wrapper = CCNNWrapper()
# se = SentimentAnalyser()


@ccnn_router.get("/")
def hello_there():
    res = wrapper.hello_there()
    return res


# @ccnn_router.post("/upload")
# async def file_upload(
#     my_file: UploadFile = File(...), text: str = "", followers: int = 0
# ):
#     print("inside upload")
#     path = "src/cnn/fmod.h5"
#     model = keras.models.load_model(path)

#     print(model)
#     # print(type(my_file))

#     # [print(i.shape, i.dtype) for i in model.inputs]
#     # [print(o.shape, o.dtype) for o in model.outputs]
#     # [print(l.name, l.input_shape, l.dtype) for l in model.layers]

#     contents = await my_file.read()
#     nparr = np.fromstring(contents, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     img2 = cv2.resize(img, (256, 256))

#     print(type(img2))

#     img_temp_2 = img2.reshape(-1, 256, 256, 3)

#     scored_text = se.get_score(text)
#     print(scored_text)
#     yep = np.array(scored_text["compound"]).reshape(1)

#     output = model([yep, img_temp_2]).numpy()
#     print(output)
#     op = output.flatten()
#     print(op)
#     likes = op[0] * followers
#     comments = op[1] * followers
#     # pred = model.predict([my_file, text])
#     # print(pred)
#     return {
#         "name": my_file.filename,
#         "text": text,
#         "followers": followers,
#         "likes": likes,
#         "commments": comments,
#     }
