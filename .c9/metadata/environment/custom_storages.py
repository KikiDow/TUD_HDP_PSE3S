{"filter":false,"title":"custom_storages.py","tooltip":"/custom_storages.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["from django.conf import settings","from storages.backends.s3boto3 import S3Boto3Storage","","","class StaticStorage(S3Boto3Storage):","    location = settings.STATICFILES_LOCATION","","","class MediaStorage(S3Boto3Storage):","    location = settings.MEDIAFILES_LOCATION"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":43},"end":{"row":9,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1620137740462,"hash":"4042e73c1d7f39d5d7b2e1d61534afd2becfa4a6"}