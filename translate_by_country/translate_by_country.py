from googletrans import Translator


def translate_text(text,language) -> str:
    """
    Translates the given text to the specified language using Google Translate API.
    Args:
        text (str): The text to be translated.
        language (str): The language to translate the text into.
    Returns:
        str: The translated text.
    """
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, dest=language).text
    return translated_text


def translate_text_by_alpha2(text,country_alpha2) -> str:
    """
    Translates the given text based on the country's alpha2 code.
    Args:
        text (str): The text to be translated.
        country_alpha2 (str): The alpha2 code of the country.
    Returns:
        str: The translated text.
    """
    country_alpha2 = country_alpha2.lower()
    language = {
    "af": "Persian",
    "ax": "Swedish",
    "al": "Albanian",
    "dz": "Arabic",
    "as": "Samoan",
    "ad": "Catalan",
    "ao": "Portuguese",
    "ai": "English",
    "ag": "English",
    "ar": "Spanish",
    "am": "Armenian",
    "aw": "Dutch",
    "au": "English",
    "at": "German",
    "az": "Azerbaijani",
    "bs": "English",
    "bh": "Arabic",
    "bd": "Bengali",
    "bb": "English",
    "by": "Belarusian",
    "be": "Dutch",
    "bz": "English",
    "bj": "French",
    "bm": "English",
    "bt": "Dzongkha",
    "bo": "Spanish",
    "ba": "Bosnian",
    "bw": "English",
    "bv": "Norwegian",
    "br": "Portuguese",
    "io": "English",
    "bn": "Malay",
    "bg": "Bulgarian",
    "bf": "French",
    "bi": "Kirundi",
    "kh": "Khmer",
    "cm": "French",
    "ca": "English",
    "cv": "Portuguese",
    "ky": "English",
    "cf": "French",
    "td": "French",
    "cl": "Spanish",
    "cn": "Mandarin Chinese",
    "cx": "English",
    "cc": "English",
    "co": "Spanish",
    "km": "Arabic",
    "cg": "French",
    "cd": "French",
    "ck": "English",
    "cr": "Spanish", 
    "ci": "French",
    "hr": "Croatian",
    "cu": "Spanish",
    "cy": "Greek",
    "cz": "Czech",
    "dk": "Danish",
    "dj": "Arabic",
    "dm": "English",
    "do": "Spanish",
    "ec": "Spanish",
    "eg": "Arabic",
    "sv": "Spanish",
    "gq": "French",
    "er": "Tigrinya",
    "ee": "Estonian",
    "et": "Amharic",
    "fk": "English",
    "fo": "Faroese",
    "fj": "English",
    "fi": "Finnish",
    "fr": "French",
    "gf": "French",
    "pf": "French",
    "tf": "French",
    "ga": "French",
    "gm": "English",
    "ge": "Georgian",
    "de": "German",
    "gh": "English",
    "gi": "English",
    "gr": "Greek",
    "gl": "Greenlandic",
    "gd": "English",
    "gp": "French",
    "gu": "English",
    "gt": "Spanish",
    "gg": "English",
    "gn": "French",
    "gw": "Portuguese",
    "gy": "English",
    "ht": "French",
    "va": "Italian",
    "hn": "Spanish",
    "hk": "Chinese",
    "hu": "Hungarian",
    "is": "Icelandic",
    "in": "Hindi",
    "id": "Indonesian",
    "ir": "Persian",
    "iq": "Arabic",
    "ie": "Irish",
    "im": "English",
    "il": "Hebrew",
    "it": "Italian",
    "jm": "English",
    "jp": "Japanese",
    "je": "English",
    "jo": "Arabic",
    "kz": "Kazakh",
    "ke": "Swahili",
    "ki": "English",
    "kp": "Korean",
    "kr": "Korean",
    "kw": "Arabic",
    "kg": "Kyrgyz",
    "la": "Lao",
    "lv": "Latvian",
    "lb": "Arabic",
    "ls": "Sotho",
    "lr": "English",
    "ly": "Arabic",
    "li": "German",
    "lt": "Lithuanian",
    "lu": "French",
    "mo": "Chinese",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "mw": "English",
    "my": "Malay",
    "mv": "Dhivehi",
    "ml": "French",
    "mt": "Maltese",
    "mh": "English",
    "mq": "French",
    "mr": "Arabic",
    "mu": "English",
    "yt": "French",
    "mx": "Spanish",
    "fm": "English",
    "md": "Moldovan",
    "mc": "French",
    "mn": "Mongolian",
    "me": "Montenegrin",
    "ms": "English",
    "ma": "Arabic",
    "mz": "Portuguese",
    "mm": "Burmese",
    "na": "English",
    "nr": "Nauru",
    "np": "Nepali",
    "nl": "Dutch",
    "nc": "French",
    "nz": "English",
    "ni": "Spanish",
    "ne": "French",
    "ng": "English",
    "nu": "Niuean",
    "nf": "English",
    "mp": "English",
    "no": "Norwegian",
    "om": "Arabic",
    "pk": "Urdu",
    "pw": "English",
    "ps": "Arabic",
    "pa": "Spanish",
    "pg": "English",
    "py": "Spanish",
    "pe": "Spanish",
    "ph": "Filipino",
    "pn": "English",
    "pl": "Polish",
    "pt": "Portuguese",
    "pr": "Spanish",
    "qa": "Arabic",
    "re": "French",
    "ro": "Romanian",
    "ru": "Russian",
    "rw": "Kinyarwanda",
    "bl": "French",
    "sh": "English",
    "kn": "English",
    "lc": "English",
    "mf": "French",
    "pm": "French",
    "vc": "English",
    "ws": "Samoan",
    "sm": "Italian",
    "st": "Portuguese",
    "sa": "Arabic",
    "sn": "French",
    "rs": "Serbian",
    "sc": "English",
    "sl": "English",
    "sg": "English",
    "sx": "Dutch",
    "sk": "Slovak",
    "si": "Slovenian",
    "sb": "English",
    "so": "Somali",
    "za": "Afrikaans",
    "gs": "English",
    "ss": "English",
    "es": "Spanish",
    "lk": "Sinhala",
    "sd": "Arabic",
    "sr": "Dutch",
    "sj": "Norwegian",
    "sz": "Swazi",
    "se": "Swedish",
    "ch": "Swedish",
    "sy": "Arabic",
    "tw": "Chinese",
    "tj": "Tajik",
    "tz": "Swahili",
    "th": "Thai",
    "tl": "Portuguese",
    "tg": "French",
    "tk": "English",
    "to": "Tongan",
    "tt": "English",
    "tn": "Arabic",
    "tr": "Turkish",
    "tm": "Turkmen",
    "tc": "English",
    "tv": "Tuvaluan",
    "ug": "English",
    "ua": "Ukrainian",
    "ae": "Arabic",
    "gb": "English",
    "us": "English",
    "um": "English",
    "uy": "Spanish",
    "uz": "Uzbek",
    "vu": "French",
    "ve": "Spanish",
    "vn": "Vietnamese",
    "vg": "English",
    "vi": "English",
    "wf": "French",
    "eh": "Arabic",
    "ye": "Arabic",
    "zm": "English",
    "zw": "English"
    }.get(country_alpha2)
    result = translate_text(text,language)
    return result
  
  
