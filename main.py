import smtplib

from db.Database import Base, engine

Base.metadata.create_all(bind=engine)

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == "__main__":
    sender_email = "amrahovnurlan@gmail.com"
    receiver_email = "nurlan.amrahov@naic.az"
    app_password = "deyisim"  # <-- Gmail App Password (not your real password)

    # --- Create email ---
    subject = "QA Təcrübə Proqramının Nəticələri"

    html_body = """\
    <!DOCTYPE html>
    <html lang="az">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Email Template</title>
      </head>
      <body>
        <div style="width: 640px; padding: 48px; margin: auto">
          <div style="background-color: #efefef; border-bottom-left-radius: 8px; border-bottom-right-radius: 8px;">
            <div style="width: 100%">
              <img alt="Cover" style="width: 100%; height: 300px; border-top-left-radius: 8px; border-top-right-radius: 8px;"
                   src="https://api-ai-academy.ailab.az/v1/files/streams/ailab-host/ailab_cover.png" />
            </div>
            <div style="padding: 40px">
              <h3 style="color: black !important">Hörmətli Nurlan Amrahov,</h3>
              <p style="line-height: 150%; font-size: 16px; margin: 0px; color: black !important;">
                <br />
                Məmnuniyyətlə bildiririk ki, QA mühəndisliyi təcrübə proqramı üzrə müsahibə mərhələsini uğurla keçmisiniz.<br /><br />
                Proqramla bağlı növbəti mərhələlər barədə ətraflı məlumat yaxın günlərdə təqdim olunacaq.<br /><br /><br />
                Hörmətlə,<br />Milli Süni İntellekt Mərkəzi
              </p>
              <div style="margin-top: 40px">
                <a href="https://www.instagram.com/naic.azerbaijan/?hl=en" style="margin-right: 10px;">
                  <img alt="instagram" src="https://api-ai-academy.ailab.az/v1/files/streams/email/social_instagram.png" />
                </a>
                <a href="https://www.facebook.com/naic.azerbaijan/" style="margin-right: 10px;">
                  <img alt="facebook" src="https://api-ai-academy.ailab.az/v1/files/streams/email/social_fb.png" />
                </a>
                <a href="https://www.linkedin.com/company/naic-az/" style="margin-right: 10px;">
                  <img alt="linkedin" src="https://api-ai-academy.ailab.az/v1/files/streams/email/social_linkedin.png" />
                </a>
                <a href="https://www.tiktok.com/@naic.azerbaijan?_t=ZS-8zfGxdA0CxO&_r=1">
                  <img alt="tiktok" src="https://api-ai-academy.ailab.az/v1/files/streams/email/social_tiktok.png" />
                </a>
              </div>
            </div>
          </div>
        </div>
      </body>
    </html>
    """

    # --- Build MIME message ---
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Attach HTML content
    message.attach(MIMEText(html_body, "html", "utf-8"))

    # --- Send via Gmail SMTP ---
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.ehlo()
            conn.starttls()
            conn.login(sender_email, app_password)
            conn.send_message(message)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")


