from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="Autoscaler Dashboard Demo")

# In-memory store (mock supervisor state)
servers = {
    "server1": {"workers": {"workerA": {"status": "RUNNING"}}},
    "server2": {"workers": {"workerB": {"status": "STOPPED"}}},
}


# --------------------
# HTML Dashboard
# --------------------
@app.get("/", response_class=HTMLResponse)
async def dashboard():
    rows = []
    for sid, srv in servers.items():
        workers_html = "<ul>" + "".join(
            f"<li>{wid} - {w['status']}</li>" for wid, w in srv["workers"].items()
        ) + "</ul>"
        rows.append(f"<tr><td>{sid}</td><td>{workers_html}</td></tr>")

    html = f"""
    <html>
      <head>
        <title>Autoscaler Dashboard</title>
        <style>
          body {{ font-family: sans-serif; }}
          table {{ border-collapse: collapse; width: 80%; margin: 20px auto; }}
          th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
          th {{ background: #f2f2f2; }}
          ul {{ margin: 0; padding-left: 20px; }}
        </style>
      </head>
      <body>
        <h1 style="text-align:center">Autoscaler Dashboard</h1>
        <table id="serversTable">
          <tr><th>Server</th><th>Workers</th></tr>
          {''.join(rows)}
        </table>
      </body>
    </html>
    """
    return HTMLResponse(html)


# --------------------
# Healthcheck
# --------------------
@app.get("/healthz")
async def health():
    return {"status": "ok"}


# --------------------
# Servers API
# --------------------
@app.get("/servers")
async def list_servers():
    return servers

@app.post("/servers/{server_id}")
async def create_server(server_id: str):
    if server_id in servers:
        raise HTTPException(400, f"Server {server_id} already exists")
    servers[server_id] = {"workers": {}}
    return {"message": f"Server {server_id} created"}

@app.get("/servers/{server_id}")
async def get_server(server_id: str):
    srv = servers.get(server_id)
    if not srv:
        raise HTTPException(404, f"Server {server_id} not found")
    return srv

@app.delete("/servers/{server_id}")
async def delete_server(server_id: str):
    if server_id not in servers:
        raise HTTPException(404, f"Server {server_id} not found")
    del servers[server_id]
    return {"message": f"Server {server_id} deleted"}


# --------------------
# Workers API
# --------------------
@app.post("/servers/{server_id}/workers/{worker_id}")
async def add_worker(server_id: str, worker_id: str, status: str = "STOPPED"):
    srv = servers.get(server_id)
    if not srv:
        raise HTTPException(404, f"Server {server_id} not found")
    if worker_id in srv["workers"]:
        raise HTTPException(400, f"Worker {worker_id} already exists")
    srv["workers"][worker_id] = {"status": status}
    return {"message": f"Worker {worker_id} added to {server_id} with status {status}"}

@app.patch("/servers/{server_id}/workers/{worker_id}")
async def update_worker(server_id: str, worker_id: str, status: str):
    srv = servers.get(server_id)
    if not srv or worker_id not in srv["workers"]:
        raise HTTPException(404, f"Worker {worker_id} not found")
    srv["workers"][worker_id]["status"] = status
    return {"message": f"Worker {worker_id} status updated to {status}"}

@app.delete("/servers/{server_id}/workers/{worker_id}")
async def delete_worker(server_id: str, worker_id: str):
    srv = servers.get(server_id)
    if not srv or worker_id not in srv["workers"]:
        raise HTTPException(404, f"Worker {worker_id} not found")
    del srv["workers"][worker_id]
    return {"message": f"Worker {worker_id} removed from {server_id}"}

