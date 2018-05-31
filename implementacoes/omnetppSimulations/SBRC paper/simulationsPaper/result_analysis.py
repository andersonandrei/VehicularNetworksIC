# -*- coding: utf-8 -*-
## result_analysis.py
## Patrick Abrahão Menani

#
# TCP Encapsulate Byte Lenght = 
# UDP Encapsulate Byte Lenght = 
#

import re
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


ROOTDIR = 'sca_source'

DASH_sp = 0
DASH_sp_2 = 0

TCP_sp = 0
TCP_sp_2 = 0

UDP_sp = 0
UDP_sp_2 = 0

DASH_sp_100 = 0
DASH_sp_100_2 = 0

TCP_sp_100 = 0
TCP_sp_100_2 = 0

UDP_sp_100 = 0
UDP_sp_100_2 = 0

DASH_sp_150 = 0
DASH_sp_150_2 = 0

TCP_sp_150 = 0
TCP_sp_150_2 = 0

UDP_sp_150 = 0
UDP_sp_150_2 = 0

DASH_sp_l= []
DASH_sp_2_l= []

TCP_sp_l= []
TCP_sp_2_l= []

UDP_sp_l= []
UDP_sp_2_l= []

DASH_sp_100_l= []
DASH_sp_100_2_l= []

TCP_sp_100_l= []
TCP_sp_100_2_l= []

UDP_sp_100_l= []
UDP_sp_100_2_l= []

DASH_sp_150_l= []
DASH_sp_150_2_l= []

TCP_sp_150_l= []
TCP_sp_150_2_l= []

UDP_sp_150_l= []
UDP_sp_150_2_l= []


DASH_rcvd_50 = 0.0
DASH_sent_50 = 0.0
DASH_rcvd_100 = 0.0
DASH_sent_100 = 0.0
DASH_rcvd_150 = 0.0
DASH_sent_150 = 0.0

TCP_rcvd_50 = 0.0
TCP_sent_50 = 0.0
TCP_rcvd_100 = 0.0
TCP_sent_100 = 0.0
TCP_rcvd_150 = 0.0
TCP_sent_150 = 0.0

UDP_rcvd_50 = 0.0
UDP_sent_50 = 0.0
UDP_rcvd_100 = 0.0
UDP_sent_100 = 0.0
UDP_rcvd_150 = 0.0
UDP_sent_150 = 0.0

DASH_rcvd_50_2 = 0.0
DASH_sent_50_2 = 0.0
DASH_rcvd_100_2 = 0.0
DASH_sent_100_2 = 0.0
DASH_rcvd_150_2 = 0.0
DASH_sent_150_2 = 0.0

TCP_rcvd_50_2 = 0.0
TCP_sent_50_2 = 0.0
TCP_rcvd_100_2 = 0.0
TCP_sent_100_2 = 0.0
TCP_rcvd_150_2 = 0.0
TCP_sent_150_2 = 0.0

UDP_rcvd_50_2 = 0.0
UDP_sent_50_2 = 0.0
UDP_rcvd_100_2 = 0.0
UDP_sent_100_2 = 0.0
UDP_rcvd_150_2 = 0.0
UDP_sent_150_2 = 0.0

def reset_host_param (type_file, analysis_type):
   if (type_file == 'DASH' or type_file == 'TCP') and analysis_type == 'endTo':
      hostB = 'scalar Net.hostB.tcpApp[0] rcvdPk:count'
      hostB_final = 'scalar Net.hostB.tcpApp[0] sentPk:count'

   elif type_file == 'UDP' and analysis_type == 'endTo':
      hostB = 'scalar Net.hostB.udpApp[0] rcvdPk:count'
      hostB_final = 'scalar Net.hostB.udp droppedPkBadChecksum:count'

   if (type_file == 'DASH' or type_file == 'TCP') and analysis_type == 'bitError':
      hostB = 'statistic Net.hostB.wlan[0].radio bitErrorRate:histogram'
      hostB_final = 'statistic Net.hostB.wlan[0].radio packetErrorRate:histogram'

   elif type_file == 'UDP' and analysis_type == 'bitError':
      hostB = 'statistic Net.hostB.wlan[0].radio bitErrorRate:histogram'
      hostB_final = 'statistic Net.hostB.wlan[0].radio packetErrorRate:histogram'

   if (type_file == 'DASH' or type_file == 'TCP') and analysis_type == 'packetError':
      hostB = 'statistic Net.hostB.wlan[0].radio packetErrorRate:histogram'
      hostB_final = 'statistic Net.hostB.wlan[0].radio minSNIR:histogram'

   elif type_file == 'UDP' and analysis_type == 'packetError':
      hostB = 'statistic Net.hostB.wlan[0].radio packetErrorRate:histogram'
      hostB_final = 'statistic Net.hostB.wlan[0].radio minSNIR:histogram'


   return [hostB,hostB_final]

