"""Utility wrapper around YOLOv8 to detect dog‑poop pose and post events."""
from __future__ import annotations
from datetime import datetime
from pathlib import Path
from ultralytics import YOLO
import requests

class PoopDetector:
    def __init__(self, model_path: str, api_url: str):
        self.model = YOLO(model_path)
        self.api_url = api_url  # e.g. http://localhost:8000/api/v1/events

    def process_image(self, img: str | Path, dog_id: str):
        res = self.model(img)[0]
        for box in res.boxes:
            if int(box.cls.item()) == 0:  # class 0 = poop
                x, y = box.xywh[0][:2].tolist()
                payload = {
                    "dog_id": dog_id,
                    "timestamp": datetime.utcnow().isoformat(),
                    "x": x,
                    "y": y,
                }
                requests.post(self.api_url, json=payload, timeout=2)