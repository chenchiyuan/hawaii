# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from bs4 import BeautifulSoup
import datetime
import requests
import xmltodict


class City(object):
    cities = {
u'CPH': u'哥本哈根',
u'CKG': u'重庆',
u'WAW': u'华沙',
u'SUX': u'苏城',
u'YUL': u'蒙特利尔',
u'CPT': u'开普敦',
u'AGR': u'阿格拉',
u'AGP': u'马拉加',
u'TAS': u'塔什干（首都）',
u'KWL': u'桂林',
u'TAE': u'大丘',
u'BWI': u'巴尔的摩',
u'TAO': u'青岛',
u'BWN': u'斯里巴加湾市',
u'TAK': u'高松',
u'LHE': u'拉合尔',
u'BTR': u'巴吞鲁日',
u'JIB': u'吉布堤',
u'JIL': u'吉林',
u'LHW': u'兰州',
u'JIU': u'九江',
u'LHR': u'伦敦希思罗',
u'IXR': u'兰契',
u'FIH': u'金沙萨',
u'VAV': u'瓦瓦乌（群岛）',
u'ROR': u'科罗尔',
u'WUS': u'武夷山',
u'LAN': u'兰辛',
u'MAR': u'马拉开波',
u'LAI': u'拉尼翁',
u'SNA': u'圣安娜/拉古纳比奇',
u'LAD': u'罗安达',
u'PQI': u'普雷斯克岛',
u'LAF': u'拉斐特',
u'SIA': u'西安',
u'MAA': u'马德拉斯',
u'JNB': u'约翰内斯堡',
u'OVA': u'瓦加杜古',
u'LAX': u'洛杉矶',
u'MAD': u'马德里',
u'MLG': u'玛琅',
u'MAJ': u'马朱罗',
u'MAO': u'玛瑙斯',
u'MAN': u'曼彻斯特',
u'CRW': u'查尔斯顿',
u'SHP': u'秦皇岛',
u'GUA': u'危地马拉',
u'EVN': u'埃里温',
u'CMH': u'哥伦布（俄亥俄州）',
u'YBP': u'宜宾',
u'ALB': u'奥尔巴尼',
u'TSE': u'阿斯塔纳',
u'CMB': u'科伦坡',
u'BEY': u'贝鲁特',
u'CMX': u'汉考克',
u'BER': u'柏林',
u'BES': u'布雷斯特',
u'DTW': u'底特律',
u'EVV': u'埃文斯维尔',
u'DTT': u'底特律',
u'LSE': u'拉克鲁斯',
u'VLL': u'巴利亚多利德',
u'KBL': u'喀布尔（首都）',
u'VLN': u'瓦伦西亚',
u'VLC': u'瓦伦西亚',
u'SIN': u'新加坡城',
u'GEO': u'乔治敦',
u'WLG': u'惠灵顿',
u'HUZ': u'徽州',
u'IGU': u'伊瓜苏',
u'GRU': u'圣保罗',
u'GRR': u'大急流（密执安州）',
u'BLQ': u'博洛尼亚',
u'BLR': u'班加罗尔',
u'ORF': u'诺福克',
u'DSM': u'德梅因',
u'BLI': u'贝林哈姆',
u'BLA': u'巴塞罗那',
u'MXZ': u'梅县',
u'MMA': u'马尔默',
u'MXP': u'米兰MXP',
u'OKA': u'冲绳',
u'HLN': u'赫勒纳',
u'OKC': u'俄克拉何马城',
u'BNA': u'诺什维尔',
u'LZO': u'泸州',
u'HLH': u'乌兰浩特',
u'IND': u'印第安纳波利斯',
u'NOU': u'努美阿',
u'OKJ': u'冈山',
u'LZD': u'兰州东',
u'CMI': u'尚贝里',
u'INC': u'银川',
u'GLH': u'格林维尔（密西西比州）',
u'BZV': u'布拉柴维尔',
u'DOH': u'多哈',
u'CTS': u'札幌',
u'GLA': u'格拉斯哥',
u'AKU': u'阿克苏',
u'REK': u'雷克雅未克',
u'KOJ': u'鹿儿岛',
u'CTA': u'卡塔尼亚',
u'AKL': u'奥克兰',
u'BZN': u'博兹曼',
u'AKA': u'安康',
u'RIO': u'里约热内卢',
u'MDG': u'牡丹江',
u'BSR': u'巴士拉',
u'SSZ': u'桑托斯',
u'BSL': u'巴塞尔',
u'FCA': u'卡利斯佩尔',
u'LFW': u'洛美',
u'BSD': u'保山',
u'HSV': u'亨茨维尔',
u'YCD': u'纳奈莫',
u'MDW': u'芝加哥（中途机场）',
u'MDT': u'哈利斯堡MDT',
u'FCO': u'罗马FCO',
u'DIG': u'迪庆香格里拉',
u'AUG': u'奥古斯塔',
u'AUH': u'阿布扎比',
u'DFW': u'达拉斯/沃斯堡',
u'YIN': u'伊宁',
u'CZX': u'常州',
u'AUS': u'奥斯汀',
u'MVD': u'蒙得维的亚',
u'JED': u'吉达',
u'ALO': u'滑铁卢',
u'QUT': u'宇都宫',
u'ORY': u'巴黎ORY',
u'ALG': u'阿尔及尔',
u'PUF': u'波（城）',
u'EDI': u'爱丁堡',
u'LMT': u'克拉马斯福尔斯',
u'ALA': u'阿拉木图',
u'JJN': u'泉州晋江',
u'ORL': u'奥兰多',
u'SBA': u'圣巴巴拉',
u'NTL': u'纽卡斯尔',
u'HLD': u'海拉尔',
u'ALV': u'安道尔',
u'ALW': u'瓦拉瓦拉',
u'ORD': u'芝加哥（奥黑尔国际机场）',
u'PUW': u'普尔曼',
u'NTE': u'南特',
u'NTG': u'南通',
u'PUS': u'釜山',
u'BAV': u'包头',
u'CAY': u'卡宴',
u'TOY': u'富山',
u'UKY': u'京都',
u'BAQ': u'巴兰基亚',
u'CAS': u'卡萨布兰卡',
u'KRY': u'克拉玛依',
u'HZG': u'汉中',
u'CAK': u'坎顿',
u'CAI': u'开罗',
u'XIC': u'西昌',
u'CAN': u'广州',
u'TOL': u'托莱多',
u'UKB': u'神户',
u'BAH': u'巴林',
u'IAH': u'休斯顿IAH',
u'PGF': u'佩皮尼昂',
u'HIR': u'霍尼亚拉',
u'VPS': u'埃格林空军基地',
u'YFC': u'弗雷德里克顿',
u'DYU': u'杜尚别（首都）',
u'BAK': u'巴库',
u'HIB': u'西宾/奇瑟姆',
u'NHV': u'努库希瓦（岛）',
u'KOW': u'赣州',
u'IAD': u'华盛顿（杜累斯机场）',
u'ERI': u'伊利',
u'HIJ': u'广岛',
u'DYG': u'张家界',
u'HIN': u'晋州',
u'WEH': u'威海',
u'ABE': u'阿伦敦/伯利恒/伊斯顿',
u'STC': u'圣克劳德',
u'STL': u'圣路易斯',
u'ABJ': u'阿比让',
u'STO': u'斯德哥尔摩',
u'KNC': u'吉安',
u'KTM': u'加德满都',
u'ABR': u'阿伯丁',
u'ABV': u'阿布贾',
u'ABX': u'奥尔伯尼',
u'SBN': u'南本德',
u'ABZ': u'阿伯丁',
u'SSG': u'马拉博',
u'ZRH': u'苏黎世',
u'NCY': u'阿内西',
u'BHM': u'伯明翰',
u'PNQ': u'浦那',
u'PNS': u'彭萨科拉',
u'CFE': u'克莱蒙费朗',
u'BHY': u'北海',
u'PNH': u'金边',
u'NCL': u'纽卡斯尔',
u'RST': u'罗切斯特（明尼苏达州）',
u'NCE': u'尼斯',
u'JFK': u'纽约（肯尼迪机场）',
u'LIG': u'里摩日',
u'DKR': u'达喀尔',
u'MIL': u'米兰',
u'MIA': u'迈阿密',
u'LIM': u'利马',
u'VFA': u'维多利亚瀑布',
u'LIT': u'小石城',
u'FNA': u'弗里敦',
u'LIS': u'里斯本',
u'GHN': u'广汉',
u'FNJ': u'平壤',
u'AOG': u'鞍山',
u'PRG': u'布拉格',
u'SAH': u'萨那',
u'SAO': u'圣保罗',
u'SAN': u'圣迭戈',
u'LBV': u'利伯维尔',
u'SAC': u'萨克拉门托SAC',
u'RAI': u'普腊亚',
u'LBA': u'利兹',
u'HAV': u'哈瓦那',
u'RAP': u'拉皮德城',
u'PRY': u'比勒陀利亚',
u'LUZ': u'庐山',
u'SAT': u'圣安敦',
u'CHA': u'查塔努加',
u'CHC': u'基督城',
u'MRY': u'卡迈尔/蒙特雷',
u'BFE': u'比勒费尔德',
u'CHG': u'朝阳',
u'MRU': u'毛里求斯',
u'MRS': u'马赛',
u'BFS': u'贝尔法斯特',
u'LPL': u'利物浦',
u'XUZ': u'徐州',
u'BFU': u'蚌埠',
u'CHW': u'酒泉',
u'HRE': u'哈拉雷',
u'HRB': u'哈尔滨',
u'TYL': u'塔拉拉',
u'TYN': u'太原',
u'TYO': u'东京（TYO）',
u'VIE': u'维也纳',
u'IPH': u'怡保',
u'SYD': u'悉尼',
u'JDZ': u'景德镇',
u'KAN': u'卡诺',
u'RHI': u'莱茵兰德',
u'SFO': u'旧金山（三藩市）',
u'LNK': u'林肯',
u'ONT': u'安大略',
u'ZAG': u'萨格勒布',
u'DBQ': u'迪比克',
u'VIX': u'维多利亚',
u'REC': u'累西腓',
u'TYS': u'诺克斯维尔',
u'YSJ': u'圣约翰',
u'NGA': u'那格浦尔',
u'NGB': u'宁波',
u'NGO': u'名古屋',
u'FUG': u'阜阳',
u'HDD': u'海德拉巴',
u'SYM': u'思茅',
u'NGS': u'长崎',
u'FUN': u'富纳富蒂',
u'FUO': u'佛山',
u'FUK': u'福冈',
u'OVB': u'新西伯利亚',
u'CEB': u'宿务',
u'SYR': u'锡拉丘兹',
u'RTM': u'鹿特丹',
u'BMI': u'布卢明顿.诺木尔',
u'SZG': u'萨尔茨堡',
u'SZD': u'设菲尔德',
u'SZZ': u'什切青',
u'SZX': u'深圳',
u'PVG': u'上海浦东',
u'HMI': u'哈密',
u'JNG': u'济宁',
u'IDA': u'爱达荷福尔斯',
u'DLC': u'大连',
u'DLA': u'杜阿拉',
u'SHS': u'沙市',
u'SHV': u'什里夫波特',
u'ENH': u'恩施',
u'CSG': u'哥伦布（佐治亚州）',
u'DLH': u'德卢斯',
u'SHA': u'上海虹桥',
u'CID': u'锡达拉皮兹',
u'CSX': u'长沙',
u'DLU': u'大理',
u'RFD': u'罗克福德',
u'ENY': u'延安',
u'SHJ': u'沙迦',
u'OXB': u'比绍',
u'MGA': u'马那瓜',
u'BTV': u'伯林顿',
u'TEN': u'铜仁',
u'BTS': u'布拉迪斯拉发',
u'ABQ': u'阿尔布凯克',
u'TBS': u'笫比利斯',
u'MIG': u'绵阳',
u'MGM': u'蒙哥马利',
u'BTZ': u'布尔萨',
u'SSE': u'绍拉布尔',
u'GZT': u'加济安泰普',
u'LAS': u'拉斯维加斯',
u'SSA': u'萨尔瓦多',
u'TSN': u'天津',
u'STR': u'斯图加特',
u'BBR': u'巴斯特尔',
u'LUX': u'卢森堡',
u'ATL': u'亚特兰大',
u'ISP': u'艾斯利普',
u'MUX': u'木尔坦',
u'ATH': u'雅典',
u'IST': u'伊斯坦布尔',
u'YHZ': u'哈里法克斯',
u'ATW': u'阿普尔顿',
u'MUC': u'慕尼黑',
u'LUH': u'卢迪亚纳',
u'ISB': u'伊斯兰堡',
u'LUL': u'苏雷尔',
u'LUM': u'德宏芒市',
u'LUN': u'卢萨卡',
u'ATY': u'沃特敦',
u'DTM': u'多特蒙德',
u'ASU': u'亚松森',
u'LNZ': u'林茨',
u'JKT': u'雅加达JKT',
u'ASB': u'阿什哈巴德',
u'NUK': u'努库塔瓦克（岛）',
u'SEA': u'西雅图',
u'ASK': u'亚穆苏克罗',
u'ASI': u'乔治敦',
u'NUE': u'纽伦堡',
u'ASM': u'阿斯马拉',
u'PVD': u'普罗维登斯',
u'TLS': u'图卢兹',
u'DUI': u'杜伊斯堡',
u'FRA': u'法兰克福',
u'CLO': u'卡利',
u'VTE': u'万象',
u'QFY': u'福山',
u'GTF': u'格雷特瀑布（旅游境区）',
u'PDX': u'波特兰',
u'CLE': u'克利夫兰',
u'EUG': u'尤金',
u'PDT': u'彭德尔顿',
u'CIH': u'长治',
u'BEG': u'贝尔格莱德',
u'YAO': u'雅温得',
u'CLY': u'卡勒威',
u'FRU': u'比什凯克',
u'PDG': u'巴东',
u'DUS': u'杜塞尔多夫',
u'TLN': u'土伦',
u'TLL': u'塔林',
u'OMA': u'奥马哈',
u'KEL': u'基尔',
u'TUP': u'图珀洛',
u'TUS': u'图森',
u'TUL': u'塔尔萨',
u'TUN': u'突尼斯',
u'WNZ': u'温州',
u'HGH': u'杭州',
u'CLM': u'安吉利斯港',
u'SWA': u'汕头',
u'TPA': u'坦帕',
u'AAT': u'阿勒泰',
u'TLV': u'特拉维夫',
u'BIO': u'毕尔巴鄂',
u'BIL': u'比林斯',
u'KWE': u'贵阳',
u'CNI': u'长海',
u'BHX': u'伯明翰',
u'KWI': u'科威特',
u'POS': u'西班牙港（首都）/特利尼达',
u'BIA': u'巴斯蒂亚',
u'POM': u'莫尔兹比港',
u'FYV': u'费耶特维尔',
u'PHL': u'费城',
u'BIS': u'俾斯麦',
u'BEL': u'贝伦',
u'BIQ': u'贝阿里兹',
u'DHN': u'多森',
u'MLA': u'马耳他（岛）',
u'VCE': u'威尼斯',
u'MLE': u'马累',
u'MLH': u'米卢斯',
u'MLI': u'莫林',
u'GOA': u'热那亚',
u'IZM': u'伊滋密尔',
u'LZH': u'柳州',
u'MLW': u'蒙罗维亚',
u'MLU': u'门罗',
u'CWA': u'莫西尼',
u'GOT': u'哥德堡',
u'CWB': u'库里蒂巴',
u'GOQ': u'格尔木',
u'RBA': u'拉巴特',
u'SLC': u'盐湖城',
u'OTH': u'北本德',
u'MCM': u'蒙特卡洛',
u'MCI': u'堪萨斯城',
u'LGA': u'纽约（拉瓜迪亚机场）',
u'GTR': u'哥伦布（密西西比州）',
u'GFK': u'大福克斯',
u'ARN': u'斯德哥尔摩ARN',
u'MCW': u'梅森城',
u'MCT': u'马斯喀特',
u'LGW': u'伦敦LGW',
u'NRT': u'东京（成田机场）',
u'PAP': u'太子港',
u'YLW': u'基洛纳',
u'PAR': u'巴黎',
u'PAT': u'巴特那',
u'BGF': u'班吉',
u'BGI': u'布里奇顿',
u'BGM': u'宾汉顿/恩迪科特/约翰逊城',
u'CLT': u'夏洛特',
u'BGR': u'班戈',
u'FNT': u'弗林特',
u'BGW': u'巴格达',
u'PAH': u'啪迪尤卡',
u'CKY': u'科纳克里',
u'LIA': u'梁平',
u'RIX': u'里加',
u'VNO': u'维尔纽斯',
u'HSN': u'舟山',
u'BTM': u'比尤特',
u'DCA': u'华盛顿（里根国家机场）',
u'WDH': u'温得和克',
u'MQS': u'摩加迪沙',
u'VNS': u'瓦拉纳西',
u'MQT': u'马凯特',
u'RIC': u'里士满',
u'HAJ': u'汉诺威',
u'HAK': u'海口',
u'HAM': u'汉堡',
u'HAN': u'河内',
u'BNS': u'巴里纳斯',
u'NAN': u'楠迪',
u'NNY': u'南阳',
u'XIL': u'锡林浩特',
u'THR': u'德黑兰',
u'XIN': u'兴宁',
u'FWA': u'韦恩堡',
u'BNJ': u'波恩',
u'SLE': u'塞勒姆',
u'CCS': u'加拉加斯',
u'GPZ': u'大急流（明尼苏达州）',
u'JNZ': u'锦州',
u'GPT': u'格尔夫波特',
u'XIY': u'西安咸阳机场',
u'HAR': u'哈利斯堡HAR',
u'KNU': u'坎普尔',
u'BNE': u'布里斯班',
u'XNN': u'西宁',
u'KIX': u'大阪（KIX）',
u'NIM': u'尼亚美',
u'NIC': u'尼科西亚',
u'QJC': u'廷布',
u'KIV': u'基希纳乌（首都）/基什尼奥夫',
u'YEG': u'埃德蒙顿',
u'KIJ': u'新泻',
u'PHX': u'菲尼克斯（凤凰城）',
u'DDG': u'丹东',
u'KIN': u'金斯敦',
u'LXA': u'拉萨',
u'ZAT': u'昭通',
u'SYX': u'三亚',
u'LEJ': u'莱比锡',
u'LXI': u'林西',
u'GBE': u'哈博罗内',
u'SKP': u'斯科普里',
u'MEI': u'默里迪恩',
u'XEN': u'兴城',
u'RGN': u'仰光',
u'BUH': u'布加勒斯特',
u'GEG': u'斯波坎',
u'JUZ': u'衢州',
u'BUF': u'布法罗',
u'BUD': u'布达佩斯',
u'BUE': u'布宜诺斯艾利斯',
u'YKA': u'坎卢普斯',
u'BRI': u'巴里',
u'JGN': u'嘉峪关',
u'YKM': u'亚基马',
u'FOD': u'道奇堡',
u'LJG': u'丽江',
u'FOC': u'福州',
u'MHT': u'曼彻斯特',
u'LJU': u'卢布尔雅那',
u'RNO': u'里诺',
u'ANC': u'安克雷奇',
u'PSC': u'帕斯科',
u'SAL': u'圣萨尔瓦多',
u'MOW': u'莫斯科',
u'ANK': u'安卡拉',
u'LCA': u'拉那卡',
u'RNS': u'雷恩',
u'GRB': u'格林贝',
u'PSP': u'棕榈泉',
u'OPO': u'波尔图',
u'KMG': u'昆明',
u'DVO': u'达沃',
u'TMS': u'圣多美',
u'FSD': u'苏福尔斯',
u'HND': u'东京（羽田机场）',
u'ETZ': u'梅兹南希',
u'PEW': u'白沙瓦',
u'HNL': u'夏威夷（檀香山）',
u'PER': u'珀斯',
u'PEN': u'槟城',
u'UIO': u'基多',
u'PEK': u'北京首都机场',
u'HNY': u'衡阳',
u'BCV': u'贝尔莫潘',
u'COO': u'科托努',
u'KDH': u'坎大哈',
u'YNJ': u'延吉',
u'KHI': u'卡拉奇',
u'MXL': u'墨西卡利',
u'AZO': u'卡拉马祖',
u'LWS': u'刘易斯顿',
u'TVF': u'锡夫里弗福尔斯',
u'TVC': u'特拉弗斯',
u'XMM': u'摩纳哥',
u'XMN': u'厦门',
u'NDJ': u'恩贾梅纳',
u'SRG': u'三宝垄',
u'SRE': u'苏克雷',
u'KRT': u'喀土穆',
u'IEV': u'基辅',
u'KRL': u'库尔勒',
u'HEL': u'赫尔辛基',
u'HEI': u'呼和浩特',
u'HEK': u'黑河',
u'YYT': u'圣约翰斯',
u'RUH': u'利雅得',
u'CDG': u'巴黎戴高乐',
u'BJM': u'布琼布拉',
u'BJL': u'班珠尔',
u'INL': u'国际瀑布',
u'BJI': u'伯米吉',
u'YYZ': u'多伦多',
u'YYG': u'温尼伯',
u'IQN': u'庆阳',
u'BJS': u'北京',
u'YYC': u'卡尔加里',
u'INU': u'瑙鲁岛',
u'PLN': u'佩尔斯顿',
u'YYJ': u'维多利亚',
u'DIL': u'帝力',
u'HYA': u'海恩尼斯',
u'MKE': u'密尔沃基',
u'JHB': u'新仙（柔佛巴鲁）',
u'MKC': u'堪萨斯城',
u'JHG': u'西双版纳',
u'MKL': u'杰克逊（田纳西州）',
u'LON': u'伦敦',
u'HYN': u'黄岩',
u'GNB': u'格勒诺布尔',
u'LOS': u'拉各斯',
u'SHE': u'沈阳',
u'AYN': u'安阳',
u'CVG': u'辛辛那提',
u'MOT': u'迈诺特',
u'MKZ': u'马六甲',
u'CBR': u'堪培拉',
u'PPG': u'帕果帕果',
u'JAX': u'杰克逊维尔',
u'SOF': u'索非亚',
u'FAR': u'法戈',
u'URC': u'乌鲁木齐',
u'MBA': u'蒙巴萨',
u'FAT': u'弗雷斯诺',
u'OWB': u'欧文斯伯勒',
u'SOU': u'南安普敦',
u'PPT': u'帕皮提',
u'MBS': u'贝城/米德兰/萨吉诺',
u'MTY': u'蒙特雷',
u'YOK': u'横滨',
u'HPN': u'韦斯特切斯特',
u'MOB': u'莫比尔',
u'YOW': u'渥太华',
u'WXN': u'万州',
u'BFL': u'贝克斯菲尔德',
u'HBA': u'霍巴特',
u'JAN': u'杰克逊（密西西比州）',
u'ZHA': u'湛江',
u'JLN': u'乔普林',
u'SDQ': u'圣多明各',
u'TGU': u'特古西加尔巴',
u'SDF': u'路易斯维尔',
u'PWM': u'波特兰（缅因州）',
u'NAO': u'南充',
u'SDJ': u'仙台',
u'GSP': u'格林维尔（南卡罗莱纳州）',
u'CTU': u'成都',
u'CCU': u'加尔格达',
u'DRS': u'德雷斯顿',
u'BOS': u'波士顿',
u'TIP': u'的梨波里',
u'BCN': u'巴塞罗那',
u'DRW': u'达尔文',
u'ZYI': u'遵义',
u'BOI': u'博伊西',
u'NAP': u'那不勒斯',
u'BOM': u'孟买',
u'TIJ': u'蒂华纳',
u'BOD': u'波尔多',
u'TIA': u'地拉那',
u'CCC': u'潮州',
u'BOG': u'圣菲波哥大',
u'PIH': u'波卡特洛',
u'SXB': u'施特拉斯堡',
u'LYP': u'费萨拉巴德',
u'LYS': u'里昂',
u'NNG': u'南宁',
u'PIA': u'皮奥里亚',
u'PIB': u'苏雷尔',
u'HKT': u'普吉',
u'UIP': u'坎佩尔',
u'LYG': u'连云港',
u'LYA': u'洛阳',
u'KHN': u'南昌',
u'PIR': u'皮尔',
u'PIT': u'匹兹堡',
u'LYI': u'临沂',
u'HKD': u'函馆',
u'KHG': u'喀什',
u'SVO': u'莫斯科SVO',
u'YVR': u'温哥华',
u'MCZ': u'马塞约',
u'FSM': u'史密斯堡',
u'YVA': u'莫罗尼',
u'SVQ': u'塞维莱',
u'UBS': u'哥伦布（密西西比州）',
u'DAX': u'达县',
u'SFY': u'斯普林菲尔德（马萨诸塞州）',
u'DAY': u'戴顿',
u'MKG': u'马斯基根',
u'CTG': u'卡塔赫纳',
u'NAS': u'拿骚',
u'LKO': u'勒克瑙',
u'TGO': u'通辽',
u'FLR': u'佛罗伦萨',
u'APW': u'阿皮亚',
u'DEL': u'新德里',
u'FLL': u'劳德尔堡',
u'DEN': u'丹佛',
u'SMF': u'萨克拉门托SMF',
u'MWH': u'摩塞斯莱克',
u'TNA': u'济南',
u'CNS': u'凯恩斯',
u'SCL': u'圣地亚哥',
u'AMM': u'安曼',
u'ROM': u'罗马',
u'SCE': u'斯泰特科利奇',
u'ROA': u'罗阿诺克',
u'ROC': u'罗切斯特（纽约州）',
u'LLW': u'利隆圭',
u'JMU': u'佳木斯',
u'ROX': u'罗索',
u'WUH': u'武汉',
u'MNL': u'马尼拉',
u'OSL': u'奥斯陆',
u'PTY': u'巴拿马城',
u'OSA': u'大阪（OSA）',
u'QVU': u'瓦杜兹',
u'AMS': u'阿姆斯特丹',
u'TRI': u'布里斯托尔/特里—思蒂',
u'TRN': u'都灵',
u'BDL': u'哈特福德BDL',
u'BDO': u'万隆',
u'YCU': u'运城',
u'PBM': u'帕拉马里博',
u'EWR': u'纽瓦克',
u'PBI': u'西棕榈滩',
u'SFD': u'圣费尔南多.阿佩尔',
u'TRW': u'塔拉瓦',
u'CJU': u'济州',
u'AIY': u'大西洋城',
u'KCA': u'库车',
u'HTN': u'和田',
u'MPL': u'蒙彼利埃',
u'MPM': u'马普托',
u'AVN': u'阿维尼瓮',
u'HTS': u'阿什兰',
u'LRT': u'洛里昂',
u'ESC': u'埃斯卡纳巴',
u'UYN': u'榆林',
u'CWL': u'加的夫',
u'ACC': u'阿克拉',
u'ACA': u'阿卡普尔科',
u'SUB': u'泗水',
u'ACK': u'楠塔基特',
u'SUN': u'哈伊利/森瓦利',
u'YQG': u'温莎',
u'YQB': u'魁北克',
u'SUW': u'苏必利尔',
u'SUV': u'苏瓦',
u'KUL': u'吉隆坡',
u'AJA': u'阿雅克修',
u'YQT': u'桑德贝',
u'ZUH': u'珠海',
u'HFE': u'合肥',
u'HFD': u'哈特福德HFD',
u'YQR': u'里贾纳',
u'CGK': u'雅加达CGK',
u'CGO': u'郑州',
u'CGN': u'科隆',
u'YXS': u'乔治王子城',
u'BKO': u'巴马科',
u'YXV': u'伦敦',
u'CGD': u'常德',
u'BKK': u'曼谷',
u'NBO': u'内罗毕',
u'QMN': u'母巴巴内',
u'CGQ': u'长春',
u'PMO': u'巴勒莫',
u'WEF': u'潍坊',
u'YXE': u'萨斯卡通',
u'RDU': u'罗利',
u'MCO': u'奥兰多',
u'SEL/ICN': u'汉城/仁川',
u'DNH': u'敦煌',
u'RDZ': u'罗德兹',
u'SJJ': u'萨拉热窝',
u'ADD': u'亚的斯亚贝巴',
u'ADE': u'亚丁',
u'SJO': u'圣何塞',
u'ADA': u'阿达纳',
u'RDM': u'雷德蒙德',
u'SJC': u'圣何塞',
u'ADL': u'阿德莱德',
u'XFN': u'襄樊',
u'LEB': u'汉诺威/莱巴嫩',
u'LED': u'彼德堡',
u'MEM': u'孟菲斯',
u'MEL': u'墨尔本',
u'BRU': u'布鲁塞尔',
u'BRS': u'布里斯托尔',
u'LEN': u'来昂',
u'BRN': u'伯尔尼',
u'BRM': u'巴基西梅托',
u'JRS': u'耶路撒冷',
u'BSB': u'巴西利亚（首都）',
u'MES': u'棉兰',
u'LEX': u'列克星敦',
u'BRE': u'不来梅',
u'BRD': u'布雷纳德',
u'GDL': u'瓜达拉哈拉',
u'MEX': u'墨西哥城',
u'TWF': u'特温福尔斯',
u'CIF': u'赤峰',
u'MSY': u'新奥尔良',
u'MFR': u'梅德福',
u'USN': u'蔚山',
u'MSU': u'马塞卢',
u'YNG': u'扬斯敦',
u'MSQ': u'明斯克',
u'MSP': u'明尼阿波利斯',
u'MSO': u'米苏拉',
u'MSN': u'麦迪逊',
u'MSL': u'佛罗伦萨/设菲尔德',
u'ZHD': u'中甸',
u'YNT': u'烟台',
u'PFN': u'巴拿马城',
u'TXN': u'黄山',
u'CHI': u'芝加哥',
u'DAC': u'达卡',
u'DAM': u'大马士革',
u'DAT': u'大同',
u'AQG': u'安庆',
u'PXO': u'圣港',
u'DAR': u'达累斯萨拉姆',
u'SGN': u'胡志明市',
u'EAU': u'欧克莱尔',
u'EAT': u'文纳奇',
u'SGF': u'斯普林菲尔德（密苏里州）',
u'ESS': u'埃森',
u'KLA': u'坎帕拉',
u'TNR': u'塔那那利佛',
u'GVA': u'日内瓦',
u'YIH': u'宜昌',
u'ESF': u'亚历山大',
u'HOU': u'休斯顿HOU',
u'ULN': u'乌兰巴托',
u'NDG': u'齐齐哈尔',
u'ICT': u'威奇塔 福尔斯',
u'NKC': u'努瓦克肖特',
u'NKG': u'南京',
u'OOL': u'黄金海岸',
u'YIW': u'义乌',
u'DXB': u'迪拜',
u'HHA': u'长沙/黄花',
u'EZE': u'布宜诺斯艾利斯',
u'KGL': u'基加利',
    }

    @classmethod
    def get_name(cls, three):
        return cls.cities.get(three, three)