def get_avg_pck_rate(file, type_file, r, s, sp):

   global DASH_sp
   global DASH_sp_2

   global TCP_sp
   global TCP_sp_2

   global UDP_sp
   global UDP_sp_2

   global DASH_sp_100
   global DASH_sp_100_2

   global TCP_sp_100
   global TCP_sp_100_2

   global UDP_sp_100
   global UDP_sp_100_2

   global DASH_sp_150
   global DASH_sp_150_2

   global TCP_sp_150
   global TCP_sp_150_2

   global UDP_sp_150
   global UDP_sp_150_2

   global DASH_sp_l
   global DASH_sp_2_l

   global TCP_sp_l
   global TCP_sp_2_l

   global UDP_sp_l
   global UDP_sp_2_l

   global DASH_sp_100_l
   global DASH_sp_100_2_l

   global TCP_sp_100_l
   global TCP_sp_100_2_l

   global UDP_sp_100_l
   global UDP_sp_100_2_l

   global DASH_sp_150_l
   global DASH_sp_150_2_l

   global TCP_sp_150_l
   global TCP_sp_150_2_l

   global UDP_sp_150_l
   global UDP_sp_150_2_l

   global  DASH_rcvd_50
   global  DASH_sent_50
   global DASH_rcvd_100
   global DASH_sent_100
   global DASH_rcvd_150
   global DASH_sent_150

   global  TCP_rcvd_50
   global  TCP_sent_50
   global TCP_rcvd_100
   global TCP_sent_100
   global TCP_rcvd_150
   global TCP_sent_150

   global UDP_rcvd_50
   global UDP_sent_50
   global UDP_rcvd_100
   global UDP_sent_100
   global UDP_rcvd_150
   global UDP_sent_150

   global  DASH_rcvd_50_2
   global  DASH_sent_50_2
   global DASH_rcvd_100_2
   global DASH_sent_100_2
   global DASH_rcvd_150_2
   global DASH_sent_150_2

   global  TCP_rcvd_50_2
   global  TCP_sent_50_2
   global TCP_rcvd_100_2
   global TCP_sent_100_2
   global TCP_rcvd_150_2
   global TCP_sent_150_2

   global UDP_rcvd_50_2
   global UDP_sent_50_2
   global UDP_rcvd_100_2
   global UDP_sent_100_2
   global UDP_rcvd_150_2
   global UDP_sent_150_2

   if '-50' in file:
      if '3mps' in file:
         if r != None:
            r = int(r.group(0))
            if type_file == 'DASH':
               DASH_rcvd_50 += r
            if type_file == 'TCP':
               TCP_rcvd_50 += r
            if type_file == 'UDP':
               UDP_rcvd_50 += r
         if s != None:
            s = int(s.group(0))
            if type_file == 'DASH':
               DASH_sent_50 += s 
            if type_file == 'TCP':
               TCP_sent_50 += s
            if type_file == 'UDP':
               UDP_sent_50 += s
         if sp != None:
            sp = int(sp.group(0))
            if type_file == 'DASH':
               DASH_sp += sp
               DASH_sp_l.append(sp)
            if type_file == 'TCP':
               TCP_sp += sp
               TCP_sp_l.append(sp)
            if type_file == 'UDP':
               UDP_sp += sp
               UDP_sp_l.append(sp)

      else:
         if r != None:
            r = int(r.group(0))
            if type_file == 'DASH':
               DASH_rcvd_50_2 += r
            if type_file == 'TCP':
               TCP_rcvd_50_2 += r
            if type_file == 'UDP':
               UDP_rcvd_50_2 += r
         if s != None:
            s = int(s.group(0))
            if type_file == 'DASH':
               DASH_sent_50_2 += s 
            if type_file == 'TCP':
               TCP_sent_50_2 += s
            if type_file == 'UDP':
               UDP_sent_50_2 += s
         if sp != None:
            sp = int(sp.group(0))
            if type_file == 'DASH':
               DASH_sp_2 += sp
               DASH_sp_2_l.append(sp)
            if type_file == 'TCP':
               TCP_sp_2 += sp
               TCP_sp_2_l.append(sp)
            if type_file == 'UDP':
               UDP_sp_2 += sp
               UDP_sp_2_l.append(sp)

   if '-100' in file:
      if '3mps' in file:
         if r != None:
            r = int(r.group(0))
            if type_file == 'DASH':
               DASH_rcvd_100 += r
            if type_file == 'TCP':
               TCP_rcvd_100 += r
            if type_file == 'UDP':
               UDP_rcvd_100 += r
         if s != None:
            s = int(s.group(0))
            if type_file == 'DASH':
               DASH_sent_100 += s 
            if type_file == 'TCP':
               TCP_sent_100 += s
            if type_file == 'UDP':
               UDP_sent_100 += s
         if sp != None:
            sp = int(sp.group(0))
            if type_file == 'DASH':
               DASH_sp_100 += sp
               DASH_sp_100_l.append(sp)
            if type_file == 'TCP':
               TCP_sp_100 += sp
               TCP_sp_100_l.append(sp)
            if type_file == 'UDP':
               UDP_sp_100 += sp
               UDP_sp_100_l.append(sp)
      else:
         if r != None:
            r = int(r.group(0))
            if type_file == 'DASH':
               DASH_rcvd_100_2 += r
            if type_file == 'TCP':
               TCP_rcvd_100_2 += r
            if type_file == 'UDP':
               UDP_rcvd_100_2 += r
         if s != None:
            s = int(s.group(0))
            if type_file == 'DASH':
               DASH_sent_100_2 += s 
            if type_file == 'TCP':
               TCP_sent_100_2 += s
            if type_file == 'UDP':
               UDP_sent_100_2 += s
         if sp != None:
            sp = int(sp.group(0))
            if type_file == 'DASH':
               DASH_sp_100_2 += sp
               DASH_sp_100_2_l.append(sp)
            if type_file == 'TCP':
               TCP_sp_100_2 += sp
               TCP_sp_100_2_l.append(sp)
            if type_file == 'UDP':
               UDP_sp_100_2 += sp
               UDP_sp_100_2_l.append(sp)

   if '-150' in file:
      if '3mps' in file:
         if r != None:
            r = int(r.group(0))
            if type_file == 'DASH':
               DASH_rcvd_150 += r
            if type_file == 'TCP':
               TCP_rcvd_150 += r
            if type_file == 'UDP':
               UDP_rcvd_150 += r
         if s != None:
            s = int(s.group(0))
            if type_file == 'DASH':
               DASH_sent_150 += s 
            if type_file == 'TCP':
               TCP_sent_150 += s
            if type_file == 'UDP':
               UDP_sent_150 += s
         if sp != None:
            sp = int(sp.group(0))
            if type_file == 'DASH':
               DASH_sp_150 += sp
               DASH_sp_150_l.append(sp)
            if type_file == 'TCP':
               TCP_sp_150 += sp
               TCP_sp_150_l.append(sp)
            if type_file == 'UDP':
               UDP_sp_150 += sp
               UDP_sp_150_l.append(sp)
      else:
         if r != None:
            r = int(r.group(0))
            if type_file == 'DASH':
               DASH_rcvd_150_2 += r
            if type_file == 'TCP':
               TCP_rcvd_150_2 += r
            if type_file == 'UDP':
               UDP_rcvd_150_2 += r
         if s != None:
            s = int(s.group(0))
            if type_file == 'DASH':
               DASH_sent_150_2 += s 
            if type_file == 'TCP':
               TCP_sent_150_2 += s
            if type_file == 'UDP':
               UDP_sent_150_2 += s
         if sp != None:
            sp = int(sp.group(0))
            if type_file == 'DASH':
               DASH_sp_150_2 += sp
               DASH_sp_150_2_l.append(sp)
            if type_file == 'TCP':
               TCP_sp_150_2 += sp
               TCP_sp_150_2_l.append(sp)
            if type_file == 'UDP':
               UDP_sp_150_2 += sp
               UDP_sp_150_2_l.append(sp)

