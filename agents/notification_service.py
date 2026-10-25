import requests
import os
import logging

logger = logging.getLogger("NotificationService")

class NotificationService:
    def __init__(self):
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL", "")

    def send_alert(self, message: str):
        if not self.webhook_url:
            logger.warning("Webhook URL not configured. Skipping notification.")
            return
            
        payload = {"content": f"🤖 **AI Muse Trading Elite Agent**: {message}"}
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
        except Exception as e:
            logger.error(f"Failed to send notification: {str(e)}")
