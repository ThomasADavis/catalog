#!/usr/bin/env python

#import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
#import elasticsearch
import time
import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import pika
import json

host = "es5-client-pool.service.consul"
port = "9200"

esdb = Elasticsearch([{
        'host': host,
        'port': port, }])

i = dict()
result = dict()
sum = 0
count = 0

i['crt-ion-db'] = {'meter:LBL_ION_07.59_MVSG_A701|data.name:Active Power Mean':'data.datum|1000|A1|LBL_ION_07.59_MVSG_A701',
                   'meter:LBL_ION_07.59_MVSG_A702|data.name:Active Power Mean':'data.datum|1000|A2|LBL_ION_07.59_MVSG_A702',
                   'meter:LBL_ION_07.59_MVSG_A704|data.name:Active Power Mean':'data.datum|1000|B1|LBL_ION_07.59_MVSG_A704',
                   'meter:LBL_ION_07.59_MVSG_A727|data.name:Active Power Mean':'data.datum|1000|B2|LBL_ION_07.59_MVSG_A727',
                   'meter:LBL_ION_07.59_590A|data.name:Active Power Mean':'data.datum|1000|Bp|LBL_ION_07.59_590A',
                   'meter:LBL_ION_07.59_MVSG_A705|data.name:Active Power Mean':'data.datum|1000|C1|LBL_ION_07.59_MVSG_A705',
                   'meter:LBL_ION_07.59_MVSG_A726|data.name:Active Power Mean':'data.datum|1000|C2|LBL_ION_07.59_MVSG_A726',
                   'meter:LBL_ION_07.59_596A|data.name:Active Power Mean':'data.datum|1000|Cp|LBL_ION_07.59_596A',
                   'meter:LBL_ION_07.59_MVSG_A706|data.name:Active Power Mean':'data.datum|1000|D1|LBL_ION_07.59_MVSG_A706',
                   'meter:LBL_ION_07.59_MVSG_A725|data.name:Active Power Mean':'data.datum|1000|D2|LBL_ION_07.59_MVSG_A725',
                   'meter:LBL_ION_07.59_612A|data.name:Active Power Mean':'data.datum|1000|Dp|LBL_ION_07.59_612A',
                   'meter:LBL_ION_07.59_MVSG_A707|data.name:Active Power Mean':'data.datum|1000|E1|LBL_ION_07.59_MVSG_A707',
                   'meter:LBL_ION_07.59_MVSG_A724|data.name:Active Power Mean':'data.datum|1000|E2|LBL_ION_07.59_MVSG_A724',
                   'meter:LBL_ION_07.59_613A|data.name:Active Power Mean':'data.datum|1000|Ep|LBL_ION_07.59_613A',
                   'meter:LBL_ION_07.59_MVSG_A709|data.name:Active Power Mean':'data.datum|1000|F1|LBL_ION_07.59_MVSG_A709',
                   'meter:LBL_ION_07.59_MVSG_A722|data.name:Active Power Mean':'data.datum|1000|F2|LBL_ION_07.59_MVSG_A722',
                   'meter:LBL_ION_07.59_628A|data.name:Active Power Mean':'data.datum|1000|Fp|LBL_ION_07.59_628A'}
i['edison-modbus'] = {'data.host:pdu10-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-1|pdu10-fpc',
                      'data.host:pdu11-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-9|pdu11-fpc'}
i['cori-modbus'] = {'data.host:pdu12-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-2|pdu12-fpc',
                    'data.host:pdu13-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-10|pdu13-fpc'}
i['ups-modbus'] = {'data.host:b59-ups1|data.meter:UPS|data.modbus_point:Output Power':'data.datum|1|ND1-1|b59-ups1',
                   'data.host:b59-ups2|data.meter:UPS|data.modbus_point:Output Power':'data.datum|1|ND1-2|b59-ups2'}
