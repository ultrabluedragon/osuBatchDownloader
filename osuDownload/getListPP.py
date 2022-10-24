from lxml import etree
from selenium import webdriver
import time
import pandas as pd
import re


def getBeatmapListPP(download_station: int, urls: list, search_url: str, url_name: list) -> None:  # 网页抓取铺面信息

    options = webdriver.ChromeOptions()
    options.add_argument('-ignore-certificate-errors')
    options.add_argument('-ignore -ssl-errors')
    options.add_argument('-ignore -net_error')
    options.add_argument('--start-maximized')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)

    driver.get(search_url)

    input('在网页上设置筛选参数，在此页面Enter开始爬取谱面（后面还有输入项）')
    beatMapCounts = input('（输入整数）设置爬取谱面数量：（大范围筛选会导致去重后谱面数量大幅减少）')
    while beatMapCounts == '':
        beatMapCounts = input('（输入整数）设置爬取谱面数量：（大范围筛选会导致去重后谱面数量大幅减少）')
    beatMapCounts = int(beatMapCounts)
    zoomRate = 8 / beatMapCounts
    print('正在爬取谱面信息，切勿关闭网页以及进行其他操作直到网页关闭为止')
    driver.execute_script(f"document.body.style.zoom='{zoomRate}'")
    time.sleep(beatMapCounts / 20)

    dom = etree.HTML(driver.page_source)
    link = dom.xpath('//*[@class="c-ljOvCE"]/a/@href')
    message = dom.xpath('//*[@class="c-ljOvCE"]/a/text()')
    id_link = dom.xpath('//*[@class="c-ivOyuF"]/@style')
    beatmap_id = []
    downLoadUrl = []

    for per_id_link in id_link:
        bm_number = re.findall('(\\d+)', per_id_link)[0]
        beatmap_id.append(bm_number)
        downLoadUrl.append(urls[download_station] + bm_number)

    save_link = pd.DataFrame({'beatmap_id': beatmap_id[0: beatMapCounts],
                              'link': link[0: beatMapCounts],
                              'message': message[0: beatMapCounts],
                              'downLoadUrl': downLoadUrl[0: beatMapCounts]})

    fileName = input('自定义文件名称（记录筛选信息）')
    save_link = save_link.drop_duplicates(['beatmap_id'])
    save_link.to_excel(f'./download_xml/{fileName}.xlsx', index=False)
    save_link['downLoadUrl'].to_csv(f'./download_xml/{fileName}_{url_name}.txt',
                                    index=False, header=False)

    print('已生成文档')
    driver.close()
