from google_images_download import google_images_download
response = google_images_download.googleimagesdownload() 
search_queries = [
'Red Bull F1 2022 racing track photos'
'Mercedes F1 2022 racing track photos'
'Ferrari F1 2022 racing track photos'
'Aston Martin F1 2022 racing track photos'
'HAAS F1 2022 racing track photos'
'McLaren F1 2022 racing track photos'
'Alfa Romeo F1 2022 racing track photos'
'Alpha Tauri F1 2022 racing track photos',
'Williams F1 2022 racing track photos',
'Alpine F1 2002 racing track photos']

def downloadimages(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit":100,
                 "print_urls":True,
                 "size": "medium",
                 "aspect_ratio":"panoramic"}
    try:
        response.download(arguments)
    except FileNotFoundError: 
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit":100,
                     "print_urls":True, 
                     "size": "medium"}
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments) 
        except:
            pass
    # Driver Code
for query in search_queries:
    downloadimages(query) 
    print() 