from PyPDF2 import PdfWriter, PdfReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(70, 700, 'Booking Id: {booking_details[0][0]}' )
can.drawString(350, 700, 'Customer Id: {login_details[0][0]}' )
can.drawString(70, 670, 'Customer Name: {login_details[0][1]}') 
can.drawString(350, 670, 'Checkin Date: {booking_details[0][3]}' )
can.drawString(70, 640, 'No of days staying: {booking_details[0][5]}')
can.drawString(350, 640, 'Checkout Date: {booking_details[0][4]}' )
can.drawString(70, 610, 'Room No: {booking_details[0][2]}')
can.drawString(350, 610, 'WiFi: {room_details[0][3]}' )
can.drawString(70, 580, 'Type: {room_details[0][2]}')
can.drawString(350, 580, 'TV: {room_details[0][4]}' )
can.drawString(70, 550, 'Price: {room_details[0][6]}')
can.drawString(350, 550,  'AC: {booking_details[0][5]}')
can.drawString(200, 15,  'Please show this at the Reception.')
can.save()

packet.seek(0)

new_pdf = PdfReader(packet)

existing_pdf = PdfReader(open('assets/rec.pdf', 'rb'))
output = PdfWriter()

page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)

output_stream = open('{booking_details[0][0]} destination.pdf', 'wb')
output.write(output_stream)
output_stream.close()