def get_data (file, file_dir, type_file, analysis_type, flag):

   hostA_udpApp = 'scalar Net.hostA.udpApp[0] sentPk:count'

   Sum_pck_tcp = 'scalar Net.hostB.tcpApp[0] rcvdPk:sum(packetBytes)'
   Sum_pck_udp = 'scalar Net.hostB.udpApp[0] rcvdPk:sum(packetBytes)'

   hostB = ''
   hostB_final = ''

   sp_tcp = ''
   sp_udp = ''

   host_param = reset_host_param (type_file, analysis_type)

   hostB = host_param[0]
   hostB_final = host_param[1]


   file_open = open(file_dir)
   text = []
   histogram = []
   with file_open as f:
      for line in f:
         text.append(line)
         if hostB in line:
            hostB = line
         if hostB_final in line:
            hostB_final = line
         if Sum_pck_tcp in line:
            sp_tcp = line
         if hostA_udpApp in line:
            hostA_udpApp = line
         if Sum_pck_udp in line:
            sp_udp = line
   text = list(reversed(text))
   if 'DASH' in file or 'TCP' in file:
      a = 0
      b = 0
      a = text.index(hostB)
      b = text.index(hostB_final)
      r = re.search('[0-9]+$',hostB)
      s = re.search('[0-9]+$',hostB_final)
      sp = re.search('[0-9]+$', sp_tcp)
      if flag:
         get_avg_pck_rate(file, type_file, r, s, sp)
      histogram = text[b:a+1]
   if 'UDP' in file:
      a = 0
      b = 0
      a = text.index(hostB)
      r = re.search('[0-9]+$',hostB)
      s = re.search('[0-9]+$',hostA_udpApp)
      b = text.index(hostB_final)
      sp = re.search('[0-9]+$', sp_udp)
      if flag:
         get_avg_pck_rate(file, type_file, r, s, sp)
      histogram = text[b:a+1]

   return histogram

