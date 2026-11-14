# Karina Batura, IT-31
import qrcode

print("Karina Batura, IT-31")

text = "Karina Batura, IT-31, karina.batura@example.com"
image = qrcode.make(text)
image.save("contact.png")
print("saved: contact.png")