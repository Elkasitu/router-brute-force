try:
    from urllib import urlencode
    import urllib2 as urllib
except:
    import urllib.request as urllib
    from urllib.parse import urlencode

from lxml import html


HEADERS = {'Accept': 'text/html',
           'Content-Type': 'application/x-www-form-urlencode'}


def get_router_data_raw(router):
    data = urlencode({'findpass': 1,
                      'router': router,
                      'findpassword': 'Find Password'}).encode('utf-8')
    r = urllib.urlopen('http://www.routerpasswords.com', data)

    return r.read()


def get_usr_password_combo(raw):
    tree = html.fromstring(raw)
    usrs = tree.xpath("//div[@id='result']/table/tbody/tr/td[4]/text()")
    pwds = tree.xpath("//div[@id='result']/table/tbody/tr/td[5]/text()")

    return list(set(zip(usrs, pwds)))


def get_router_list():
    r = urllib.urlopen('http://www.routerpasswords.com')
    tree = html.fromstring(r.read())
    routers = [router.attrib['value'] for router in tree.xpath("//option")]

    return routers


if __name__ == '__main__':
    routers = get_router_list()
    print(routers)
    raw = get_router_data_raw('Belkin')
    for pair in get_usr_password_combo(raw):
        print(pair[0], pair[1])