i['crt-modbus'] = {'data.host:pdu21-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-3|pdu21-fpc',
                   'data.host:pdu22-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-15|pdu22-fpc',
                   'data.host:pdu23-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-4|pdu23-fpc',
                   'data.host:pdu24-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-16|pdu24-fpc',
                   'data.host:pdu25-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-5|pdu25-fpc',
                   'data.host:pdu26-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-11|pdu26-fpc',
                   'data.host:pdu28-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-12|pdu28-fpc',
                   'data.host:pdu30-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-13|pdu30-fpc',
                   'data.host:pdu32-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-17|pdu32-fpc',
                   'data.host:pdu33-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-6|pdu33-fpc',
                   'data.host:pdu34-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-14|pdu34-fpc',
                   'data.host:pdu35-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-7|pdu35-fpc',
                   'data.host:pdu36-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-18|pdu36-fpc',
                   'data.host:pdu37-fpc|data.meter:output power|data.modbus_point:Real Power':'data.datum|1000|ND2-8|pdu37-fpc',
                   'data.host:p590a19a-pqube|data.meter:p590a19a-pqube|data.modbus_point:Real Power':'data.datum|1|ND1-3|p590a19a-pqube',
                   'data.host:p590a20a-pqube|data.meter:p590a20a-pqube|data.modbus_point:Real Power':'data.datum|1|ND1-4|p590a20a-pqube',
                   'data.host:p590a21a-pqube|data.meter:p590a21a-pqube|data.modbus_point:Real Power':'data.datum|1|ND1-5|p590a21a-pqube',
                   'data.host:p590a22a-pqube|data.meter:p590a22a-pqube|data.modbus_point:Real Power':'data.datum|1|ND1-6|p590a22a-pqube',
                   'data.host:dent-590a6a|data.meter:p590a6a-main|data.modbus_point:Real Power A':'data.datum|1000|N5|dent-590a6a',
                   'data.host:dent-590a6a|data.meter:p590a6a-main|data.modbus_point:Real Power B':'data.datum|1000|N5|dent-590a6a',
                   'data.host:dent-590a6a|data.meter:p590a6a-main|data.modbus_point:Real Power C':'data.datum|1000|N5|dent-590a6a',
                   'data.host:ats-gw-2-503|data.meter:e590-a7a-ats|data.modbus_point:Real Power Total':'data.datum|1|N6|ats-gw-2-503',
                   'data.host:dent-ue600a|data.meter:ue600a-main|data.modbus_point:Real Power A':'data.datum|1000|N7p|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a-main|data.modbus_point:Real Power B':'data.datum|1000|N7p|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a-main|data.modbus_point:Real Power C':'data.datum|1000|N7p|dent-ue600a',
                   'data.host:dent-e596a1a1a|data.meter:p596a1a1a|data.modbus_point:Real Power A':'data.datum|1000|N10p|dent-e596a1a1a',
                   'data.host:dent-e596a1a1a|data.meter:p596a1a1a|data.modbus_point:Real Power B':'data.datum|1000|N10p|dent-e596a1a1a',
                   'data.host:dent-e596a1a1a|data.meter:p596a1a1a|data.modbus_point:Real Power C':'data.datum|1000|N10p|dent-e596a1a1a',
                   'data.host:dent-e596a1a39a|data.meter:p596a1a39a|data.modbus_point:Real Power A':'data.datum|1000|N10|dent-e596a1a39a',
                   'data.host:dent-e596a1a39a|data.meter:p596a1a39a|data.modbus_point:Real Power B':'data.datum|1000|N10|dent-e596a1a39a',
                   'data.host:dent-e596a1a39a|data.meter:p596a1a39a|data.modbus_point:Real Power C':'data.datum|1000|N10|dent-e596a1a39a',
                   'data.host:dent-e596a1a2a|data.meter:p596a1a2a|data.modbus_point:Real Power A':'data.datum|1000|N11pp|dent-e596a1a2a',
                   'data.host:dent-e596a1a2a|data.meter:p596a1a2a|data.modbus_point:Real Power B':'data.datum|1000|N11pp|dent-e596a1a2a',
                   'data.host:dent-e596a1a2a|data.meter:p596a1a2a|data.modbus_point:Real Power C':'data.datum|1000|N11pp|dent-e596a1a2a',
                   'data.host:dent-ue600a|data.meter:ue600a5a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a8a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a13a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a29a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a30a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a37a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a38a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a39a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a',
                   'data.host:dent-ue600a|data.meter:ue600a40a|data.modbus_point:Real Power':'data.datum|1000|N7pp|dent-ue600a'}

