{"filter":false,"title":"settings.py","tooltip":"/PSE3S/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":151,"column":0},"end":{"row":175,"column":21},"action":"insert","lines":["AWS_S3_OBJECT_PARAMETERS = {","    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',","    'CacheControl': 'max-age=94608000'","}","","AWS_STORAGE_BUCKET_NAME = 'fullstack-django-issuetracker'","AWS_S3_REGION_NAME = 'eu-west-1'","AWS_ACCESS_KEY_ID = os.environ.get(\"AWS_SECRET_KEY_ID\")","AWS_SECRET_ACCESS_KEY = os.environ.get(\"AWS_SECRET_ACCESS_KEY\")","","AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME","","STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","","STATIC_URL = '/static/'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")","","MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'","","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"],"id":86}],[{"start":{"row":156,"column":27},"end":{"row":156,"column":56},"action":"remove","lines":["fullstack-django-issuetracker"],"id":87}],[{"start":{"row":156,"column":27},"end":{"row":156,"column":28},"action":"insert","lines":["p"],"id":88},{"start":{"row":156,"column":28},"end":{"row":156,"column":29},"action":"insert","lines":["s"]},{"start":{"row":156,"column":29},"end":{"row":156,"column":30},"action":"insert","lines":["e"]},{"start":{"row":156,"column":30},"end":{"row":156,"column":31},"action":"insert","lines":["3"]},{"start":{"row":156,"column":31},"end":{"row":156,"column":32},"action":"insert","lines":["s"]},{"start":{"row":156,"column":32},"end":{"row":156,"column":33},"action":"insert","lines":["-"]}],[{"start":{"row":156,"column":33},"end":{"row":156,"column":34},"action":"insert","lines":["s"],"id":89},{"start":{"row":156,"column":34},"end":{"row":156,"column":35},"action":"insert","lines":["t"]},{"start":{"row":156,"column":35},"end":{"row":156,"column":36},"action":"insert","lines":["a"]},{"start":{"row":156,"column":36},"end":{"row":156,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":156,"column":37},"end":{"row":156,"column":38},"action":"insert","lines":["i"],"id":90},{"start":{"row":156,"column":38},"end":{"row":156,"column":39},"action":"insert","lines":["c"]}],[{"start":{"row":158,"column":45},"end":{"row":158,"column":46},"action":"remove","lines":["T"],"id":91},{"start":{"row":158,"column":44},"end":{"row":158,"column":45},"action":"remove","lines":["E"]},{"start":{"row":158,"column":43},"end":{"row":158,"column":44},"action":"remove","lines":["R"]},{"start":{"row":158,"column":42},"end":{"row":158,"column":43},"action":"remove","lines":["C"]},{"start":{"row":158,"column":41},"end":{"row":158,"column":42},"action":"remove","lines":["E"]},{"start":{"row":158,"column":40},"end":{"row":158,"column":41},"action":"remove","lines":["S"]}],[{"start":{"row":158,"column":40},"end":{"row":158,"column":41},"action":"insert","lines":["a"],"id":92}],[{"start":{"row":158,"column":40},"end":{"row":158,"column":41},"action":"remove","lines":["a"],"id":93}],[{"start":{"row":158,"column":40},"end":{"row":158,"column":41},"action":"insert","lines":["A"],"id":94},{"start":{"row":158,"column":41},"end":{"row":158,"column":42},"action":"insert","lines":["C"]},{"start":{"row":158,"column":42},"end":{"row":158,"column":43},"action":"insert","lines":["C"]},{"start":{"row":158,"column":43},"end":{"row":158,"column":44},"action":"insert","lines":["E"]},{"start":{"row":158,"column":44},"end":{"row":158,"column":45},"action":"insert","lines":["S"]},{"start":{"row":158,"column":45},"end":{"row":158,"column":46},"action":"insert","lines":["S"]}],[{"start":{"row":175,"column":21},"end":{"row":176,"column":0},"action":"insert","lines":["",""],"id":95}],[{"start":{"row":176,"column":0},"end":{"row":176,"column":2},"action":"insert","lines":["''"],"id":96}],[{"start":{"row":176,"column":2},"end":{"row":176,"column":3},"action":"insert","lines":["'"],"id":97}],[{"start":{"row":184,"column":0},"end":{"row":184,"column":2},"action":"insert","lines":["''"],"id":98}],[{"start":{"row":184,"column":2},"end":{"row":184,"column":3},"action":"insert","lines":["'"],"id":99}],[{"start":{"row":165,"column":0},"end":{"row":165,"column":2},"action":"insert","lines":["''"],"id":100}],[{"start":{"row":165,"column":2},"end":{"row":165,"column":3},"action":"insert","lines":["'"],"id":101}],[{"start":{"row":170,"column":0},"end":{"row":170,"column":2},"action":"insert","lines":["''"],"id":102}],[{"start":{"row":170,"column":2},"end":{"row":170,"column":3},"action":"insert","lines":["'"],"id":103}],[{"start":{"row":176,"column":2},"end":{"row":176,"column":3},"action":"remove","lines":["'"],"id":104},{"start":{"row":176,"column":1},"end":{"row":176,"column":2},"action":"remove","lines":["'"]},{"start":{"row":176,"column":0},"end":{"row":176,"column":1},"action":"remove","lines":["'"]}],[{"start":{"row":184,"column":2},"end":{"row":184,"column":3},"action":"remove","lines":["'"],"id":105},{"start":{"row":184,"column":1},"end":{"row":184,"column":2},"action":"remove","lines":["'"]},{"start":{"row":184,"column":0},"end":{"row":184,"column":1},"action":"remove","lines":["'"]},{"start":{"row":183,"column":1},"end":{"row":184,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":183,"column":1},"end":{"row":184,"column":0},"action":"insert","lines":["",""],"id":106}],[{"start":{"row":165,"column":2},"end":{"row":165,"column":3},"action":"remove","lines":["'"],"id":107},{"start":{"row":165,"column":1},"end":{"row":165,"column":2},"action":"remove","lines":["'"]},{"start":{"row":165,"column":0},"end":{"row":165,"column":1},"action":"remove","lines":["'"]}],[{"start":{"row":151,"column":0},"end":{"row":152,"column":0},"action":"insert","lines":["",""],"id":108}],[{"start":{"row":151,"column":0},"end":{"row":151,"column":2},"action":"insert","lines":["''"],"id":109}],[{"start":{"row":151,"column":2},"end":{"row":151,"column":3},"action":"insert","lines":["'"],"id":110}],[{"start":{"row":171,"column":2},"end":{"row":171,"column":3},"action":"remove","lines":["'"],"id":111},{"start":{"row":171,"column":1},"end":{"row":171,"column":2},"action":"remove","lines":["'"]},{"start":{"row":171,"column":0},"end":{"row":171,"column":1},"action":"remove","lines":["'"]}],[{"start":{"row":177,"column":0},"end":{"row":177,"column":2},"action":"insert","lines":["''"],"id":112}],[{"start":{"row":177,"column":2},"end":{"row":177,"column":3},"action":"insert","lines":["'"],"id":113}],[{"start":{"row":184,"column":1},"end":{"row":185,"column":0},"action":"insert","lines":["",""],"id":114}],[{"start":{"row":170,"column":1},"end":{"row":171,"column":0},"action":"insert","lines":["",""],"id":117}],[{"start":{"row":171,"column":0},"end":{"row":171,"column":51},"action":"insert","lines":["STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')"],"id":118}],[{"start":{"row":78,"column":70},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":119},{"start":{"row":79,"column":0},"end":{"row":79,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":79,"column":16},"end":{"row":79,"column":58},"action":"insert","lines":["'django.template.context_processors.media'"],"id":120}],[{"start":{"row":79,"column":58},"end":{"row":79,"column":59},"action":"insert","lines":[","],"id":121}],[{"start":{"row":187,"column":0},"end":{"row":187,"column":2},"action":"insert","lines":["''"],"id":122}],[{"start":{"row":187,"column":2},"end":{"row":187,"column":3},"action":"insert","lines":["'"],"id":123}],[{"start":{"row":152,"column":2},"end":{"row":152,"column":3},"action":"remove","lines":["'"],"id":124},{"start":{"row":152,"column":1},"end":{"row":152,"column":2},"action":"remove","lines":["'"]},{"start":{"row":152,"column":0},"end":{"row":152,"column":1},"action":"remove","lines":["'"]}],[{"start":{"row":163,"column":70},"end":{"row":164,"column":0},"action":"insert","lines":["",""],"id":125},{"start":{"row":164,"column":0},"end":{"row":164,"column":1},"action":"insert","lines":["A"]},{"start":{"row":164,"column":1},"end":{"row":164,"column":2},"action":"insert","lines":["W"]},{"start":{"row":164,"column":2},"end":{"row":164,"column":3},"action":"insert","lines":["S"]}],[{"start":{"row":164,"column":3},"end":{"row":164,"column":4},"action":"insert","lines":["_"],"id":126},{"start":{"row":164,"column":4},"end":{"row":164,"column":5},"action":"insert","lines":["D"]},{"start":{"row":164,"column":5},"end":{"row":164,"column":6},"action":"insert","lines":["E"]},{"start":{"row":164,"column":6},"end":{"row":164,"column":7},"action":"insert","lines":["F"]},{"start":{"row":164,"column":7},"end":{"row":164,"column":8},"action":"insert","lines":["A"]},{"start":{"row":164,"column":8},"end":{"row":164,"column":9},"action":"insert","lines":["U"]},{"start":{"row":164,"column":9},"end":{"row":164,"column":10},"action":"insert","lines":["L"]},{"start":{"row":164,"column":10},"end":{"row":164,"column":11},"action":"insert","lines":["T"]}],[{"start":{"row":164,"column":11},"end":{"row":164,"column":12},"action":"insert","lines":["_"],"id":127},{"start":{"row":164,"column":12},"end":{"row":164,"column":13},"action":"insert","lines":["A"]},{"start":{"row":164,"column":13},"end":{"row":164,"column":14},"action":"insert","lines":["C"]},{"start":{"row":164,"column":14},"end":{"row":164,"column":15},"action":"insert","lines":["L"]}],[{"start":{"row":164,"column":15},"end":{"row":164,"column":16},"action":"insert","lines":[" "],"id":128},{"start":{"row":164,"column":16},"end":{"row":164,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":164,"column":17},"end":{"row":164,"column":18},"action":"insert","lines":[" "],"id":129}],[{"start":{"row":164,"column":18},"end":{"row":164,"column":20},"action":"insert","lines":["''"],"id":130}],[{"start":{"row":164,"column":19},"end":{"row":164,"column":20},"action":"insert","lines":["p"],"id":131}],[{"start":{"row":164,"column":19},"end":{"row":164,"column":20},"action":"remove","lines":["p"],"id":132}],[{"start":{"row":164,"column":19},"end":{"row":164,"column":20},"action":"insert","lines":["p"],"id":133},{"start":{"row":164,"column":20},"end":{"row":164,"column":21},"action":"insert","lines":["u"]},{"start":{"row":164,"column":21},"end":{"row":164,"column":22},"action":"insert","lines":["b"]},{"start":{"row":164,"column":22},"end":{"row":164,"column":23},"action":"insert","lines":["l"]},{"start":{"row":164,"column":23},"end":{"row":164,"column":24},"action":"insert","lines":["i"]},{"start":{"row":164,"column":24},"end":{"row":164,"column":25},"action":"insert","lines":["c"]}],[{"start":{"row":164,"column":25},"end":{"row":164,"column":26},"action":"insert","lines":["-"],"id":134},{"start":{"row":164,"column":26},"end":{"row":164,"column":27},"action":"insert","lines":["r"]},{"start":{"row":164,"column":27},"end":{"row":164,"column":28},"action":"insert","lines":["e"]},{"start":{"row":164,"column":28},"end":{"row":164,"column":29},"action":"insert","lines":["a"]},{"start":{"row":164,"column":29},"end":{"row":164,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":13,"column":15},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":135}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":22},"action":"insert","lines":["import dj_database_url"],"id":136}],[{"start":{"row":27,"column":41},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":137},{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"remove","lines":["",""],"id":138},{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":["#"],"id":139}],[{"start":{"row":31,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":140}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":32},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:"],"id":141}],[{"start":{"row":31,"column":32},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":142},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["d"],"id":143},{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"insert","lines":["e"]},{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"remove","lines":["e"],"id":144}],[{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["v"],"id":145},{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"insert","lines":["e"]},{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["l"]},{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":["o"]},{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":["p"]},{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"insert","lines":["e"]},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"insert","lines":["m"]},{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":["n"]},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"remove","lines":["t"],"id":146},{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"remove","lines":["n"]},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"remove","lines":["m"]},{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"remove","lines":["e"]}],[{"start":{"row":32,"column":11},"end":{"row":32,"column":12},"action":"insert","lines":["m"],"id":147},{"start":{"row":32,"column":12},"end":{"row":32,"column":13},"action":"insert","lines":["e"]},{"start":{"row":32,"column":13},"end":{"row":32,"column":14},"action":"insert","lines":["n"]},{"start":{"row":32,"column":14},"end":{"row":32,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":15},"end":{"row":32,"column":16},"action":"insert","lines":[" "],"id":148},{"start":{"row":32,"column":16},"end":{"row":32,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":32,"column":17},"end":{"row":32,"column":18},"action":"insert","lines":[" "],"id":149}],[{"start":{"row":32,"column":18},"end":{"row":32,"column":19},"action":"insert","lines":["F"],"id":150},{"start":{"row":32,"column":19},"end":{"row":32,"column":20},"action":"insert","lines":["a"]},{"start":{"row":32,"column":20},"end":{"row":32,"column":21},"action":"insert","lines":["l"]},{"start":{"row":32,"column":21},"end":{"row":32,"column":22},"action":"insert","lines":["s"]},{"start":{"row":32,"column":22},"end":{"row":32,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":32,"column":23},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":151},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":152}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"insert","lines":["e"],"id":153},{"start":{"row":33,"column":1},"end":{"row":33,"column":2},"action":"insert","lines":["l"]},{"start":{"row":33,"column":2},"end":{"row":33,"column":3},"action":"insert","lines":["s"]},{"start":{"row":33,"column":3},"end":{"row":33,"column":4},"action":"insert","lines":["e"]},{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":[":"]}],[{"start":{"row":33,"column":5},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":154},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"insert","lines":["d"]},{"start":{"row":34,"column":5},"end":{"row":34,"column":6},"action":"insert","lines":["e"]},{"start":{"row":34,"column":6},"end":{"row":34,"column":7},"action":"insert","lines":["v"]},{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["e"]},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["l"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["o"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["p"]}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["m"],"id":155}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"remove","lines":["m"],"id":156}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["e"],"id":157}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"remove","lines":["e"],"id":158}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["m"],"id":159},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["e"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["n"]},{"start":{"row":34,"column":14},"end":{"row":34,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":34,"column":15},"end":{"row":34,"column":16},"action":"insert","lines":[" "],"id":160},{"start":{"row":34,"column":16},"end":{"row":34,"column":17},"action":"insert","lines":["="]}],[{"start":{"row":34,"column":17},"end":{"row":34,"column":18},"action":"insert","lines":[" "],"id":161},{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["T"]},{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["R"]}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"remove","lines":["R"],"id":162}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":20},"action":"insert","lines":["r"],"id":163},{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["u"]},{"start":{"row":34,"column":21},"end":{"row":34,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":22},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":164},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"insert","lines":["    "]},{"start":{"row":35,"column":4},"end":{"row":36,"column":0},"action":"insert","lines":["",""]},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"remove","lines":["    "],"id":165}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["D"],"id":166},{"start":{"row":36,"column":1},"end":{"row":36,"column":2},"action":"insert","lines":["E"]},{"start":{"row":36,"column":2},"end":{"row":36,"column":3},"action":"insert","lines":["B"]},{"start":{"row":36,"column":3},"end":{"row":36,"column":4},"action":"insert","lines":["U"]},{"start":{"row":36,"column":4},"end":{"row":36,"column":5},"action":"insert","lines":["G"]}],[{"start":{"row":36,"column":5},"end":{"row":36,"column":6},"action":"insert","lines":[" "],"id":167},{"start":{"row":36,"column":6},"end":{"row":36,"column":7},"action":"insert","lines":["="]}],[{"start":{"row":36,"column":7},"end":{"row":36,"column":8},"action":"insert","lines":[" "],"id":168},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["D"]},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["E"]},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["V"]}],[{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"remove","lines":["V"],"id":169},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"remove","lines":["E"]},{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"remove","lines":["D"]}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":9},"action":"insert","lines":["d"],"id":170},{"start":{"row":36,"column":9},"end":{"row":36,"column":10},"action":"insert","lines":["e"]},{"start":{"row":36,"column":10},"end":{"row":36,"column":11},"action":"insert","lines":["v"]},{"start":{"row":36,"column":11},"end":{"row":36,"column":12},"action":"insert","lines":["e"]},{"start":{"row":36,"column":12},"end":{"row":36,"column":13},"action":"insert","lines":["l"]},{"start":{"row":36,"column":13},"end":{"row":36,"column":14},"action":"insert","lines":["o"]},{"start":{"row":36,"column":14},"end":{"row":36,"column":15},"action":"insert","lines":["p"]},{"start":{"row":36,"column":15},"end":{"row":36,"column":16},"action":"insert","lines":["m"]},{"start":{"row":36,"column":16},"end":{"row":36,"column":17},"action":"insert","lines":["e"]},{"start":{"row":36,"column":17},"end":{"row":36,"column":18},"action":"insert","lines":["n"]},{"start":{"row":36,"column":18},"end":{"row":36,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":98,"column":64},"end":{"row":99,"column":0},"action":"remove","lines":["",""],"id":171}],[{"start":{"row":98,"column":64},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":172}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":2},"action":"insert","lines":["''"],"id":173}],[{"start":{"row":99,"column":2},"end":{"row":99,"column":3},"action":"insert","lines":["'"],"id":174}],[{"start":{"row":106,"column":0},"end":{"row":106,"column":2},"action":"insert","lines":["''"],"id":175}],[{"start":{"row":106,"column":2},"end":{"row":106,"column":3},"action":"insert","lines":["'"],"id":176}],[{"start":{"row":99,"column":0},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":177}],[{"start":{"row":99,"column":0},"end":{"row":108,"column":5},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"],"id":178}],[{"start":{"row":38,"column":86},"end":{"row":38,"column":87},"action":"insert","lines":[","],"id":179}],[{"start":{"row":38,"column":87},"end":{"row":38,"column":88},"action":"insert","lines":[" "],"id":180}],[{"start":{"row":38,"column":88},"end":{"row":38,"column":90},"action":"insert","lines":["''"],"id":181}],[{"start":{"row":38,"column":89},"end":{"row":38,"column":90},"action":"insert","lines":["p"],"id":182},{"start":{"row":38,"column":90},"end":{"row":38,"column":91},"action":"insert","lines":["r"]},{"start":{"row":38,"column":91},"end":{"row":38,"column":92},"action":"insert","lines":["o"]},{"start":{"row":38,"column":92},"end":{"row":38,"column":93},"action":"insert","lines":["j"]}],[{"start":{"row":38,"column":92},"end":{"row":38,"column":93},"action":"remove","lines":["j"],"id":183},{"start":{"row":38,"column":91},"end":{"row":38,"column":92},"action":"remove","lines":["o"]},{"start":{"row":38,"column":90},"end":{"row":38,"column":91},"action":"remove","lines":["r"]},{"start":{"row":38,"column":89},"end":{"row":38,"column":90},"action":"remove","lines":["p"]}],[{"start":{"row":38,"column":89},"end":{"row":38,"column":90},"action":"insert","lines":["p"],"id":184},{"start":{"row":38,"column":90},"end":{"row":38,"column":91},"action":"insert","lines":["r"]},{"start":{"row":38,"column":91},"end":{"row":38,"column":92},"action":"insert","lines":["o"]},{"start":{"row":38,"column":92},"end":{"row":38,"column":93},"action":"insert","lines":["j"]},{"start":{"row":38,"column":93},"end":{"row":38,"column":94},"action":"insert","lines":["e"]},{"start":{"row":38,"column":94},"end":{"row":38,"column":95},"action":"insert","lines":["c"]},{"start":{"row":38,"column":95},"end":{"row":38,"column":96},"action":"insert","lines":["t"]},{"start":{"row":38,"column":96},"end":{"row":38,"column":97},"action":"insert","lines":["-"]}],[{"start":{"row":38,"column":97},"end":{"row":38,"column":98},"action":"insert","lines":["p"],"id":185},{"start":{"row":38,"column":98},"end":{"row":38,"column":99},"action":"insert","lines":["s"]}],[{"start":{"row":38,"column":97},"end":{"row":38,"column":99},"action":"remove","lines":["ps"],"id":186},{"start":{"row":38,"column":97},"end":{"row":38,"column":102},"action":"insert","lines":["pse3s"]}],[{"start":{"row":38,"column":102},"end":{"row":38,"column":103},"action":"insert","lines":["."],"id":187},{"start":{"row":38,"column":103},"end":{"row":38,"column":104},"action":"insert","lines":["h"]},{"start":{"row":38,"column":104},"end":{"row":38,"column":105},"action":"insert","lines":["e"]},{"start":{"row":38,"column":105},"end":{"row":38,"column":106},"action":"insert","lines":["r"]},{"start":{"row":38,"column":106},"end":{"row":38,"column":107},"action":"insert","lines":["o"]},{"start":{"row":38,"column":107},"end":{"row":38,"column":108},"action":"insert","lines":["k"]},{"start":{"row":38,"column":108},"end":{"row":38,"column":109},"action":"insert","lines":["u"]}],[{"start":{"row":38,"column":109},"end":{"row":38,"column":110},"action":"insert","lines":["a"],"id":188},{"start":{"row":38,"column":110},"end":{"row":38,"column":111},"action":"insert","lines":["p"]},{"start":{"row":38,"column":111},"end":{"row":38,"column":112},"action":"insert","lines":["p"]},{"start":{"row":38,"column":112},"end":{"row":38,"column":113},"action":"insert","lines":["."]},{"start":{"row":38,"column":113},"end":{"row":38,"column":114},"action":"insert","lines":["c"]},{"start":{"row":38,"column":114},"end":{"row":38,"column":115},"action":"insert","lines":["o"]},{"start":{"row":38,"column":115},"end":{"row":38,"column":116},"action":"insert","lines":["m"]}]]},"ace":{"folds":[],"scrolltop":571,"scrollleft":0,"selection":{"start":{"row":38,"column":118},"end":{"row":38,"column":118},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1620495453342,"hash":"2d63954797e00bc474ca1a44c91fb98f5df70359"}