class Company(object):
    companies = {
u'DL': u'三角航空',
u'ZH': u'深圳航空',
u'BA': u'英国航空',
u'CI': u'中华航空',
u'3U': u'四川航空',
u'HU': u'海南航空',
u'JL': u'日本航空',
u'BR': u'长荣航空',
u'FI': u'冰岛航空',
u'FK': u'阿联酋航空',
u'FM': u'上海航空',
u'NH': u'全日空航空',
u'SK': u'北欧航空',
u'IB': u'西班雅航空',
u'6U': u'乌克兰航空',
u'LO': u'波兰航空',
u'LH': u'汉莎航空',
u'NZ': u'新西兰航空',
u'RG': u'巴西航空',
u'TK': u'土耳其航空',
u'PK': u'巴基斯坦航空',
u'UM': u'津巴布韦航空',
u'LY': u'以色列空',
u'AA': u'美国航空',
u'PR': u'菲律宾航空',
u'AC': u'加拿大航空',
u'CO': u'大陆航空',
u'KU': u'科威特航空',
u'AF': u'法国航空',
u'AI': u'印度航空',
u'CA': u'中国国际航空',
u'OM': u'蒙古航空',
u'VN': u'越南航空',
u'BI': u'汶莱航空',
u'CZ': u'中国南方航空',
u'GE': u'台湾复兴航空',
u'CX': u'国泰航空',
u'QR': u'卡塔尔航空',
u'GA': u'嘉鲁达印度尼西亚航空',
u'TG': u'泰国航空',
u'AY': u'芬兰航空',
u'ET': u'埃塞阿比亚航空',
u'AZ': u'意大利航空',
u'KA': u'港龙航空',
u'MF': u'厦门航空',
u'MA': u'匈牙利航空',
u'UX': u'西班牙欧洲航空',
u'KE': u'大韩航空',
u'GF': u'海湾航空',
u'JS': u'朝鲜航空',
u'UA': u'美国联合航空',
u'SQ': u'新加坡航空',
u'MH': u'马来西亚航空',
u'OA': u'希腊奥林匹克航空',
u'KL': u'荷兰航空',
u'MU': u'中国东方航空',
u'UL': u'斯里兰卡航空',
u'VS': u'维珍航空',
u'OZ': u'韩亚航空',
u'MS': u'埃及航空',
u'QF': u'澳洲航空',
u'SC': u'山东航空',
u'SA': u'南非航空',
u'NW': u'美国西北航空',
u'OS': u'毛利航空',
u'SU': u'俄罗斯航空',
u'HX': u'香港航空',
}
    @classmethod
    def get_name(cls, three):
        return cls.companies.get(three, three)


