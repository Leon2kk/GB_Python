def showToScreen(data):
   data = [i.replace('|', '').rstrip('\n') for i in data]
   print()
   for i in range(len(data)):
        print(f"{i+1}) {data[i]}")

def saveToTXT(data):
    data = [i.replace('|', '') for i in data]
    with open('dz7/export.txt', 'w+', encoding='UTF-8') as txt:
        for i in range(len(data)):
            txt.write(f"{i+1}) {data[i]}")

def saveToHTML(data):
    data = [i.replace('|', '').rstrip('\n') for i in data]
    html = '<html>\n  <head></head>\n  <body style="font-size:14px;">\n'
    for i in range(len(data)):
        html += '  <p>{}) {}</p>\n'.format(i+1, data[i])
    html += ' </body>\n</html>'    
    with open('dz7/export.html', 'w', encoding='UTF-8') as page:
        page.write(html)

def saveToXML(data):
    data = [i.replace('|', '').rstrip('\n') for i in data]
    xml = '<xml>\n'
    for i in range(len(data)):
        xml += '<telephone>{}) {}</telephone>\n'.format(i+1, data[i])
    xml += '</xml>'
    with open('dz7/export.xml', 'w', encoding='UTF-8') as page:
        page.write(xml)


