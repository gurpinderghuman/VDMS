import urllib2
import json
import sys

def med(ti):
    median = -1
    if len(ti)%2 == 0:
        median = float(ti[len(ti)/2])+float(ti[len(ti)/2 +1])
        median = median/2
    else:
        median = float(ti[len(ti)/2])
    return median
features = sys.argv[1]
if features == 'tide':
    ur = 'http://api.wunderground.com/api/57604644ebf9efb6/'+features+'/q/CA/Santa_Monica.json'
    f = urllib2.urlopen(ur)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    tide = parsed_json['tide']
    hightide = []
    lowtide = []
    tidetime = {}
    tidesunrise = []
    tidemoonrise = []
    tidesunset = []
    tidemoonset = []
    tidesum = tide['tideSummary']
    #print len(tidesum)
    for i in range(len(tidesum)):

        tidesum1 = tidesum[i]
        #print tidesum1
        if tidesum1['data']['type'] == 'High Tide':

            hightide.append(tidesum1['data']['height'][:-2])
            tidetime[tidesum1['data']['height'][:-2]] = {tidesum1['utcdate']['hour'],tidesum1['utcdate']['min']}
        if tidesum1['data']['type'] == 'Low Tide':
            #print tidesum1
            lowtide.append(tidesum1['data']['height'][:-2])
            tidetime[tidesum1['data']['height'][:-2]] = {tidesum1['utcdate']['hour'],tidesum1['utcdate']['min']}
        if tidesum1['data']['type'] == 'Sunrise':
            tidesunrise.append((int(tidesum1['utcdate']['hour'])*60 + int(tidesum1['utcdate']['min'])))
        if tidesum1['data']['type'] == 'Moonrise':
            tidemoonrise.append((int(tidesum1['utcdate']['hour'])*60 + int(tidesum1['utcdate']['min'])))
        if tidesum1['data']['type'] == 'Sunset':
            tidesunset.append((int(tidesum1['utcdate']['hour'])*60 + int(tidesum1['utcdate']['min'])))
        if tidesum1['data']['type'] == 'Moonset':
            tidemoonset.append((int(tidesum1['utcdate']['hour'])*60 + int(tidesum1['utcdate']['min'])))
            #print tidesunrise
    sum_high,sum_low = 0,0
    for i in hightide:
        sum_high += float(i)
    for i in lowtide:
        sum_low += float(i)
    hightide.sort()
    lowtide.sort()
    length_high = len(hightide)
    length_low = len(lowtide)
    avg_high = sum_high/length_high
    avg_low = sum_low/length_low
    #print tidetime
    tideinfo = tide['tideInfo']
    tidesite = tideinfo[0]['tideSite']
    tidesunrise.sort()
    tidemoonrise.sort()
    tidesunset.sort()
    tidemoonset.sort()
    print "Geographic site that data is associated with: ",tidesite
    print "Maximum height of Hightide: ", hightide[length_high-1]
    print "Minimum height of Hightide: ", hightide[0]
    print "Average height of Hightide: ", avg_high;
    print "Median height of Hightide: ", med(hightide);
    print "Maximum height of Lowtide: ", lowtide[length_low-1]
    print "Minimum height of lowtide: ", lowtide[0]
    print "Average height of Lowtide: ", avg_low;
    print "Median height of Lowtide: ", med(lowtide);
    print "Time associated with Maximum Hightide: ", tidetime[hightide[length_high-1]]
    print "Time associated with Minimum Hightide: ", tidetime[hightide[0]]
    print "Time associated with Maximum Lowtide: ", tidetime[lowtide[length_low-1]]
    print "Time associated with Minimum Lowtide: ", tidetime[lowtide[0]]
    print "Median of time at Sunrise:",int(med(tidesunrise)/60),'hrs',int(med(tidesunrise)%60),'mins'
    print "Median of time at Moonrise:",int(med(tidemoonrise)/60),'hrs',int(med(tidemoonrise)%60),'mins'
    print "Median of time at Sunset:",int(med(tidesunset)/60),'hrs',int(med(tidesunset)%60),'mins'
    print "Median of time at Moonset:",int(med(tidemoonset)/60),'hrs',int(med(tidemoonset)%60),'mins'
    f.close()
elif features == 'hourly':
    ur = 'http://api.wunderground.com/api/57604644ebf9efb6/'+features+'/q/CA/Santa_Monica.json'
    f1 = urllib2.urlopen(ur)
    json_string = f1.read()
    temperature_metric = []
    temperature_english = []
    temp_sum_metric,temp_sum_english = 0,0
    parsed_json = json.loads(json_string)
    hourly = parsed_json['hourly_forecast']
    for i in range(len(hourly)):
        temperature_metric.append(hourly[i]['temp']['metric'])
        temperature_english.append(hourly[i]['temp']['english'])

    """print temperature_metric
    print temperature_english"""
    for j in temperature_metric:
        temp_sum_metric += float(j)
    for i in temperature_english:
        temp_sum_english += float(i)
    print "Average Temerature in metric: ", temp_sum_metric/len(temperature_metric)
    print "Average Temerature in english: ", temp_sum_english/len(temperature_english)
    f1.close()

elif features == 'alerts' or features == 'almanac' or features == 'astronomy' or features == 'conditions' or features == 'currenthurricane':
    ur = 'http://api.wunderground.com/api/57604644ebf9efb6/'+features+'/q/CA/Santa_Monica.json'
    f = urllib2.urlopen(ur)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    print "Data for ",features + " was successfully obtained."
    f.close()
elif features == 'forecast' or features == 'forecast10day' or features == 'geolookup' or features == 'history' or features == 'hourly10day':
    ur = 'http://api.wunderground.com/api/57604644ebf9efb6/'+features+'/q/CA/Santa_Monica.json'
    f = urllib2.urlopen(ur)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    print "Data for ",features + " was successfully obtained."
    f.close()

elif features == 'planner' or features == 'rawtide' or features == 'webcams' or features == 'yesterday':
    ur = 'http://api.wunderground.com/api/57604644ebf9efb6/'+features+'/q/CA/Santa_Monica.json'
    f = urllib2.urlopen(ur)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    print "Data for ",features + " was successfully obtained."
    f.close()

else:
    print "Input is Invalid"