class Route(object):
    def __init__(self, company_three, starting, destination, price, tax, limit_no, data, turn=0, flights=[]):
        self.company_three = company_three
        self.company = Company.get_name(company_three)
        self.starting = starting
        self.destination = destination
        self.departure = flights[0].departure
        self.arrival = flights[-1].arrival
        self.price = price
        self.tax = tax
        self.flights = flights
        self.turn = turn
        self.limit_no = limit_no
        self.limits = []
        self.data = data

    @classmethod
    def search(cls, starting, destination, departure, back_time="", seat_type="Y", **kwargs):
        base_url = "http://intf.fare2go.com/tukeq.php"
        params = {
            "fromCity": starting,
            "toCity": destination,
            "fromDate": departure,
            "seatType": seat_type
        }
        if back_time:
            params['returnDate'] = back_time

        url = base_url + "?" + "&".join(map(lambda item: "%s=%s" % (item[0], item[1]), params.items()))
        content = requests.get(url).content
        return cls.parse_xml(content)

    def to_json(self):
        turn = self.turn
        if not int(turn):
            turn = u"直飞"
        else:
            turn = unicode(turn)
        return {
            "company": self.company,
            "company_three": self.company_three,
            "turn": turn,
            "starting": self.starting,
            "destination": self.destination,
            "departure": self.departure,
            "arrival": self.arrival,
            "price": self.price,
            "tax": self.tax,
            "flights": map(lambda flight: flight.to_json(), self.flights),
            "limit_no": self.limit_no,
            "data": self.data
        }

    @classmethod
    def parse_xml(cls, content):
        soup = BeautifulSoup(content)
        datas = xmltodict.parse(content)

        routes = soup.find_all("r")
        result_routes = []
        for index, route in enumerate(routes):
            route_segments = route.find_all("s")
            price = route.find("pm").text
            tax = route.find("x").text
            route_starting = City.get_name(route.find("f").text)
            route_destination = City.get_name(route.find("t").text)
            route_company_three = route.find("a").text
            route_limit = route.find("l").text


            route_turn_tag = route.find("zz")
            if not route_turn_tag:
                route_turn = 0
            else:
                route_turn = route_turn_tag.text[0]

            flights = []
            for route_segment in route_segments:
                number = route_segment.find("no")
                from_city = City.get_name(route_segment.find("f").text)
                to_city = City.get_name(route_segment.find("t").text)
                company = route_segment.find("a").text
                departure_date = route_segment.find("fd").text
                departure_time = route_segment.find("ft").text
                arrival_date = route_segment.find("td")
                if not arrival_date:
                    arrival_date = departure_date
                else:
                    arrival_date = arrival_date.text

                arrival_time = route_segment.find("tt").text
                seat_type = route_segment.find("st").text
                flight_price = route_segment.find("m")
                duration = route_segment.find("d").text
                modal = route_segment.find("et").text
                status = int(route_segment.find("dp").text)

                flight_data = {
                    "number": number.text,
                    "staring": from_city,
                    "destination": to_city,
                    "company": company,
                    "departure": "%s %s:%s" % (departure_date, departure_time[:2], departure_time[2:]),
                    "arrival": "%s %s:%s" % (arrival_date, arrival_time[:2], arrival_time[2:]),
                    "duration": duration,
                    "modal": modal,
                    "status": status,
                    "seat_type": seat_type
                }
                flight = Flight(**flight_data)
                flights.append(flight)

            route = Route(route_company_three, route_starting,
                          route_destination, price=price, data=datas['RS']['R'][index],
                          tax=tax, flights=flights, turn=route_turn, limit_no=route_limit)
            result_routes.append(route)

        return result_routes

    @classmethod
    def get_limits(cls, limit_no):
        url = "http://intf.fare2go.com/limit.php?p=%s" % limit_no
        try:
            content = requests.get(url).content
            soup = BeautifulSoup(content, from_encoding="utf-8")
            limits = soup.find_all("limit")
            final_limits = []
            for limit in limits:
                limit_type = limit.find('type').text
                content = limit.find('content').text
                final_limits.append({"limit_type": limit_type, "content": content})
            return final_limits
        except:
            return []


class Flight(object):
    def __init__(self, number, staring, destination, company, departure, arrival, duration, modal, seat_type="Y",
                 status=1, amount=1, **kwargs):
        self.number = number
        self.starting = staring
        self.destination = destination
        self.company = company
        self.departure = datetime.datetime.strptime(departure, "%Y-%m-%d %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
        self.arrival = datetime.datetime.strptime(arrival, "%Y-%m-%d %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
        self.duration = duration
        self.amount = amount
        self.modal = modal
        self.status = status
        self.seat_type = seat_type

    def to_json(self):
        return {
            "number": self.number,
            "starting": self.starting,
            "destination": self.destination,
            "company": self.company,
            "departure": self.departure,
            "arrival": self.arrival,
            "amount": self.amount,
            "duration": self.duration,
            "modal": self.modal,
            "status": self.status,
            "seat_type": self.seat_type
        }

    @classmethod
    def format_datetime(cls, string):
        return datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%S")

    @classmethod
    def get_type(cls, seat_type):
        mapping = {
            "Y": u"经济舱",
            "C": u"商务舱",
            "F": u"头等舱"
        }
        return mapping.get(seat_type, u"经济舱")


class PNR(object):
    @classmethod
    def gen_by_routes(cls, routes):
        pass
