from fastapi import FastAPI
from gradio_client import Client

app = FastAPI()

# هنا نضع الرابط الذي نسختِه سابقاً
HF_SPACE_ID = "innoai/LivePortrait" 

@app.get("/")
def home():
    return {"message": "API is Running!"}

@app.post("/animate")
def animate_face(image_url: str):
    client = Client(HF_SPACE_ID)
    # هذا السطر هو الذي يطلب من السيرفر القوي تحريك الصورة
    result = client.predict(
        input_image=image_url,
        api_name="/predict"
    )
    return {"video_url": result}