def get_mean (type_a, index, vel):

   count_50 = 0
   count_100 = 0
   count_150 = 0
   sum_mean_50 = 0
   sum_mean_100 = 0
   sum_mean_150 = 0
   for a in type_a:
      if '-50'+vel in a[0]:
         for c in a[index]:
            stri = c
            if 'field mean' in stri:
               count_50 += 1
               sum_mean_50 += float(stri [11:])
      if '-100'+vel in a[0]:
         for c in a[index]:
            stri = c
            if 'field mean' in stri:
               count_100 += 1
               sum_mean_100 += float(stri [11:])
      if '-150'+vel in a[0]:
         for c in a[index]:
            stri = c
            if 'field mean' in stri:
               count_150 += 1
               sum_mean_150 += float(stri [11:])
   if count_50 > 0:
      sum_mean_50 = sum_mean_50 / count_50
   if count_100 > 0:
      sum_mean_100 = sum_mean_100 / count_100
   if count_150 > 0:
      sum_mean_150 = sum_mean_150 / count_150

   return [sum_mean_50, sum_mean_100, sum_mean_150]

def get_stddev (type_a, index, vel):

   count_50 = 0
   count_100 = 0
   count_150 = 0
   sum_stddev_50 = 0
   sum_stddev_100 = 0
   sum_stddev_150 = 0
   for a in type_a:
      if '-50'+vel in a[0]:
         for c in a[index]:
            stri = c
            if 'field stddev' in stri:
               count_50 += 1
               sum_stddev_50 += float(stri [12:])
      if '-100'+vel in a[0]:
         for c in a[index]:
            stri = c
            if 'field stddev' in stri:
               count_100 += 1
               sum_stddev_100 += float(stri [12:])
      if '-150'+vel in a[0]:
         for c in a[index]:
            stri = c
            if 'field stddev' in stri:
               count_150 += 1
               sum_stddev_150 += float(stri [12:])
   if count_50 > 0:
      sum_stddev_50 = sum_stddev_50 / count_50
   if count_100 > 0:
      sum_stddev_100 = sum_stddev_100 / count_100
   if count_150 > 0:
      sum_stddev_150 = sum_stddev_150 / count_150

   return [sum_stddev_50, sum_stddev_100, sum_stddev_150]

def get_mean_stddev (a):
   mean_stddev = []
   mean_stddev.append (get_mean(a, 1, ',normal(3mps'))
   mean_stddev.append (get_mean(a, 2, ',normal(3mps'))
   mean_stddev.append (get_mean(a, 3, ',normal(3mps'))
   mean_stddev.append (get_mean(a, 1, ',normal(6mps'))
   mean_stddev.append (get_mean(a, 2, ',normal(6mps'))
   mean_stddev.append (get_mean(a, 3, ',normal(6mps'))
   mean_stddev.append (get_stddev(a, 1, ',normal(3mps'))
   mean_stddev.append (get_stddev(a, 2, ',normal(3mps'))
   mean_stddev.append (get_stddev(a, 3, ',normal(3mps'))
   mean_stddev.append (get_stddev(a, 1, ',normal(6mps'))
   mean_stddev.append (get_stddev(a, 2, ',normal(6mps'))
   mean_stddev.append (get_stddev(a, 3, ',normal(6mps'))

   return mean_stddev

