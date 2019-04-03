# coding:utf-8
__author__ = 'XingHua'

"""
文件描述
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from glob import glob

all_1 = """
1	-2	0	1	-1	1	-2	3	-3	2	-2	3	-3	1	-1	3	-5	4	-5	4	-1	5	-1	5	-4	6	-3	10	-2	9
-2	-1	-3	0	-4	-3	-4	-1	-4	0	-4	0	-6	3	-3	1	-4	1	-3	2	-4	5	-5	6	-5	3	-3	4	-4	6
-2	-4	-4	-1	-5	-1	-4	-3	-3	-2	-3	2	-6	1	-5	2	-3	1	-7	1	-6	2	-5	4	-6	4	-4	4	-2	6
0	-2	-5	-3	-7	-5	-5	-4	-5	-5	-6	-3	-6	0	-7	0	-8	-4	-8	-2	-9	0	-9	1	-8	1	-5	3	-5	4
-1	-2	-4	-1	-5	-2	-5	-3	-3	-2	-4	0	-7	0	-4	2	-5	-1	-7	0	-7	2	-6	4	-7	2	-4	3	-2	7
"""

all_2 = """
-2	0	-3	0	-3	-2	-5	-2	-4	-1	-2	3	-8	1	-4	2	-5	0	-6	-1	-6	4	-8	4	-6	3	-5	1	-4	5
-12	-10	-13	-10	-13	-11	-15	-12	-13	-10	-11	-6	-17	-8	-13	-8	-13	-9	-14	-10	-15	-5	-16	-5	-14	-6	-14	-8	-12	-4
-20	-19	-22	-19	-21	-21	-24	-21	-23	-20	-21	-16	-26	-18	-22	-17	-23	-19	-24	-19	-24	-14	-26	-15	-24	-16	-23	-18	-22	-23
-30	-29	-32	-29	-30	-31	-33	-31	-31	-30	-30	-26	-35	-28	-31	-27	-32	-29	-32	-29	-33	-23	-34	-25	-33	-26	-32	-27	-31	-23
-41	-38	-43	-38	-42	-40	-44	-40	-42	-39	-40	-35	-46	-37	-42	-36	-43	-38	-43	-39	-43	-33	-44	-34	-43	-35	-42	-38	-41	-33
"""

all_3 = """
-7	-6	-11	-7	-8	-9	-10	-8	-12	-9	-11	-7	-12	-5	-9	-8	-11	-8	-8	-5	-11	-3	-13	-4	-9	-4	-8	-5	-10	-3
-15	-15	-20	-16	-17	-19	-18	-17	-20	-18	-20	-17	-21	-14	-19	-17	-20	-17	-17	-14	-21	-13	-22	-13	-18	-13	-17	-14	-19	-12
"""

all_lunwen = """
-0.08	-0.25	-3.12	-3.3	-19.52	-22.07	-23.76	-23.94	-13.31	-13.26	-12.88	-13.16	-21.25	-23.2	-24.14	-24.31	-27.02	-26.95	-31.79	-31.84	-30.96	-32.31
-0.05	-0.26	-3.22	-3.34	-19.83	-21.86	-23.82	-23.95	-13.3	-13.35	-12.96	-13.23	-21.19	-23.06	-24.22	-24.32	-27.04	-27.05	-32.01	-32.06	-30.91	-32.4
-0.03	-0.2	-3.26	-3.24	-19.54	-22.09	-23.85	-23.91	-13.41	-13.3	-13.1	-13.28	-21.25	-23.44	-24.06	-24.33	-27.02	-27.12	-32.01	-32.04	-30.73	-32.44
-0.13	-0.1	-3.19	-3.38	-19.9	-21.94	-23.87	-23.99	-13.47	-13.55	-13.15	-13.48	-21.18	-23.58	-24.23	-24.41	-27.19	-27.18	-32.06	-32.05	-30.72	-32.74
-0.1	-0.08	-3.17	-3.32	-20	-22.14	-23.83	-23.98	-13.52	-13.45	-13	-13.41	-21.35	-23.49	-24.33	-24.26	-27.17	-27.06	-31.82	-32.13	-31.06	-32.67
"""

all_4 = """
-7	-5	-12	-6	-7	-5	-10	-5	-11	-5	-11	-4	-12	-2	-11	-5	-11	-5	-8	-2	-11	-1	-13	-3	-10	-2	-9	-3	-11	-2
-16	-15	-21	-15	-16	-15	-18	-14	-20	-15	-20	-14	-21	-11	-20	-14	-20	-14	-17	-12	-20	-10	-22	-12	-19	-12	-18	-12	-20	-11
-26	-25	-30	-25	-26	-25	-28	-25	-29	-25	-30	-24	-30	-22	-29	-25	-30	-24	-27	-22	-30	-20	-32	-22	-29	-22	-28	-22	-30	-22
-37	-42	-41	-43	-37	-42	-39	-41	-41	-42	-42	-41	-42	-38	-42	-41	-43	-40	-40	-38	-43	-36	-45	-37	-43	-37	-42	-37	-44	-36
-54	-59	-58	-60	-54	-60	-56	-59	-58	-60	-60	-59	-60	-56	-59	-58	-60	-58	-58	-55	-61	-54	-63	-55	-61	-55	-60	-54	-62	-53
"""
offset_4 = """
-7
-16
-26
-44
-61
"""

all_5 = """
-1	-8	1	-1	-2	-9	-1	-4	-2	-2	-4	-3	-3	0	-1	-2	-4	-2	-7	-4	-4	2	-5	4	-8	-1	-6	1	-4	4
-21	-28	-17	-21	-21	-28	-20	-23	-21	-21	-23	-22	-22	-18	-20	-20	-23	-20	-25	-22	-23	-15	-23	-14	-26	-20	-24	-17	-22	-14
-40	-46	-37	-39	-40	-47	-39	-42	-40	-40	-42	-41	-41	-37	-40	-40	-42	-39	-44	-41	-42	-35	-42	-33	-45	-39	-43	-36	-42	-34
-58	-63	-55	-56	-59	-64	-57	-59	-59	-58	-60	-58	-60	-55	-58	-58	-60	-57	-63	-60	-61	-54	-61	-52	-64	-57	-62	-55	-61	-53
-76	-81	-72	-74	-76	-82	-75	-76	-76	-75	-78	-76	-77	-73	-76	-75	-78	-75	-81	-76	-79	-71	-79	-69	-81	-74	-79	-72	-78	-70
"""

all_6 = """
-9	-20	-10	-20	-10	-23	-10	-22	-13	-18	-15	-19	-14	-17	-13	-19	-16	-19	-15	-18	-17	-15	-18	-15	-16	-16	-15	-12	-16	-12
-28	-41	-31	-41	-30	-43	-30	-43	-33	-40	-36	-40	-34	-38	-35	-40	-38	-40	-36	-38	-38	-35	-39	-36	-37	-37	-36	-33	-37	-33
-49	-61	-52	-61	-50	-63	-51	-62	-54	-59	-56	-59	-55	-58	-55	-60	-58	-60	-56	-58	-58	-55	-59	-56	-57	-57	-56	-54	-57	-53
-68	-79	-71	-79	-69	-81	-69	-81	-72	-77	-74	-77	-73	-76	-73	-78	-77	-78	-75	-76	-76	-74	-78	-74	-75	-75	-74	-72	-75	-71
-86	-98	-89	-98	-88	-100	-88	-99	-91	-96	-93	-96	-93	-95	-93	-97	-97	-97	-94	-96	-96	-93	-97	-94	-95	-95	-94	-92	-95	-91
"""

all_7="""
-10	-16	-13	-18	-12	-18	-11	-16	-15	-15	-17	-15	-17	-14	-17	-17	-20	-17	-19	-14	-19	-12	-22	-15	-19	-13	-18	-11	-18	-10
-28	-34	-31	-36	-30	-36	-29	-35	-33	-34	-36	-34	-35	-33	-36	-35	-39	-35	-38	-32	-37	-30	-40	-33	-37	-31	-36	-30	-37	-28
-46	-51	-50	-54	-49	-54	-48	-52	-52	-51	-54	-51	-54	-50	-54	-53	-57	-54	-57	-51	-56	-49	-59	-52	-56	-51	-55	-48	-55	-47
-64	-71	-68	-73	-67	-73	-65	-71	-70	-70	-72	-70	-72	-69	-72	-72	-76	-73	-75	-70	-74	-67	-77	-70	-74	-69	-73	-67	-73	-65
-83	-90	-87	-92	-86	-92	-84	-91	-89	-90	-91	-90	-91	-89	-91	-91	-95	-92	-93	-89	-93	-86	-96	-90	-92	-87	-92	-86	-92	-84
"""
all_8="""
-5	-12	-8	-14	-6	-13	-7	-14	-8	-10	-9	-8	-11	-10	-9	-10	-12	-11	-15	-9	-14	-6	-12	-6	-12	-7	-11	-4	-10	-1
-5	-12	-8	-14	-6	-13	-7	-14	-8	-10	-9	-8	-11	-10	-9	-10	-12	-11	-15	-9	-14	-6	-12	-6	-12	-7	-11	-4	-10	-1
-5	-12	-8	-14	-6	-13	-7	-14	-8	-10	-9	-8	-11	-10	-9	-10	-12	-11	-15	-9	-14	-6	-12	-6	-12	-7	-11	-4	-10	-1
-5	-12	-8	-14	-6	-13	-7	-14	-8	-10	-9	-8	-11	-10	-9	-10	-12	-11	-15	-9	-14	-6	-12	-6	-12	-7	-11	-4	-10	-1
-5	-12	-8	-14	-6	-13	-7	-14	-8	-10	-9	-8	-11	-10	-9	-10	-12	-11	-15	-9	-14	-6	-12	-6	-12	-7	-11	-4	-10	-1"""

all_9="""
-5	-8	-6	-10	-6	-8	-8	-10	-8	-7	-9	-4	-8	-5	-9	-6	-8	-6	-12	-4	-15	-6	-11	-4	-9	-4	-11	-3	-10	1
-22	-25	-23	-27	-23	-25	-25	-27	-25	-24	-26	-22	-25	-22	-26	-23	-26	-23	-29	-21	-32	-23	-28	-21	-27	-21	-29	-20	-28	-17
-38	-40	-39	-43	-39	-41	-41	-43	-41	-40	-43	-38	-41	-39	-42	-40	-42	-39	-45	-37	-48	-39	-45	-37	-43	-37	-45	-36	-44	-33
-54	-56	-55	-58	-55	-57	-56	-58	-57	-55	-59	-54	-57	-54	-58	-55	-58	-55	-61	-53	-64	-55	-60	-53	-59	-53	-61	-52	-59	-49
-69	-72	-70	-74	-70	-73	-72	-74	-73	-71	-74	-69	-72	-69	-73	-71	-73	-70	-76	-68	-80	-70	-76	-68	-74	-68	-76	-67	-75	-64
"""

all_10="""
-2	21	0	21	3	22	2	23	0	22	2	22	5	21	4	21	5	23	3	22	4	19	6	20	7	19	6	17	5	17	7
10	33	13	32	15	34	14	35	13	34	15	34	17	33	16	33	17	35	16	34	16	30	18	31	19	31	18	29	16	29	19
22	43	24	43	27	44	25	46	24	45	26	45	29	43	28	44	28	46	27	45	27	41	29	42	30	42	29	40	27	40	30
32	55	35	55	38	56	36	57	36	56	37	56	40	55	39	55	40	57	38	56	39	53	41	54	42	54	41	51	39	52	42
44	66	47	66	49	67	48	69	46	68	48	68	51	66	50	67	51	69	50	67	50	64	52	66	53	65	52	63	51	64	53
"""

all_11="""
0 -1	0	-2	-3	-1	-2	-2	2	-5	0	-7	0	-5	-1	-6	0	-5	0	-6	4	-9	2	-8	0	-6	1	-5	3	-9	3	-9
-1 -12	-10	-12	-13	-12	-12	-13	-8	-16	-10	-18	-10	-16	-11	-17	-11	-16	-10	-18	-7	-19	-8	-19	-10	-17	-10	-16	-7	-19	-8	-19
-11 -21	-19	-22	-22	-22	-21	-22	-17	-26	-19	-27	-19	-25	-20	-26	-20	-25	-19	-27	-16	-28	-17	-28	-19	-26	-19	-25	-17	-28	-17	-28
-20 -31	-28	-31	-31	-31	-30	-32	-26	-35	-28	-36	-28	-34	-29	-36	-29	-34	-27	-36	-25	-37	-25	-37	-28	-35	-28	-34	-26	-37	-26	-37
-29 -39	-36	-40	-40	-40	-39	-40	-34	-44	-36	-45	-36	-43	-37	-44	-37	-43	-36	-44	-34	-46	-34	-45	-36	-43	-37	-43	-34	-46	-35	-45
"""

all_12="""
-3	-2	-4	-4	-2	-3	-1	-2	-3	-1	-2	1	-3	2	-4	-2	-2	-1	-5	2	-4	4	-5	0	-4	1	-2	4	-1	3	-2
-9	-9	-10	-11	-8	-10	-7	-9	-9	-7	-9	-5	-9	-5	-10	-9	-9	-8	-11	-5	-10	-3	-11	-7	-10	-6	-8	-3	-7	-3	-7
-16	-15	-17	-18	-15	-16	-14	-16	-15	-14	-15	-12	-16	-11	-17	-15	-16	-15	-17	-11	-17	-9	-18	-13	-16	-12	-15	-10	-14	-10	-15
-23	-22	-24	-25	-22	-24	-21	-23	-22	-21	-23	-20	-23	-19	-24	-23	-23	-22	-25	-18	-25	-17	-23	-20	-23	-19	-22	-17	-21	-17	-23
-30	-30	-31	-32	-30	-31	-28	-30	-30	-28	-30	-25	-30	-26	-31	-29	-30	-29	-31	-25	-31	-24	-31	-27	-31	-27	-30	-24	-28	-24	-30
"""

all_13="""
-2	21	0	21	3	22	2	23	0	22	2	22	5	21	4	21	5	23	3	22	4	19	6	20	7	19	6	17	5	17	7
10	33	13	32	15	34	14	35	13	34	15	34	17	33	16	33	17	35	16	34	16	30	18	31	19	31	18	29	16	29	19
22	43	24	43	27	44	25	46	24	45	26	45	29	43	28	44	28	46	27	45	27	41	29	42	30	42	29	40	27	40	30
32	55	35	55	38	56	36	57	36	56	37	56	40	55	39	55	40	57	38	56	39	53	41	54	42	54	41	51	39	52	42
44	66	47	66	49	67	48	69	46	68	48	68	51	66	50	67	51	69	50	67	50	64	52	66	53	65	52	63	51	64	53
"""

all_14="""
-5	-8	-6	-10	-6	-8	-8	-10	-8	-7	-9	-4	-8	-5	-9	-6	-8	-6	-12	-4	-15	-6	-11	-4	-9	-4	-11	-3	-10	1	-13
-22	-25	-23	-27	-23	-25	-25	-27	-25	-24	-26	-22	-25	-22	-26	-23	-26	-23	-29	-21	-32	-23	-28	-21	-27	-21	-29	-20	-28	-17	-30
-38	-40	-39	-43	-39	-41	-41	-43	-41	-40	-43	-38	-41	-39	-42	-40	-42	-39	-45	-37	-48	-39	-45	-37	-43	-37	-45	-36	-44	-33	-46
-54	-56	-55	-58	-55	-57	-56	-58	-57	-55	-59	-54	-57	-54	-58	-55	-58	-55	-61	-53	-64	-55	-60	-53	-59	-53	-61	-52	-59	-49	-62
-69	-72	-70	-74	-70	-73	-72	-74	-73	-71	-74	-69	-72	-69	-73	-71	-73	-70	-76	-68	-80	-70	-76	-68	-74	-68	-76	-67	-75	-64	-77
"""

all_15="""
-1	5	0	5	1	5	0	8	-1	9	-2	7	1	7	0	8	-1	9	-2	12	0	10	0	10	2	11	5	15	1	15	-1
-5	1	-4	1	-3	0	-4	3	-5	4	-6	3	-3	3	-4	4	-5	5	-6	8	-4	6	-4	6	-2	7	1	11	-3	11	-4
-10	-3	-9	-4	-8	-4	-9	-1	-10	0	-11	-1	-8	-1	-8	0	-9	1	-10	3	-9	2	-8	2	-6	3	-3	7	-6	7	-9
-14	-7	-13	-7	-11	-7	-12	-4	-14	-3	-14	-4	-12	-5	-12	-4	-13	-3	-13	0	-12	-2	-11	-1	-10	0	-7	3	-10	3	-12
-17	-10	-16	-11	-15	-10	-16	-8	-17	-7	-17	-8	-15	-8	-15	-7	-17	-6	-16	-3	-15	-5	-15	-5	-13	-4	-11	0	-13	0	-16
"""

all_16="""
-1	3	-1	3	1	3	2	8	-1	8	-1	7	2	7	1	7	-1	8	-1	11	2	10	2	10	3	13	6	17	4	16
-7	-2	-7	-2	-5	-3	-4	2	-7	2	-7	1	-4	2	-5	1	-8	2	-8	5	-4	4	-5	4	-3	7	-1	10	-3	9
-12	-7	-12	-7	-10	-8	-11	-3	-13	-3	-13	-4	-11	-4	-11	-5	-14	-3	-14	-1	-11	-1	-11	-2	-9	1	-8	4	-9	3
-17	-12	-17	-12	-15	-13	-16	-8	-18	-9	-18	-9	-16	-9	-16	-10	-20	-9	-19	-6	-16	-7	-17	-8	-15	-5	-14	-2	-15	-3
-22	-17	-22	-18	-21	-18	-21	-13	-23	-14	-23	-15	-21	-15	-22	-15	-25	-14	-25	-12	-22	-12	-22	-13	-20	-11	-19	-8	-20	-8
"""

all_17="""
3	7	0	4	1	3	-1	6	-1	8	0	9	-1	4	1	7	-1	9	-2	11	-2	7	-3	6	-2	7	-3	8	-3	10
-3	2	-5	-1	-5	-2	-7	0	-7	3	-6	3	-7	-1	-5	1	-7	3	-8	5	-8	2	-8	0	-8	2	-9	3	-9	4
-8	-4	-11	-7	-10	-8	-12	-5	-12	-3	-11	-2	-13	-7	-10	-4	-13	-3	-13	0	-13	-3	-14	-5	-13	-3	-14	-2	-14	-1
-14	-10	-16	-13	-16	-14	-18	-11	-18	-9	-17	-8	-19	-12	-16	-9	-19	-8	-19	-5	-18	-9	-20	-11	-19	-9	-20	-9	-19	-6
-20	-15	-22	-18	-22	-19	-24	-17	-24	-14	-23	-13	-24	-18	-22	-15	-24	-14	-24	-11	-24	-15	-25	-16	-24	-14	-25	-14	-24	-12
"""

all_axicon="""
4	25	5	21	5	21	12	22	15	22	18	28	17	23	11	22	0	11	3	2	-15	-10
-5	27	-3	23	-2	22	7	24	8	25	10	27	8	25	6	20	-2	4	-5	0	-20	-9
-9	25	-7	20	-7	19	2	21	4	20	6	25	6	21	4	17	-6	4	-10	-5	-20	-14
-7	30	-3	26	-2	25	7	30	7	25	11	29	10	25	8	22	1	10	-3	1	-15	-10
6	43	8	37	11	37	19	36	21	37	22	39	18	31	17	29	8	16	2	-8	-10	-2
"""

all_v1_z1="""
-1	8	-1	9	0	9	1	9	1	9	3	12	5	12	3	12	6	14	5	16	5	18	8	19	9	21	11	21	10	17	
0	7	0	8	0	8	0	8	0	8	2	11	3	11	2	11	5	13	4	15	4	17	7	18	8	20	11	20	9	16	
2	8	1	9	2	9	2	10	2	9	4	12	6	13	5	12	8	14	6	16	7	19	10	20	11	21	13	22	11	18	
2	9	1	10	2	9	2	10	2	9	4	13	5	13	4	12	8	14	6	16	7	19	9	20	10	21	12	21	10	18	
1	8	0	8	1	9	1	10	1	9	3	12	4	13	3	11	6	14	5	16	6	18	8	20	10	20	12	21	10	18	
"""

all_v1_z1_after_bl="""
-3	0	-4	-2	-4	-1	-3	-2	-4	-1	-3	-1	-4	-3	-3	-2	-4	-3	-4	-2	-4	-3	-5	-4	-3	-3	-5	-4	-3	-3
-1	-1	-3	-3	-3	-2	-2	-2	-4	-2	-3	-2	-5	-4	-3	-2	-4	-4	-4	-3	-4	-3	-5	-4	-3	-4	-5	-5	-3	-4
-2	-2	-4	-3	-4	-3	-3	-3	-5	-3	-4	-3	-5	-4	-3	-3	-5	-5	-4	-3	-4	-4	-5	-5	-4	-4	-5	-5	-4	-4
-3	-3	-4	-4	-4	-3	-4	-4	-5	-3	-4	-3	-5	-5	-4	-3	-5	-5	-5	-4	-5	-4	-6	-5	-4	-4	-6	-5	-4	-4
-2	-3	-4	-4	-5	-3	-4	-4	-5	-3	-5	-3	-6	-5	-4	-3	-5	-5	-5	-4	-5	-4	-6	-5	-5	-5	-6	-5	-4	-4
"""
if __name__ == "__main__":
    data_all = np.array(all_v1_z1_after_bl.split(), dtype=float).reshape(5, -1)
    offset = np.array(offset_4.split(), dtype=float).reshape(5, -1)
    for each in range(len(data_all) - 1, 0, -1):
        print each, data_all[each], data_all[each - 1]
        # data_all[each] = data_all[each] - data_all[each - 1]
        # data_all[each] = data_all[each] + 9*each
        # data_all[each] = data_all[each] -offset[each]
        print each, data_all[each], data_all[each - 1]
    # print data_all
    t1 = data_all[0]
    blsize=[]
    for index in range(0, len(data_all)):
        plt.plot(data_all[index][::2], '-o', label="t" + str(index))
        print u"正向误差均值", data_all[index][::2].mean()
        print u"正向误差值", data_all[index][::2]
        plt.plot(data_all[index][1::2], '--o', label="t_b" + str(index))
        print u"反向误差均值", data_all[index][1::2].mean()
        print u"反向误差值", data_all[index][1::2]


        blsize.append(data_all[index][1::2]-data_all[index][::2])
        print u"反向间隙",blsize[index]

        # break
    blsize=np.array(blsize)
    print "all",blsize.shape
    for index in range(blsize.shape[1]):
        print blsize[:,index].mean()*2.971,",",
    plt.legend(loc=0)
    plt.grid()
    plt.show()
    pass
