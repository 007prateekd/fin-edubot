import pandas as pd
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import ssl
import trafilatura
import json
from tqdm import tqdm


def get_sitemap(url):
    req = Request(
        url=url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response = urlopen(req)
    xml = BeautifulSoup(
        response, 
        "lxml-xml", 
        from_encoding=response.info().get_param("charset")
    )
    return xml


def sitemap_to_dataframe(xml, name=None, data=None, verbose=False):
    df = pd.DataFrame(columns=["loc", "changefreq", "priority", "domain", "sitemap_name"])
    urls = xml.find_all("url")
    for url in urls:
        if xml.find("loc"):
            loc = url.findNext("loc").text
            parsed_uri = urlparse(loc)
            domain = "{uri.netloc}".format(uri=parsed_uri)
        else:
            loc = ""
            domain = ""
        if xml.find("changefreq"):
            changefreq = url.findNext("changefreq").text
        else:
            changefreq = ""
        if xml.find("priority"):
            priority = url.findNext("priority").text
        else:
            priority = ""
        if name:
            sitemap_name = name
        else:
            sitemap_name = ""
        row = {
            "domain": domain,
            "loc": loc,
            "changefreq": changefreq,
            "priority": priority,
            "sitemap_name": sitemap_name,
        }
        if verbose:
            print(row)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    return df


def extract_text_from_url(url):
    downloaded_url = trafilatura.fetch_url(url)
    extracted = trafilatura.extract(
        downloaded_url, 
        output_format="json", 
        with_metadata=True, 
        include_comments = False,
        date_extraction_params={"extensive_search": True, "original_date": True}
    )
    json_output = json.loads(extracted)
    return json_output["text"]
        

def main():
    ssl._create_default_https_context = ssl._create_stdlib_context
    url = "https://zerodha.com/varsity/chapter-sitemap2.xml"
    xml = get_sitemap(url)
    df = sitemap_to_dataframe(xml, verbose=False)
    urls = df["loc"].to_numpy()
    urls = [url for url in urls if "%" not in url]

    with open("./chapters.txt", "w") as f:
        for url in tqdm(urls[1:]):
            topic = url.split("/")[-2]
            if "hindi" in topic or topic in ["the-vegetable-list", "bonus-share-vs-stock-split", "getting-started-2"]:
                continue
            text = extract_text_from_url(url=url)
            text = text.lower()
            text = text.replace("key takeaways from this chapter", "")
            text = text.replace("we recommend reading this chapter on varsity to learn more and understand the concepts in-depth.", "")
            text = text.replace("varsity", "")
            f.writelines(topic + "\n")
            f.writelines(text  + "\n###\n")


if __name__ == "__main__":
    main()