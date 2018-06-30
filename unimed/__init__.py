import requests
from lxml import html
from io import StringIO, BytesIO


class Unimed(object):

    def __init__(self, card_number, password):
        '''
        Params:
            card_number:
                number of your green card
            password:
                date of birth
        '''
        self.card_number = card_number
        self.include_path = 'http://www.unimedbelem.com.br/themes/unimed'
        self.password = password

    def slips(self):
        url = 'http://www.unimedbelem.com.br/boleto'
        data = {
            'cartao1': self.card_number[:3], # 088
            'cartao2': self.card_number[:12], # 090701386200
            'cartao3': self.card_number[-1], # 6
            'include_path': self.include_path,
            'portal': 'externo',
            'senha': self.password, #'21/01/1992'
            'usuario': self.card_number,  # 0880907013862006
        }
        headers = {
            'Host': 'www.unimedbelem.com.br',
            'Referer': url
        }
        resp = requests.post(url, data=data, headers=headers)
        tree = html.fromstring(resp.content)
        table = tree.xpath(
            '//table[@class="table table-striped"]/tbody/tr[@align="center"]'
        )
        ret = []
        for tr in table:
            for td in tr[1:]:
                #print etree.tostring(td)
                print '[{}]'.format(td.text.strip())
            ret.append({
                'month': tr[1].text.strip()[:-4],
                'year': tr[1].text.strip()[4:],
                'due_date': tr[2].text.strip(),
                'monthly_payment': tr[3].text.strip(),
                'utilization': tr[4].text.strip(),
                'value': tr[5].text.strip(),
                'delay': tr[6].text.strip(),
                'status': tr[7].text.strip(),
            })
        return ret

