# Zack Oakley
# 11/27/2025
# Utility functions for building and sending earthquake alert emails.
from email.message import EmailMessage
import smtplib
import ssl
from typing import List, Dict
from src.config import (
    get_magnitude_threshold,
    get_email_user,
    get_email_password,
    get_email_to,
    get_smtp_host,
    get_smtp_port
)

# Build email body, listing all high magnitude events
def build_email_body(events: List[Dict]) -> str:
    if not events:
        return "No earthquakes over the configured magnitude threshold in the last check.\n"

    # lines will be email body as string, do some formatting
    lines: list[str] = []
    lines.append("Earthquakes over threshold\n")
    lines.append(f"{'Mag':>4}  {'Time (UTC)':<20}  {'Place'}")
    lines.append("-" * 80)

    # For each earthquake, pull out event data
    for e in events:
        mag = e.get("magnitude")
        time_utc = e.get("time_utc")
        place = e.get("place")

        try:
            mag_str = f"{mag:>4.1f}"
        except TypeError:
            mag_str = f"{mag}"

        lines.append(f"{mag_str}  {time_utc:<20}  {place}")

    lines.append("")

    # join all lines together, producing email body
    return "\n".join(lines)

# Sends an email using SMTP setting defined in .env
def send_email(subject: str, body: str):
    from_addr = get_email_user()
    password = get_email_password()
    to_addr = get_email_to()
    smtp_host = get_smtp_host()
    smtp_port = get_smtp_port()
    

    # Basic safety check so you don't silently fail due to missing env vars
    if not all([from_addr, password, to_addr, smtp_host, smtp_port]):
        raise RuntimeError(
            "SMTP configuration incomplete; check your .env variables "
            "(EMAIL_USER, EMAIL_PASS, EMAIL_TO, SMTP_SERVER, SMTP_PORT)."
        )

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)

    # Create secure connection context
    context = ssl.create_default_context()

    # Send the email over SMTP
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls(context=context)
        server.login(from_addr, password)
        server.send_message(msg)