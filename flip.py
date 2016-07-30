#!/usr/bin/python
#
# a quick hack script to flip x and y coordinates for the URL
# http://api.tmpforchch.co.nz/v4/tmps?key=govhack2016&format=geojson&limit=10000
#
# found out later that it wasn't need if used URL
# http://api.tmpforchch.co.nz/v3/tmps?key=govhack2016&format=geojson&limit=10000
#


import json

with open('c.geojson', 'r') as myfile:
    s = myfile.read()

#s = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"id":36001,"title":"J005600 - BSL - HB706 L1 Highfield Plc, Area ","address":"Highfield Plc","startdate":"2016-08-26","enddate":"2016-09-09","publicdescription":"Trenching drilling and reinstatement works for installation of UFB network","roadclosurestatus":"Non Road Closure","lastupdated":"2016-07-26 10:31:01","jobtype":"Road Works","significance":"Not Significant","timeofday":"Daytime (7am - 6pm)","is_strategic_route":false,"joblevels":["Level 1"],"trafficimpacts":["Pedestrians Affected","Shoulder Closure"]},"geometry":{"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[-43.51670409557,172.55786776543],[-43.5197694438,172.55670905113],[-43.519893921656,172.55724549294],[-43.518135648134,172.55836129189],[-43.518773611706,172.55904793739],[-43.517248711961,172.56462693214],[-43.516532929403,172.56451964378],[-43.51670409557,172.55786776543]]],"properties":{"model":"TMP","type":"extent"}},{"type":"Point","coordinates":[-43.517217591157,172.56153702736],"properties":{"model":"TMP","type":"focus"}}]}}]}'


# s = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"id":36001,"title":"J005600 - BSL - HB706 L1 Highfield Plc, Area ","address":"Highfield Plc","startdate":"2016-08-26","enddate":"2016-09-09","publicdescription":"Trenching drilling and reinstatement works for installation of UFB network","roadclosurestatus":"Non Road Closure","lastupdated":"2016-07-26 10:31:01","jobtype":"Road Works","significance":"Not Significant","timeofday":"Daytime (7am - 6pm)","is_strategic_route":false,"joblevels":["Level 1"],"trafficimpacts":["Pedestrians Affected","Shoulder Closure"]},"geometry":{"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[-43.51670409557,172.55786776543],[-43.5197694438,172.55670905113],[-43.519893921656,172.55724549294],[-43.518135648134,172.55836129189],[-43.518773611706,172.55904793739],[-43.517248711961,172.56462693214],[-43.516532929403,172.56451964378],[-43.51670409557,172.55786776543]]],"properties":{"model":"TMP","type":"extent"}},{"type":"Point","coordinates":[-43.517217591157,172.56153702736],"properties":{"model":"TMP","type":"focus"}}]}},{"type":"Feature","properties":{"id":36141,"title":"Linfox Building Re-branding","address":"Opposite 740 Halswell Junction Road","startdate":"2016-08-22","enddate":"2016-08-26","publicdescription":"Small lane shift to accommodate for the swing of the boom while the new brand sign is installed","roadclosurestatus":"Non Road Closure","lastupdated":"2016-07-29 06:53:25","jobtype":"Road Works","significance":"Not Significant","timeofday":"Inter-peak (9am-4pm Mon-Thur, 9am-3:30pm Fri)","is_strategic_route":true,"joblevels":["Level 2"],"trafficimpacts":["Cyclists Affected"]},"geometry":{"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[-43.548260392224,172.51133143902],[-43.548439244544,172.51107394695],[-43.550274394204,172.51382052898],[-43.550453240547,172.51419603825],[-43.550966448847,172.51570880413],[-43.550686517589,172.51589119434],[-43.550235514494,172.51439988613],[-43.550002235707,172.51391708851],[-43.548260392224,172.51133143902]]],"properties":{"model":"TMP","type":"extent"}},{"type":"Point","coordinates":[-43.549940027878,172.51350671053],"properties":{"model":"TMP","type":"focus"}}]}}]}'

obj = json.loads(s);

#print obj 

for k, v in obj.items():
    if k == "features":
        for i in v:
            #print type(i)
            for a , b in i.items():
                if a == "geometry":
                    for c,d in b.items():
                        if c == "geometries":
                            for e in d:
                                #print type(e)
                                for f,g in e.items():
                                    #print f
                                    if f == "coordinates":
                                        #print g
                                        #print type(g)
                                        #print len(g)
                                        if len(g) == 2:
                                            
                                            aa = g[1]
                                            bb = g[0]
                                            g[1] = bb
                                            g[0] = aa
                                            #for coord in g:
                                                # print coord
                                                #print ""
                                        if len(g) == 1:
                                            for h in g:
                                                #print h
                                                #print type(h)
                                                #print len(h)
                                                for j in h:
                                                    # print j
                                                    aa = j[1]
                                                    bb = j[0]
                                                    j[1] = bb
                                                    j[0] = aa
                                                #print "****"
                                    #print "===="
                                    #print f
                                    #print "*****"
                                    #print type(g) 
                                    #print g
        
print json.dumps(obj)