def translate_text_by_alpha3(text,country_alpha3) -> str: 
    """
    Translates the given text based on the country's alpha3 code.
    Args:
        text (str): The text to be translated.
        country_alpha3 (str): The alpha3 code of the country.
    Returns:
        str: The translated text.
    """
    country_alpha3 = country_alpha3.lower()
    language = {
    "afg": "Persian",
    "ala": "Swedish",
    "alb": "Albanian",
    "dza": "Arabic",
    "asm": "Samoan",
    "and": "Catalan",
    "ago": "Portuguese",
    "aia": "English",
    "atg": "English",
    "arg": "Spanish",
    "arm": "Armenian",
    "abw": "Dutch",
    "aus": "English",
    "aut": "German",
    "aze": "Azerbaijani",
    "bhs": "English",
    "bhr": "Arabic",
    "bgd": "Bengali",
    "brb": "English",
    "blr": "Belarusian",
    "bel": "Dutch",
    "blz": "English",
    "ben": "French",
    "bmu": "English",
    "btn": "Dzongkha",
    "bol": "Spanish",
    "bih": "Bosnian",
    "bwa": "English",
    "bvt": "Norwegian",
    "bra": "Portuguese",
    "iot": "English",
    "brn": "Malay",
    "bgr": "Bulgarian",
    "bfa": "French",
    "bdi": "Kirundi",
    "khm": "Khmer",
    "cmr": "French",
    "can": "English",
    "cpv": "Portuguese",
    "cym": "English",
    "caf": "French",
    "tcd": "French",
    "chl": "Spanish",
    "chn": "Mandarin Chinese",
    "cxr": "English",
    "cck": "English",
    "col": "Spanish",
    "com": "Arabic",
    "cog": "French",
    "cod": "French",
    "cok": "English",
    "cri": "Spanish",
    "civ": "French",
    "hrv": "Croatian",
    "cub": "Spanish",
    "cyp": "Greek",
    "cze": "Czech",
    "dnk": "Danish",
    "dji": "Arabic",
    "dma": "English",
    "dom": "Spanish",
    "ecu": "Spanish",
    "egy": "Arabic",
    "slv": "Spanish",
    "gnq": "French",
    "eri": "Tigrinya",
    "est": "Estonian",
    "eth": "Amharic",
    "flk": "English",
    "fro": "Faroese",
    "fji": "English",
    "fin": "Finnish",
    "fra": "French",
    "guf": "French",
    "pyf": "French",
    "atf": "French",
    "gab": "French",
    "gmb": "English",
    "geo": "Georgian",
    "deu": "German",
    "gha": "English",
    "gib": "English",
    "grc": "Greek",
    "grl": "Greenlandic",
    "grd": "English",
    "glp": "French",
    "gum": "English",
    "gtm": "Spanish",
    "ggg": "English",
    "gin": "French",
    "gnb": "Portuguese",
    "guy": "English",
    "hti": "French",
    "vat": "Italian",
    "hnd": "Spanish",
    "hkg": "Chinese",
    "hun": "Hungarian", 
    "isl": "Icelandic",
    "ind": "Hindi",
    "idn": "Indonesian",
    "irn": "Persian",
    "irq": "Arabic",
    "irl": "Irish",
    "imn": "English",
    "isr": "Hebrew",
    "ita": "Italian",
    "jam": "English",
    "jpn": "Japanese",
    "jey": "English",
    "jor": "Arabic",
    "kaz": "Kazakh",
    "ken": "Swahili",
    "kir": "English",
    "prk": "Korean",
    "kor": "Korean",
    "kwt": "Arabic",
    "kgz": "Kyrgyz",
    "lao": "Lao",
    "lva": "Latvian",
    "lbn": "Arabic",
    "lso": "Sotho",
    "lbr": "English",
    "lby": "Arabic",
    "lie": "German",
    "ltu": "Lithuanian",
    "lux": "French",
    "mac": "Chinese",
    "mkd": "Macedonian",
    "mdg": "Malagasy",
    "mwi": "English",
    "mys": "Malay",
    "mdv": "Dhivehi",
    "mli": "French",
    "mlt": "Maltese",
    "mhl": "English",
    "mtq": "French",
    "mrt": "Arabic",
    "mus": "English",
    "myt": "French",
    "mex": "Spanish",
    "fsm": "English",
    "mda": "Moldovan",
    "mco": "French",
    "mng": "Mongolian",
    "mne": "Montenegrin",
    "msr": "English",
    "mar": "Arabic",
    "moz": "Portuguese",
    "mmr": "Burmese",
    "nam": "English",
    "nru": "Nauru",
    "npl": "Nepali",
    "nld": "Dutch",
    "ncl": "French",
    "nzl": "English",
    "nic": "Spanish",
    "ner": "French",
    "nga": "English",
    "niu": "Niuean",
    "nfk": "English",
    "mnp": "English",
    "nor": "Norwegian",
    "omn": "Arabic",
    "pak": "Urdu", 
    "plw": "English",
    "pse": "Arabic",
    "pan": "Spanish",
    "png": "English",
    "pry": "Spanish",
    "per": "Spanish",
    "phl": "Filipino",
    "pcn": "English",
    "pol": "Polish",
    "prt": "Portuguese",
    "pri": "Spanish",
    "qat": "Arabic",
    "reu": "French",
    "rou": "Romanian",
    "rus": "Russian",
    "rwa": "Kinyarwanda",
    "blm": "French",
    "shn": "English",
    "kna": "English",
    "lca": "English",
    "maf": "French",
    "spm": "French",
    "vct": "English",
    "wsm": "Samoan",
    "smr": "Italian",
    "stp": "Portuguese",
    "sau": "Arabic",
    "sen": "French",
    "srb": "Serbian",
    "syc": "English",
    "sle": "English",
    "sgp": "English",
    "sxm": "Dutch",
    "svk": "Slovak",
    "svn": "Slovenian",
    "slb": "English",
    "som": "Somali",
    "zaf": "Afrikaans",
    "sgs": "English",
    "ssd": "English",
    "esp": "Spanish",
    "lka": "Sinhala",
    "sdn": "Arabic",
    "sur": "Dutch",
    "sjm": "Norwegian",
    "swz": "Swazi",
    "swe": "Swedish",
    "che": "Swedish",
    "syr": "Arabic",
    "twn": "Chinese",
    "tjk": "Tajik",
    "tza": "Swahili",
    "tha": "Thai",
    "tls": "Portuguese",
    "tgo": "French",
    "tkl": "English",
    "ton": "Tongan",
    "tto": "English",
    "tun": "Arabic",
    "tur": "Turkish",
    "tkm": "Turkmen",
    "tca": "English",
    "tuv": "Tuvaluan",
    "uga": "English",
    "ukr": "Ukrainian",
    "are": "Arabic",
    "gbr": "English",
    "usa": "English",
    "umi": "English",
    "ury": "Spanish",
    "uzb": "Uzbek",
    "vut": "French",
    "ven": "Spanish",
    "vnm": "Vietnamese",
    "vgb": "English",
    "vir": "English",
    "wlf": "French",
    "esh": "Arabic",
    "yem": "Arabic",
    "zmb": "English",
    "zwe": "English"
    }.get(country_alpha3)
    result = translate_text(text,language)
    return result


