cp=float(input())
cgst=float(input('Enter the percentage(%) of CGST Rate =>'))
sgst=float(input('Enter the percentage(%) of SGST Rate =>'))
#(CGST Tax Rate on product) + (SGST Tax Rate on product)
ta=0 
Tcgst=((cgst/100)*cp)
Tsgst=((sgst/100)*cp)
ta=cp+Tcgst+Tsgst
print('Total cost of the Product is Rs. =>',ta)