import requests, os, argparse
from requests.utils import parse_header_links
from utils.helper import *
from utils.logger import Logger

def scrape(api_url, max_downloads=100, separate_by_status=False, stop_early=True, skip_existing=True):

    # Create base directory and logger
    base_dir = "images"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create log file
    logger = Logger(base_dir, "download_log.json")

    # Pagination loop
    downloads = []
    loop_count = 0
    stop = False
    while api_url and not stop:

        # Get HTTP Response
        response = requests.get(api_url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            rprint(f"Failed to get response (error: {response.status_code})")
            return

        # Get waterfall and download
        data = response.json()
        for observation in data:

            if len(downloads) >= max_downloads:
                stop = True
                mprint(f"Max downloads reached ({max_downloads})")
                break

            if stop_early and loop_count >= max_downloads:
                mprint(f"Max loop count reached ({loop_count})")
                stop = True
                break

            loop_count += 1
            img_id = observation["id"]
            img_url = observation["waterfall"]
            log_data = logger.load()

            if img_url is None:
                yprint(f"Image is not there (id: {img_id})")
                continue
            elif skip_existing and img_id in log_data:
                yprint(f"Image was downloaded before (id: {img_id})")
                continue
        
            downloads.append(img_id)
            img_status = observation["status"]
            img_name = f"waterfall_{img_id}.png"
            if separate_by_status:
                img_dir = os.path.join(base_dir, img_status)
            else:
                img_dir = base_dir
            img_path = os.path.join(img_dir, img_name)
                
            response = requests.get(img_url)

            if not os.path.exists(img_dir):
                os.makedirs(img_dir)               
            with open(img_path, 'wb') as f:
                f.write(response.content)

            logger.append(img_id)
            yprint(f"Image downloaded: {img_path} ({len(downloads)}/{max_downloads})")

        # Find next cursor link
        link_header = response.headers.get("Link", "")
        links = parse_header_links(link_header) # Parses into a list of dicts
        for link in links:
            if link.get("rel") == "next":
                api_url = link["url"]
                mprint(f"Next Page: {api_url}")
                break
            
    mprint(f"All Images Downloaded")
    return downloads

def download(id):
    api_url = f"https://network.satnogs.org/api/observations/?id={id}&status=&ground_station=&start=&end=&satellite__norad_cat_id=&transmitter_uuid=&transmitter_mode=&transmitter_type=&waterfall_status=&vetted_status=&vetted_user=&observer=&start__lt=&observation_id="
    downloads = scrape(
        api_url, 
        max_downloads=1, 
        separate_by_status=False, 
        stop_early=True,
        skip_existing=False
    )
    if len(downloads) == 0:
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UTILS - SCRAPER")
    parser.add_argument("-m", "--max_downloads", type=int, default=100, help="Max Downloads (default: 100)")
    parser.add_argument("-s", "--status", type=str, default="", help="Status (default: '', options: 'good', 'bad', 'unknown')")
    parser.add_argument("-sd", "--start_date", type=str, default="2018-08-07", help="Start Date (default: '2018-08-07', format: 'YYYY-MM-DD')")
    parser.add_argument("-ed", "--end_date", type=str, default="", help="End Date (default: '', format: 'YYYY-MM-DD')")
    parser.add_argument("-o", "--observation_id", type=int, default="", help="Observation ID (default: '', format: integer)")
    args = parser.parse_args()

    api_url_query = f"https://network.satnogs.org/api/observations/?id={args.observation_id}&status={args.status}&ground_station=&start={args.start_date}&end={args.end_date}&satellite__norad_cat_id=&transmitter_uuid=&transmitter_mode=&transmitter_type=&waterfall_status=&vetted_status=&vetted_user=&observer=&start__lt=&observation_id="
    
    scrape(
        api_url_query, 
        args.max_downloads, 
        separate_by_status=True, 
        stop_early=False, 
        skip_existing=True
    )