def get_histogram(type_sim, index, vel):
   hist_a = []
   hist_b = []
   hist_c = []
   max_def_a = 0
   max_def_b = 0
   max_def_c = 0
   for a in type_sim:
      if '-50'+vel in a[0]:
         for c in a[index]:
            m = re.match('bin', c)
            if m:
               n = re.search('[+-]?([0-9]+[.])?[0-9]+\t',c[4:])
               k = re.search('[0-9]+$',c[4:])
               if n != None and k != None:
                  number_of_occur = int(k.group(0))
                  if number_of_occur > max_def_a:
                     max_def_a = number_of_occur
                  for i in range(0,number_of_occur):
                     ap = float(n.group(0))
                     hist_a.append(ap)
      if '-100'+vel in a[0]:
         for c in a[index]:
            m = re.match('bin', c)
            if m:
               n = re.search('[+-]?([0-9]+[.])?[0-9]+\t',c[4:])
               k = re.search('[0-9]+$',c[4:])
               if n != None and k != None:
                  number_of_occur = int(k.group(0))
                  if number_of_occur > max_def_b:
                     max_def_b = number_of_occur
                  for i in range(0,number_of_occur):
                     ap = float(n.group(0))
                     hist_b.append(ap)
      if '-150'+vel in a[0]:
         for c in a[index]:
            m = re.match('bin', c)
            if m:
               n = re.search('[+-]?([0-9]+[.])?[0-9]+\t',c[4:])
               k = re.search('[0-9]+$',c[4:])
               if n != None and k != None:
                  number_of_occur = int(k.group(0))
                  if number_of_occur > max_def_c:
                     max_def_c = number_of_occur
                  for i in range(0,number_of_occur):
                     ap = float(n.group(0))
                     hist_c.append(ap)

   return [hist_a, max_def_a, hist_b, max_def_b, hist_c, max_def_c]

def save_plot (obj, obj_title):
   fig, axs = plt.subplots(sharey=True, tight_layout=True, figsize=(8, 6))

   x = obj[len(obj) - 6]
   n_bins = len(obj[len(obj) - 6])

   axs.hist(x, bins=n_bins)

   axs.set_title(obj_title + '50')
            
   plt.savefig('analysis_plots/' + obj_title + '50')
   plt.clf()

   fig, axs = plt.subplots(sharey=True, tight_layout=True, figsize=(8, 6))
   x = obj[len(obj) - 4]
   n_bins = len(obj[len(obj) - 4])

   axs.hist(x, bins=n_bins)

   axs.set_title(obj_title + '100')

   plt.savefig('analysis_plots/' + obj_title + '100')
   plt.clf()

   fig, axs = plt.subplots(sharey=True, tight_layout=True, figsize=(8, 6))
   x = obj[len(obj) - 2]
   n_bins = len(obj[len(obj) - 2])

   axs.hist(x, bins=n_bins)

   axs.set_title(obj_title + '150')

   plt.savefig('analysis_plots/' + obj_title + '150')
   plt.clf()

def print_endTo_mean (obj, file):

   print >> file,'endToEndDelay       Means          Stddev'
   print >> file,'50  - 3mps\t' + str(obj[0][0]) + '\t'  + str(obj[6][0]) + '\n'
   print >> file,'100 - 3mps\t' + str(obj[0][1]) + '\t'  + str(obj[6][1]) + '\n'
   print >> file,'150 - 3mps\t' + str(obj[0][2]) + '\t'  + str(obj[6][2]) + '\n'
   print >> file,'50  - 6mps\t' + str(obj[3][0]) + '\t'  + str(obj[9][0]) + '\n'
   print >> file,'100 - 6mps\t' + str(obj[3][1]) + '\t'  + str(obj[9][1]) + '\n'
   print >> file,'150 - 6mps\t' + str(obj[3][2]) + '\t'  + str(obj[9][2]) + '\n'

