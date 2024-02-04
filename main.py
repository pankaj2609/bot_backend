from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import helper

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

#jis kaam ke liye backend pe ana zruri h, uske liye fulfillment ko on set kro
@app.post("/")
async def handle_request(request_from_bot: Request):
    payload = await request_from_bot.json()

    # extracting the useful info from the payload, as per the 
    # structure of webhookrequest from dialogflow

    query_text = payload['queryResult']['queryText']
    msg_intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']

    full_string = payload['queryResult']['outputContexts'][0]['name']
    session_id = helper.find_session_id(full_string)

    if (msg_intent == "nutrient_level"):
        return JSONResponse(content={
            "fulfillmentText": f"this is what backend knows: {parameters}"
        })