from fastapi import Header, HTTPException

# if "allowed" token not in header throw an exception
async def get_token_header(internal_token: str = Header(...)):
    if internal_token != "allowed":
        raise HTTPException(status_code=400, detail="Internal-Token header invalid")
