
#Necessary Library
import speech_recognition as sr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# E-posta Gönderme Fonksiyonu
def send_email(subject,to_email,body):

    #Write own mail
    from_email = "your_mail@gmail.com"

    #The key you receive with the binary verification code
    verification_code = "your_verification_code"

    #Create Mail frame
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Email ingeridents (as send plain text)
    msg.attach(MIMEText(body, 'plan'))

    # Gmail connect SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start encoding
        server.login(from_email, verification_code)  # Log in using your email login details
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)  # Send EMail
        print("Have Sent Email")
    except Exception as e:
        print(f"Error of sending EMail: {e}")
    finally:
        server.quit()  # Close connection

# Send email with text from conversation
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Konuşun...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Declared environment noise
        audio = recognizer.listen(source, phrase_time_limit=10)  # Listen 10 second(you can change)

        try:
            text = recognizer.recognize_google(audio, language="tr-TR")  # You can change the language(I prefer turkish; English code is: en-EN)
            return text
        except sr.UnknownValueError:
            print("Voice did not recognization")
            return ""
        except sr.RequestError:
            print("Have not reached server")
            return ""

if __name__ == "__main__":
    text = speech_to_text()  # Convert the speech to the text
    if text:
        print(f"Speech: {text}")
        send_email("Speech Result: ", text, "your_destination@gmail.com")  # Send EMail