def calc(result):
   #xx = datetime.datetime.utcnow()
   #print 'x: ', xx
   #result['level1']['start'] = datetime.datetime.now().strftime("%B %d %Y, %X")
   #result['level1']['start'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

   pue = dict()
   # Constants

   #pue['N1'] = 1000 / 1000
   #pue['N2'] = 1000 / 1000
   #pue['N3'] = 710 / 1000
   #pue['N4'] = 1700 / 1000
   ##pue['N6'] = 0
   #pue['N8'] = 500 / 1000
   #pue['N9'] = 1600 / 1000

   pue['N1'] = 1000
   pue['N2'] = 1000
   pue['N3'] = 710
   pue['N4'] = 1700
   ##pue['N6'] = 0
   pue['N8'] = 500
   pue['N9'] = 1600

   result['level1']['start'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
   result['level2']['start'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
   for x in i:
      indx = x + '*'
      ##print 'index', indx 
      for eskey in i[x]:
         ##timespan = i[x][eskey]
         ##print 'key', eskey 
         ##print 'value', i[x][eskey]
         (valueField, scale, variable, source) = i[x][eskey].split('|')
         if variable not in pue:
            pue[variable] = 0
            #print("clears pue")
         k = eskey.split('|')
         s = Search(using=esdb, index=indx)
         for j in k:
            (subkey, subvalue) = j.split(':')
            s = s.query("term", **{subkey: subvalue})
            ##print 'subkey', subkey
            ##print 'subvalue', subvalue
         ##s = s.query('range', **{'@timestamp':{'gte': '2018-07-01T00:00:00.000Z', 'lt':'2018-08-01T00:00:00.000Z'}})
         s = s.query('range', **{'@timestamp':{'gte': 'now-30m', 'lt':'now'}})
         s = s.sort('-@timestamp')
         #s = s.aggs.metric('power_sum', 'sum', field=valueField)
         s = s[0:1]

         #print s.to_dict() 
         response = s.execute() 

         #print 'Total %d hits found.' % response.hits.total 
         if response.hits.total != 0:
            for commit in response:
         #      print commit.to_dict()
               pue[variable] += commit['data']['datum'] * float(scale)
         #      ##print commit.to_dict()
         #      for n in k:
         #         (sk, sv) = n.split(':')
         #         if sk.find('.') != -1:
         #            (psk, ssk) = sk.split('.')
         #            ##print 'key: ', psk 
         #            ##print 'ha', commit[psk][ssk] 
         #         ##else:
         #            ##print 'key: ', sk 
         #            ##print 'value: ', sv 
         #            ##print 'ha', commit[sk] 
         #      v = response.aggregations.power_sum
         #      pue[variable] += ( v['value'] / response.hits.total )
         #      print("Processing %s" % variable)
         else:
            ##print s.to_dict() 
            if result['level1'].has_key('missing') is False:
               result['level1']['missing'] = [variable]
               result['level2']['missing'] = [variable]
            else:
               result['level1']['missing'].append(variable)
               result['level2']['missing'].append(variable)

            if result['level2'].has_key('missing-meters') is False:
               result['level1']['missing-meters'] = [source]
               result['level2']['missing-meters'] = [source]
            else:
               result['level1']['missing-meters'].append(source)
               result['level2']['missing-meters'].append(source)
            #print 'No Value for: ', variable, ' ', source

   pue['N7'] = pue['N7p'] - pue['N7pp']
   pue['N10pp'] = pue['N10p'] - pue['N10']
   pue['D'] = pue['D1'] + pue['D2']
   pue['E'] = pue['E1'] + pue['E2']
   pue['F'] = pue['F1'] + pue['F2']
   if (pue['B1'] + pue['B2'] + pue['C1'] + pue['C2'] + pue['D1'] + pue['D2'] + pue['E1'] + pue['E2'] + pue['F1'] + pue['F2']) == 0:
      lineLoss = 0
   else:
      lineLoss = (pue['A1'] + pue['A2']) / (pue['B1'] + pue['B2'] + pue['C1'] + pue['C2'] + pue['D1'] + pue['D2'] + pue['E1'] + pue['E2'] + pue['F1'] + pue['F2'])
   if pue['Bp'] == 0:
      txLoss590 = 0
   else:
      txLoss590 = (pue['B1'] + pue['B2']) / pue['Bp']
   if pue['Cp'] == 0:
      txLoss596 = 0
   else:
      txLoss596 = (pue['C1'] + pue['C2']) / pue['Cp']

   #numm1 = ( ( pue['N1'] + pue['N2'] + pue['N3'] + pue['N4'] + pue['N5'] + pue['N6'] + pue['N7'] + pue['N8'] + pue['N9'] - pue['N7p'] + (pue['ND1-1'] + pue['ND1-2'] + pue['ND1-3'] + pue['ND1-4'] + pue['ND1-5'] + pue['ND1-6']) / 1000 ) * txLoss590 + ( pue['Cp'] - pue['N10pp'] - pue['N11pp'] ) * txLoss596 + pue['D'] + pue['E'] + pue['F'] ) * lineLoss
   #demon1 = (pue['ND1-1'] + pue['ND1-2'] + pue['ND1-3'] + pue['ND1-4'] + pue['ND1-5'] + pue['ND1-6']) / 1000 - pue['N7p'] + pue['Dp'] + pue['Ep'] + pue['Fp']

   numm1 = ( ( pue['N1'] + pue['N2'] + pue['N3'] + pue['N4'] + pue['N5'] + pue['N6'] + pue['N7'] + pue['N8'] + pue['N9'] - pue['N7p'] + pue['ND1-1'] + pue['ND1-2'] + pue['ND1-3'] + pue['ND1-4'] + pue['ND1-5'] + pue['ND1-6']) * txLoss590 + ( pue['Cp'] - pue['N10pp'] - pue['N11pp'] ) * txLoss596 + pue['D'] + pue['E'] + pue['F'] ) * lineLoss
   demon1 = (pue['ND1-1'] + pue['ND1-2'] + pue['ND1-3'] + pue['ND1-4'] + pue['ND1-5'] + pue['ND1-6']) - pue['N7p'] + pue['Dp'] + pue['Ep'] + pue['Fp']

   numm2 = ( ( pue['N1'] + pue['N2'] + pue['N3'] + pue['N4'] + pue['N5'] + pue['N7'] + pue['N6'] + pue['N8'] + pue['N9'] + pue['ND2-1'] + pue['ND2-2'] + pue['ND2-3'] + pue['ND2-4'] + pue['ND2-5'] + pue['ND2-6'] + pue['ND2-7'] + pue['ND2-8'] + pue['ND2-9'] + pue['ND2-10'] + pue['ND2-11'] + pue['ND2-12'] + pue['ND2-13'] + pue['ND2-14'] + pue['ND2-15'] + pue['ND2-16'] + pue['ND2-17'] + pue['ND2-18'] ) * txLoss590 + ( pue['Cp'] - pue['N10pp'] - pue['N11pp'] ) * txLoss596 + pue['D'] + pue['E'] + pue['F'] ) * lineLoss

   demon2 = pue['ND2-1'] + pue['ND2-2'] + pue['ND2-3'] + pue['ND2-4'] + pue['ND2-5'] + pue['ND2-6'] + pue['ND2-7'] + pue['ND2-8'] + pue['ND2-9'] + pue['ND2-10'] + pue['ND2-11'] + pue['ND2-12'] + pue['ND2-13'] + pue['ND2-14'] + pue['ND2-15'] + pue['ND2-16'] + pue['ND2-17'] + pue['ND2-18'] + pue['Dp'] + pue['Ep'] + pue['Fp']

   if demon1 == 0:
      p1 = 0
   else:
      p1 = numm1 / demon1
   if demon2 == 0:
      p2 = 0
   else:
      p2 = numm2 / demon2

   result['level1']['pue'] = p1
   result['level2']['pue'] = p2
   result['level1']['end'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
   result['level2']['end'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
   #print 'numm1: ', numm1
   #print 'numm2: ', numm2

   #print("N1:     %s" % pue['N1'])
   #print("N2:     %s" % pue['N2'])
   #print("N3:     %s" % pue['N3'])
   #print("N4:     %s" % pue['N4'])
   #print("N5:     %s" % pue['N5'])
   #print("N6:     %s" % pue['N6'])
   #print("N7:     %s" % pue['N7'])
   #print("N7p:    %s" % pue['N7p'])
   #print("N7pp:   %s" % pue['N7pp'])
   #print("N8:     %s" % pue['N8'])
   #print("N9:     %s" % pue['N9'])
   #print("N10:    %s" % pue['N10'])
   #print("N10p:   %s" % pue['N10p'])
   #print("N10pp:  %s" % pue['N10pp'])
   ##print("N11:    %s" % pue['N11'])
   ##print("N11p:   %s" % pue['N11p'])
   #print("N11pp:  %s" % pue['N11pp'])
   ##print("A:      %s" % pue['A'])
   #print("A1:     %s" % pue['A1'])
   #print("A2:     %s" % pue['A2'])
   ##print("B:      %s" % pue['B'])
   #print("B1:     %s" % pue['B1'])
   #print("B2:     %s" % pue['B2'])
   ##print("C:      %s" % pue['C'])
   #print("C1:     %s" % pue['C1'])
   #print("C2:     %s" % pue['C2'])
   #print("D:      %s" % pue['D'])
   #print("D1:     %s" % pue['D1'])
   #print("D2:     %s" % pue['D2'])
   #print("E:      %s" % pue['E'])
   #print("E1:     %s" % pue['E1'])
   #print("E2:     %s" % pue['E2'])
   #print("F:      %s" % pue['F'])
   #print("F1:     %s" % pue['F1'])
   #print("F2:     %s" % pue['F2'])
   #print("ND1-1:  %s" % pue['ND1-1'])
   #print("ND1-2:  %s" % pue['ND1-2'])
   #print("ND1-3:  %s" % pue['ND1-3'])
   #print("ND1-4:  %s" % pue['ND1-4'])
   #print("ND1-5:  %s" % pue['ND1-5'])
   #print("ND1-6:  %s" % pue['ND1-6'])
   #print("ND2-1:  %s" % pue['ND2-1'])
   #print("ND2-2:  %s" % pue['ND2-2'])
   #print("ND2-3:  %s" % pue['ND2-3'])
   #print("ND2-4:  %s" % pue['ND2-4'])
   #print("ND2-5:  %s" % pue['ND2-5'])
   #print("ND2-6:  %s" % pue['ND2-6'])
   #print("ND2-7:  %s" % pue['ND2-7'])
   #print("ND2-8:  %s" % pue['ND2-8'])
   #print("ND2-9:  %s" % pue['ND2-9'])
   #print("ND2-10: %s" % pue['ND2-10'])
   #print("ND2-11: %s" % pue['ND2-11'])
   #print("ND2-12: %s" % pue['ND2-12'])
   #print("ND2-13: %s" % pue['ND2-13'])
   #print("ND2-14: %s" % pue['ND2-14'])
   #print("ND2-15: %s" % pue['ND2-15'])
   #print("ND2-16: %s" % pue['ND2-16'])

   #print 'demon1: ', demon1
   #print 'demon2: ', demon2

def main():
   exchange = 'ha-metric'
   routingKey = 'crt.pue'
   creds = pika.PlainCredentials('logstash', 'c0ntrOl')
   #conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit.crt.nersc.gov', credentials = creds))
   #channel = conn.channel()
   #channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)

   while 1:
      conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit.crt.nersc.gov', credentials = creds))
      channel = conn.channel()
      channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)
      time.sleep(10)

      result['level1'] = dict(count=0, var='eup-last-1l', type='eup-saved-level1', factor=1, meter='Experimental2 Last Value', host='crt', system='crt', start=None, end=None)
      result['level2'] = dict(count=0, var='eup-last-2l', type='eup-saved-level2', factor=1, meter='Experimental2 Last Value', host='crt', system='crt', start=None, end=None)

      calc(result)

      #print('PUE1: %s\n', (json.dumps(result['level1'])))
      #print('PUE2: %s\n', (json.dumps(result['level2'])))
      #print('PUE1: %s', result['level1']['pue'])
      #print('PUE2: %s\n', result['level2']['pue'])
      #print('\n')
      #msg = json.dumps(result['level1'])
      #print('msg: %s', (msg))

      channel.basic_publish(exchange='%s' % (exchange),
         routing_key='%s' % (routingKey),
         body = '%s' % (json.dumps(result['level1'])))

      time.sleep(5)
      channel.basic_publish(exchange='%s' % (exchange),
         routing_key='%s' % (routingKey),
         body = '%s' % (json.dumps(result['level2'])))

      conn.close()
      time.sleep(290)
      #time.sleep(600)

if __name__ == '__main__': main()
