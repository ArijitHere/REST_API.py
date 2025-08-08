import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

class SimpleAPI(BaseHTTPRequestHandler):
    def _send(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        parts = self.path.strip("/").split("/")
        if self.path == "/users":
            self._send(200, users)
        elif len(parts) == 2 and parts[0] == "users":
            try:
                uid = int(parts[1])
                user = next((u for u in users if u["id"] == uid), None)
                if user:
                    self._send(200, user)
                else:
                    self._send(404, {"message": "User not found"})
            except ValueError:
                self._send(400, {"message": "Invalid ID"})
        else:
            self._send(404, {"message": "Not Found"})

    def do_POST(self):
        if self.path == "/users":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length))
            new_id = max([u["id"] for u in users]) + 1 if users else 1
            new_user = {"id": new_id, "name": data.get("name"), "email": data.get("email")}
            users.append(new_user)
            self._send(201, new_user)
        else:
            self._send(404, {"message": "Not Found"})

    def do_PUT(self):
        parts = self.path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "users":
            try:
                uid = int(parts[1])
                user = next((u for u in users if u["id"] == uid), None)
                if not user:
                    self._send(404, {"message": "User not found"})
                    return
                length = int(self.headers.get("Content-Length", 0))
                data = json.loads(self.rfile.read(length))
                user["name"] = data.get("name", user["name"])
                user["email"] = data.get("email", user["email"])
                self._send(200, user)
            except ValueError:
                self._send(400, {"message": "Invalid ID"})
        else:
            self._send(404, {"message": "Not Found"})

    def do_DELETE(self):
        global users
        parts = self.path.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "users":
            try:
                uid = int(parts[1])
                users = [u for u in users if u["id"] != uid]
                self._send(200, {"message": "User deleted"})
            except ValueError:
                self._send(400, {"message": "Invalid ID"})
        else:
            self._send(404, {"message": "Not Found"})

if __name__ == "__main__":
    server = HTTPServer(("localhost", 5000), SimpleAPI)
    print("Server running on http://localhost:5000")
    server.serve_forever()
