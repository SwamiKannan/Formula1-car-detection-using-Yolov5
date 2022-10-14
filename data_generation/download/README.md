## Download the data
### Data Sources:
#### Video Playlist
Formula 1 Singapore Airlines Singapore Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjUSj1PGNT9Qprzr4skApDL3

Formula 1 Pirelli Italian Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjVhMF3o9_NRLTaRm0Uo00p3

Formula 1 Heineken Dutch Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjVDsp8q-Mhz2spTbCGvS6YE

Formula 1 Rolex Belgian Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjVlE_qK47JS_ub8x7O1CIGm

Formula 1 Aramco Magyar Nagydij 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjVc0FGw4etk42NNDtQ8AeR1

Formula 1 Lenovo Grand Prix de France 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjVdFYvMrynKTEEAZteLXH5e

Formula 1 Lenovo British Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjUSmLc9TXKJfE8PmZ6kpLQF

Formula 1 AWS Canadian Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjVeZnFNaL_bBMLnBTkhIX93

Formula 1 Azerbaijan Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjW8uJ9mQvmHsvpVuZ_fw95z

Formula 1 Grand Prix De Monaco 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjV7cXDWU8-KTtb4cHNbMqMv

Verstappen vs. Leclerc: The 2022 Title Fight
https://www.youtube.com/playlist?list=PLfoNZDHitwjV4Z5uTey0-PPknE9z37qHr

Formula 1 Pirelli Gran Premio De España 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjXJGpwSzN8nMB6DyzS1bURm

Formula 1 Crypto.com Miami Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjX_M-51x6WUoJ-adIwqW2Tn

Formula 1 Rolex Grossen Preis von Österreich 2022 
https://www.youtube.com/playlist?list=PLfoNZDHitwjVheBZvl1z155n0cz0nyHzj

Formula 1 Gulf Air Bahrain Grand Prix 2022
https://www.youtube.com/playlist?list=PLfoNZDHitwjUPPIQnrImKqkJ9-hycKnVX

#### Google Image Search.
Since the primary data for testing was going to be the videos, this was used only as a secondary tool for data augmentation. 

### Downloading the data
#### Videos
Used ytd's tool to download the videos of each playlist using a batch process

```
pip install ytd-dlp
```
run [download-videos.bat](https://github.com/SwamiKannan/Formula1-car-detection/blob/main/data_generation/download/download-videos.bat) from the root directory where you want to store the videos


#### Google Image Search.
Follow this tutorial here: <https://www.geeksforgeeks.org/how-to-download-google-images-using-python/>

or:
<ul><li>Install Google Image Downloader</li></ul>

```
pip install google_images_download
```
<ul>
<li>Navigate to the 'Lib\site-packages\google-images-download' folder (where google_images_download is installed)</li>
<li> run <a href="https://github.com/SwamiKannan/Formula1-car-detection/blob/main/data_generation/download/google_dl.py">google_dl.py </a> from this folder </li></ul>

```
python google_dl.py
```
Note: The current setting is to download 100 images. You can change the number of images to be downloaded by changing the value of 'limits' in the arguments dictionary of downloadimages() (two places)
