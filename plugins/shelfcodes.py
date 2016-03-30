
SHELFCODES = [
    {"name": "Technological Artifacts of the Lower Holocene", "code": "ARTIFACT", "shelf": "1 (reserve)"},
    {"name": "Booklet Double", "code": "BD", "shelf": "1 (reserve)"},
    {"name": "Binary Star [doubles]", "code": "BS", "shelf": "1 (reserve)"},
    {"name": "Ace Double", "code": "D", "shelf": "1 (reserve)"},
    {"name": "Dictionary", "code": "DICT", "shelf": "1 (reserve)"},
    {"name": "Eraserhead Double", "code": "ERD", "shelf": "1 (reserve)"},
    {"name": "Gryphon Double", "code": "GRD", "shelf": "1 (reserve)"},
    {"name": "Gollancz Double", "code": "GZD", "shelf": "1 (reserve)"},
    {"name": "Millennium Binary [doubles]", "code": "MB", "shelf": "1 (reserve)"},
    {"name": "Ocean View Doubles", "code": "OVD", "shelf": "1 (reserve)"},
    {"name": "Large Reserve Art", "code": "R/L-ART", "shelf": "1 (reserve)"},
    {"name": "Very Large Reserve Fiction", "code": "R/VL", "shelf": "1 (reserve)"},
    {"name": "Very Large Reserve Art", "code": "R/VL-ART", "shelf": "1 (reserve)"},
    {"name": "Very Large Reserve Anthology", "code": "R/VLA", "shelf": "1 (reserve)"},
    {"name": "Even Bigger Reserve Art", "code": "R/XL-ART", "shelf": "1 (reserve)"},
    {"name": "Tor Double", "code": "TD", "shelf": "1 (reserve)"},
    {"name": "(New Books)", "code": " ", "shelf": "2 (reserve)"},
    {"name": "Large Reserve Comics", "code": "R/L-CX", "shelf": "3 (reserve)"},
    {"name": "Small Reserve Comics", "code": "R/S-CX", "shelf": "3 (reserve)"},
    {"name": "Very Large Reserve Comics", "code": "R/VL-CX", "shelf": "3 & 4 (reserve)"},
    {"name": "(Recent Magazines)", "code": " ", "shelf": "3 & 4 (reserve)"},
    {"name": "Large Reserve Reference", "code": "R/L-REF", "shelf": "4 (reserve)"},
    {"name": "Reserve Multimedia", "code": "R/MM", "shelf": "4 (reserve)"},
    {"name": "Small Reserve Reference", "code": "R/S-REF", "shelf": "4 (reserve)"},
    {"name": "Very Large Reserve Reference", "code": "R/VL-REF", "shelf": "4 (reserve)"},
    {"name": "Even Bigger Reserve Fiction", "code": "R/XL", "shelf": "4 (reserve)"},
    {"name": "Even Bigger Reserve Comics", "code": "R/XL-CX", "shelf": "4 (reserve)"},
    {"name": "Even Bigger Reserve Reference", "code": "R/XL-REF", "shelf": "4 (reserve)"},
    {"name": "Even Bigger Reserve Anthology", "code": "R/XLA", "shelf": "4 (reserve)"},
    {"name": "Foreign-language Hardcover Anthology", "code": "FH", "shelf": "5 (reserve)"},
    {"name": "Foreign-language Hardcover Anthology", "code": "FHA", "shelf": "5 (reserve)"},
    {"name": "Foreign-language Paperback Anthology", "code": "FP", "shelf": "5 (reserve)"},
    {"name": "Foreign-language Paperback Anthology", "code": "FPA", "shelf": "5 (reserve)"},
    {"name": "Small Circulating Reference", "code": "S-REF", "shelf": "6"},
    {"name": "Very Large Circulating Reference", "code": "VL-REF", "shelf": "6 & 7"},
    {"name": "Large Circulating Reference", "code": "L-REF", "shelf": "7"},
    {"name": "Even Bigger Circulating Reference", "code": "XL-REF", "shelf": "7 & 8"},
    {"name": "Circulating Mixed Media", "code": "C/MM", "shelf": "9"},
    {"name": "Large Circulating Comics", "code": "L-CX", "shelf": "9"},
    {"name": "Small Circulating Comics", "code": "S-CX", "shelf": "9"},
    {"name": "Very Large Circulating Fiction", "code": "VL", "shelf": "9"},
    {"name": "Very Large Circulating Comics", "code": "VL/CX", "shelf": "9"},
    {"name": "Very Large Circulating Anthology", "code": "VLA", "shelf": "9"},
    {"name": "Small Anthology", "code": "SA", "shelf": "10 -- 17"},
    {"name": "Small Fiction (authors A-L)", "code": "S", "shelf": "17 -- 54"},
    {"name": "Large Fiction", "code": "L", "shelf": "55 -- 79, 111 -- 145"},
    {"name": "Large Anthology", "code": "LA", "shelf": "80 -- 82, tops of 92 -- 110, tops of 83 -- 87"},
    {"name": "Small Fiction (authors M-Z)", "code": "S", "shelf": "83 -- 110"}, ]

ORDER = 11


def preBuildPage(site, page, context, data):
    if page.path == "map.html":
        context['shelfcodes'] = SHELFCODES
    return context, data
