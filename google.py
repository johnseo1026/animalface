from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"박보영, 손예진, 한효주, 태연, 아이유, 한예슬, 오연서, 김희선, 이효리, 안소희, 수지, 나연(트와이스), 예린(여자친구), 한승연, 문채원, 경리(나인뮤지스), 예지(ITZY), 한혜진, 헤이즈, 지연(티아라), 윤아, 이연희, 고아라, 문근영,강다니엘, 백현, 박보검, 송중기, 황민현, 시우민, 강동원, 이종석, 이준기, 정국, 바비, 박지훈, 수호, 윤두준, 이민기, 김우빈, 육성재, 공유, 마동석, 조진웅, 조세호, 안재홍","limit":100,"print_urls":True,"format":"jpg"}
paths = response.download(arguments)
print(paths)
