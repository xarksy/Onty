import re

class ExtractNMS:
    folder_zte = r'C:\Users\Sandr\Documents\hasiluncfgZTE.txt'
    folder_huawei = r'C:\Users\Sandr\Documents\hasiluncfg.txt'
    folder_alu = r'C:\Users\Sandr\Dropbox\Kerja\Rekapan\Rekap UNCFG\cleanyes.txt'
    

    def split_zte(self,inputnya):
        with open(ExtractNMS.folder_zte) as f:
            baca = f.read()
            ricek = re.search('(.*)' + inputnya,baca)
            ricek1 = re.search(inputnya + '(.*)',baca)        
            ricek2 = ricek[0] + inputnya + ricek1[0]
            ricek3 = ricek2.split()
            for hasil in ricek3:
                # if re.match(r'ALCL.{8}|ZTEG.{8}|HWTC.{8}',hasil):
                #     snont = hasil
                if re.match(r'GPON[^\s]+|MGPON[^\s]+',hasil):
                    hostname = hasil            
                elif re.match(r'F609|F625|F660|F670|F821|[^\s]+240W[^\s]+|HG824[^\s]+',hasil):                
                    tipeont = hasil
                elif re.match(r'V\d.{11}|3FE.{11}|V\d.\d.*',hasil):
                    softwareont = hasil
                elif re.match(r'1-\d.*',hasil):                
                    if len(hasil) <= 7:
                        slotport = hasil
            try:
                try:
                    try:
                        return hostname,slotport,tipeont,softwareont
                    except:
                        tipeont = 'N/A'
                        return hostname,slotport,tipeont,softwareont
                except:
                    softwareont = 'N/A'
                    return hostname,slotport,tipeont,softwareont
            except:
                softwareont = 'N/A'
                tipeont = 'N/A'
                return hostname,slotport,tipeont,softwareont
        f.close()
    
    def split_hw(self,inputnya):
        with open(ExtractNMS.folder_huawei) as hw:
            bacahw = hw.read()
            ricek1 = re.search('(.*)' + inputnya, bacahw)
            ricek2 = re.search(inputnya + '(.*)Normal', bacahw)
            ricek = ricek1[0] + inputnya + ricek2[0]
            hasilhw = ricek.split()
            hostname = hasilhw[0]
            slotport = hasilhw[1].replace('Frame:','').replace('Slot:','').replace('Port:','')
            tipeont = hasilhw[7]
            softwareont = hasilhw[8]
        
        hw.close()            
        return hostname,slotport,tipeont,softwareont

    def split_alu(self,inputnya):
        with open(ExtractNMS.folder_alu) as t:
            bacaalu = t.read()
            ricek = re.search('(.*)'+ inputnya, bacaalu)
            hasil = ricek.group(1).split()
            hostname = hasil[1]
            ip = hasil[0]
            slotport = hasil[2]
        t.close()
        return hostname,ip,slotport

    def cek_digit_sn(self,inputnya):
        # try:
        #     we = re.search('ALCL.{8}|ZTEG.{8}|HWTC.{8}', inputnya)
        #     len(we)
        #     inputnya = we.group(0)
        # except:
        #     we = re.search('ALC[^\s]+|ZTE[^\s]+|HWT[^\s]+', inputnya)
        #     inputnya = we.group(0)
        if int(len(inputnya)) == 12:
            return 'OK'
        else:
            if len(inputnya) > 12:
                kelebihan = len(inputnya) - 12
                fault_message = 'harap periksa kembali SN ONTnya lebih ' + str(kelebihan) + ' digit'
                return fault_message
            elif len(inputnya) < 12:
                kekurangan = 12 - len(inputnya)
                fault_message = 'harap periksa kembali SN ONTnya kurang ' + str(kekurangan) + ' digit'
                return fault_message
            
    def convert_hw(self,inputnya):
        if '4857544' in inputnya:
            inputnya = inputnya.replace('48575443','HWTC')

    def convert_todict(self,input_hasil):
        if len(input_hasil) == 4:
            format_hasil = ['hostname','slotport','versiont','softwareont']
            datek = {format_hasil[i]: input_hasil[i] for i in range(len(format_hasil))}
            return datek
        else:
            format_hasil = ['hostname','ip','slotport']
            datek = {format_hasil[i]: input_hasil[i] for i in range(len(format_hasil))}
            return datek

# zte = ExtractNMS()
# # print(zte.split_zte('HWTCE349CC9C'))
# # print(zte.split_hw('ZTEGCCB2024D'))
# print(zte.split_alu('ALCLFA18BE10'))
# print(zte.cek_digit_sn('ALCLFA18BE'))
# # ztez = 
# dateknya = zte.convert_todict(zte.split_alu('ALCLFA18BE10'))
# print(dateknya['ip'])