def translate_text_by_code(text,country_code) -> str:
    """
    Translates the given text based on the country's code.
    Args:
        text (str): The text to be translated.
        country_code (int): The code of the country.
    Returns:
        str: The translated text.
    """
    country_code = int(country_code)
    language = {
    93: "Persian",
    358: "Swedish",
    355: "Albanian",
    213: "Arabic",
    1684: "Samoan",
    376: "Catalan",
    244: "Portuguese",
    1264: "English",
    1268: "English",
    54: "Spanish",
    374: "Armenian",
    297: "Dutch",
    61: "English",
    43: "German",
    994: "Azerbaijani",
    1242: "English",
    973: "Arabic",
    880: "Bengali",
    1246: "English",
    375: "Belarusian",
    32: "Dutch",
    501: "English",
    229: "French",
    1441: "English",
    975: "Dzongkha",
    591: "Spanish",
    387: "Bosnian",
    267: "English",
    47: "Norwegian",
    55: "Portuguese",
    1284: "English",
    673: "Malay",
    359: "Bulgarian",
    226: "French",
    257: "Kirundi",
    855: "Khmer",
    237: "French",
    1: "English",
    238: "Portuguese",
    1345: "English",
    236: "French",
    235: "French",
    56: "Spanish",
    86: "Mandarin Chinese",
    57: "Spanish",
    269: "Arabic",
    242: "French",
    243: "French",
    682: "English",
    506: "Spanish",
    225: "French",
    385: "Croatian",
    53: "Spanish",
    357: "Greek",
    420: "Czech",
    45: "Danish",
    253: "Arabic",
    1767: "English",
    1809: "Spanish",
    593: "Spanish",
    20: "Arabic",
    503: "Spanish",
    240: "French",
    291: "Tigrinya",
    372: "Estonian",
    251: "Amharic",
    500: "English",
    298: "Faroese",
    594: "French",
    689: "French",
    262: "French",
    241: "French",
    220: "English",
    995: "Georgian",
    49: "German",
    233: "English",
    350: "English",
    30: "Greek",
    299: "Greenlandic",
    1473: "English",
    590: "French",
    1671: "English",
    502: "Spanish",
    224: "French",
    245: "Portuguese",
    592: "English",
    509: "French",
    379: "Italian",
    504: "Spanish",
    852: "Chinese",
    36: "Hungarian",
    354: "Icelandic",
    91: "Hindi",
    62: "Indonesian",
    98: "Persian",
    964: "Arabic",
    353: "Irish",
    972: "Hebrew",
    39: "Italian",
    1876: "English",
    81: "Japanese",
    962: "Arabic",
    7: "Kazakh",
    254: "Swahili",
    686: "English",
    850: "Korean",
    82: "Korean",
    965: "Arabic",
    996: "Kyrgyz",
    856: "Lao",
    371: "Latvian",
    961: "Arabic",
    266: "Sotho",
    231: "English",
    218: "Arabic",
    423: "German",
    370: "Lithuanian",
    352: "French",
    853: "Chinese",
    389: "Macedonian",
    261: "Malagasy",
    265: "English",
    60: "Malay",
    960: "Dhivehi",
    223: "French",
    356: "Maltese",
    692: "English",
    596: "French",
    222: "Arabic",
    230: "English",
    52: "Spanish",
    691: "English",
    373: "Moldovan",
    377: "French",
    976: "Mongolian",
    382: "Montenegrin",
    1664: "English",
    212: "Arabic",
    258: "Portuguese",
    95: "Burmese",
    264: "English",
    674: "Nauru",
    977: "Nepali",
    31: "Dutch",
    687: "French",
    64: "English",
    505: "Spanish",
    227: "French",
    234: "English",
    683: "Niuean",
    672: "English",
    1670: "English",
    968: "Arabic",
    92: "Urdu",
    680: "English",
    970: "Arabic",
    507: "Spanish",
    675: "English",
    595: "Spanish",
    51: "Spanish",
    63: "Filipino",
    48: "Polish",
    351: "Portuguese",
    1787: "Spanish",
    974: "Arabic",
    40: "Romanian",
    7: "Russian",
    250: "Kinyarwanda",
    290: "English",
    1869: "English",
    1758: "English",
    508: "French",
    1784: "English",
    685: "Samoan",
    378: "Italian",
    239: "Portuguese",
    966: "Arabic",
    221: "French",
    381: "Serbian",
    248: "English",
    232: "English",
    65: "English",
    1721: "Dutch",
    421: "Slovak",
    386: "Slovenian",
    677: "English",
    252: "Somali",
    27: "Afrikaans",
    211: "English",
    34: "Spanish",
    94: "Sinhala",
    249: "Arabic",
    597: "Dutch",
    268: "Swazi",
    46: "Swedish",
    41: "Swedish",
    963: "Arabic",
    886: "Chinese",
    992: "Tajik",
    255: "Swahili",
    66: "Thai",
    670: "Portuguese",
    228: "French",
    690: "English",
    676: "Tongan",
    1868: "English",
    216: "Arabic",
    90: "Turkish",
    993: "Turkmen",
    1649: "English",
    688: "Tuvaluan",
    256: "English",
    380: "Ukrainian",
    971: "Arabic",
    598: "Spanish",
    998: "Uzbek",
    678: "French",
    58: "Spanish",
    84: "Vietnamese",
    681: "French",
    967: "Arabic",
    260: "English",
    263: "English"
    }.get(country_code)
    result = translate_text(text,language)
    return result


