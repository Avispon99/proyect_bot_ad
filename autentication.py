import os
import zipfile
import time

from selenium import webdriver

PROXY_HOST = '200.0.61.254'  # rotating proxy
PROXY_PORT = 29842
PROXY_USER = 'olopez03'
PROXY_PASS = '09Ngt4q6'


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)

    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    
    #driver = webdriver.Chrome(os.path.join(path, 'chromedriver'),chrome_options=chrome_options)
    chrome_options.add_argument('--disable-gpu')
    #driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe',chrome_options=chrome_options)
    driver = webdriver.Chrome(executable_path='D:\\c_driver\\chromedriver.exe',chrome_options=chrome_options)

    
    return driver

def main():
    driver = get_chromedriver(use_proxy=True)
    #driver.get('https://www.google.com/search?q=my+ip+address')
    driver.get('https://www.myip.com/')
    time.sleep(20)
    driver.execute_script('alert("HELLO")')
    time.sleep(20)

if __name__ == '__main__':
    main()