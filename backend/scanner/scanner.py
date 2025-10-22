import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

class Scanner:
    def __init__(self, url, max_pages=20):
        self.url = url
        self.session = requests.Session()
        self.session.headers['User-Agent'] = 'VulnSight/1.0'
        self.scanned_links = set()
        self.max_pages = max_pages

    def crawl(self):
        """
        Performs an iterative crawl to discover links, respecting a page limit.
        """
        queue = deque([self.url])
        visited = {self.url}

        while queue and len(self.scanned_links) < self.max_pages:
            url = queue.popleft()
            if url in self.scanned_links:
                continue

            self.scanned_links.add(url)
            print(f"Crawling: {url}")

            try:
                response = self.session.get(url, timeout=5)
                soup = BeautifulSoup(response.content, 'html.parser')
                for a_tag in soup.find_all('a', href=True):
                    link = urljoin(url, a_tag['href'])
                    # Stay on the same domain
                    if urlparse(link).netloc == urlparse(self.url).netloc and link not in visited:
                        visited.add(link)
                        queue.append(link)
            except requests.exceptions.RequestException as e:
                print(f"Error crawling {url}: {e}")

    def scan(self):
        """
        Performs the vulnerability scan on discovered pages.
        """
        self.crawl()
        vulnerabilities = []
        print(f"Scanning {len(self.scanned_links)} pages...")
        for link in self.scanned_links:
            vulnerabilities.extend(self.check_sql_injection(link))
            vulnerabilities.extend(self.check_xss(link))
        return vulnerabilities

    def get_forms(self, url):
        """
        Extracts all forms from a given URL.
        """
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.find_all('form')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url} for forms: {e}")
            return []

    def submit_form(self, form, value, url):
        """
        Submits a form with a given value in all relevant input fields.
        """
        action = form.get('action')
        post_url = urljoin(url, action)
        method = form.get('method', 'get').lower()

        post_data = {}
        # Find all input and textarea tags
        for input_tag in form.find_all(['input', 'textarea']):
            input_name = input_tag.get('name')
            input_type = input_tag.get('type', 'text') # Default type for inputs
            input_value = input_tag.get('value', '')

            # Fill text-like fields with the payload
            if input_type in ['text', 'search', 'email', 'url', 'password']:
                input_value = value

            # Handle textareas
            if input_tag.name == 'textarea':
                post_data[input_name] = value
            elif input_name:
                post_data[input_name] = input_value

        try:
            if method == 'post':
                return self.session.post(post_url, data=post_data, timeout=5)
            else:
                return self.session.get(post_url, params=post_data, timeout=5)
        except requests.exceptions.RequestException as e:
            print(f"Error submitting form to {post_url}: {e}")
            return None


    def check_sql_injection(self, url):
        """
        Checks for error-based SQL injection vulnerabilities in forms on a given URL.
        """
        sql_payloads = ["' OR 1=1 --", "' OR '1'='1", "' OR 1=1 #"]
        sql_errors = [
            "you have an error in your sql syntax",
            "warning: mysql",
            "unclosed quotation mark",
            "syntax error",
        ]
        vulnerabilities = []
        for form in self.get_forms(url):
            for payload in sql_payloads:
                response = self.submit_form(form, payload, url)
                if response:
                    content = response.content.decode('utf-8', errors='ignore').lower()
                    for error in sql_errors:
                        if error in content:
                            vulnerabilities.append({
                                'type': 'SQL Injection',
                                'url': url,
                                'payload': payload,
                                'description': f'Potential error-based SQLi found. Response contains: "{error}"'
                            })
                            # Stop after finding one error for this form
                            break
        return vulnerabilities

    def check_xss(self, url):
        """
        Checks for reflected Cross-Site Scripting (XSS) vulnerabilities.
        """
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
        ]
        vulnerabilities = []
        for form in self.get_forms(url):
            for payload in xss_payloads:
                response = self.submit_form(form, payload, url)
                if response and payload in response.content.decode('utf-8', errors='ignore'):
                     vulnerabilities.append({
                        'type': 'XSS',
                        'url': url,
                        'payload': payload,
                        'description': 'Potential reflected XSS vulnerability found.'
                    })
        return vulnerabilities