def translate_text_by_name(text,country_name) -> str:
    """
    Translates the given text based on the country's name.
    Args:
        text (str): The text to be translated.
        country_name (str): The name of the country.
    Returns:
        str: The translated text.
    """
    country_name= country_name.lower()
    language = {
    "afghanistan": "Persian",
    "aland islands": "Swedish",
    "albania": "Albanian",
    "algeria": "Arabic",
    "american samoa": "Samoan",
    "andorra": "Catalan",
    "angola": "Portuguese",
    "anguilla": "English",
    "antigua and barbuda": "English",
    "argentina": "Spanish",
    "armenia": "Armenian",
    "aruba": "Dutch",
    "australia": "English",
    "austria": "German",
    "azerbaijan": "Azerbaijani",
    "bahamas": "English",
    "bahrain": "Arabic",
    "bangladesh": "Bengali",
    "barbados": "English",
    "belarus": "Belarusian",
    "belgium": "Dutch",
    "belize": "English",
    "benin": "French",
    "bermuda": "English",
    "bhutan": "Dzongkha",
    "bolivia": "Spanish",
    "bosnia": "Bosnian",
    "botswana": "English",
    "bouvet island": "Norwegian",
    "brazil": "Portuguese",
    "british indian ocean territory": "English",
    "brunei": "Malay",
    "bulgaria": "Bulgarian",
    "burkina faso": "French",
    "burundi": "Kirundi",
    "cambodia": "Khmer",
    "cameroon": "French",
    "canada": "English",
    "cape verde": "Portuguese",
    "cayman islands": "English",
    "central african": "French",
    "chad": "French",
    "chile": "Spanish",
    "china": "Mandarin Chinese",
    "christmas island": "English",
    "cocos islands": "English",
    "colombia": "Spanish",
    "comoros": "Arabic",
    "congo": "French",
    "cook islands": "English",
    "costa rica": "Spanish",
    "Ivory coast": "French",
    "croatia": "Croatian",
    "cuba": "Spanish",
    "cyprus": "Greek",
    "czech": "Czech",
    "denmark": "Danish",
    "djibouti": "Arabic",
    "dominica": "English",
    "dominican": "Spanish",
    "ecuador": "Spanish",
    "egypt": "Arabic",
    "el salvador": "Spanish",
    "equatorial guinea": "French",
    "eritrea": "Tigrinya",
    "estonia": "Estonian",
    "ethiopia": "Amharic",
    "falkland islands": "English",
    "faroe islands": "Faroese",
    "fiji": "English",
    "finland": "Finnish",
    "france": "French",
    "french guiana": "French",
    "french polynesia": "French",
    "french southern territories": "French",
    "gabon": "French",
    "gambia": "English",
    "georgia": "Georgian",
    "germany": "German",
    "ghana": "English",
    "gibraltar": "English",
    "greece": "Greek",
    "greenland": "Greenlandic",
    "grenada": "English",
    "guadeloupe": "French",
    "guam": "English",
    "guatemala": "Spanish",
    "guernsey": "English",
    "guinea": "French",
    "guinea-bissau": "Portuguese",
    "guyana": "English",
    "haiti": "French",
    "holy see": "Italian",
    "honduras": "Spanish",
    "hong kong": "Chinese",
    "hungary": "Hungarian",
    "iceland": "Icelandic",
    "india": "Hindi",
    "indonesia": "Indonesian",
    "iran": "Persian",
    "iraq": "Arabic",
    "ireland": "Irish",
    "isle of man": "English",
    "israel": "Hebrew",
    "italy": "Italian",
    "jamaica": "English",
    "japan": "Japanese",
    "jersey": "English",
    "jordan": "Arabic",
    "kazakhstan": "Kazakh",
    "kenya": "Swahili",
    "kiribati": "English",
    "korea": "Korean",
    "korea": "Korean",
    "kuwait": "Arabic",
    "kyrgyzstan": "Kyrgyz",
    "lao": "Lao",
    "latvia": "Latvian",
    "lebanon": "Arabic",
    "lesotho": "Sotho",
    "liberia": "English",
    "libya": "Arabic",
    "liechtenstein": "German",
    "lithuania": "Lithuanian",
    "luxembourg": "French",
    "macao": "Chinese",
    "macedonia": "Macedonian",
    "madagascar": "Malagasy",
    "malawi": "English",
    "malaysia": "Malay",
    "maldives": "Dhivehi",
    "mali": "French",
    "malta": "Maltese",
    "marshall islands": "English",
    "martinique": "French",
    "mauritania": "Arabic",
    "mauritius": "English",
    "mayotte": "French",
    "mexico": "Spanish",
    "micronesia": "English",
    "moldova": "Moldovan",
    "monaco": "French",
    "mongolia": "Mongolian",
    "montenegro": "Montenegrin",
    "montserrat": "English",
    "morocco": "Arabic",
    "mozambique": "Portuguese",
    "myanmar": "Burmese",
    "namibia": "English",
    "nauru": "Nauru",
    "nepal": "Nepali",
    "netherlands": "Dutch",
    "new caledonia": "French",
    "new zealand": "English",
    "nicaragua": "Spanish",
    "niger": "French",
    "nigeria": "English",
    "niue": "Niuean",
    "norfolk island": "English",
    "northern mariana islands": "English",
    "norway": "Norwegian",
    "oman": "Arabic",
    "pakistan": "Urdu",
    "palau": "English",
    "palestine": "Arabic",
    "panama": "Spanish",
    "papua new guinea": "English",
    "paraguay": "Spanish",
    "peru": "Spanish",
    "philippines": "Filipino",
    "pitcairn": "English",
    "poland": "Polish",
    "portugal": "Portuguese",
    "puerto rico": "Spanish",
    "qatar": "Arabic",
    "reunion": "French",
    "romania": "Romanian",
    "russia": "Russian",
    "rwanda": "Kinyarwanda",
    "bartholomew": "French",
    "saint helena": "English",
    "saint kitts and nevis": "English",
    "saint lucia": "English",
    "saint martin": "French",
    "saint pierre and miquelon": "French",
    "saint vincent and the grenadines": "English",
    "samoa": "Samoan",
    "san marino": "Italian",
    "sao tome and principe": "Portuguese",
    "saudi arabia": "Arabic",
    "senegal": "French",
    "serbia": "Serbian",
    "seychelles": "English",
    "sierra leone": "English",
    "singapore": "English",
    "sint maarten": "Dutch",
    "slovakia": "Slovak",
    "slovenia": "Slovenian",
    "solomon islands": "English",
    "somalia": "Somali",
    "south africa": "Afrikaans",
    "south georgia and the south sandwich islands": "English",
    "south sudan": "English",
    "spain": "Spanish",
    "sri lanka": "Sinhala",
    "sudan": "Arabic",
    "suriname": "Dutch",
    "svalbard and jan mayen": "Norwegian",
    "swaziland": "Swazi",
    "sweden": "Swedish",
    "switzerland": "Swedish",
    "syrian arab republic": "Arabic",
    "taiwan": "Chinese",
    "tajikistan": "Tajik",
    "tanzania": "Swahili",
    "thailand": "Thai",
    "timor leste": "Portuguese",
    "togo": "French",
    "tokelau": "English",
    "tonga": "Tongan",
    "trinidad and tobago": "English",
    "tunisia": "Arabic",
    "turkey": "Turkish",
    "turkmenistan": "Turkmen",
    "turks and caicos islands": "English",
    "tuvalu": "Tuvaluan",
    "uganda": "English",
    "ukraine": "Ukrainian",
    "united arab emirates": "Arabic",
    "united kingdom": "English",
    "usa": "English",
    "united states minor outlying islands": "English",
    "uruguay": "Spanish",
    "uzbekistan": "Uzbek",
    "vanuatu": "French",
    "venezuela": "Spanish",
    "viet nam": "Vietnamese",
    "virgin islands": "English",
    "wallis and futuna": "French",
    "western sahara": "Arabic",
    "yemen": "Arabic",
    "zambia": "English",
    "zimbabwe": "English"
    }.get(country_name)
    result = translate_text(text,language)
    return result


