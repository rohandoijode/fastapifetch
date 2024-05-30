from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Corrected GitHub raw URL
GITHUB_URL = "https://raw.githubusercontent.com/rohandoijode/fastapifetch/main/json.json"

@app.get("/nacore")
async def fetch_json():
    try:
        response = requests.get(GITHUB_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as errh:
        raise HTTPException(status_code=response.status_code, detail=str(errh))
    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail=str(err))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
