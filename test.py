import re

s = '<span><a href="http://api.facebook.com/restserver.php" target="_blank" rel="nofollow">http://api.facebook.com/restserver.php</a></span>'
testlist = ['<span>Specs</span>',
            '<span><a href="http://api.facebook.com/restserver.php" target="_blank" rel="nofollow">http://api.facebook.com/restserver.php</a></span>',
            '<span><a href="https://developers.facebook.com/" target="_blank" rel="nofollow">https://developers.facebook.com/</a></span>',
            '<span><a href="/category/social">Social</a></span>',
            '<span><a href="/category/webhooks">Webhooks</a></span>',
            '<span><a href="/company/facebook">Facebook</a></span>',
            '<span>Yes</span>',
            '<span><a href="http://forum.developers.facebook.com/" target="_blank" rel="nofollow">http://forum.developers.facebook.com/</a></span>',
            '<span><a href="http://twitter.com/fbplatform" target="_blank" rel="nofollow">http://twitter.com/fbplatform</a></span>',
            '<span><a href="http://developers.facebook.com/group.php?gid=2205007948" target="_blank" rel="nofollow">http://developers.facebook.com/group.php?gid=2205007948</a></span>',
            '<span><a href="http://developers.facebook.com/tools/explorer" target="_blank" rel="nofollow">http://developers.facebook.com/tools/explorer</a></span>',
            '<span>API Key, OAuth 2</span>',
            '<span>Recommended <span class="desc-recommended">(active, supported)</span></span>',
            '<span>No</span>',
            '<span>Single purpose API</span>',
            '<span>No</span>',
            '<span><a href="https://developers.facebook.com/" target="_blank" rel="nofollow">https://developers.facebook.com/</a></span>',
            '<span>REST</span>',
            '<span>URI Query String/CRUD</span>',
            '<span>CSV, GeoJSON, JSON, XML</span>',
            '<span>No</span>',
            '<span>Yes</span>',
            '<span>No</span>']


def handle_value(item):
    item = str(item[6:])
    if not item.startswith('<a'):
        return item.split('</span>')[0]
    else:
        return re.findall(r'<a.*?>(.*?)</a>', item)[0]


tt = list(map(handle_value, testlist))
print(tt)
