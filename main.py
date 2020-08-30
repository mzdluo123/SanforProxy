from io import BytesIO
import rsa
from config import URL, USER, VERIFY, PWD
import requests
from lxml import etree

session = requests.Session()
rsp = session.get(f"{URL}/por/login_auth.csp?apiversion=1", verify=VERIFY)
xml = etree.parse(BytesIO(rsp.content))

rsa_key = xml.xpath("/Auth/RSA_ENCRYPT_KEY/text()")[0]
rand_code = xml.xpath("/Auth/CSRF_RAND_CODE/text()")[0]

pub_key = rsa.PublicKey(int(rsa_key, 16), 65537)

encrypted_pwd = rsa.encrypt(f"{PWD}_{rand_code}".encode("utf-8"), pub_key).hex()

rsp = session.post(f"{URL}/por/login_psw.csp?anti_replay=1&encrypt=1&apiversion=1", data={
    'mitm_result': '',
    'svpn_req_randcode': rand_code,
    'svpn_name': USER,
    'svpn_password': encrypted_pwd,
    'svpn_rand_code': ''
}, verify=False)
print(rsp.text)
print(session.cookies)