def translate_text_by_emoji(text,country_emoji) -> str:
    """
    Translates the given text based on the country's emoji.
    Args:
        text (str): The text to be translated.
        country_emoji (str): The emoji of the country.
    Returns:
        str: The translated text.
    """
    language ={
    "🇦🇫": "Persian",
    "🇦🇽": "Swedish",
    "🇦🇱": "Albanian",
    "🇩🇿": "Arabic",
    "🇦🇸": "Samoan",
    "🇦🇩": "Catalan",
    "🇦🇴": "Portuguese",
    "🇦🇮": "English",
    "🇦🇬": "English",
    "🇦🇷": "Spanish",
    "🇦🇲": "Armenian",
    "🇦🇼": "Dutch",
    "🇦🇺": "English",
    "🇦🇹": "German",
    "🇦🇿": "Azerbaijani",
    "🇧🇸": "English",
    "🇧🇭": "Arabic",
    "🇧🇩": "Bengali",
    "🇧🇧": "English",
    "🇧🇾": "Belarusian",
    "🇧🇪": "Dutch",
    "🇧🇿": "English",
    "🇧🇯": "French",
    "🇧🇲": "English",
    "🇧🇹": "Dzongkha",
    "🇧🇴": "Spanish",
    "🇧🇦": "Bosnian",
    "🇧🇼": "English",
    "🇧🇻": "Norwegian",
    "🇧🇷": "Portuguese",
    "🇮🇴": "English",
    "🇧🇳": "Malay",
    "🇧🇬": "Bulgarian",
    "🇧🇫": "French",
    "🇧🇮": "Kirundi",
    "🇰🇭": "Khmer",
    "🇨🇲": "French",
    "🇨🇦": "English",
    "🇨🇻": "Portuguese",
    "🇰🇾": "English",
    "🇨🇫": "French",
    "🇹🇩": "French",
    "🇨🇱": "Spanish",
    "🇨🇳": "Mandarin Chinese",
    "🇨🇽": "English",
    "🇨🇨": "English",
    "🇨🇴": "Spanish",
    "🇰🇲": "Arabic",
    "🇨🇬": "French",
    "🇨🇩": "French",
    "🇨🇰": "English",
    "🇨🇷": "Spanish",
    "🇨🇮": "French",
    "🇭🇷": "Croatian",
    "🇨🇺": "Spanish",
    "🇨🇾": "Greek",
    "🇨🇿": "Czech",
    "🇩🇰": "Danish",
    "🇩🇯": "Arabic",
    "🇩🇲": "English",
    "🇩🇴": "Spanish",
    "🇪🇨": "Spanish",
    "🇪🇬": "Arabic",
    "🇸🇻": "Spanish",
    "🇬🇶": "French",
    "🇪🇷": "Tigrinya",
    "🇪🇪": "Estonian",
    "🇪🇹": "Amharic",
    "🇫🇰": "English",
    "🇫🇴": "Faroese",
    "🇫🇯": "English",
    "🇫🇮": "Finnish",
    "🇫🇷": "French",
    "🇬🇫": "French",
    "🇵🇫": "French",
    "🇹🇫": "French",
    "🇬🇦": "French",
    "🇬🇲": "English",
    "🇬🇪": "Georgian",
    "🇩🇪": "German",
    "🇬🇭": "English",
    "🇬🇮": "English",
    "🇬🇷": "Greek",
    "🇬🇱": "Greenlandic",
    "🇬🇩": "English",
    "🇬🇵": "French",
    "🇬🇺": "English",
    "🇬🇹": "Spanish",
    "🇬🇬": "English",
    "🇬🇳": "French",
    "🇬🇼": "Portuguese",
    "🇬🇾": "English",
    "🇭🇹": "French",
    "🇻🇦": "Italian",
    "🇭🇳": "Spanish",
    "🇭🇰": "Chinese",
    "🇭🇺": "Hungarian",
    "🇮🇸": "Icelandic",
    "🇮🇳": "Hindi",
    "🇮🇩": "Indonesian",
    "🇮🇷": "Persian",
    "🇮🇶": "Arabic",
    "🇮🇪": "Irish",
    "🇮🇲": "English",
    "🇮🇱": "Hebrew",
    "🇮🇹": "Italian",
    "🇯🇲": "English",
    "🇯🇵": "Japanese",
    "🇯🇪": "English",
    "🇯🇴": "Arabic",
    "🇰🇿": "Kazakh",
    "🇰🇪": "Swahili",
    "🇰🇮": "English",
    "🇰🇵": "Korean",
    "🇰🇷": "Korean",
    "🇰🇼": "Arabic",
    "🇰🇬": "Kyrgyz",
    "🇱🇦": "Lao",
    "🇱🇻": "Latvian",
    "🇱🇧": "Arabic",
    "🇱🇸": "Sotho",
    "🇱🇷": "English",
    "🇱🇾": "Arabic",
    "🇱🇮": "German",
    "🇱🇹": "Lithuanian",
    "🇱🇺": "French",
    "🇲🇴": "Chinese",
    "🇲🇰": "Macedonian",
    "🇲🇬": "Malagasy",
    "🇲🇼": "English",
    "🇲🇾": "Malay",
    "🇲🇻": "Dhivehi",
    "🇲🇱": "French",
    "🇲🇹": "Maltese",
    "🇲🇭": "English",
    "🇲🇶": "French",
    "🇲🇷": "Arabic",
    "🇲🇺": "English",
    "🇾🇹": "French",
    "🇲🇽": "Spanish",
    "🇫🇲": "English",
    "🇲🇩": "Moldovan",
    "🇲🇨": "French",
    "🇲🇳": "Mongolian",
    "🇲🇪": "Montenegrin",
    "🇲🇸": "English",
    "🇲🇦": "Arabic",
    "🇲🇿": "Portuguese",
    "🇲🇲": "Burmese",
    "🇳🇦": "English",
    "🇳🇷": "Nauru",
    "🇳🇵": "Nepali",
    "🇳🇱": "Dutch",
    "🇳🇨": "French",
    "🇳🇿": "English",
    "🇳🇮": "Spanish",
    "🇳🇪": "French",
    "🇳🇬": "English",
    "🇳🇺": "Niuean",
    "🇳🇫": "English",
    "🇲🇵": "English",
    "🇳🇴": "Norwegian",
    "🇴🇲": "Arabic",
    "🇵🇰": "Urdu",
    "🇵🇼": "English",
    "🇵🇸": "Arabic",
    "🇵🇦": "Spanish",
    "🇵🇬": "English",
    "🇵🇾": "Spanish",
    "🇵🇪": "Spanish",
    "🇵🇭": "Filipino",
    "🇵🇳": "English",
    "🇵🇱": "Polish",
    "🇵🇹": "Portuguese",
    "🇵🇷": "Spanish",
    "🇶🇦": "Arabic",
    "🇷🇪": "French",
    "🇷🇴": "Romanian",
    "🇷🇺": "Russian",
    "🇷🇼": "Kinyarwanda",
    "🇧🇱": "French",
    "🇸🇭": "English",
    "🇰🇳": "English",
    "🇱🇨": "English",
    "🇲🇫": "French",
    "🇵🇲": "French",
    "🇻🇨": "English",
    "🇼🇸": "Samoan",
    "🇸🇲": "Italian",
    "🇸🇹": "Portuguese",
    "🇸🇦": "Arabic",
    "🇸🇳": "French",
    "🇷🇸": "Serbian",
    "🇸🇨": "English",
    "🇸🇱": "English",
    "🇸🇬": "English",
    "🇸🇽": "Dutch",
    "🇸🇰": "Slovak",
    "🇸🇮": "Slovenian",
    "🇸🇧": "English",
    "🇸🇴": "Somali",
    "🇿🇦": "Afrikaans",
    "🇬🇸": "English",
    "🇸🇸": "English",
    "🇪🇸": "Spanish",
    "🇱🇰": "Sinhala",
    "🇸🇩": "Arabic",
    "🇸🇷": "Dutch",
    "🇸🇯": "Norwegian",
    "🇸🇿": "Swazi",
    "🇸🇪": "Swedish",
    "🇨🇭": "Swedish",
    "🇸🇾": "Arabic",
    "🇹🇼": "Chinese",
    "🇹🇯": "Tajik",
    "🇹🇿": "Swahili",
    "🇹🇭": "Thai",
    "🇹🇱": "Portuguese",
    "🇹🇬": "French",
    "🇹🇰": "English",
    "🇹🇴": "Tongan",
    "🇹🇹": "English",
    "🇹🇳": "Arabic",
    "🇹🇷": "Turkish",
    "🇹🇲": "Turkmen",
    "🇹🇨": "English",
    "🇹🇻": "Tuvaluan",
    "🇺🇬": "English",
    "🇺🇦": "Ukrainian",
    "🇦🇪": "Arabic",
    "🇬🇧": "English",
    "🇺🇸": "English",
    "🇺🇲": "English",
    "🇺🇾": "Spanish",
    "🇺🇿": "Uzbek",
    "🇻🇺": "French",
    "🇻🇪": "Spanish",
    "🇻🇳": "Vietnamese",
    "🇻🇬": "English",
    "🇻🇮": "English",
    "🇼🇫": "French",
    "🇪🇭": "Arabic",
    "🇾🇪": "Arabic",
    "🇿🇲": "English",
    "🇿🇼": "English"
    }.get(country_emoji)
    result = translate_text(text,language)
    return result

