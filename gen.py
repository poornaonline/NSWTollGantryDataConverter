import json

i = 0

with open('data.json') as json_file:
    data = json.load(json_file)

    for p in data['rows']:

        i = i + 1

        genname = p['reference'].lower().replace('-', '_').replace(' ', '_').replace('/', '_')
        direction = 'null'

        if "e_b" in genname:
            genname = genname.replace('e_b', 'eb')
            direction = '"eb"'

        if "w_b" in genname:
            genname = genname.replace('w_b', 'wb')
            direction = '"wb"'

        tolltype = p['toll_type'].upper()

        if p['toll_type'] == "TimeofDay":
            tolltype = "TIME_OF_DAY"

        tollRoadName = '-'

        if genname.startswith('m'):
            tollRoadName = """m{y}""".format(y=genname[1])

        print("""
            Gantry {varname} = new Gantry();
            {varname}.setId("{reference}");
            {varname}.setLatitude({latitude});
            {varname}.setLongitude({longitude});
            {varname}.setWidth(13.78);
            {varname}.setTollType(TollType.{toll_type});
            {varname}.setTollGateCode("{tollgate_code}");
            {varname}.setDirection({direc});
            {varname}.setTollRoadName("{toll_road_name}");
            {varname}.setCountry("australia");
            {varname}.setCity("sydney");
        """.format(reference=p['reference'], latitude=p['latitude'], longitude=p['longitude'], tollgate_code=p['tollgate_code'], toll_type=tolltype, varname=genname, direc=direction, toll_road_name=tollRoadName))
