from sys import argv
from decimal import Decimal
from collections import defaultdict
import csv

def update_item_pos(header):
    """
    add column index of specific parament correspond to csv header
    """
    global item_pos
    headers_list = header.split(',')
    for i, x in enumerate(headers_list):
        x = x.rstrip("\"")[1:]
        if x == "usr":
            item_pos["cpu_usr"].append(i)
        elif x == "sys":
            item_pos["cpu_sys"].append(i)
        elif x == "wai":
            item_pos["cpu_wait"].append(i)
        elif x == "used":
            item_pos["memory_used"].append(i)
        elif x == "buff":
            item_pos["memory_buff"].append(i)
        elif x == "cach":
            item_pos["memory_cache"].append(i)
        elif x == "free":
            item_pos["memory_free"].append(i)
        elif x == "epoch":
            item_pos["epoch"].append(i)
        elif x == "read":
            item_pos["disk_read"].append(i)
        elif x == "writ":
            item_pos["disk_write"].append(i)
        elif x == "1m":
            item_pos["load"].append(i)
        elif x == "csw":
            item_pos["context_switch"].append(i)
        elif x == "int":
            item_pos["interrupt"].append(i)
    # print(item_pos)

def get_item(record, key):
    """
    getting avg from all column correspond to parametr (forexample for cpu, getting avg of all core usage)
    """
    result = 0
    for pos in item_pos[key]:
        result += float(record[pos])
    return result/len(item_pos[key])

def load_csv_reader(file_handler):
    for line in file_handler:
        if line.startswith("\"1m"):
            update_item_pos(line)
            break
    return csv.reader(fh)

def extract_epoch(record):
    """
    return eleapsed time from first epoch recieved.
    """
    global time_origin
    if time_origin is None:
        time_origin = float(get_item(record, "epoch"))
        return float(0)
    return float(get_item(record, "epoch")) - time_origin

#generete tuple for parameters:
def extract_cpu_usage(record):
    return (
        extract_epoch(record),
        get_item(record, "cpu_usr") + get_item(record, "cpu_sys") + get_item(record, "cpu_wait")
        )

def extract_memory_usage(record):
    return (
        extract_epoch(record),
        (get_item(record, "memory_used")+get_item(record, "memory_cache")+get_item(record, "memory_buff"))/(10**6)
        )

def get_string_result(result, max_result_len):
    """
    summerize result (getting avg from second datum)
    """
    if not isinstance(result, list):
        return "{:.2f}".format(result)
    result_string = ""
    skip_step = len(result)//max_result_len
    current_skip_step = 0
    store = 0
    for record in result:
        if current_skip_step == skip_step:
            store += record[1]
            result_string += " ("+str(int(record[0]))+" , "+str(store//(current_skip_step+1))+")"
            current_skip_step = 0
            store = 0
        else:
            store += record[1]
            current_skip_step += 1
    if current_skip_step:
        result_string += " ("+str(int(record[0]))+" , "+str(store//(current_skip_step))+")"

    return result_string+"\n"

def get_average(tuple_list):
    if len(tuple_list) == 0:
        return 0
    s = 0
    for t in tuple_list:
        s += t[1]
    return s/len(tuple_list)

def extract_all_reports(reader):
    """
    return dict which contain all reports from inout csv reader
    """
    result = defaultdict(list)
    for row in reader:
        result["cpu"].append(extract_cpu_usage(row))
        result["memory"].append(extract_memory_usage(row))
    return result

dstat_file_path = argv[1]

image_name = dstat_file_path.split("/")[-2]

time_origin = None
item_pos = defaultdict(list)
report_original = {}
with open(dstat_file_path+"/dtat-result-orginal.csv") as fh:
    report_original = extract_all_reports(load_csv_reader(fh))

time_origin = None
item_pos = defaultdict(list)
report_slim = {}
with open(dstat_file_path+"/dtat-result-slim.csv") as fh:
    report_slim = extract_all_reports(load_csv_reader(fh))

# generate result tex from template by replacing placeholders
with open("dstat-template.tex") as fh:
    template = fh.read()
    for k, v in report_original.items():
        template = template.replace("{"+k+"-original}", get_string_result(v, 500))
    for k, v in report_slim.items():
        template = template.replace("{"+k+"-slim}", get_string_result(v, 500))

rendered_tex = template.replace("{Q}", image_name)

print(rendered_tex)