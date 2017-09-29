#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Written / Edited by Philipp Näther
# philipp.naether@stadt-meissen.de

# Perf-O-Meters for Check_MK's checks
#
# They are called with:
# 1. row -> a dictionary of the data row with at least the
#    keys "service_perf_data", "service_state" and "service_check_command"
# 2. The check command (might be extracted from the performance data
#    in a PNP-like manner, e.g if perfdata is "value=10.5;0;100.0;20;30 [check_disk]
# 3. The parsed performance data as a list of 7-tuples of
#    (varname, value, unit, warn, crit, min, max)

def perfometer_emcunity_fs(row, check_command, perf_data):
    used_mb        = perf_data[0][1]
    maxx           = perf_data[0][-1]
    # perf data might be incomplete, if trending perfdata is off...
    allocated_mb = 0
    for entry in perf_data:
        if entry[0] == "allocated":
            allocated_mb = entry[1]
            break

    perc_used = 100 * (float(used_mb) / float(maxx))
    perc_allocated = 100 * (float(allocated_mb) / float(maxx))
    perc_totally_free = 100 - perc_used

    h = '<table><tr>'
    h += perfometer_td(perc_used, "#00ffc6")
    h += perfometer_td(perc_allocated, "#eeccff")
    h += perfometer_td(perc_totally_free, "white")
    h += "</tr></table>"

    legend = "%0.2f%%" % perc_used
    if allocated_mb:
        legend += " (alloc:%0.2f%%)" % perc_allocated
    return legend, h

perfometers["check_mk-emcunity_fs"] = perfometer_emcunity_fs
