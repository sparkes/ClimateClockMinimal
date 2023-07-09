import requests

#if anyone knows how to only request the one module I'd love to know
r = requests.get('https://api.climateclock.world/v2/generic/clock.json')

if (r.status_code == 200):
    data = r.json()["data"]["modules"]["carbon_deadline_1"]["timestamp"]
    with open('Docs/deadline.txt', 'w') as f:     
        f.write(data)
    with open('Docs/deadline.xml', 'w') as f:     
        f.write("<?xml version=\"1.0\"?>\n<datetime>"+data+"</datetime>")
    with open('Docs/deadline.json', 'w') as f:     
        f.write("{\n\t\"datetime\": \"" +data + "\"\n}")
    with open('Docs/index.html', 'w') as f:     
        f.write("<html><head/><body>" +data + "</body>")
