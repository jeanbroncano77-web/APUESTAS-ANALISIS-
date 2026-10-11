# -*- coding: utf-8 -*-
"""
app.py
Servidor Web Dinámico en Tiempo Real para SportsAI Pronósticos Deportivos
Compatible al 100% con Render.com (Linux Gunicorn) y ejecución local.
"""

import os
import sys
import json
import threading
import subprocess
from datetime import datetime, timezone, timedelta

from flask import Flask, jsonify, send_file, request, Response

# Configurar encoding UTF-8
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = os.path.dirname(os.path.abspath(__file__))
agents_dir = os.path.join(base_dir, "sports_agents")

app = Flask(__name__)


def get_lima_time():
    utc_now = datetime.now(timezone.utc)
    return utc_now - timedelta(hours=5)


@app.route("/", methods=["GET"])
def serve_dashboard():
    """Sirve el dashboard interactivo principal index.html"""
    index_file = os.path.join(base_dir, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read()
        return Response(content, mimetype="text/html")
    return Response("<h2>Dashboard no encontrado</h2>", status=404, mimetype="text/html")


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint para Render"""
    return jsonify({
        "status": "healthy",
        "service": "SportsAI Dynamic Engine",
        "lima_time": get_lima_time().strftime("%Y-%m-%d %H:%M:%S"),
        "version": "4.5.0"
    })


@app.route("/api/matches", methods=["GET"])
def get_matches():
    """Retorna los 6 partidos estelares con sus simulaciones y La Fija"""
    sim_file = os.path.join(agents_dir, "simulations_tomorrow_results.json")
    if os.path.exists(sim_file):
        try:
            with open(sim_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Simulaciones no encontradas"}), 404


@app.route("/api/audit", methods=["GET"])
def get_audit():
    """Retorna el historial completo de auditoría (Win Rate, Banca, PnL)"""
    audit_file = os.path.join(agents_dir, "audit_history.json")
    if os.path.exists(audit_file):
        try:
            with open(audit_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Auditoría no encontrada"}), 404


@app.route("/api/learning", methods=["GET"])
def get_learning_log():
    """Retorna la bitácora de autoaprendizaje continuo (Área 3)"""
    log_file = os.path.join(agents_dir, "autonomous_feedback_log.json")
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Bitácora no encontrada"}), 404


def run_pipeline_task():
    """Ejecuta el ciclo de auditoría y predicciones en la nube"""
    py_exe = sys.executable
    script_path = os.path.join(agents_dir, "run_daily_cloud.py")
    subprocess.run([py_exe, script_path], cwd=base_dir, check=False)


@app.route("/api/update", methods=["POST"])
def trigger_update():
    """Dispara la actualización y auditoría automática en segundo plano"""
    t = threading.Thread(target=run_pipeline_task, daemon=True)
    t.start()
    return jsonify({
        "status": "in_progress",
        "message": "Ciclo de auto-auditoría y pronósticos iniciado en segundo plano",
        "timestamp": get_lima_time().strftime("%Y-%m-%d %H:%M:%S")
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
