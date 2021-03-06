import pandas as pd
from scipy.io.arff import loadarff


def data_albrecht():
    raw_data = loadarff("./data/albrecht.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_alb = df_data.drop(columns=['FPAdj', 'RawFPcounts', 'AdjFP'])
    return new_alb


def data_china():
    raw_data = loadarff("./data/china.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_chn = df_data.drop(columns=['ID', 'AFP', 'Added', 'Changed', 'Deleted', 'PDR_AFP', 'PDR_UFP', 'NPDR_AFP'
        , 'NPDU_UFP', 'Dev.Type', 'Duration', 'N_effort'])
    return new_chn


def data_desharnais():
    raw_data = loadarff("./data/desharnais.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_desh = df_data.drop(index=[37, 43, 65, 74],
                            columns=['Project', 'YearEnd', 'Envergure', 'PointsNonAjust', 'Language'])
    columnsTitles = ['TeamExp', 'ManagerExp', 'Length', 'Transactions', 'Entities', 'PointsAdjust', 'Effort']
    new_desh = new_desh.reindex(columns=columnsTitles)
    new_desh = new_desh.drop(columns=['Length'])
    return new_desh


def data_finnish():
    raw_data = loadarff("./data/finnish.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_finn = df_data.drop(columns=['ID'])
    columnsTitles = ['hw', 'at', 'FP', 'co', 'prod', 'lnsize', 'lneff', 'dev.eff.hrs.']
    new_finn = new_finn.reindex(columns=columnsTitles)
    new_finn = new_finn.drop(columns=['prod', 'lnsize', 'lneff'])
    return new_finn


def data_isbsg10():
    raw_data = [
        [1, 1, 1, 1, 1, 1, 1, 225, 1, 1, 1, 1856],
        [1, 1, 1, 1, 1, 2, 1, 599, 2, 1, 2, 10083],
        [1, 1, 1, 2, 1, 2, 1, 333, 2, 1, 3, 5208],
        [1, 1, 2, 3, 2, 3, 1, 748, 2, 2, 3, 1518],
        [1, 1, 1, 1, 1, 4, 1, 158, 1, 1, 4, 3376],
        [1, 1, 1, 1, 1, 2, 1, 427, 2, 1, 3, 5170],
        [2, 2, 3, 4, 3, 5, 1, 461, 2, 3, 4, 12149],
        [1, 1, 4, 3, 2, 3, 1, 257, 1, 2, 3, 452],
        [1, 1, 1, 2, 3, 6, 1, 115, 1, 1, 4, 441],
        [1, 1, 5, 3, 2, 3, 1, 116, 1, 4, 4, 112],
        [1, 1, 1, 2, 1, 7, 1, 323, 2, 1, 3, 1530],
        [1, 1, 1, 2, 1, 1, 1, 134, 1, 1, 3, 1807],
        [1, 1, 1, 2, 1, 14, 1, 292, 1, 1, 3, 1087],
        [2, 2, 4, 4, 1, 8, 1, 399, 2, 3, 3, 7037],
        [1, 1, 1, 1, 1, 2, 1, 44, 3, 1, 4, 784],
        [1, 1, 1, 2, 1, 9, 1, 298, 1, 1, 4, 3268],
        [1, 1, 1, 2, 1, 2, 1, 66, 3, 1, 3, 800],
        [1, 1, 6, 3, 2, 3, 1, 243, 1, 2, 4, 257],
        [1, 1, 1, 4, 1, 10, 1, 1105, 4, 1, 5, 14453],
        [1, 1, 4, 3, 2, 3, 1, 679, 2, 4, 4, 326],
        [2, 2, 7, 5, 1, 4, 1, 303, 2, 3, 4, 8490],
        [1, 1, 1, 2, 1, 1, 1, 147, 1, 1, 3, 672],
        [1, 1, 7, 3, 2, 3, 1, 143, 1, 2, 3, 98],
        [1, 1, 1, 2, 1, 11, 1, 614, 2, 1, 4, 3280],
        [2, 2, 7, 4, 3, 5, 1, 183, 1, 3, 4, 7327],
        [1, 1, 8, 3, 2, 3, 1, 138, 1, 2, 4, 87],
        [1, 1, 1, 2, 3, 12, 1, 129, 1, 1, 3, 1261],
        [1, 1, 1, 2, 1, 2, 1, 205, 1, 1, 3, 3272],
        [1, 1, 1, 2, 1, 1, 1, 471, 2, 1, 3, 1464],
        [1, 1, 1, 5, 1, 4, 1, 97, 3, 1, 3, 1273],
        [1, 1, 3, 3, 2, 3, 1, 1371, 4, 2, 3, 2274],
        [1, 1, 1, 4, 1, 2, 1, 291, 1, 1, 4, 1772],
        [1, 1, 9, 3, 2, 3, 1, 995, 2, 2, 4, 614],
        [1, 2, 4, 2, 3, 6, 2, 211, 1, 3, 4, 1021],
        [2, 2, 10, 2, 3, 13, 2, 192, 1, 3, 4, 1806],
        [2, 2, 10, 2, 3, 13, 2, 98, 3, 3, 4, 921],
        [2, 2, 7, 4, 1, 14, 1, 112, 1, 3, 4, 2134]
    ]
    df_isbsg10 = pd.DataFrame(raw_data, columns=['Data_Quality','UFP','IS','DP','LT','PPL','CA','FS','RS',
                                                 'Recording_Method','FPS','Effort'])
    return df_isbsg10


def data_kemerer():
    raw_data = loadarff("./data/kemerer.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_keme = df_data.drop(columns=['ID', 'Duration', 'KSLOC', 'RAWFP'])
    return new_keme


def data_kitchenham():
    raw_data = [
      [1,1,107,101.65,495,3,485],
      [1,2,144,57.12,1365,1,990],
      [1,2,604,1010.88,8244,3,13635],
      [1,3,226,45.6,1595,2,1576],
      [1,2,326,1022.58,3828,1,3826],
      [1,3,294,77.04,879,3,1079],
      [1,1,212,159.6,2895,3,2224],
      [1,4,175,225.54,1800,1,1698],
      [1,5,584,144.72,1160,3,1173],
      [1,2,171,84.42,885,3,1401],
      [1,2,201,126.42,2125,3,2170],
      [1,2,195,392.16,1381,3,1122],
      [1,6,109,18.9,1142,2,1024],
      [1,3,263,112.14,1895,3,1832],
      [1,1,165,210.08,1339,3,1016],
      [1,2,46,260.95,447,3,322],
      [2,2,186,609.7,507,3,580],
      [2,2,189,169.85,952,3,1003],
      [2,3,95,56,380,3,380],
      [2,3,53,30,220,3,220],
      [2,3,365,241.86,2879,3,2356],
      [2,3,438,219.88,1483,3,1388],
      [2,3,109,229.71,1667,3,1066],
      [2,2,283,458.38,2125,1,2860],
      [2,3,137,177.63,1175,1,1143],
      [2,3,102,287.64,2213,1,1431],
      [2,3,103,343.54,2247,1,1868],
      [2,3,192,346.8,1926,1,2172],
      [2,2,219,1121.48,5641,3,8509],
      [2,3,484,761.08,3928,3,5927],
      [2,3,173,464,1995,1,2663],
      [2,3,169,203.01,2281,3,1425],
      [2,3,207,550.14,3305,3,3504],
      [2,3,61,86.45,797,3,652],
      [2,3,311,1362.11,3922,1,7649],
      [2,3,418,681,6809,1,5927],
      [2,3,410,485.1,4955,1,6607],
      [2,0,497,172.96,1294,3,2591],
      [2,3,259,2075.8,5688,3,4494],
      [2,2,234,756.25,5245,3,4824],
      [2,0,462,789.66,3930,3,5094],
      [2,3,291,357,2562,3,3088],
      [2,3,116,62.08,1526,4,892],
      [2,3,128,157.56,1018,3,750],
      [2,2,185,322.62,5646,4,5646],
      [2,3,207,81.34,1532,3,1532],
      [2,3,151,191,1532,3,1280],
      [2,3,99,121.52,314,3,313],
      [2,3,61,222.78,412,1,339],
      [2,3,101,113.52,738,3,583],
      [2,0,462,15.36,763,3,726],
      [2,3,133,320.12,1750,1,1939],
      [2,3,106,84.28,682,1,669],
      [2,3,68,248.88,1320,3,1413],
      [2,3,239,616.32,3573,3,4115],
      [2,3,330,515.07,2913,1,4009],
      [2,3,37,88.2,701,3,630],
      [2,3,187,115.14,725,1,718],
      [2,3,329,63.84,1826,1,1584],
      [2,3,120,1015.98,5000,3,5816],
      [2,3,85,359.64,2640,1,2037],
      [2,3,49,240.84,2534,1,1428],
      [2,3,152,285.12,2231,1,1252],
      [2,3,47,61.2,1000,3,655],
      [2,0,148,287.28,1645,2,1318],
      [2,2,141,172,1067,3,995],
      [2,2,235,144.06,2270,3,2265],
      [2,2,298,108.64,656,3,654],
      [2,0,99,165.36,121,1,718],
      [2,3,127,680.9,1685,3,2029],
      [2,2,163,409.4,2350,3,1650],
      [2,2,316,313.95,2308,3,2223],
      [2,2,388,1136.34,7850,1,8600],
      [2,3,152,177,2004,3,1884],
      [2,2,166,746.24,3715,5,5359],
      [2,3,114,274.92,1273,1,1159],
      [2,3,82,43.5,437,1,437],
      [2,2,123,54.75,813,3,570],
      [2,3,49,130,900,3,502],
      [2,3,183,525.96,2475,1,1877],
      [2,3,149,311.85,799,1,1693],
      [2,0,370,1185.08,2160,3,3319],
      [2,2,128,258.24,1770,3,1557],
      [2,3,126,60,760,3,557],
      [2,3,200,303.52,2588,1,3050],
      [2,2,76,98.9,1148,1,1113],
      [2,3,299,711.9,4064,3,5456],
      [2,2,131,182.4,933,3,763],
      [2,0,140,351.9,2096,3,2203],
      [2,3,169,401.98,3284,3,3483],
      [2,3,130,162.61,4576,1,2393],
      [2,2,389,1210.99,14226,3,15673],
      [2,2,166,156.42,6080,3,2972],
      [2,3,148,603.58,4046,3,4068],
      [2,3,131,73.92,649,3,698],
      [2,3,144,121.55,817,3,676],
      [2,0,369,1234.2,6340,3,6307],
      [2,3,155,35,300,3,219],
      [2,0,102,61.06,315,3,254],
      [2,3,149,162,750,3,324],
      [2,3,548,1285.7,898,3,874],
      [2,2,946,18137.48,79870,3,113930],
      [2,2,186,1020.6,1600,3,1722],
      [2,2,212,377,1702,3,1660],
      [2,3,84,210.45,592,3,693],
      [2,2,250,410,2158,3,1455],
      [2,2,86,279,994,3,988],
      [2,2,102,240,1875,3,1940],
      [2,3,137,230,2527,3,2408],
      [2,2,87,150.29,2606,3,1737],
      [2,2,291,1940.68,12694,3,12646],
      [2,2,392,401,4176,3,4414],
      [2,2,165,267,2240,3,2480],
      [2,2,88,102,980,3,980],
      [2,2,249,403,3720,3,3189],
      [2,2,186,857,2914,3,2895],
      [2,2,63,69,360,3,322],
      [2,1,192,980.95,3700,3,3555],
      [2,3,123,100.8,200,3,570],
      [2,3,123,105.28,578,3,464],
      [2,2,186,158.4,1652,3,1742],
      [2,2,119,219.88,780,1,896],
      [2,3,195,1292.56,8690,3,8656],
      [2,3,210,616.08,3748,3,3966],
      [2,2,180,103.4,710,3,989],
      [2,3,238,74.4,856,3,585],
      [2,3,144,356.31,2436,3,1860],
      [2,3,432,862,4101,3,5249],
      [2,3,392,791.84,5231,3,5192],
      [2,2,205,661.27,2853,1,1832],
      [2,2,49,179,1246,3,928],
      [3,3,205,518.4,2570,3,2570],
      [3,2,145,370,1328,3,1328],
      [3,2,172,839.05,3380,3,2964],
      [3,3,137,243.86,1522,3,1304],
      [4,2,371,557.28,2264,3,1631],
      [4,4,217,485.94,2790,3,955],
      [4,2,308,698.54,1312,3,286],
      [4,2,217,752.64,2210,1,1432],
      [5,2,40,809.25,337,3,321],
      [6,3,253,178.1,865,3,593],
      [6,3,405,81.48,441,3,302],
      [6,3,241,1093.86,2731,3,2634],
      [6,0,156,1002.76,1039,3,1040],
      [2,2,92,551.88,1393,1,887]
    ]
    df_kitch = pd.DataFrame(raw_data, columns=['code','type','duration','function_points',
                                               'estimate','estimate_method','effort'])
    new_kitch = df_kitch.drop(columns=['duration', 'estimate', 'estimate_method'])
    return new_kitch


def data_maxwell():
    raw_data = loadarff("./data/maxwell.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_maxw = df_data.drop(columns=['Syear', 'Duration', 'Time'])
    return new_maxw


def data_miyazaki():
    raw_data = loadarff("./data/miyazaki94.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_miya = df_data.drop(columns=['ID', 'KLOC'])
    return new_miya


def data_webshop_shoppingsite_v1_final():
    raw_data = loadarff("./data/webshop_shoppingsite_v1_final.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_webshop_shoppingsite_v1_final = df_data.drop(columns=['ID', 'LOC'])
    return new_webshop_shoppingsite_v1_final


def data_webshop_shoppingsite_v1_incre():
    raw_data = loadarff("./data/webshop_shoppingsite_v1_incre.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_webshop_shoppingsite_v1_incre = df_data.drop(columns=['ID', 'LOC'])
    return new_webshop_shoppingsite_v1_incre


def data_webshop_shoppingsite_v1_init():
    raw_data = loadarff("./data/webshop_shoppingsite_v1_init.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_webshop_shoppingsite_v1_init = df_data.drop(columns=['ID', 'LOC'])
    return new_webshop_shoppingsite_v1_init


def data_java_app_final_v1():
    raw_data = loadarff("./data/java_app_final_v1.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_java_app_final_v1 = df_data.drop(columns=['ID', 'LOC'])
    return new_java_app_final_v1


def data_java_app_incre_v1():
    raw_data = loadarff("./data/java_app_incre_v1.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_java_app_incre_v1 = df_data.drop(columns=['ID', 'LOC'])
    return new_java_app_incre_v1


def data_java_app_init_v1():
    raw_data = loadarff("./data/java_app_init_v1.arff")
    df_data = pd.DataFrame(raw_data[0])
    new_java_app_init_v1 = df_data.drop(columns=['ID', 'LOC'])
    return new_java_app_init_v1


def data_cocomo81():
    raw_data = loadarff("./data/cocomo81.arff")
    df_data = pd.DataFrame(raw_data[0])
    df_data = df_data.drop(columns=['loc'])
    return df_data


def data_nasa93():
    raw_data = loadarff("./data/nasa93.arff")
    df_data = pd.DataFrame(raw_data[0]).drop(
        columns=['recordnumber', 'projectname', 'cat2', 'forg', 'center', 'year', 'mode'])
    rely_dict = {b'vl': 0.75, b'l': 0.88, b'n': 1.00, b'h': 1.15, b'vh': 1.40, b'xh': 0}
    data_dict = {b'vl': 0, b'l': 0.94, b'n': 1.00, b'h': 1.08, b'vh': 1.16, b'xh': 0}
    cplx_dict = {b'vl': 0.70, b'l': 0.85, b'n': 1.00, b'h': 1.15, b'vh': 1.30, b'xh': 1.65}
    time_dict = {b'vl': 0, b'l': 0, b'n': 1.00, b'h': 1.11, b'vh': 1.30, b'xh': 1.66}
    stor_dict = {b'vl': 0, b'l': 0, b'n': 1.00, b'h': 1.06, b'vh': 1.21, b'xh': 1.56}
    virt_dict = {b'vl': 0, b'l': 0.87, b'n': 1.00, b'h': 1.15, b'vh': 1.30, b'xh': 0}
    turn_dict = {b'vl': 0, b'l': 0.87, b'n': 1.00, b'h': 1.07, b'vh': 1.15, b'xh': 0}
    acap_dict = {b'vl': 1.46, b'l': 1.19, b'n': 1.00, b'h': 0.86, b'vh': 0.71, b'xh': 0}
    aexp_dict = {b'vl': 1.29, b'l': 1.13, b'n': 1.00, b'h': 0.91, b'vh': 0.82, b'xh': 0}
    pcap_dict = {b'vl': 1.42, b'l': 1.17, b'n': 1.00, b'h': 0.86, b'vh': 0.70, b'xh': 0}
    vexp_dict = {b'vl': 1.21, b'l': 1.10, b'n': 1.00, b'h': 0.90, b'vh': 0, b'xh': 0}
    lexp_dict = {b'vl': 1.14, b'l': 1.07, b'n': 1.00, b'h': 0.95, b'vh': 0, b'xh': 0}
    modp_dict = {b'vl': 1.24, b'l': 1.10, b'n': 1.00, b'h': 0.91, b'vh': 0.82, b'xh': 0}
    tool_dict = {b'vl': 1.24, b'l': 1.10, b'n': 1.00, b'h': 0.91, b'vh': 0.83, b'xh': 0}
    sced_dict = {b'vl': 1.23, b'l': 1.08, b'n': 1.00, b'h': 1.04, b'vh': 1.10, b'xh': 0}
    df_data.rely = df_data.rely.map(lambda i: rely_dict[i])
    df_data.data = df_data.data.map(lambda i: data_dict[i])
    df_data.cplx = df_data.cplx.map(lambda i: cplx_dict[i])
    df_data.time = df_data.time.map(lambda i: time_dict[i])
    df_data.stor = df_data.stor.map(lambda i: stor_dict[i])
    df_data.virt = df_data.virt.map(lambda i: virt_dict[i])
    df_data.turn = df_data.turn.map(lambda i: turn_dict[i])
    df_data.acap = df_data.acap.map(lambda i: acap_dict[i])
    df_data.aexp = df_data.aexp.map(lambda i: aexp_dict[i])
    df_data.pcap = df_data.pcap.map(lambda i: pcap_dict[i])
    df_data.vexp = df_data.vexp.map(lambda i: vexp_dict[i])
    df_data.lexp = df_data.lexp.map(lambda i: lexp_dict[i])
    df_data.modp = df_data.modp.map(lambda i: modp_dict[i])
    df_data.tool = df_data.tool.map(lambda i: tool_dict[i])
    df_data.sced = df_data.sced.map(lambda i: sced_dict[i])
    df_data = df_data.drop(columns=['equivphyskloc'])
    return df_data


def data_cocomo_nasa_1():
    raw_data = loadarff("./data/cocomonasa_v1.arff")
    df_data = pd.DataFrame(raw_data[0])
    RELY_dict = {b'Very_Low': 0.75, b'Low': 0.88, b'Nominal': 1.00, b'High': 1.15, b'Very_High': 1.40, b'Extra_High': 0}
    DATA_dict = {b'Very_Low': 0, b'Low': 0.94, b'Nominal': 1.00, b'High': 1.08, b'Very_High': 1.16, b'Extra_High': 0}
    CPLX_dict = {b'Very_Low': 0.70, b'Low': 0.85, b'Nominal': 1.00, b'High': 1.15, b'Very_High': 1.30,
                 b'Extra_High': 1.65}
    TIME_dict = {b'Very_Low': 0, b'Low': 0, b'Nominal': 1.00, b'High': 1.11, b'Very_High': 1.30, b'Extra_High': 1.66}
    STOR_dict = {b'Very_Low': 0, b'Low': 0, b'Nominal': 1.00, b'High': 1.06, b'Very_High': 1.21, b'Extra_High': 1.56}
    VIRT_dict = {b'Very_Low': 0, b'Low': 0.87, b'Nominal': 1.00, b'High': 1.15, b'Very_High': 1.30, b'Extra_High': 0}
    TURN_dict = {b'Very_Low': 0, b'Low': 0.87, b'Nominal': 1.00, b'High': 1.07, b'Very_High': 1.15, b'Extra_High': 0}
    ACAP_dict = {b'Very_Low': 1.46, b'Low': 1.19, b'Nominal': 1.00, b'High': 0.86, b'Very_High': 0.71, b'Extra_High': 0}
    AEXP_dict = {b'Very_Low': 1.29, b'Low': 1.13, b'Nominal': 1.00, b'High': 0.91, b'Very_High': 0.82, b'Extra_High': 0}
    PCAP_dict = {b'Very_Low': 1.42, b'Low': 1.17, b'Nominal': 1.00, b'High': 0.86, b'Very_High': 0.70, b'Extra_High': 0}
    VEXP_dict = {b'Very_Low': 1.21, b'Low': 1.10, b'Nominal': 1.00, b'High': 0.90, b'Very_High': 0, b'Extra_High': 0}
    LEXP_dict = {b'Very_Low': 1.14, b'Low': 1.07, b'Nominal': 1.00, b'High': 0.95, b'Very_High': 0, b'Extra_High': 0}
    MODP_dict = {b'Very_Low': 1.24, b'Low': 1.10, b'Nominal': 1.00, b'High': 0.91, b'Very_High': 0.82, b'Extra_High': 0}
    TOOL_dict = {b'Very_Low': 1.24, b'Low': 1.10, b'Nominal': 1.00, b'High': 0.91, b'Very_High': 0.83, b'Extra_High': 0}
    SCED_dict = {b'Very_Low': 1.23, b'Low': 1.08, b'Nominal': 1.00, b'High': 1.04, b'Very_High': 1.10, b'Extra_High': 0}
    df_data.RELY = df_data.RELY.map(lambda i: RELY_dict[i])
    df_data.DATA = df_data.DATA.map(lambda i: DATA_dict[i])
    df_data.CPLX = df_data.CPLX.map(lambda i: CPLX_dict[i])
    df_data.TIME = df_data.TIME.map(lambda i: TIME_dict[i])
    df_data.STOR = df_data.STOR.map(lambda i: STOR_dict[i])
    df_data.VIRT = df_data.VIRT.map(lambda i: VIRT_dict[i])
    df_data.TURN = df_data.TURN.map(lambda i: TURN_dict[i])
    df_data.ACAP = df_data.ACAP.map(lambda i: ACAP_dict[i])
    df_data.AEXP = df_data.AEXP.map(lambda i: AEXP_dict[i])
    df_data.PCAP = df_data.PCAP.map(lambda i: PCAP_dict[i])
    df_data.VEXP = df_data.VEXP.map(lambda i: VEXP_dict[i])
    df_data.LEXP = df_data.LEXP.map(lambda i: LEXP_dict[i])
    df_data.MODP = df_data.MODP.map(lambda i: MODP_dict[i])
    df_data.TOOL = df_data.TOOL.map(lambda i: TOOL_dict[i])
    df_data.SCED = df_data.SCED.map(lambda i: SCED_dict[i])
    df_data = df_data.drop(columns=['LOC'])
    return df_data


def latex_print_detail(func):
    s = func.__name__[5:]
    df = func()
    attr_nums = len(df.columns)
    print('\multirow{%d}{*}{\\begin{sideways}%s\\end{sideways}\\begin{sideways}(%d)\\end{sideways}}' % (
    attr_nums, s, df.shape[0]))
    for attr in df.columns:
        name = attr
        m = df[attr].min()
        M = df[attr].max()
        avg = df[attr].mean()
        sd = df[attr].std()
        print("& %s & %.0f & %.0f & %.1f & %.1f\\\\" % (name, m, M, avg, sd))
    print('\\hline')


def latex_print_all_details():
    # latex_print_detail(data_albrecht)
    # latex_print_detail(data_china)
    # latex_print_detail(data_desharnais)
    # latex_print_detail(data_finnish)
    # latex_print_detail(data_isbsg10)
    # latex_print_detail(data_kemerer)
    # latex_print_detail(data_kitchenham)
    # latex_print_detail(data_maxwell)
    # latex_print_detail(data_miyazaki)
    latex_print_detail(data_java_app_init_v1)
    latex_print_detail(data_java_app_incre_v1)
    latex_print_detail(data_java_app_final_v1)
    latex_print_detail(data_webshop_shoppingsite_v1_init)
    latex_print_detail(data_webshop_shoppingsite_v1_incre)
    latex_print_detail(data_webshop_shoppingsite_v1_final)


if __name__ == '__main__':
    # latex_print_all_details()
    # print(data_kitchenham().shape)
    # latex_print_detail(data_albrecht)
    print(data_java_app_init_v1())
