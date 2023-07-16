from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app = FastAPI()


@app.get("/json")
async def json_response():
    # JSONレスポンスの生成
    return JSONResponse(content={"message": "This is a JSON response"})


@app.get("/html")
async def html_response():
    # HTMLレスポンスの生成
    return HTMLResponse(content="<h1>This is an HTML response</h1>")


@app.get("/custom-header")
async def custom_header_response():
    # レスポンスヘッダーの設定
    response = Response(content="This response has a custom header")
    response.headers["Custom-Header"] = "Custom Value"
    return response


@app.get("/status-code")
async def status_code_response():
    # ステータスコードの設定
    response = Response(content="Created", status_code=201)
    return response


@app.get("/redirect")
async def redirect_response():
    # リダイレクトの実行
    return RedirectResponse(url="/json")


@app.get("/error")
async def error_response():
    # エラーレスポンスの生成
    return JSONResponse(content={"error": "An error occurred"}, status_code=500)
