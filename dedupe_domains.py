import tldextract

# Read URLs efficiently
with open('domains.txt', encoding='utf-8', errors='ignore') as file:
    all_urls = file.read().splitlines()

print('All URLs count:', len(all_urls))

unique_urls = {}
for url in all_urls:
    root_domain = tldextract.extract(url).registered_domain
    if root_domain and root_domain not in unique_urls:
        unique_urls[root_domain] = url  # Store the first occurrence of the domain

# Write unique URLs to file
with open('unique-urls.txt', 'w') as output_file:
    output_file.write('\n'.join(unique_urls.values()) + '\n')

print('Unique URLs count:', len(unique_urls))
