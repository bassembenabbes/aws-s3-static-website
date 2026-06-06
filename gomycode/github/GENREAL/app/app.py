import os
from datetime import datetime, timezone

from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest


def create_app():
    app = Flask(__name__)
    requests_total = Counter("app_requests_total", "Total HTTP requests", ["path"])

    @app.get("/")
    def index():
        requests_total.labels(path="/").inc()
        return jsonify(
            {
                "service": os.getenv("APP_NAME", "devops-starter-app"),
                "message": "Hello from the DevOps starter lab",
                "time": datetime.now(timezone.utc).isoformat(),
            }
        )

    @app.get("/health")
    def health():
        requests_total.labels(path="/health").inc()
        return jsonify({"status": "ok"})

    @app.get("/metrics")
    def metrics():
        requests_total.labels(path="/metrics").inc()
        return generate_latest(), 200, {"Content-Type": "text/plain; version=0.0.4"}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
