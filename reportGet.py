import time,pandas,json
from collections import Counter
from pyecharts import TreeMap

def getRightNum(json_data,k):
    i = 0
    for n in range(len(json_data)):
        if json_data[str(n)]['testSuiteName'] == k:
            # print(k)
            # print(json_data[str(n)]['testSuiteName'])
            if json_data[str(n)]['type'] == ' PASSD ':
                # print(json_data[str(n)]['type'])
                i += 1
    return i


def dataCleaning(filename = ''):
    headers = ["actTime","threadName","levelName","testSuiteName","type","identificationData","messages"]
    data = pandas.DataFrame(pandas.read_csv(filename,delimiter='|',names = headers,engine = 'python',sep = '|'))
    json_data = json.loads(data.to_json(orient="index",force_ascii=False))

    header_data = [json_data[str(i)]['testSuiteName'] for i in range(len(json_data))]
    header_dict = Counter(header_data)
    # print(header_dict.items())
    data_grid = [{"value":v,"name":[k,getRightNum(json_data,k), \
                int(v)-int(getRightNum(json_data,k))],"children":[]}  \
                for k,v in header_dict.items()]
    for i in range(len(json_data)):
        for node_grid in data_grid:
            if json_data[str(i)]['testSuiteName'] == node_grid['name'][0]:
                node_grid['children'].append({"value":1,"name":[json_data[str(i)]['messages'] \
                    ,json_data[str(i)]['identificationData'],json_data[str(i)]['type']]})
    print(data_grid)
    return data_grid

def label_formatter(params):
    params.color = '#61a0a8' if params.name[2]>0 or params.name[2] == ' ERROR ' else '#c23531'
    return params.name[0] + "\n" \
        + params.name[1]+":"+params.name[2]

def tooltip_formatter(params):
    params.color = '#61a0a8' if params.name[2]>0 or params.name[2] == ' ERROR ' else '#c23531'
    return params.name[0] + "<br>" \
        + params.name[1] + "<br>" \
            + params.name[2]
def treeReport():
    treemap = TreeMap(width=1200,height=800)
    data_Cleaning = dataCleaning()
    # color_contor = ['#61a0a8'  if ' ERROR ' in str(data_node) else '#c23531' for data_node in data_Cleaning]
    # print(color_contor)
    # treemap_left_depth=1
    treemap.add("Report about TestCase",data = data_Cleaning,is_random=False,\
                is_label_show=True,label_pos='inside',tooltip_formatter=tooltip_formatter,\
                    label_formatter=label_formatter,legend_orient='vertical')
                # label_color=['#61a0a8', '#c23531', '#61a0a8', '#c23531', '#61a0a8', '#c23531']
    # treemap.set_series_opts(label_opts=opts.label_opts(formatter=Js))
    treemap.render('%s.html'%(time.ctime()))

treeReport() 

