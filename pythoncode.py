import base64

with open('eicar-excel-macro-cmd-echo.xls', 'rb') as f:
	text = base64.b64encode(f.read())
	print(text)
#    text = encodedZip.decode()

with open('decode.xls', 'wb') as g:
	image = base64.decodebytes(text)
	g.write(image)
