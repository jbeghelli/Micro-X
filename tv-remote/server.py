#!/usr/bin/env python3
"""Control remoto personalizado para Samsung UN55MU6100 (Tizen 3.0).

Uso:  python3 server.py            (TV real)
      python3 server.py --mock     (simulado, para probar la interfaz)
Luego abre http://IP_DEL_PC:8080 en el celular (misma red Wi-Fi).
"""
import json, sys, threading, time, mimetypes
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).parent
CFG = json.loads((ROOT / "config.json").read_text())
MOCK = "--mock" in sys.argv
STATIC = ROOT / "static"
lock = threading.Lock()
_tv = None


def tv():
    """Conexion perezosa y reutilizable a la TV (el token se guarda en token.txt)."""
    global _tv
    if MOCK:
        return None
    if _tv is None:
        from samsungtvws import SamsungTVWS
        _tv = SamsungTVWS(host=CFG["tv_ip"], port=8002, name=CFG["tv_name"],
                          token_file=str(ROOT / "token.txt"), timeout=5)
    return _tv


def send_key(key, repeat=1):
    for _ in range(max(1, min(int(repeat), 30))):
        if MOCK:
            print("KEY", key)
        else:
            tv().send_key(key)
        time.sleep(0.15)


def power_on():
    if MOCK:
        print("WOL"); return
    from wakeonlan import send_magic_packet
    send_magic_packet(CFG["tv_mac"])


def run_app(app_id):
    if MOCK:
        print("APP", app_id)
    else:
        tv().rest_app_run(app_id)


def run_macro(name):
    macro = next((m for m in CFG["macros"] if m["name"] == name), None)
    if not macro:
        raise ValueError("macro desconocida")
    for s in macro["steps"]:
        if "wait" in s:
            time.sleep(min(float(s["wait"]), 10))
        elif "key" in s:
            send_key(s["key"], s.get("repeat", 1))
        elif "app" in s:
            run_app(s["app"])


def reset_conn():
    global _tv
    try:
        if _tv: _tv.close()
    finally:
        _tv = None


class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def _json(self, obj, code=200):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)

    def do_GET(self):
        if self.path == "/api/config":
            return self._json({"apps": CFG["apps"],
                               "macros": [m["name"] for m in CFG["macros"]],
                               "mock": MOCK})
        rel = "index.html" if self.path in ("/", "") else self.path.lstrip("/").split("?")[0]
        f = (STATIC / rel).resolve()
        if STATIC.resolve() not in f.parents or not f.is_file():
            self.send_error(404); return
        b = f.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mimetypes.guess_type(f.name)[0] or "application/octet-stream")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers(); self.wfile.write(b)

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length", 0))
            d = json.loads(self.rfile.read(n) or b"{}")
            with lock:
                try:
                    self._dispatch(d)
                except Exception:
                    reset_conn()      # reintenta una vez con conexion nueva
                    self._dispatch(d)
            self._json({"ok": True})
        except Exception as e:
            self._json({"ok": False, "error": str(e)}, 500)

    def _dispatch(self, d):
        a = self.path
        if a == "/api/key":
            k = d["key"]
            if not (isinstance(k, str) and k.startswith("KEY_") and k.replace("_", "").isalnum()):
                raise ValueError("tecla invalida")
            send_key(k, d.get("repeat", 1))
        elif a == "/api/app":
            run_app(str(d["id"]))
        elif a == "/api/macro":
            run_macro(d["name"])
        elif a == "/api/wake":
            power_on()
        else:
            raise ValueError("ruta desconocida")


if __name__ == "__main__":
    port = CFG.get("port", 8080)
    print(f"Control remoto en http://0.0.0.0:{port}  ({'SIMULADO' if MOCK else 'TV ' + CFG['tv_ip']})")
    ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
