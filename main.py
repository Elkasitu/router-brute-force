import urllib2

from lxml import html


HEADERS = {'Accept': 'text/html',
           'Content-Type': 'application/x-www-form-urlencode'}


def get_router_data_raw(router):
    data = "findpass=1&router=%s&findpassword=Find+Password" % router
    r = urllib2.urlopen('http://www.routerpasswords.com', data)

    return r.read()


def get_usr_password_combo(raw):
    tree = html.fromstring(raw)
    usrs = tree.xpath("//div[@id='result']/table/tbody/tr/td[4]/text()")
    pwds = tree.xpath("//div[@id='result']/table/tbody/tr/td[5]/text()")

    return list(set(zip(usrs, pwds)))


if __name__ == '__main__':
    raw = get_router_data_raw('Belkin')
    for pair in get_usr_password_combo(raw):
        print(pair[0], pair[1])