def print_name(x, file_output):
   if x == 0:
      print  >> file_output, 'DASH_50_3mps:'
   if x == 2:
      print  >> file_output, 'DASH_100_3mps:'
   if x == 4:
      print  >> file_output, 'DASH_150_3mps:'
   if x == 6:
      print  >> file_output, 'TCP_50_3mps:'
   if x == 8:
      print  >> file_output, 'TCP_100_3mps:'
   if x == 10:
      print  >> file_output, 'TCP_150_3mps:'
   if x == 12:
      print  >> file_output, 'UDP_50_3mps:'
   if x == 14:
      print  >> file_output, 'UDP_100_3mps:'
   if x == 16:
      print  >> file_output, 'UDP_150_3mps:'
   if x == 18:
      print  >> file_output, 'DASH_50_6mps:'
   if x == 20:
      print  >> file_output, 'DASH_100_6mps:'
   if x == 22:
      print  >> file_output, 'DASH_150_6mps:'
   if x == 24:
      print  >> file_output, 'TCP_50_6mps:'
   if x == 26:
      print  >> file_output, 'TCP_100_6mps:'
   if x == 28:
      print  >> file_output, 'TCP_150_6mps:'
   if x == 30:
      print  >> file_output, 'UDP_50_6mps:'
   if x == 32:
      print  >> file_output, 'UDP_100_6mps:'
   if x == 34:
      print  >> file_output, 'UDP_150_6mps:'

def byte_pck_stddev (l, m):
   stddev = 0.0
   n = len(l)

   for yi in l:
      stddev += math.pow((yi - m), 2)
   stddev /= n
   stddev = math.sqrt(stddev)

   return stddev

