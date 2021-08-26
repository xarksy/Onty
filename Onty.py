import telebot
import re
from splitingnmsresult import ExtractNMS
import listip
from datetime import datetime
import time

api = 'BOT_TOKEN'

bot = telebot.TeleBot(api)
telebot.apihelper.READ_TIMEOUT = 5

kumpulan_id = [] #specific_telegram_ID

#Folder_rekap
Rekap_Config = r'C:\Users\Sandr\Dropbox\Kerja\Rekapan\Rekap Config\Datek config '+ datetime.today().strftime('%Y-%m-%d') + '.txt'
Rekap_Uncfg = r'C:\Users\Sandr\Dropbox\Kerja\Rekapan\Rekap UNCFG\Uncfg '+ datetime.today().strftime('%Y-%m-%d') + '.txt'

@bot.message_handler(regexp=('ZTEG*|ALCL*|HWTC*|48575443*|FHTT*'))
def cek_sn(message):    
    cocokinid = message.from_user.id     
    if cocokinid in kumpulan_id:
            if re.search('ALCL.{8}|ZTEG.{8}|HWTC.{8}|48575443.{8}|FHTT.{8}', be):
                if '4857544' in be:
                    be = be.replace('48575443','HWTC')
                try:
                    we = re.search('ALCL.{8}|ZTEG.{8}|HWTC.{8}|FHTT.{8}', be)
                    len(we)
                    be = we.group(0)         
                except:
                    we = re.search(r'ALC[^\s]+|ZTE[^\s]+|HWT[^\s]+|FHTT[^\s]+', be)
                    be = we.group(0)       
                cekdigit = w.cek_digit_sn(be)
                if cekdigit == 'OK':
                    try:
                        try:
                            try:
                                dateknya = w.convert_todict(w.split_alu(be))
                                bot.reply_to(message, '{}\n{}\n{}\n{}\nOLT : Alcatel-Lucent'.format(be,dateknya['hostname'],dateknya['ip'],dateknya['slotport']))
                            except:
                                dateknya = w.convert_todict(w.split_zte(be))
                                hostname = dateknya['hostname']
                                try:
                                    ip = listip.ipnya[hostname]
                                    bot.reply_to(message, '{}\n{}\n{}\n{}:1\n Versi ONT : {}\n Software ONT : {}\n OLT : ZTE'.format(be,hostname,ip,dateknya['slotport'].replace('-','/'),dateknya['versiont'],dateknya['softwareont']))
                                except:
                                    ip = 'tidak ditemukan tunggu update selanjutnya'                        
                                    bot.reply_to(message, '{}\n{}\n{}\n{}:1\n Versi ONT : {}\n Software ONT : {}\n OLT : ZTE'.format(be,hostname,ip,dateknya['slotport'].replace('-','/'),dateknya['versiont'],dateknya['softwareont']))
                        except:
                            dateknya = w.convert_todict(w.split_hw(be))
                            hostname = dateknya['hostname']
                            try:
                                ip = listip.ipnya[hostname]
                                bot.reply_to(message, '{}\n{}\n{}\n{}\n Versi ONT : {}\n Software ONT : {}\n OLT : Huawei'.format(be,hostname,ip,dateknya['slotport'],dateknya['versiont'],dateknya['softwareont']))
                            except:
                                ip = 'tidak ditemukan tunggu update selanjutnya'  
                                bot.reply_to(message, '{}\n{}\n{}\n{}\n Versi ONT : {}\n Software ONT : {}\n OLT : Huawei'.format(be,hostname,ip,dateknya['slotport'],dateknya['versiont'],dateknya['softwareont']))
                    except:
                        bot.reply_to(message, '{} SN ONT tidak ditemukan'.format(be))
                else:
                    bot.reply_to(message, '{} {}'.format(be,cekdigit))
            else:
                pass


bot.polling()
