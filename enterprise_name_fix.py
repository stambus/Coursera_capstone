import pandas as pd

# Companies in Vilnius data
sheet_url_ED = 'https://docs.google.com/spreadsheets/d/1JKj4-dYQqW6gB_Xr3inEZfr88YogIDVTGbezOgbJxIc/edit#gid=1786717215'
csv_export_url_ED = sheet_url_ED.replace('/edit#gid=', '/export?format=csv&gid=')
enterprise_df = pd.read_csv(csv_export_url_ED)

enterprise_name = enterprise_df['Pavadinimas (name)'].to_list()
fix_name = []
for i in enterprise_name:
    ab = 'AKCINE'
    uab = 'UŽDAROJI'
    vsi = 'VIEŠOJI'
    vi = 'VALSTYBES'
    if uab in i:
        name = i.replace('UŽDAROJI','').replace('AKCINE','').replace('BENDROVE','UAB')
        if name[0] == ' ':
            new_name = name[1:]
            if new_name[0] == ' ':
                new_name_1 = new_name[1:]
                fix_name.append(new_name_1)
            else:
                fix_name.append(new_name)
        else:
            fix_name.append(name)
    elif ab in i:
        name = i.replace('AKCINE','').replace('BENDROVE','AB')
        if name[0] == ' ':
            new_name = name[1:]
            fix_name.append(new_name)
        else:
            fix_name.append(name)
    elif vsi in i:
        name = i.replace('VIEŠOJI','').replace('ISTAIGA','Všį')
        if name[0] == ' ':
            new_name = name[1:]
            fix_name.append(new_name)
        else:
            fix_name.append(name)
    elif vi in i:
        name = i.replace('VALSTYBES','').replace('IMONE','Vį')
        if name[0] == ' ':
            new_name = name[1:]
            fix_name.append(new_name)
        else:
            fix_name.append(name)
    else:
        fix_name.append(i)