def print_pck_analysis (total, file_output):

   TCP_encap_length = 0
   UDP_encap_length = 1440

   print  >> file_output,  '\n ---- Packet Analysis ---- \n'
   print  >> file_output,  'All the values of this table are the means of all the ' + str(total) + ' 0experiments.' 

   pck_r_s = [DASH_rcvd_50, DASH_sent_50, DASH_rcvd_100, DASH_sent_100, DASH_rcvd_150, DASH_sent_150, TCP_rcvd_50, TCP_sent_50, TCP_rcvd_100, TCP_sent_100, TCP_rcvd_150, TCP_sent_150, UDP_rcvd_50, UDP_sent_50, UDP_rcvd_100, UDP_sent_100, UDP_rcvd_150, UDP_sent_150, DASH_rcvd_50_2, DASH_sent_50_2, DASH_rcvd_100_2, DASH_sent_100_2, DASH_rcvd_150_2, DASH_sent_150_2, TCP_rcvd_50_2, TCP_sent_50_2, TCP_rcvd_100_2, TCP_sent_100_2, TCP_rcvd_150_2, TCP_sent_150_2, UDP_rcvd_50_2, UDP_sent_50_2, UDP_rcvd_100_2, UDP_sent_100_2, UDP_rcvd_150_2, UDP_sent_150_2, DASH_sp, DASH_sp_2, DASH_sp_100, DASH_sp_100_2,DASH_sp_150,DASH_sp_150_2,TCP_sp,TCP_sp_2,TCP_sp_100,TCP_sp_100_2,TCP_sp_150,TCP_sp_150_2,UDP_sp,UDP_sp_2,UDP_sp_100,UDP_sp_100_2,UDP_sp_150,UDP_sp_150_2]

   n_l_rs = len(pck_r_s)- 18

   avgs = []
   for x in range(0, n_l_rs):
      if x % 2 == 0:
         avg_pck_rate = (pck_r_s[x + 1] - pck_r_s[x]) / pck_r_s[x + 1] * 100
         avg_pck_rate_ideal = (90 - pck_r_s[x] / total) / 90 * 100
         avgs.append(avg_pck_rate)
         avgs.append(avg_pck_rate_ideal)

   for x in range(0, n_l_rs):
      print_name(x, file_output)
      if x % 2 == 0:
         print  >> file_output, 'App Request: ', pck_r_s[x + 1] / total
         print  >> file_output, 'App Received: ', pck_r_s[x] / total
         print  >> file_output, 'Pck Loss Rate: ', str(avgs[x]) + '%'

   D = pck_r_s[n_l_rs:n_l_rs + 6]
   T = pck_r_s[n_l_rs + 6: n_l_rs + 12]
   U = pck_r_s[n_l_rs + 12: n_l_rs + 18]

   all_l_D = [DASH_sp_l, DASH_sp_2_l, DASH_sp_100_l, DASH_sp_100_2_l, DASH_sp_150_l, DASH_sp_150_2_l]
   all_l_T = [TCP_sp_l, TCP_sp_2_l, TCP_sp_100_l, TCP_sp_100_2_l, TCP_sp_150_l, TCP_sp_150_2_l]
   all_l_U = [UDP_sp_l, UDP_sp_2_l, UDP_sp_100_l, UDP_sp_100_2_l, UDP_sp_150_l, UDP_sp_150_2_l]

   for x in range(0,len(D)):
      if x % 2 == 0:
         m1 = (D[x] - TCP_encap_length * pck_r_s[x]) / total
         stddev1 = byte_pck_stddev(all_l_D[x], m1)
         print  >> file_output, 'DASH 3mps'
         print  >> file_output, 'Pck Mean Received Bits: ', m1
         print  >> file_output, 'Stddev: {} \n'.format(stddev1)
      else:
         m2 = (D[x] - TCP_encap_length * pck_r_s[x + 18]) / total
         stddev2 = byte_pck_stddev(all_l_D[x], m2)
         print  >> file_output, 'DASH 6mps'
         print  >> file_output, 'Pck Mean Received Bits: ', m2
         print  >> file_output, 'Stddev: {} \n'.format(stddev2)
   for x in range(0,len(T)):
      if x % 2 == 0:
         m1 = (T[x] - TCP_encap_length * pck_r_s[x + 6]) / total
         stddev1 = byte_pck_stddev(all_l_T[x], m1)
         print  >> file_output, 'TCP 3mps'
         print  >> file_output, 'Pck Mean Received Bits: ', m1
         print  >> file_output, 'Stddev: {} \n'.format(stddev1)
      else:
         m2 = (T[x] - TCP_encap_length * pck_r_s[x + 24]) / total
         stddev2 = byte_pck_stddev(all_l_T[x], m2)
         print  >> file_output, 'TCP 6mps'
         print  >> file_output, 'Pck Mean Received Bits: ', m2
         print  >> file_output, 'Stddev: {} \n'.format(stddev2)
   for x in range(0,len(U)):
      if x % 2 == 0:
         m1 = (U[x] - UDP_encap_length * pck_r_s[x + 12]) / total
         stddev1 = byte_pck_stddev(all_l_U[x], m1)
         print  >> file_output, 'UDP 3mps'
         print  >> file_output, 'Pck Mean Received Bits: ', m1
         print  >> file_output, 'Stddev: {} \n'.format(stddev1)
      else:
         m2 = (U[x] - UDP_encap_length * pck_r_s[x + 30]) / total
         stddev2 = byte_pck_stddev(all_l_U[x], m2)
         print  >> file_output, 'UDP 6mps'
         print  >> file_output, 'Pck Mean Received Bits: ', m2
         print  >> file_output, 'Stddev: {} \n'.format(stddev2)

