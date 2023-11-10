# from urllib.parse import urlparse
import tldextract

urls_file = open('domains.txt', encoding='utf-8', errors='ignore')
all_urls = urls_file.read().splitlines()
print('all urls count = ', len(all_urls))
unique_urls = set()
unique_root_domains = set()

for url in all_urls:
    # root_domain = urlparse(url).hostname  # get host name of each URL
    root_domain = tldextract.extract(url).registered_domain
    if root_domain not in unique_root_domains:
        unique_root_domains.add(root_domain)  # if it is new, add to the unique domains list
        unique_urls.add(url)  # add the URL to the final output set

with open('unique-urls.txt', 'w') as unique_urls_file:
    unique_urls_file.write('\n'.join(unique_urls) + '\n')

print('all unique urls count = ', len(unique_urls))