def main ():
   print ('Starting analysis...')

   index_exp = []
   DASH = []
   TCP = []
   UDP = []
   index = 0

   file_output = open("Output_analysis.txt", "a")

   for root, dirs, files in os.walk(ROOTDIR):
      for name in files:
         m = re.search('(?<=#)[0-9]?[0-9]', name)
         new = int(m.group(0))
         if new > index:
            index = new
         if index not in index_exp:
            index_exp.append(index)
      
      for name in files:
         file_dir = os.path.join(root, name)

         data_1 = []
         data_2 = []
         data_3 = []

         if 'DASH' in name:
            print ('Analysing DASH:')
            print('FILE NAME: ' + name)
            data_1 = get_data(name, file_dir, 'DASH', 'endTo', True)
            data_2 = get_data(name, file_dir, 'DASH', 'bitError', False)
            data_3 = get_data(name, file_dir, 'DASH', 'packetError', False)
            DASH.append([name, data_1, data_2, data_3])
         elif 'TCP' in name:
            print ('Analysing TCP:')
            print('FILE NAME: ' + name)
            data_1 = get_data(name, file_dir, 'TCP', 'endTo', True)
            data_2 = get_data(name, file_dir, 'TCP', 'bitError', False)
            data_3 = get_data(name, file_dir, 'TCP', 'packetError', True)
            TCP.append([name, data_1, data_2, data_3])
         elif 'UDP' in name:
            print ('Analysing UDP:')
            print('FILE NAME: ' + name)
            data_1 = get_data(name, file_dir, 'UDP', 'endTo', True)
            data_2 = get_data(name, file_dir, 'UDP', 'bitError', False)
            data_3 = get_data(name, file_dir, 'UDP', 'packetError', False)
            UDP.append([name, data_1, data_2, data_3])

   print ('Calculating DASH means and stddev...')
   means_stddev_DASH = get_mean_stddev(DASH)
   print ('Calculating TCP means and stddev...')
   means_stddev_TCP = get_mean_stddev(TCP)
   print ('Calculating UDP means and stddev...')
   means_stddev_UDP = get_mean_stddev(UDP)

   vel1 = ',normal(3mps'
   vel2 = ',normal(6mps'

   print ('Calculating DASH histograms...')
   hist_endTo_DASH_3 = get_histogram(DASH, 1, vel1)
   hist_endTo_DASH_6 = get_histogram(DASH, 1, vel2)
   hist_bitError_DASH_3 = get_histogram(DASH, 2, vel1)
   hist_bitError_DASH_6 = get_histogram(DASH, 2, vel2)
   hist_pckError_DASH_3 = get_histogram(DASH, 3, vel1)
   hist_pckError_DASH_6 = get_histogram(DASH, 3, vel2)

   print ('Calculating TCP histograms...')
   hist_endTo_TCP_3 = get_histogram(TCP, 1, vel1)
   hist_endTo_TCP_6 = get_histogram(TCP, 1, vel2)
   hist_bitError_TCP_3 = get_histogram(TCP, 2, vel1)
   hist_bitError_TCP_6 = get_histogram(TCP, 2, vel2)
   hist_pckError_TCP_3 = get_histogram(TCP, 3, vel1)
   hist_pckError_TCP_6 = get_histogram(TCP, 3, vel2)

   print ('Calculating UDP histograms...')
   hist_endTo_UDP_3 = get_histogram(UDP, 1, vel1)
   hist_endTo_UDP_6 = get_histogram(UDP, 1, vel2)
   hist_bitError_UDP_3 = get_histogram(UDP, 2, vel1)
   hist_bitError_UDP_6 = get_histogram(UDP, 2, vel2)
   hist_pckError_UDP_3 = get_histogram(UDP, 3, vel1)
   hist_pckError_UDP_6 = get_histogram(UDP, 3, vel2)


   print ('Printing DASH graphics...')
   save_plot(hist_endTo_DASH_3,'hist_endTo_DASH_3')
   save_plot(hist_endTo_DASH_6,'hist_endTo_DASH_6')
   # save_plot(hist_bitError_DASH_3,'hist_bitError_DASH_3')
   # save_plot(hist_bitError_DASH_6,'hist_bitError_DASH_6')
   # save_plot(hist_pckError_DASH_3,'hist_pckError_DASH_3')
   # save_plot(hist_pckError_DASH_6,'hist_pckError_DASH_6')

   print ('Printing TCP graphics...')
   save_plot(hist_endTo_TCP_3,'hist_endTo_TCP_3')
   save_plot(hist_endTo_TCP_6,'hist_endTo_TCP_6')
   # save_plot(hist_bitError_TCP_3,'hist_bitError_TCP_3')
   # save_plot(hist_bitError_TCP_6,'hist_bitError_TCP_6')
   # save_plot(hist_pckError_TCP_3,'hist_pckError_TCP_3')
   # save_plot(hist_pckError_TCP_6,'hist_pckError_TCP_6')

   print ('Printing UDP graphics...')
   save_plot(hist_endTo_UDP_3,'hist_endTo_UDP_3')
   save_plot(hist_endTo_UDP_6,'hist_endTo_UDP_6')
   # save_plot(hist_bitError_UDP_3,'hist_bitError_UDP_3')
   # save_plot(hist_bitError_UDP_6,'hist_bitError_UDP_6')
   # save_plot(hist_pckError_UDP_3,'hist_pckError_UDP_3')
   # save_plot(hist_pckError_UDP_6,'hist_pckError_UDP_6')

   print_pck_analysis (index + 1, file_output)

   print >> file_output, 'DASH:\n'
   print_endTo_mean(means_stddev_DASH, file_output)
   print >> file_output, 'TCP:\n'
   print_endTo_mean(means_stddev_TCP, file_output)
   print >> file_output, 'UDP:\n'
   print_endTo_mean(means_stddev_UDP, file_output)

   print ('End of analysis.')

if __name__ == '__main__':
   
   main()